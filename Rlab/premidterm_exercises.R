#for the exams: dates, for, while 

#DATES: brief review

today<-as.Date("2023-10-24")
today
format(today, "%A, %B %Y")
datetime<-"2023-10-24 09:00"
datetime2<- today +1
dttm1<- strptime(datetime, format = "%Y-%m-%d %H:%M", tz = "UTC")
dttm2<-dttm1+3600*24
dttm2
dttm1+4

seq(from=as.Date("2023-10-24"),to = as.Date("2023-12-07"), by = "day")
seq(from=as.Date("2023-10-24"),to = as.Date("2023-12-07"), by = "week")
seq(from=as.Date("2023-10-24"),to = as.Date("2023-12-07"), by = "year")
seq(dttm1, dttm2, by = "hour")
seq(dttm1, dttm2, by = "minutes")

weekdays(dttm1)
months(dttm1)

as.numeric(dttm1)

#EXERCISE 1
shipping_book<-function(cost, number,shipping_cost){
  if (number<100){
    return (number*cost+shipping_cost)
  }else{
    return (number*cost)
  }
}
shipping_book(10,55,2)

#trick1
shipping_book<-function(cost, number,shipping_cost){
  if (number<100){
    (number*cost+shipping_cost) #it returns it if is the last function
  }else{
    (number*cost)
  }
}

#trick2
shipping_book<-function(cost, number,shipping_cost){
  cost*number+ifelse(number<100,shipping_cost,0)
}


#EXERCISE 2
is_palindrome <-function(string){
  nc<-nchar(string)
  palindrome<-""
  for (c in nc:1){
    lett_c <-substr(string,c,c)
    palindrome<-paste0(palindrome, lett_c)
  }
  if (string==palindrome){
    print(paste(string,"IS PALINDROME"))
  }else{
    print(string, "IS NOT PALINDROME")
  }
  }
is_palindrome('anna')

#optimize: do not consider spaces or puntuaction
string<-"the hot sun"
string<-tolower(string) #to delete 
string<-gsub(" ","",string)
string<-gsub(",","",string)

#trick1
stringsplit(string,"") #it separates all the letters and put it in a list
palindrome <- paste(unlist(strsplit(string,""))[nc:1],collapse="")

#my solution
is_palindrome<-function(string){
  i<-1
  while (i<=nchar(string)){
    if (substr(string,i,i)==substr(string,nchar(string)-i+1, nchar(string)-i+1)){
      j<-i
      i<-i+1
    }else{
      j<-0
      i<-nchar(string)+1
    }
  }
  if (j==nchar(string)){
    "palindrome"
  }else{
    "not palindrome"
  }
}

is_palindrome("anna")
is_palindrome("bookclub")



#EXERCISE 3
no_dup<-function(v){
  v1<-v[1]
  for (i in 1:length(v)){
      if (!(v[i] %in% v1)){
          v1<-c(v1,v[i])
        }
  }
  return (v1)
  }
v <-c(1,5,3,4,3,2)
no_dup(v) 

#official solution
elements<-c(1,6, 1:10)
elements_nodup<-elements[1]
for (e in 2:length(elements)){
  id<-which(elements[1:(e-1)]==elements[e])
  if (length(id)==0) elements_nodup<-c(elements_nodup, elements[e])
}
elements


?as.Date


#EXERCISE 4
about_dates<-function(year,month,day,n){
  my_date<- as.Date(paste(year,month,day, sep = "-"))
  seqdate <- seq(my_date, by ="day", length.out=n+1)
return(seqdate[n+1])}
about_dates(2023,10,23,20)

#trick1
about_dates<-function(year,month,day,n){
  my_date<- as.Date(paste(year,month,day, sep = "-")) +n
  return(my_date)}
about_dates(2023,10,23,20)



#EXERCISE 5 
n<-100
primes<-c()
if (n<1){
  "None"
}else{
primes<-c(2)
k<-1
while (length(primes)<n){
  i<-1
  while (i<length(primes) & (primes[length(primes)]+k)%%primes[i]!=0){
    i<-i+1}
  if(i!=length(primes)){
        k<-k+1
      }else{
        i<-1
      primes<-c(primes,primes[length(primes)]+k)
      k<-1
    }
}
}

primes

#official solution
N<-100
prime <-c(2)
start<-2
while (length(prime)<N){
  start<-start+1
  div<-start%%prime
  if (min(div)>0) prime<-c(prime, start)
}
cbind(1:100,prime)

#EXERCISE 8
common_values<-function(v1,v2){
  v3<-c()
  for (i in v1){
    if (i %in% v2){
      v3<-c(v3, i)
    }
  }
  unique(v3)
}
v1<-c(3,4,5,6,4)
v2<-c(3,4,2,23,4)
common_values(v1,v2)
