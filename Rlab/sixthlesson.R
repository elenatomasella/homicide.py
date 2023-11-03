#HERE THE SECOND PART OF THE COURSE STARTS

#many of the libraries that was part of the first R are obsolete. 
#we need to wait to innovated libraries of to write functions substituting the ones of old versions 
#R was born 30 years ago. Instead of modify R, developers introduces innovations through new packages 
#example of libraries: ggplot2 and dplyr


#add a great number of libraries, new sintax and technologies. 
#dplyr is the best to be used for dataframe analysis: faster on data.frames (tibble), contains a set of tools for data exploration and transformation, 
#intuitive to write and easy to read, especially in the "chain" version


install.packages("dplyr")
library("dplyr")
install.packages("tidyverse")


library("dplyr")

#TIBBLE is a smart dataframe:
#it never changes an input's type
#it never uses row.names()
#when you print a tibble, it only shows the first ten rows and all the columns that fit on one screen. 
#It also prints an abbreviated description of the column type
head(iris)
iris2<-as_tibble(iris) #faster then dataframes
iris2
#tibble says that we have six more variables even if we can't visualize them 

install.packages("nycflights13")
library(nycflights13)
flights<-flights

class(flights)
head(flights)

data.frame(flights) #id we need to work with a dataframe instead

#BASIC FUNCTIONALITIES OF DPLYR
#can work with data stored in databases and data tables 
#joins: inner, left, semi, anti
#five basic verbs to solve the vast majority of data manipulation challenges:
#FILTER() to pick observation by their values 
#SELECT() to pick variables by their names
#ARRANGE() to reorder the rows
#MUTATE() to create new variables with functions of exiting variables 
#SUMMARISE() to collapse many values down to a single summary

#all of the verbs above can be used in conjunction with group_by(), which changes the scope of each function from
#operating on the entire dataset to operating on it group by group 
#dplyr is good also because it can join different dataframe in order to collect all different 
#possible information for data structures
#in our dataset we can group according to the destination in the case of our dataset

#FILTER
#select all flights on January 1st
flights[flights$month==1 & flights$day==1,]
filter(flights, carrier =="AA" | carrier =="UA") #it works as the OR condition 

#the dlpyr functions never modify their inputs so to have the result, we need to create a new variable 
jan1<- filter(flights, month ==1 , day ==1)
filter(flights, carrier %in% c("AA","UA"))
(jan1<- filter(flights, month ==1 , day ==1)) #to have and print the result directly we use then the brackets: otherwise we need to take into 
#consideration that R is either printing out the result or saving them into a variable 
#and indeed you see the result on screen and to the workspace as well

#ARRANGE changes the order of rows in a tibble 
#arrange function
flights[order(flights$dep_delay),] 
arrange(flights, dep_delay) #to organize in a different manner. I'm ordering with departure delay
arrange(flights, dep_delay, month, day)
#we can ri-arrange flights but in a decreasing order 
arrange(flights, desc(dep_delay))

#SELECT()
flights[,c('dep_time', 'arr_time','flight')]
select(flights, dep_time, arr_time, flight) #it's not so different from dataframe now. 

#TRICKS: to select multiple contiguous columns, use colon, to match columns by name use contains, starts_with, ends_with, matches 
select(flights, year:day, starts_with("arr"), contains("delay")) #all the columns from year to day
#subset could be used to rearrange the order of the columns to move variables at the first positions, using everything()
select(flights, time_hour, air_time, everything())

#MUTATE to add new variables 
#mutate function is useful to create a new variable. 
flights_sml = select(flights, 
                     year:day,
                     ends_with('delay'),
                     distance, 
                     air_time)
mutate(flights_sml,
       gain = dep_delay - arr_delay,
       speed = distance/ air_time *60)

#TRANSMUTE
#I can keep the new variables and deleting all the rest with transmute
transmute(flights, 
          gain = dep_delay-arr_delay,
          hours = air_time /60,
          gain_per_hour = gain/hours)

#SUMMARISE
#we want to group our variables sometimes
#basic R approach is the following: 
data.frame(delay = mean(flights$dep_delay
                        , na.rm = TRUE))
#dplyr approach: summarise collapes a whole dataframe to a single row 
summarise(flights, delay = mean(dep_delay, na.rm = TRUE))

#GROUP BY creates the group that will be operated on 
#groups in which we can operate: summarise then according to the groups I've set with group_by 
#basic R approach, quite unreadable:
tapply(flights$arr_delay, flights$dest,mean, na.rm = TRUE) #very hard to be read
#now I can do the following with dplyr
by_dest = group_by (flights, dest) #not different tibble from the original one 
#the ony information in the tibbles is that the next information is about dest variable
summarise(by_dest, delay = mean(dep_delay, na.rm = TRUE))

#also grouping by more variables
by_day = group_by(flights, year, month, day)
summarise(by_day, delay = mean(dep_delay, na.rm = TRUE))
summarise(by_car, across(contains("delay"),))

#TRICKS
#across allows you to apply the same function to multiple columns at once 

#for each car, calculate the maximus values of delays
by_car <- group_by(flights, carrier)
summarise(by_car, across(contains("delay"), ~max(.x, na.rm = TRUE)))
summarise(by_car, flight_count=n())#n() counts the number of rows in a group
#for each carrier I have every info regarding the delay, and the maximum value of delay and so on. 
#powerful command to have syntetic sum about the data with short instructions

by_dest <-group_by(flights, dest) #I'm grouping about destinations, sorting from the greater to the lower 
add_count(by_dest)
tally(by_dest, sort = TRUE) #this adds a column

#CHAINING OR PIPELINING 
#a bit tricky: we need to change our thinking the code. We can see great number 
#of example in the next session 

#three steps to prepare this data: group flights by destinations, summarise to compute distance, ...

by_dest<-group_by(flights, dest)
delay <- summarise(by_dest,flight_count = n(), place_count = n_distinct(tailnum))
#count() and tally() is equivalnet to n()
by_dest<-group_by(flights, dest)
tally(by_dest, sort= TRUE)
delay <- summarise(by_dest,
                   count = n(), 
                   dist = mean(distance, na.rm=TRUE),
                   delay = mean(arr_dealy, na.rm =TRUE)
                   )
#we can add columns as well: with add_count() and add_tally()
by_dest <-group_by(flights, dest)
add_count(by_dest)
delay <- filter(delay, count >20, dest != 0)
#we can order our operation : operation 1 THEN operation 2 THEN operation 3 
group %>% summarise %>% filter 
#if I use this expression then it's the same as writing f(x,y), it's a sort of composing functions. 

#the code is really well written to read what we have done. 
#once the original code required the group day etc, we can chain all the instructions and then print the result  


#all the data manipulation we will do, we will do it this way. 


