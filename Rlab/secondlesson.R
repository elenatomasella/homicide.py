#you can write whatever you want in R, for examples both slides and websites
#you can also plot something in R and this is very useful to present data analysis

#for the final presentation we would need a presentation with plots inside

#FOR and WHILE
for (i in c(1,3,5,7)){
  cat(i^2,"-- ") #concatenate the outputs
  #cat is a command used to concatenate as a sequence what you have inside
}
#we can use while as well

names <- c("Marco", "Antonia", "Federica","Alessandro","Luca")
for (i in names){
  print(paste(i, "consists in ",nchar(i) ,"characters."))}

#we want to sample a random number in a certain interval and we want the remainder of its division by 10
rem <- 1
set.seed(3) #in case of random operations, it ensure the reproducibility of the run
#you can have a random operation, but everytime you fix smth on set.seed() you would receive the same "random" output
#at a glance: you actually fix the way of randomizing 
while (rem>0){
  sam <- sample(1:100,1) #extract random value in a vector 1:100
  rem <-sam%%10 #remainder of the division
  print(paste("sample =", sam, "- remainder = ", rem)) #the function paste is putting all in a string 
}


#IF/ELSE/ELSE IF code
zeta <- c(1,7)
for (z in zeta){
  if(z>5){ #check if z is greater then 5
    y<-z
}else{
    y<- -z
}
  print(paste("z=", z, "-- y = ",y))
  }

#VERY IMPORTANT WHAT FOLLOWS
#ifelse() command: the first argument is the thing which is valuated to be true or false, 
#the second argument is the one valuated if true, the second is the one valuated if false
y<- ifelse(zeta>5, zeta, -zeta) 
print(paste("z= ", zeta, "-- y =", y))

#CONDITIONS
a<-2
b<-3
a==b

a!=b
a<b
a>b
is.na(a)
is.character(a)
is.numeric(a)
is.factor(a) #factor is a type used in machine learning mainly, to store both integers and strings 
is.complex(a)

a <- c(1:10, NA)
a
is.na(a[11])
is.numeric(a) #it returns true because NA type is adapting (kind of a jolly)
is.vector(a)
is.data.frame(a)

a<-5
b<- -2
c<-NA
!is.na(c) #we're asking if a is NOT na, so answer would be TRUE
(a>=0)&(b<=0)
(b>=a)| (b==0) #we're asking whether one of the two is TRUE, it's on OR. & for AND


#EXERCISE1
#calculate the weighted average of your marks 
#MY CODE: USING A WHILE LOOP
marksandcredits <- c(24, 30, 18, 18, 27, 28,6,9,6,12,6,6)
matchmc <- array(marksandcredits, dim=c(6,2))
matchmc
sum <- 0
totalcredits <-0
i<-1
while (i <=6) {
  sum <- sum+ matchmc[i,1]*matchmc[i,2]
  totalcredits <- sum(matchmc[,2])
  i<-i+1
}
weightedmean = sum/totalcredits
weightedmean

#code with the for loop
results <- c(24, 30, 18, 18, 27, 28)
credits <- c(6,9,6,12,6,6)
num <- 0
den<- 0
n_exams <-length(results)
for (i in 1:n_exams){
  num <- num + credits[i]*results[i]
  den <- den + credits[i]
}
wei_mean <- num/den
wei_mean

#same result but with a single line code
sum(credits * results)/sum(credits)


#FIBONACCI SEQUENCE, but the first n elements must be printed only if odd

#another try fro a better solution
Fib<-c(0,1)
N<-10
Fib_odd<-c()
while (length(Fib_odd)<N){
  if(Fib[length(Fib)]%%2!=0){ 
    Fib_odd<-c(Fib_odd,Fib[length(Fib)])
    Fib<-c(Fib, Fib[length(Fib)]+Fib[length(Fib)-1])
  }else{
    Fib<-c(Fib, Fib[length(Fib)]+Fib[length(Fib)-1])

  }
}
Fib
Fib_odd

#MY SOLUTION with a WHILE loop
fsequence <- c(0,1)
k<-length(fsequence)
while (k<10){
  newfreq <- fsequence[k-1]+fsequence[k-2]
  fsequence <- c(fsequence, newfreq)
  k<-length(fsequence)+1
}
defseq <-c()
for (j in fsequence){
  if (j%%2 !=0){
defseq <- c(defseq,j)}}
defseq

#solution with a FOR loop 
Fib_seq <- c(0,1)
N<- 10
for (i in 3:N){ #because we can start building the sequence from the third element only
  new <- Fib_seq[i-2]+Fib_seq[i-1]
  print(paste("F", i, " = ", new)) #it's a concatenation of strings
  Fib_seq <- c(Fib_seq, new)
}
Fib_seq%%2
Fib_seq %%2==1
Fib_seq[which(Fib_seq %%2==1)]


#DATA STRUCTURES
#one dimensional: vector is homogeneous, list is heterogeneous
#two dimensional: matrix is homogeneous and numeric while dataframe and list are heterogeneous 
#multi-dimensional vectors: array is homogeneous, list is heterogeneous

#MATRIX is a two-dimensional array that has m number of rows and n number of columns
M<- matrix(1:12,nrow =4, ncol=3) #data ordered by column
M
M<- matrix(1:12,nrow =4, ncol=3, byrow = T) #data ordered by column
M
M<- matrix(LETTERS[1:8], 4, byrow=T)
M

#we can combine vectors 
M<- matrix(letters[1:8], ncol=4)
M

#how to combine vectors
a<- 1:4
b <- 11:14
M <- cbind(a,b) #combining by column
M

M<- rbind(a,b) #combining by row
M

#we can explore elements in matrices by indexing both matrices and vectors
M<-matrix(c(1,6,4,8,1,NA,2,8,9,3,6,NA),3,4)
M[1,2]
M[,2]#second column
M[1,]#first row
M[c(1,3), 3] #set of row or set of columns 

#to have the dimensions of the matrix
dim(M)


#TAKE CARE: if we have missing values on a matrix then the mean of the matrix is not calculate, 
#but if we calculate the mean without the missing values then we evaluate the mean 
mean(M)
mean(M, na.rm=TRUE)

min(M, na.rm=TRUE)
colMeans(M, na.rm =TRUE)  #we've the mean of each columns
rowMeans(M, na.rm = TRUE)
min(M[,1])

summary(M) #most important: it returns statistics of the matrix

M<-matrix(1:6,2)
M
t(M) #it would give us the transposed matrix 
N<-matrix(6:1,3)
N
N*t(M)
N%*%M #multiplication element by element 


#DATA FRAMES = list of vectors of equal length
#I can combine more then a vector in a single structures: each column has a data type
#the most important thing is the name of columns (matrix required ALL same type)

a<-1:4
b<-c("R","Python","Matlab", "Excel")
c <- c(TRUE,TRUE,FALSE,TRUE)
d<-c(0,0,600,200)
df<-data.frame(a,b,c,d) #command to join vectors
df

names(df)<- c("Id", "language","Known","Price")
df
dim(df)

c(nrow(df),ncol(df))

#print the structure
str(df) #it's automatical for R to recognize a data frame type

#how to add a column to a data frame 
#first solution
rate <- c(1,2,4,3)
df[,5]<-rate
names(df)[5]<-"rate"
df
#alternative faster solution
df$rate <-rate
df

#we can explore elements of the data frame, for example by writing df$ID, 
df[,1] #first column
df$Id #so with a dollar between the name of the data frame and the name of the column

#subset a Data Frame based on whether or not a certain condition is true
subset(df,subset = Price<100) #it's a kind a filter before printing 


#EXAMPLES of DATA FRAMES
#we can explore iris which is a botanical dataframe with botanical observations
#IRIS dataset gives the measurements of the sepal length and width and petal length and width, for 3 species of iris
is.data.frame(iris) 
head(iris, 10)


#fuel consumption and 10 aspects of automobile design and performance for 32 automobiles
data(mtcars)
is.data.frame(mtcars)
head(mtcars, 10) 
#we can have the explanations of all the parameters of the dataframe writings ?mtcars


#IMPORT DATA FROM TEXT (CSV) FILE
#you can import dataframes. Mainly excel sheets but you have to be prepared
#there are guidelines to explain how to be prepared
#if the file is not in wd, file must report the entire path

#csv file example with airport 2022: classical text file with data
all_airport <-read.table(file = "Airports_2022.csv",
                           header = T, sep = ";",dec =",",na.strings = "n/a")
airports <-all_airport[,c(1,2,3,6,9)]
airports

#SAVE your data from text or csv file
write.table(airports, file = "Airports_2022.csv",
            sep = ";", row.names = F, col.names = T, quote = FALSE)

#SOME EXPLORATIVE ANALYSIS: let's play with airport data set 
#I can modify it adding columns
x<-1:4 #suppose 4 levels of rank (level 1 to 4)
y<-sample(x, nrow(airports), replace = T) #sample a rank value for each airport
#take note: replace=T stands for the sample to be with the replacement 

rank<-factor(y) #transform values in factor (categorical parameter)
levels(rank) <- c("A", "B", "C", "D") #assign a label for each level 
airports$rank <- rank
head(airports, 5)

airports[c(32,33),] #airports in Rome

#I can select airports in Rome only or some particular columns and so on
airports[1:3,c(2,4)]
#I can select columns by ID or name
airports[1:3,c("Airport","Passengers")]
dim(airports) #dimension of the object
str(airports) #str function displays structures of R objects

summary(airports) #the output would be statistics about our dataset, airport in this case 

airports[airports$rank =="A",] #the output would be all the rows having A as rank
subset(airports, rank=="A")

#for numerical parameters
sapply(airports[,sapply(airports,is.logical) | sapply(airports, is.numeric)], mean)
sapply(airports[,sapply(airports,is.logical)|sapply(airports, is.numeric)], range)
sapply(airports[,sapply(airports,is.logical)|sapply(airports, is.numeric)], max)
sapply(airports[,sapply(airports, is.logical)|sapply(airports, is.numeric)],min)

mean(airports$Passengers)
range(airports$Passengers) 
mean(airports$Cargo_tons,na.rm=T)      
min(airports$Flights)
max(airports$Flights)

#frequency distribution for categorical values 
#table() is for categorical values: how many times a certain things is in the dataset
table(airports$rank)



#EXERCISE 1
#explore the data set "iris"

#check the class of each variable 
irisdf<- data.frame(iris)
irisdf
names(irisdf)
sapply(irisdf, class)

class(irisdf[,1])
class(irisdf[,2])
class(irisdf[,3])
class(irisdf[,4])
class(irisdf[,5])

#subset all rows of Species "virginica" in a new data frame
virginica <- subset(irisdf, Species == "virginica")
virginica

#create a vector called "sepal.dif" with the difference between "Sepal.length" and "Sepal.width"
sepal.dif<-c(irisdf$Sepal.Length-irisdf$Sepal.Width)
sepal.dif

#assign NA to sepal.dif <=3
sepal.dif[sepal.dif<=3] = NA
sepal.dif
#evaluate minimum, maximum, mean value of sepal.dif (with missing values)
min(sepal.dif, na.rm = TRUE)
min(sepal.dif)
max(sepal.dif)
mean(sepal.dif)


#EXERCISE 2
#explore the dataset swiss
?swiss
#create a data frame of only the rows 1,2,3,10,11,13 
#and only the variables Examination, Education, Infant.Mortality
swissdf <- data.frame(swiss)
smallerswiss <- swissdf[c(1,2,3,10,11,13), c("Examination", "Education", "Infant.Mortality")]
smallerswiss

#the infant mortality of Sarine is wrong, it should be a NA, change it 
smallerswiss["Sarine","Infant.Mortality"] = NA
smallerswiss

#create a row that will be the total sum of the column, name it Total
newrow<- c(sum(smallerswiss[,1]),sum(smallerswiss[,2]), sum(smallerswiss[,3]) )
#better as it follows 
newrow<-sapply(smallerswiss, sum)
smallerswiss<-rbind(smallerswiss,newrow)
smallerswiss
rownames(smallerswiss)[nrow(smallerswiss)]<-"Total"
smallerswiss

#create a new variable that will be the proportion of Examination (Examination/Total)
proportion<- smallerswiss[,"Examination"]/smallerswiss["Total",]
proportion


#EXERCISE 3
#import the .csv file 
airports<-read.table(file = "Airports_2022.csv", header = T, sep = ";") 
airports 
#check the class of the variables 
sapply(airports, class)

class(airports[,1])
class(airports[,2])
class(airports[,3])
class(airports[,4])
class(airports[,5])
class(airports[,6])

?subset
#generate a new dataframe with the larger airports in terms of passengers and/or cargo
#(more than one condition with logical operators)
biggestairportspass <- subset(airports, subset = airports$Passengers >50000)
biggestairportspass
biggestairportcars <- subset(airports,subset = airports$Cargo_tons >500)
biggestairportcars


#EXERCISE 4

#import the .csv file required 
weather<- read.csv(file = "weather.csv")
weather

#check the class of each variable 
for (i in 1:length(weather)){
  print(class(weather[,i]))}
#optimised as it follows:
sapply(weather, class)
weather
#generate a new dataframe with the average value of each station : CAPIRE MEGLIO
str(weather)

meanstations <- data.frame(weather$Station.Code, sapply(weather, mean))
meanstations
