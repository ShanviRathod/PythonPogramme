# Python Program to Find Sum of First n Natural Numbers 

x=1
sum=0
num=int(input("How long do you want to print the sum of n natural numbers?:= "))
while x<=num:
    sum=sum+x
    x=x+1

print(sum,"= sum of natural numbers")