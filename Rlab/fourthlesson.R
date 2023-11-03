#GENERATE A DATASET
#from one input (it means one file) but also from multiple sources (more files, 
#different sources), and also we can generate a dataset from other information

#rules to generate a dataset:
#file names, api requests, db queries and lots of values hidden are strings 

#to have a value as a string we should specify stringAsFactors =FALSE
x<-read.table(file = "iris.data.txt", header = T, sep = ",", stringsAsFactors = FALSE)
head(x)
str(x)

x<-read.csv2(file ="iris.csv", header = T)
head(x)

x<-read.table(file = "iris.csv", header = T, sep = ";", dec = ",")
y<- read.csv2(file = "iris.csv",header = T)
head(x)
head(y)

#INPUT FROM FILES 
install.packages("httr")
library(readxl)
x<-read_excel("ostreopsis.xlsx", sheet = 1)
hea(x[,c(3,4,6,7,8,9)])

install.packages("raster")
library(raster)
s<-shapefile("shp/Italy.shp")
plot(s)


#STRING MANIPULATION 
nchart() #to count the number of char in a string
paste() and paste0() #to concatenate vectors after converting to a character
substr() #extract a portion of string in a string
gsub() #replaces characters of group of characters in a string 
#and others in the slide

#I can work on the exact position of smth in a string
string<- "PYTHON AND R FOR DATA SCIENCE"

nchar(string)

tolower(string)

paste("Luiss", string, sep = "-")

paste0("Luiss - ",string)

substr(string, start = 11, stop =13)

gsub("PYTHON", "MATLAB", string)

strsplit(string, " FOR ")

grep("TH",unlist(strsplit(string, " FOR ")))

#SEVERAL OPTIONS TO OPERATE ON FILES 
#here we have functions about files.

file.create()  #to create a file
file.create("download/empty.csv")

file.exists() #verifies if file exists
file.remove() #per rimuovere il file 

file.rename() #rename il file 
file.rename(from = "download/empty.csv", to = "download/to_complete.csv")

file.append() #append the content of a file 
file.copy() #to copy one file
file.info() #returns primary info a file

dir.create() #to create a directory
dir.create("download")
download.file("urlofthefile", destfile = "download/wind.csv")
file.exists("download/wind.csv")
file.info("download/wind.csv")

dir.exists() #to verify if a directory exists 

list.files() #return a complete list of files in a selected path
list.files(past = "download/")

list.dis() #return a complete list of directories in a selected path
download.file() #to download file from web


#DATES AND TIMES: dates and times appear as a string but they can be treated as numerical values, 
#because they are thought as the number of days starting from an origin

#if in date I add one it means that I'm adding one day. I can also have some algebrical operation 

date_str<-"2023-10-09"
typeof(date_str)

date_tod<-as.Date(date_str)
typeof(date_tod)

date_tom<-date_tod +1
date_tom

date_tom-date_tod

#I can perform sequencies. I can decide how to order the sequence
seq(from = as.Date("2023-10-09"), to = as.Date("2023-11-09"), by="day")
seq(from = as.Date("2023-10-09"), to= as.Date("2023-11-09"), by ="week")

#if you are setting you operational system in Italian you would have Italian and so on
format(date_tod,"%A %B %Y") #see ?strtime
months(date_tod)
weekdays(date_tod)
as.numeric(date_tod)

#If we have date and time in this sense, I have to convert the string in a datetime format. I can convert then
string1 <- "2023-10-09 09:00"
dtt1<-strptime(string1,format = "%Y -%m-%d %H:%M", tz = "UTC")
dtt1

string2<- "2023-10-09 12:00"
dtt2 <- strptime(string2,format = "%Y-%m-%d %H:%M", tz = "UTC")
seq(dtt1,dtt2,by = 30*60)

seq(dtt1,dtt2,by = "hour")

#first I need to download the file and then to read it with read.table(...)
inp <- read.table("download/wind.csv", header = T, sep = ";")
inp2<- inp[-(1000:2500)] #remove data
par(mfrow=c(1,2))
plot(inp$WS,type="1")
datetime <-strptime(inp2$UTC, "%Y-%m-%d %H:%M", tz = "UTC")
plot(datetime, inp2$WS,type ="1")
#if I simply plot the data I have a different result from the case of plotting with datetime connection 

#HOW TO BUILT MY DATASET: generally I type "enviromental data" on Google specifying the area I'm interested in 

#FOR ALL THE THREE EXERCISES YOU SHOULD OPEN THE SEPARATED FILES 
#EXAMPLE 1 
#pollution in villa Ada: for each pollutant and for each year we should download all the data.
#chaotic information in all the file: lot of columns
#for each column we need to select the rown only regarding Villa Ada. 
#all data has a standard url 

ada<- 39
years<-2015:2022
poll<- c("PM10","PM_5","SO2")

star_date <-as.Date(paste0(years[1], "01-01"))
end_year <- as.Date(paste(years[length(years)]))
date_seq <- seq(start_date,end_date, by = "day")
pollutant <- data.frame(date_p=data_seq)



for (p in poll){
  year<-c()
  day <-c()
  values<-c()}

#by fixing the collutant we can read all the cycle below 

#now I'm going to generate a new url: observing that all the urls are the same I must start from the part which is differing 
for (a in years){
  print(paste(p,a))
  #download file
#we have to concatenate the url 
#we can test it: I am simulating a run in my cycle and I can run this frame 
url <-paste0("theurl"), p, "_",a,"gg_txt")
download.file(url, destfile = "temp.txt")
#read file
x<-read.table("tempt.txt",header = T, na.strings = "-999.0")
#find monitoring system
#now we have to look for villa ada, which corresponds to x39
id<-which(names(x)==paste0("x", ada))
val<- c(val,x[,id])
year <- c(year, x[,1])
day<-c(day, x[,2])}

#we have different ways to follow achieve the required result in terms of function coded. 
#now I have everything in a single variable: I want the way to start from the first file and append the second and the following 

#we can also plot the data in 2020 plot(val, type = "l")
#we have to convert this sequence in a date. We can paste 
as.Date(paste(year, day),"%Y %j") #the second argument is to define the format (?strptime to know the possibilities)

#merge into the final dataframe
pollutant <- merge(pollutant, poll, by = "date_p", all.x =T)
date_p

#at the end you can run all at a time and you should have the finale dataframe to look at. 
#at the end you have an ordered dataframe starting from a chaotic one. This is powerful. 
plot(pollutant$date_p,pollutant$PM10,type = "l")
plot(pollutant$date_p,pollutant$PM2,col = 2)
abline(h=50, color = "green")
legend("top", legend = (c("PM10", "PM 2.5"), lty = 1, col = 1:2, horiz = T))



#SUM UP: this is all the process we have to invent every time we have a set of data

#about APIs services: for forecasts, historical data and so on
#you have to built some url, you want to forecast smth

install.packages("httr")
library(httr)
#we want a weather forecast in LUISS
api_url <- ""
sample <-GET(api_url)


lat <-41.92
lon <- 12.49
curr <-"true"
hou<-"temperature_2m, reative_humidity"

#you can then investigate the data
date_str <- unlist(x$hourly$time)
temp<-unilist(x$hourly$temperature_2m)
#to transform a list in a vector


#and you can then plot it 
#you can see examples also of historical data

#to show us smth funny: you need to download also an external software.
library(imager)
library(animation)
saveGIF(
  for(i in 1:29){download.file(ph$)}
)


#HOMEWORK: EXAMPLE 3
#generate the fiscal code 
name<-"ELENA"
surname<-"TOMASELLA"
birth<-"2001-G-23"
city<-"VITTORIO VENETO"


# Function to calculate the Italian Fiscal Code (ChatGPT)
calculateItalianFiscalCode <- function(lastName, firstName, gender, birthDate, birthPlace) {
  # Remove spaces and convert to uppercase
  lastName <- toupper(gsub(" ", "", lastName))
  firstName <- toupper(gsub(" ", "", firstName))
  birthPlace <- toupper(gsub(" ", "", birthPlace))
  
  # Extract the year, month, and day from the birth date
  birthDate <- as.Date(birthDate, format = "%Y-%m-%d")
  birthYear <- format(birthDate, "%y")
  birthMonth <- format(birthDate, "%m")
  birthDay <- format(birthDate, "%d")
  
  # Define a string of allowed consonants and vowels
  allowedChars <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  # Function to calculate the code for the name
  calculateNameCode <- function(name) {
    nameCode <- character(3)
    name <- gsub("[AEIOU]", "", name)
    
    if (nchar(name) >= 3) {
      nameCode <- substr(name, start = c(1, 2, 4), stop = c(1, 2, 3))
    } else {
      nameCode[1] <- substr(name, start = 1, stop = 3)
      nameCode[2] <- substr(name, start = 1, stop = 3)
      nameCode[3] <- substr(name, start = 1, stop = 3)
    }
    return(nameCode)
  }
  
  # Calculate the code for the last name and first name
  lastNameCode <- calculateNameCode(lastName)
  firstNameCode <- calculateNameCode(firstName)
  
  # Calculate the code for the birthplace
  birthPlaceCode <- character(4)
  for (i in 1:4) {
    if (i <= nchar(birthPlace)) {
      char <- substr(birthPlace, start = i, stop = i)
      if (char %in% allowedChars) {
        birthPlaceCode[i] <- char
      } else {
        birthPlaceCode[i] <- "X"
      }
    } else {
      birthPlaceCode[i] <- "X"
    }
  }
  
  # Calculate the code for the birthdate and gender
  if (gender == "Male") {
    birthDateCode <- paste(birthYear, birthMonth, birthDay, sep = "")
  } else {
    birthDateCode <- as.numeric(birthYear) + 40
    birthDateCode <- paste(birthDateCode, birthMonth, birthDay, sep = "")
  }
  
  # Combine all the codes
  fiscalCode <- paste(lastNameCode, firstNameCode, birthDateCode, birthPlaceCode, sep = "")
  return(fiscalCode)
}

# Example usage
lastName <- "Rossi"
firstName <- "Mario"
gender <- "Male"
birthDate <- "1980-05-15"
birthPlace <- "Milano"

fiscalCode <- calculateItalianFiscalCode(lastName, firstName, gender, birthDate, birthPlace)
cat("Italian Fiscal Code:", fiscalCode, "\n")

