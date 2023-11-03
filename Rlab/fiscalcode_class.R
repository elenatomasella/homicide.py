
###########################################
####  Exercise  ###########################
###########################################

# First part: Generate 20 random FC

# Suggestion in comments

### Part 1
#Generate 20 random FC

# number of CF to generate
n <- 20
# Codes and parameters
months_codes <- c('A','B','C','D','E','H','L','M','P','R','S','T')
gender_codes <- c("F", "M")
years <- 1970:2023

# Look for municipal codes
# list of the municipal codes https://www.istat.it/en/archivio/6789
# https://www.istat.it/storage/codici-unita-amministrative/Elenco-codici-statistici-e-denominazioni-delle-unita-territoriali.zip


## import municipal codes in the excel file from ISTAT
ISTAT <- read.csv("ISTAT.csv", head=F,sep = ";")
twenty_codes <- c() #we need to inizialize the vector of the twenty fiscal codes
i<-1
while (i<=20){
## generate random first and last names (only codes, 3 letters for firstname and 3 letters for last name)
first_name<-sample(LETTERS,3) #letters contains all the letters, it's a string we can use for free
fname<- paste0(first_name[1],first_name[2],first_name[3]) #paste zero has the property to delete the space between elements we need to paste

last_name<-sample(LETTERS,3) #same for the last name
lname<-paste0(last_name[1],last_name[2],last_name[3])

## generate random month of birth
birth_month<- sample(months_codes,1) #months_codes has already been defined indeed
birth_year <- substr(birth_year<-as.character(sample(years,1)),3,4) #it sample a year, it converts into char and it takes the thirs and fourth

## generate random day of birth according to extracted month and year
if (birth_month=="B"){ #special case for February
  birth_day <-sample(1:28,1)
} else if (birth_month %in% c("A",'C','E','L','P','S')){ #%in% to filter rows and columns of a dataframe: in this case I need to divide months with 30/31 days
  birth_day <- sample(1:31, 1)
}else {
  birth_day <-sample(1:30,1)
}

if (sample(gender_codes =="F",1 )) birth_day +40 #we avoid the {} if it's a oneline code 
birth_day<10
if (birth_day<10) birth_day<-sprintf("%02d", birth_day) #smth having two characters, otherwise you add a zero

## generate random municipality code

city_code <- sample(ISTAT$V20[-1],1) #we need to sample from the csv we are provided of; V20 is for the codice catastale del comune
#with [-1] we delete the title from our city_code vector

## generate random control char

control_char <- sample(LETTERS,1) #sample a letter to use it as ending char
new_code <-paste0(lname, fname,birth_year,birth_month,birth_day,city_code,control_char) #set a new codice fiscale
twenty_codes <- c(twenty_codes, new_code) #for the while loop involvment 

i=i+1 #to break the while loop once we get the twenty fiscal codes 
}

# Second Part: Starting from the random generated FCs, build a dataframe 
# with all possible information about people associated to FC 
# (names as code, date of birth, gender, city of birth)

df<- data.frame(twenty_codes) #twenty code is now a list of 20 fiscal codes
df$first_name <-substr(twenty_codes,1,3) #we take each part of the fiscal code to be intended as was it rapresent: explicit 
df$last_names<-substr(twenty_codes,4,6)
birth_month_codes <-substr(twenty_codes,9,9)

i<-1 #we initialize again i
birth_month2<-c() #we set birth_month2 involved in the following while loop
#the following loop os needed to write down the reverse of above: from the code to the month it refers to 
while (i<=20){
  if (i<length(birth_month_codes)+2) birth_month2<-c(birth_month2,sprintf("%02d",which(months_codes == birth_month_codes[i])))
  #R hepl: how can I add a leading zero? that's the use for which the sprintf function is needed 
  i=i+1
}


i<-1
birth_year2<- c()
while (i<=20){
  if (substr(twenty_codes[i],7,8)>=70){
  birth_year2<-c(birth_year2,paste0("19",substr(twenty_codes[i],7,8)))
} else{
  birth_year2 <-c(birth_year2,paste0("20",substr(twenty_codes[i],7,8)))
}
i = i+1
}


# Useful function
# sample() 
# download.file()
# paste() and paste0()
#substr()
#which()
# as.Date()
# data.frame()
# maybe you have to look for new function on google (not necessary)