##### Fiscal Code

# ABCDEF12G34H567X

# ABC - Last Name

# DEF - Fist Name

# 12 - Year of birth

# G - Month of birth (code, single character)

# 34 - Day of birth (if female, +40)

# H567 - City of birth (code)

# X - control char, random character

# Details here https://en.wikipedia.org/wiki/Italian_fiscal_code (but considering "Check character" only as a random character)


###########################################
####  Exercise  ###########################
###########################################

# First part: Generate 20 random FC

# Suggestion in comments

### Part 1
#Generate 20 random FC
fc <- "ABCDEF12G34H567X"
# number of CF to generate
n <- 20
# Codes and parameters
months_codes <- c(1:12)
gender_codes <- c("F", "M")
years <- 1970:2023

# Look for municipal codes
# list of the municipal codes https://www.istat.it/en/archivio/6789
# https://www.istat.it/storage/codici-unita-amministrative/Elenco-codici-statistici-e-denominazioni-delle-unita-territoriali.zip


## import municipal codes in the excel file from ISTAT
municipal_codes<-read_xlsx("Codici-statistici-e-denominazioni-al-30_06_2023.xlsx")
head(municipal_codes)
## generate random first e last names (only codes, 3 letters for firstname and 3 letters for last name)
install.packages("random")
library(random)
listfc<-list()
for (i in 1:n){
firstname <- randomStrings(len=3,digits = FALSE)
substr(fc,1,3)<-firstname
lastname<- randomStrings(len=3,digits=FALSE)
substr(fc,4,6)<-lastname
## generate random year of birth
birthyear<- as.character(sample(1970:2023,1))
substr(fc,7,8)<-birthyear[2:4]
## generate random month of birth
birthmonth <- as.character(sample(1:12, size =1))
substr(fc,9,9)<-birthmonth
## generate random day of birth according to extracted month and year
days_in_month <- as.integer(format(as.Date(paste(birthyear, birthmonth, "01", sep = "-"), "%d")))
birthday <- sample(1:days_in_month, 1)
if (gender_codes==F){
  substr(fc,10,11)<-birthday+40}
  else {substr(fc,10,11)<-birthday}
## generate random municipality code
municipalitycode<- sample(municipal_codes["Codice Comune formato alfanumerico"], size = 1)
substr(fc,12,15)<-municipalitycode
## generate random control char
set.seed(4)
last<-randomStrings(len=1, digits=FALSE)
substr(fc,16,16,last)
listfc<-list.append(fc)}
listfc

# Second Part: Starting from the random generated FCs, build a dataframe 
# with all possible information about people associated to FC 
# (names as code, date of birth, gender, city of birth)

# Useful function
# sample() 
# download.file()
# paste() and paste0()
#substr()
#which()
# as.Date()
# data.frame()
# maybe you have to look for new function on google (not necessary)