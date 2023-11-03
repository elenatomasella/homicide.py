#EXERCISES FOR THE MIDTERM

#ex1
for (i in 1:29){
  cat(paste0(i," -- ")) #this is used to concatenate the outputs
}

#ex2
names<-c('Marco','Antonia','Federica','Alessandro','Luca')
for (i in names){
  print(paste(i,"consists in", nchar(i), "characters"))
}

#ex3
i <- 1
set.seed(5)
while (rem>0){
  sam<-sample(1:100,1)
  rem<-sam%%10
  print(paste("Sample = ", sam, "Remainer =", rem))
}

#ex3
zeta<-c(1,7)
for (z in zeta){
  if (z>5){
    y<-z
  }else{
    y<--z
  }
  print(paste("z = ", zeta, "-- y = ", y))
}

#ex4: calculate the weighted average of your marks 
marks <- list(c(27,6),c(28,7),c(29,5),c(22,8))
j<-0
n<-0
for (i in marks){
  j <- j+i[[1]]*i[[2]]}
for (i in marks){
  n<-n+i[[2]]
}
wmean <- j/n
wmean

#ex5
Fib <- c(0,1)
length(Fib)
n<-6
while (length(Fib)<n){
  Fib<-c(Fib, Fib[length(Fib)]+Fib[length(Fib)-1])
}
print(Fib)
print(subset(Fib,Fib%%2!=0))

#ex6
subset(df,b<5)
subset(df,c=='mum')

#ex7: examples with datadrame iris
data(iris)
is.data.frame(iris)
head(iris,5)

#ex8: examples with dataframe mtcars
data(mtcars)
is.data.frame(mtcars)
head(mtcars, 6)

#ex9: mtcars a column 
data(mtcars)
x<-1:4
y<-sample(x,nrow(mtcars),replace = T) #sample a rank value for each model
rank <- factor(y) #to have a categorical variable 
levels(rank)<-c('A','B','C','D')
mtcars$rank<-rank
mtcars

#ex10
mean(mtcars$mpg, na.rm=TRUE) #for numerical parameters I can use many statistical functions 
range(mtcars$cyl, na.rm = TRUE)
min(mtcars$hp)
max(mtcars$wt)
table(mtcars$rank) #to get frequency distributions for categorial variables 


#ex11
iris<-data.frame(iris)
sapply(iris, class)
irisvirginica<-subset(iris, Species == 'virginica')
sepal.dif <-irisvirginica$Sepal.Length-irisvirginica$Sepal.Width
for (i in 1:length(sepal.dif)){
  if (i<=3)
    sepal.dif[c(i)]<-NA
}
sepal.dif
min(sepal.dif, na.rm=TRUE)
max(sepal.dif,na.rm=TRUE)
mean(sepal.dif,na.rm=TRUE)


#ex12
swiss<-data.frame(swiss)[c(1,2,3,10,11,12,13),c('Examination','Education','Infant.Mortality')]
swiss['Sarine',]$Infant.Mortality<-NA
Total <- sapply(swiss, sum)
swiss[nrow(swiss)+1,] <- Total
row.names(swiss)[nrow(swiss)]<-'Total'
proportions <- c()
for (i in swiss$Examination[-c(nrow(swiss))]){
  proportions <-c(proportions, i/swiss['Total','Examination'])
}
proportions


#ex13: merge of differnt dataframes
d1<-data.frame(course=c( "optimization", "sviluppi", "metodi"), score = c(28,32,32))
d2 <- data.frame(exam =c("optimization","finanza", "metodi"), credits = c(6,6,6))
merge(d1,d2,by.x = "course",by.y="exam",all=TRUE)
