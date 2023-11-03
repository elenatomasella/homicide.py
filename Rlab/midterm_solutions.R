#midterm exam correction 
#EXERCISE 1
#write an R function that takes as input 3 integers (year, month, day) and 
#returns the number of days to the day of the same years 
days_to_the_end <- function(year, month,day){
  input_date <-as.Date(paste(year, month,day, sep = "-"))
  dec31<-as.Date(paste(year, 12,31,sep = "-"))
  return(as.numeric(dec31-input_date))
}
day<-2
month<-11
year <- 2023
days_to_the_end(year, month, day)

#OTHER SOLUTION
days_to_the_end<-function(year,month, day){
  input_date<-as.Date(paste(year, month, day, sep = "-"))
  dec31<-as.Date(paste(year, 12,31,sep = "-"))
  seqdays<-seq(input_date,dec31,by = "day")
  days_to_dec31<-length(seqdays)-1
  return(days_to_dec31)
}
days_to_the_end(year, month, day)


#EXERCISE 2
#write an R function that returns the final mark of this test using as input the number of correct 
#answers in theoric questions as well as in exercises
grade2 <-function(th, py1,py2,R1,R2){
  totpoint<- 2*th+py1+py2+R1+R2
  grade <-"not sufficient"
  if (totpoint>30){
    "cum laude"
  } else if (totpoint<18){
    grade
  }else{
    totpoint
  }
}
grade2(8,2,4,2,0)

grade3<- function(result_vector){
  th<result_vector[1]
  py1<-python_vector[2]
  py2<-result_vector[3]
  R1<-result_vector[4]
  R2<-result_vector[5]
  if ...
}