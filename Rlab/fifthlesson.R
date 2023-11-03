#EXERCISE 2: what does this function do?
r01<- function(x) {
  rng<-range(x) #minimum and max of a vector
  (x-rng[1])/(rng[2]-rng[1])
}
r01(c(1:10))

#can we rewrite it in a better way? yes, managing the missing values as well
reshape02<- function(x){
  rng<-range(x,na.rm=TRUE,finite = TRUE) #compute only finite values
  (x-rng[1])/(rng[2]-rng[1])
}
reshape02(c(NA,1:10))

reshape03 <- function(x,na.rm =FALSE, finite=TRUE){
  rng<-range(x,na.rm=TRUE,finite = TRUE) #compute only finite values
  (x-rng[1])/(rng[2]-rng[1])
}
reshape03(c(1,2)) #I don't call parameters so I'm using the default values 


#EXERCISE 3
my_norm <- function(x){
  n<-length(x)
  xmean <-sum(x)/n
  xsd <- sqrt(sum(x^2-xmean^2)/(n-1))
  xnorm<-(x-xmean)/xsd
  return (xnorm)
}
my_norm(c(1:10))
  
#write better: leave all the evaluation via using pre prepared functions 
#I can set another parameter inside the function as well
#we can complicate the function as well 
my_norm<-function(x){
  xnorm<-(x-mean(x))/sd(x)
  return (xnorm)
}
my_norm(c(1:10))
  
my_norm<-function(x,narm =TRUE){
  xnorm<-(x-mean(x,na.rm = narm))/sd(x,na.rm=narm)
  return (xnorm)
}
my_norm(c(1:10, NA,7:10))


#EXPLORE A DATASET AND DO SOMETHING 
#preloaded dataset into R
?airquality #it reports measurements of air quality of NY daily
#use function of ex3 you have written to operate on the dataset 
dates<-as.Date(paste("1973",airquality$Month,airquality$Day,sep = "-"))
id<-which(dates>=as.Date("1973-06-01") & dates<as.Date("1973-08-01"))
my_df<-data.frame(date= dates[id], ozone = airquality$Ozone[id],solar = airquality$Solar.R[id],
                   wind = airquality$Wind[id],temp = -31+airquality$Temp[id]*5/9)
#as.date recognize 5 as May even if it's not 05

boxplot(my_df[c(2:5)])
#no boxplots for dates as they are useless 


my_df2 <- data.frame(data=my_df[,1], apply(my_df[,c(2:5)],2,my_norm, narm=TRUE))#I want to normalize my data col by col 
plot(my_df2)

#I can define a new variable called ozone that has my norm of col ozone in dataframe 
#and another variable and so on. This is the syntetic way to do that
lim<- max(abs(range(my_df2[,c(2:5)],na.rm=T))) #limits of the vertical axis 
plot(my_df2$data,my_df2$ozone,ylim =c(-lim,lim),type = "l",xlab = "Date",ylab = "Values" )
lines(my_df2$data,my_df2$solar,col=2)
lines(my_df2$data,my_df2$wind,col=3)
lines(my_df2$data,my_df2$temp,col=4)
legend("bottomright",legend=c("ozone","solar","wind","temp"),lty =1,col=1:4)
#and more than that I also plot a legend in the bottom line 


#EXERCISE 5
#sequence of time and value associated with this seq
#for each time we have a value associated. 
my_func<- function(date0, time0, date1,time1,dt=3600,tz = "GMT+1"){ #tz stands for time zone
  datetime0<-strptime(paste(date0, time0),format = "%Y-%m-%d %H:%M",tz=tz) #not paste0 because I do want the while space between the two
datetime1<- strptime(paste(date1, time1),format = "%Y-%m-%d %H:%M",tz=tz)
  seqdt<-seq(datetime0,datetime1,by=dt)
  df<-data.frame(times = seqdt,values = as.numeric(seqdt))
  return(df)
}
my_func("2023-10-01","00:00","2023-10-05","12:00")

#EXERCISE 6 (homework)
#using the iris dataset, print two character for each row.
#the first is 'A' if Sepal.Length/Sepal.Width>2, 'B' otherwise
#the second char is 'A' for setosa, 'B' for versicolor, 'C'for virginica

irisdf<-data.frame(iris)
rapp <- rep('A', nrow(irisdf))
for(i in 1:length(rapp)){
  rapp[i]<-ifelse(irisdf[i,"Sepal.Length"]/irisdf[i,"Sepal.Width"]>2,'A','B')
}
type <- rep('A', nrow(irisdf))
for(i in 1:length(type)){
  if(irisdf[i,"Species"]=='versicolor'){
    type[i]<-'B'
  }else if (irisdf[i,"Species"]=='virginica'){
    type[i]<-'C'
  }
}
levels<-paste0(rapp,type)
irisdf<-irisdf[,-c(6,7)]
head(irisdf)
irisdf['levels']<-levels
irisdf
