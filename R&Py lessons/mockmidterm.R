#TAKE CARE: 
#1) if you want to directly print an object once you are defining it, then
#you should write the assignment into brackets
#2)the R type for strings is characters
#3)vectors are homogeneous for types, while lists are eterogeneous
#Same difference between matrices and arrays
#4)while in Python we use range(star,stop,step), in R there is seq(start,stop,step,lenght.out=tot)
#5)the filtering of elements can be done with any(), all(), ==, via indexes,

#Define the min_max function that has 3 integers as parameters, 
#and that calculates the sum of the lesser and the greater. 
a<- 4
b<- 7
c<- 2
min_max = function(a,b,c){
  return (max(a,b,c)+min(a,b,c))
  }
min_max(a,b,c)

#Define the plus_minus function which takes 3 numbers as parameters 
#and returns the sum divided by 2 if the sum is less than 100, the sum divided by 5 if greater.
plus_minus =function(a,b,c){
  if (a+b+c<100){
    return ((a+b+c)/2)
  }else{
    return ((a+b+c)/5)
  }
}
plus_minus(44,66,22)
plus_minus(22,33,11)

#Define the function first_last that has as parameter a list 
#and returns the sum of the first and last elements
first_last = function(lst){
  return (lst[[1]]+lst[[length(lst)]])
}
first_last(list(1,4,5,6,2))

#Define the calculator function that has as parameter two integers and a character 
#(of the type +,-,*,/ in a string, so in inverted commas) and returns the result 
#of the appropriate operation.
calculator = function(n,m,s){
  if (s=="+"){
    return (n+m)
  }
  if (s=="-"){
  return (n-m)
  }
  if (s=="*"){
    return (n*m)
  }
  else{
    return (n/m)
  }
}
calculator(4,5,'/')

#The first two years of a dog are equal to 11.5 human years each. 
#From the third are equal to 5 human years each. Write the function 
#canine_years_count(integer) which takes an integer representing the number of 
#canine years as parameter and prints out the equivalent in human years. (The result should always be a float).
canine_years_count=function(integer){
  if (integer<=2){
    return (integer*11.5)
  }else{
    return ((integer-2)*5+23)
  }
}
canine_years_count(2)
canine_years_count(4)

#Write the function shipping_book that takes as input a floating point number (float) 
#and two integers that represent respectively: the cost of a book; the number of copies purchased;
#the shipping cost of the entire order, to be applied only if the number of copies purchased is less than 100.
#The function calculates and prints the total cost of the purchase order.
shipping_book = function(c,n,s){
  if (n<100){
    return (s+c*n)
  }else{
    return (c*n)
  }
}
shipping_book(10,5,2)

#Write a function celsius_to_fahr that reads from input an integer number 
#representing a temperature in degrees Celsius and returns the converted value 
#in degrees Fahrenheit. value converted to degrees Fahrenheit. The formula for 
#calculating degrees Fahrenheit from Celsius is as follows: F = (C * 9/5) + 32
celsius_to_fahr = function(degrees){
  print(paste("the degrees in Fahr is", (degrees*9/5)+32))
}
celsius_to_fahr(22)

#Write a function find_name that reads from input an name and a list of strings 
#and returns the string "Yes" if name is present in the list "No" otherwise
find_name = function(name, list){
  if (name %in% list){
    print("Yes")
  }else{
    print("No")
  }
}
find_name("elena", list('elena','mamma','Giulio','papà'))


#Write a function vote that takes as parameter a vote (number) and translate it 
#in a judgement (a string). Vote less than 18 is "Not sufficient", less than 22 
#is "Sufficient", less than 25 is "Good", less than 28 is "Great", 28 or more is "Excellent".
grades = function(vote){
  if (vote<18){
    print("Not sufficient")}
  else if (vote<22){
    print("Sufficient")}
  else if (vote<25){
    print("Good")}
  else if (vote<28){
    print("Great")
  }else{
    print("Excellent")}
}
grades(22)
grades(25)
grades(30)


#Define the function count_num_characters that has as parameter a number n and 
#that takes as input the same number n of strings returning the sum of the 
#characters (if n=3 and as input I have 'hello', 'home', 'Luiss' then it returns 14).

string1<-'anna'
string2<-'sole'
string3<-'koala'
total_char<-function(string1, string2, string3){
  l<-0
  for (i in c(string1,string2,string3)){
  l<-l+nchar(i)
  }
  return (l)
}
total_char(string1,string2,string3)


#all prime numbers in a given range
N<-100
print(2)
for (i in 2:N){
  if(min(i%%(2:(i-1))>0)){
    print(i)
  }
}
