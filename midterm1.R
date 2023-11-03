remaining <- function(year, month, day){
today <-as.Date(c(year,month,day)), "%Y-%m%d" )
return (seq(from = today, to = as.Date(c(year,12,31), "%Y-%m%d")))
}


#ex2
score<-function(theory, ex1,ex2,ex3,ex4){
  mark <- theory+ex1+ex2+ex3+ex4
  if (mark<18){
    "not sufficient"
  }  else if (mark>=18 &mark<=30 ){
    mark
  }else{
    "cum laude"
  }
}

score(10,2,4,2,4)
score(10,0,0,0,0)
score(10,2,4,2,4)
