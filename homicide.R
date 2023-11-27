rm(list = ls())
library(dplyr)
library(ggplot2)
library(tidyverse)

#set the working directory
filepath = 'C:/Users/39324/Desktop/luiss/master/python and r/homicide project'
setwd(filepath)
getwd()

# load the data with read_csv, arrange it with tibble() function
library(readr)
library(readxl)
homicide = read_csv('database.csv')
homicide = homicide %>% as_tibble()
str(homicide)
nrow(homicide)
# Prepare the data
# select only useful columns, turn char columns into factor columns, change the names to be easily written
homicide = homicide %>%
  select(`Incident`,`Agency Type`,`City`, `State`, `Year`, `Month`, `Crime Type`, `Crime Solved`, `Victim Sex`,
         `Victim Age`, `Victim Race`, `Relationship`, `Weapon`,`Perpetrator Age`,`Perpetrator Sex`) %>%
  mutate(across(where(is.character),as.factor)) %>%
  setNames(c('incident','agency_type','city','state','year','month','ctype','csolved',
             'vsex','vage','vrace','relationship','weapon','aperpetrator','sperpetrator'))

str(homicide)
summary(homicide)

# filter the na values, unknown values, and evident impossible values
backup = unique(homicide)
homicide = unique(homicide)
sort(homicide$aperpetrator)
homicide = homicide %>% na.omit() %>%
  filter(aperpetrator >4) %>%
  filter(vage<100) %>%
  filter(vsex %in% c('Female','Male'),vrace != 'Unknown',
         relationship != 'Unknown', sperpetrator != 'Unknown')

# 1.1 summary statistics
sumstat = function(x){
  summary(x)
}
# give a glance to the victim age statistics, taking only the 95% of data from left side

q99 = quantile(homicide$vage,0.99)
quantvage = subset(homicide, vage<=q99)
sumstat(quantvage$vage)

# 2.0 Time and frequency
# look at the frequency of crime type
table(homicide$ctype)
# detect it by time series
homicide = homicide %>% as_tibble()
crime_trends = homicide %>% 
  group_by(year,month,ctype) %>%
  summarise(crimeFreq = n())

# in the 90s we have higher criminality frequency, while in 80s and after 2000 the frequency become lower
print(crime_trends)
ggplot(crime_trends, aes(x = month, y = crimeFreq, group = year, color = factor(year))) +
  geom_line() +
  labs(title = "Crime Trends Over Time by Year and Month",
       x = "Month", y = "Crime Count") +
  theme_minimal()

#----------------------------------
# Statistcal analysis
# 1. Distribution of Victim and Perpetrator Ages
library(gridExtra)

plot1 = ggplot(homicide, aes(x = vage)) +
  geom_histogram(binwidth = 5, fill = "blue", color = "black") +
  labs(title = "Distribution of Victim Ages", x = "Age", y = "Count") +
  theme_minimal()

plot2 = ggplot(homicide, aes(x = aperpetrator)) +
  geom_histogram(binwidth = 5, fill = "red", color = "black") +
  labs(title = "Distribution of Perpetrators Ages", x = "Age", y = "Count") +
  theme_minimal()

grid.arrange(plot1, plot2, ncol = 2)

# 2. Distribution of Victim Races
plot3 = ggplot(homicide, aes(x = vrace, fill = vrace)) +
  geom_bar() +
  labs(title = "Distribution of Victim Races", x = "Race", y = "Count") +
  theme_minimal()

# 2.1 Distribution of Victim Sexes
plot4 = ggplot(homicide, aes(x = vsex, fill = vsex)) +
  geom_bar() +
  labs(title = "Distribution of Victim Sexes", x = "Sex", y = "Count") +
  theme_minimal()

grid.arrange(plot3, plot4, ncol = 1)


# 2.2 we want to see if there is a significant percentage of crime solving percentage among Black and White
backup1 = backup[backup$vrace %in% c('Black', 'White'), ]

backup1$vrace = droplevels(backup1$vrace, exclude = c("Unknown", 
                                                       "Asian/Pacific Islander", 
                                                       "Native American/Alaska Native"))

table1 = table(backup1$vrace, backup1$csolved)

# Convert the table to a data frame
bar1 = as.data.frame(table1)

# Calculate the percentages within each victim race
bar1$percentage = prop.table(bar1$Freq) * 100

ggplot(bar1, aes(x = Var1, y = Freq, fill = Var2, label = sprintf("%.1f%%", percentage))) +
  geom_bar(stat = "identity", position = "stack", color = "white") +
  geom_text(position = position_stack(vjust = 0.5), size = 3) +
  labs(title = "Bar Plot of Crime Solved by Victim Race",
       x = "Victim Race",
       y = "Frequency",
       fill = "Crime Solved") +
  theme_minimal()

# 2.3 the same we can find the 

# 3.1 distribution of victim and perpetrator relationship
min_count_threshold = 2000
filtered_homicide = homicide %>%
  group_by(relationship) %>%
  filter(n() >= min_count_threshold) %>%
  ungroup()

# Arrange levels by count in decreasing order
filtered_homicide$relationship = factor(filtered_homicide$relationship, levels = names(sort(table(filtered_homicide$relationship), decreasing = TRUE)))

# Plot relationship
ggplot(filtered_homicide, aes(x = relationship, fill = relationship)) +
  geom_bar() +
  labs(title = "Distribution of Homicide Relationship", x = "Relationship", y = "Count") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# 3.2 see which weapon kills the most Wife
wife_data = homicide %>%
  filter(relationship == "Wife")

# Arrange levels by count in decreasing order
wife_data$weapon = factor(wife_data$weapon, levels = names(sort(table(wife_data$weapon), decreasing = TRUE)))

# Plot weapon distribution for Wife
ggplot(wife_data, aes(x = weapon, fill = weapon)) +
  geom_bar() +
  labs(title = "Which Weapon Kills Most Wives", x = "Weapon", y = "Count") +
  theme_minimal()



#-------------------------------
# Prediction models
# 1. find and select only three most important state with largest number of observations
a = sort(table(homicide$state))
plot(a)
# we find that the three most relevant states are:
# 1.California
# 2.Texas
# 3.New York

dataset = homicide[homicide$state %in% c('California','Texas','New York'),]
summary(dataset$state)

# 2. train a model and predict the sex of victim
# 2.1 organize data
# list the names of columns
dataset_name = names(dataset)
# find the indexes
dataset_index = seq_along(dataset_name)
# build the info matrix
column_info = data.frame(Column_Name = dataset_name, Column_Index = dataset_index )
column_info
#select wanted columns as new df

df = dataset %>% select(9:15)
df = df %>% na.omit()
str(df)
# transform as factors all the chr variables
df$vsex = droplevels(df$vsex, exclude = "Unknown")
df$vrace = droplevels(df$vrace, exclude = "Unknown")
df$sperpetrator = droplevels(df$sperpetrator, exclude = "Unknown")
levels(df$vsex)
# 2.2 split traina and test set
set.seed(1)
index = sample(nrow(df), size = 0.8*nrow(df))
train = df[index,]
test = df[-index,]
# 2.4 glm model
library(pROC)
logall = glm(vsex ~ ., family = 'binomial', data = train)
logall.pred = predict(logall, test, type = 'response')
summary(logall)

#find the optimal threshold for ROC curve 
roc_curve = roc(test$vsex, logall.pred)
optimal_threshold = coords(roc_curve, "best", ret = "threshold")$threshold
test = test %>% 
  mutate(pred = logall.pred)
test = test %>% 
  mutate(pred = case_when(pred > optimal_threshold ~ 'Male', TRUE ~ 'Female'))


logall.accuracy = mean(test$vsex == test$pred)
cat("The accuracy is", round(logall.accuracy * 100, 2), "%\n")

# Plot the ROC curve
plot(roc_curve, main = "ROC Curve", col = "blue", lwd = 2)

# Add labels and a legend
# Find the point on the ROC curve corresponding to a specific threshold (e.g., 0.5)
threshold_point = coords(roc_curve, "best", ret = "threshold")

# Add an abline at the height of the specified threshold point
abline(h = threshold_point$threshold, col = "red", lty = 2)
optimal_threshold
# Add labels and a legend
legend("bottomright", legend = c("ROC Curve", "Threshold Point"), col = c("blue", "red"), lty = c(1, 2), lwd = c(2, 1))













