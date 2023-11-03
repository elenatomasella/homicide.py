#array and matrix: multiple tables at one time in the first case
#arrays can store data in more than two dimensions 

arr <- array(1:24, dim = c(3,4,2))
arr
arr_ij <- 1:24
arr_ij
name_x <- paste("obs", 1:3,sep = "_")
name_y <- paste( "par",1:4, sep = "_")
name_z<-c("2023-10-01","2023-10-02")

arr<-array(arr_ij, dim =c(3,4,2), dimnames = list(name_x,name_y,name_z))
arr

arr[1,,] #obs_1, all parameters, all dates
arr[,2,] #parameter 2, all observations, all dates 
arr[2,3,] #observation 2, parameter 3, all dates
arr[2,3,2] #observation 2, parameter 3, date 2



#LISTS contain elements of different types like numbers, strings, vectors and another list inside it
#list is created using list() function

list_data <- list("Red", "Green", c(21,32,11), TRUE, 119.1) #mixture of data types
list_data


#take care: list are allowed to have lists or matrices inside as well 
#we can name some variables before and then put them inside a list afterwards as well
list_data <- list(c("Jan", "Feb", "Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2), list("green", 12.3))
names(list_data) <- c("months", "random_matrix", "new_list")
list_data

mon <- c("Jan","Feb","Mar")
mat <- matrix(c(3,9,5,1,-2,8),nrow=2)
lis<- list("green", 12.3)
list_data <- list(list(months = mon, random_matrix = mat, new_list = lis))
list_data

list_data[[2]] #to have the second element we need to use the double brackets 
list_data$new_list #to have the element named new_list of the list 


#there are functions that make you avoid the use of loops for function/array/matrix
arr<- array(c(1:24), dim=c(3,4,2))

#FUNCTION APPLY : for array or matrix 
apply(arr,3,sum) #for (z in 1:2) print(sum[z])
#it will print the sum of the third dimensions "columns", indeed they are two
apply(arr,c(1,2), sum) #matrix dim_1 x dim_2
#in the first row and second column we have three value for the third variable 

#FUNCTION LAPPLY: for lists, it returns a list 
#this function returns a list which has the same length of the list you started from,
#but in every entry you find the result on the function indicated as argument, once applied to the entry
lis <- list(a=1:10,b=sample(1:100,5),c=rep(T,3)) #T=1, F=0
lapply(lis,mean)

#FUNCTION SAPPLY(): for list, it returns a vector, matrix or array
#completely equal to lapply but in this case the outputs are in a vector 
lis <-list(a=1:10, b=sample(1:100,5), c= rep(TRUE,3))
sapply(lis,mean)

#FUNCTION TAPPLY(): for vectors whose elements can be grouped by factors 
#to apply a certain function to every single entry of an array 
vec<-1:23
fac<-factor((1:23%%2)+1,levels=1:2) 
#I have 23 values which are 1 and 2 only and levels which are 1 and 2 only as well, and I want factors 
tapply(vec,fac,sum) #according to this factor sum this values 


#DATA AUGENTATION IN DATA.FRAME: function MERGE 
d1<-data.frame(course = c("Stats","Math", "CompScience"), score=c(30,28,28))
d2<-data.frame(exam = c("Stats", "Physics", "CompScience"), credits=c(6,9,6))
d1
d2
merge(d1,d2,by.x="course",by.y = "exam", all=T)

d1<-data.frame(course = c("Stats","Math", "CompScience"), score=c(30,28,28))
d2<-data.frame(exam = c("Stats", "Physics", "CompScience"), credits=c(6,9,6))
merge(d1,d2,by.x="course",by.y = "exam", all=F)
#if observation is missing in general all the information is missing, 
#but it's important to have all the information available

#HOW TO PLOT THINGS IN R

#SCATTERPLOT: data are displayed as collection of points, each having the value of one variable determining the position 
#on the horizontal axis and the value of the other variable determining the position on the vertical axis 
#LINE CHART: every point is linked with lines
#GRAPH that connects a series of points by drawing line segments between them 

#scatterplot 
airports <- read.table(file ="Airports_2022.csv", header = T, sep = ";")
names(airports)
plot(airports$N,airports$Passengers)

#line chart
plot(airports$N, airports$Passengers, type = "l")

#multi-scatterplot
#I have then multiple scatterplot and the table is telling you what's on x axis and what's on y axis
#this is useful when you don't know anything about the data, this is the first thing to do in order to understand if the variables are correlated
plot(airports)

## plot(v,type, col,xlab,ylab,xlim,ylim, main, asp) and to know all the variables you may write
#v is the vector containing the numeric values, but also a couple of vector can be reported 
#"p" for points, "l" for lines, "o" for both points and lines 
#xlab and ylab are for the label on the axis
#main is for the main title 
#asp is for the aspect ratio (y/x): same scale on the two axes if it's set to be 1 
#col is for the colors of the plot

#many other functions/parameters can be set:
#lwd for line tickness
#lty line type 
#pch point type (symbol)
#cex for point size
#col for colors of objects
#log to have logaritmic scale on the axis 
#xaxt,yaxt omit values on axis
#mar external marging of the plot 
#mfrow, mfcol more then 1 graph in a window in a table 

#basic plots
plot(x= airports$Flights, y = airports$Passengers, main = "flights and passengers",
     xalb = "Number of flights", ylab="number of passengers", col = "red", type = "p", 
     pch=8, cex = 1.5)

plot(airports$Flights, main = "Flights", xlab = "Airport", ylab = "number of flights", 
     col = "red", type = "l")

#HISTOGRAMS 
plot(airports$Flights, main="Flights", xlab = "Airport", ylab = "number of flights", col = "red", type = "h")

plot(airports$Flights, main="Flights", xlab = "Airport", ylab = "number of flights",
     col = "red", log = "y", pch = 19,ylim = c(2,max(airports$Passengers)))#19 means solid points
lines(airports$Flights, col = "green")
abline ( v=3,lty=2)#vertical, dasched 
abline(h=1000,lwd=3)#horizontal, thick
legend("bottomright", legend=c("Passengers", "Flights"), col = c("red","green"), lty = c(NA,1), pch=c(19,NA))#I can also add a legend that contains passengers and flights, ren and green

#we can compose the plot starting from something and adding everything we want then 
#let's complicate again the plot. 

x<-airports$Flights/50000
y<-airports$Passengers/5000000
plot(x,y, main="Flights and Passengers", xlab = "x", ylab = "y",
     col = "green", axes=F)

#I want to add axis: in the first I want to put, corresponding to the mean of x smth and so on. 
#I'm reconstructing the axis in the way I prefer. 
#I can also plot axis 3 and axis 4
axis(1,c(mean(x),0:6), c(expression(bar(x)),0:6))
axis(2,c(mean(y),0:6),c(expression(bar(y)),0:6))#
#I have a line (made of segments) that has as value the maximum value of x and 0, goes to max(x,y) and finish on the max(0,y)
lines(c(max(x), max(x),0),c(0,max(y),max(y)),lty = 2)
lines(c(mean(x),mean(x),0),c(0,mean(y),mean(y)), lty=3)
text(mean(x)+0.3,mean(y),expression((list(bar(x)[n],bar(y)[n])))) #we add a little gap for the text not to be overlab
#cex unit means that the point must be three times the maximal dimension
#the average value of x and the average value of y
points(mean(x), mean(y),pch=4, cex=3, col="red")

#there are many kinds of points we can choose for our points, which correspond to numbers
#here we're seeing long functions having parameters 

#HISTOGRAMS: a bar pot for numerical values 
hist(airports$Flights,xlab="Flights", yab = "Frequency", col = "violetred", main = "Flight")

#sometime it's useful to set the width: breaks(c(0,10000,20000),2999999,4000000000) regular sequence for the first part and then bigger
hist(airports$Flights, xlab = "Flights", yab = "Frequency", main = "flights",
     breaks = c(seq(0,100000,20000),200000,400000))
#we can have the density frequencies instead of the absolute frequencies: on the vertical axis is generic to have frequency
#False to have the density, True for the absolute 
hist(airports$Flights, xlab = "Flights", yab = "probability density", main = "flights",
     breaks = c(seq(0,100000,20000),200000,400000), freq = F)

#multiple plots in a table 1x2
par(mfrow=c(1,2)) #group plots: I'm dividing my windows 
barplot(table(airports$rank),xlab = "rank", ylab = "Frequency", main = "Airport rank")
pie(table(airports$rank), main ="Airport rank")


#boxplot is a graphical rapresentation of quantiles 
boxplot(airports$Passengers)
boxplot(Passengers ~ rank, data = airports) #four boxplots divided by rank with one command only 
?boxplot

#how to choose colors: by labels, by number 1-8, as rbg between 0-255, as hexadecimal
#an also as palettes as there are libraries to take colors from colors() typing 
plot(1:50,1:50,pch = 19, col=grey((1:50)/50))
points(50:1,1:50,pch=19,col =heat.colors(50))
points(rep(25,50),1:50,pch=19,col =rainbow(50))


#WHAT CAN WE DO AS PLOTS IN R? in the webpage we can download the code to have each of those plots 
https://r-graph-gallery.com⁄
#wordcloud is quite common to have on social netoworks or on newspapers for instance 
#even with boxplot: violin boxplot reproduce the distributions 



#EXERCISE

#explore the data set "iris"

#check the class of each variable 
irisdf<- data.frame(iris)
irisdf
View(iris)
head(iris) #first five elements or head(iris, 10) if you want the first 10
names(irisdf)
sapply(irisdf,class)
class(irisdf[,1])
class(irisdf[,2])
class(irisdf[,3])
class(irisdf[,4])
class(irisdf[,5])
str(iris) #to see the type of the columns

#optimized here below 
for (i in 1:ncol(iris)) {
  print(paste("column", names(iris)[i], "has class", sapply(iris,class)[i]))}

apply(iris,2,class) #it's trying to find the type for the entire dataframe so it's not working here
sapply(iris, class)

#subset all rows of Species "virginica" in a new data frame
virginica <- subset(irisdf, Species == "virginica") #this is right
virginica

#create a vector called "sepal.dif" with the difference between "Sepal.length" and "Sepal.width"
sepal.dif<-irisdf$Sepal.Length-irisdf$Sepal.Width #they are vectors of same length so I can manage it this way
sepal.dif

#assign NA to sepal.dif <=3
sepal.dif[sepal.dif<=3] = NA
sepal.dif
#evaluate minimum, maximum, mean value of sepal.dif (with missing values)
min(sepal.dif)
max(sepal.dif)
mean(sepal.dif)

#it makes sense to remove the not observed values 
min(sepal.dif, na.rm = T) 
max(sepal.dif, na.rm = T)
mean(sepal.dif, na.rm = T)

#we can also ask for the range
range(sepal.dif,na.rm =T)

plot(iris)
#it's useful to make us understand where's there is correlation and where not
plot(iris$Sepal.Length)
plot(iris$Sepal.Length,col = factor(iris$Species)) #different colours fot different species
plot(iris$Sepal.Length,col = factor(iris$Species),pch=19) #changing the tyoe of points (sort of font)
plot(iris$Sepal.Length,col = factor(iris$Species),pch=19, ylim=c(3,9)) #restrict the y axis
plot(iris$Sepal.Length,col = factor(iris$Species),pch=19, ylim=c(3,9),
     xlab = "",ylab = "Length", main="IRIS") #add names of axis and the main title

abline(h=mean(iris$Sepal.Length), lwd = 2,col = "mediumorchid3") 
#add an horizontal line correspondent to the mean of the sepal length
#lwd stands for line width, while col stands for the colour of the line

abline(a=4.5,b=0.02,col=4)
#add a line of colour corresponding to the four, where a and b are the intercept and the slope 

legend("topleft", legend = c("mean", "line(a=4.5,b=0.02)"),lty=c(1,1),lwd=c(2,1),col = c("mediumorchid3",4))

plot(iris$Sepal.Length,iris$Petal.Length,pch=19,xlab="Sepal",ylab="Petal", 
     main="Lenght", col = iris$Species)
xmean <-tapply(iris$Sepal.Length,iris$Species, mean)
ymean<-tapply()



barplot(table(iris$Species))

iris2<-iris[-sample(1:150,30),]
barplot(table(iris2$Species))
#generate a set of appropriate descriptive plots 
boxplot()
plot(iris$Sepal.Length,iris$Sepal.Width, main = "Length and Width", xlab = "Lenght", ylab = "Width",
     type = "h")
hist(iris$Length, xlab="Species of iris")

boxplot(iris) #last box doesn't make sense so we need the following 
boxplot(iris[,1:4])
