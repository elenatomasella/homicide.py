#this is a comment 
#all strings after the hash have no effect on the console 

#here we print a number
2

#we perform our first calculation
2+3

#we calculate a log and we try to be e a little creative in the base of it

log(2)
log(2,10)
log(2, base = 5)

#how to store an object 
x<- 34
y<-16
z<-x+y
w<-y/x

#check the value of x
x

#to store and print an object 
(c<- z+w)

#there are different ways to do an assignment 
x<- "Pippo" #strings
123456->y #right arrow 
xx=x #also the equal could be used but it's good to use it for parameters only 

#FUNCTIONS
#functions in R are very similar to the ones in Python and indeed the refer to
#the mathematical definition of a function 

function_name <- function(arg1, arg2, ... ){
  #list of instructions
  #...
  return(out1, out2, ...)#outputs
}


#useful knowledge to have: there are already implemented functions in R as sd
sd #standard deviation 

##function (x,na.rm = FALSE)
##sqrt (var(if(is.vector(x) || is.factor(x)) x else as.double(x),
## na.rm = na.rm)

mad #median absolute deviation

##read the code on the slides if you're curious

##FUNCION FOR THE THE AREA OF A CIRCLE OF GIVEN RAY
circle_area <- function(r){area<- pi*r^2 
return(area)}
circle_area(3)

#FUNCTION OF AREA AND PERIMETER OF A RECTANGLE
rect_area <-function(a=2,b=3){
  area = a*b
  per = 2*(a+b)
  return (c(area, per))
}
rect_area()

getwd()
