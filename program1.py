# write a python programme to check given umber is "positive" "nagative" or "zero"
number=int(input("Enter number: "))
if number > 0:
    print("positive number")
elif number<0:
    print("nagative number")
else:
    print("Zero")
 

 # 2. write a programmer to find middle number in a group of three numbers
a=int(input("Enter first number: "))
b= int(input("Enter 2nd number: "))
c= int(input("Enter 3rd number: "))
if (a > b and a < c) or (a < b and a > c):
    print (f"{a} num is middle number")
elif (b > a and b < c) or (b < a and b > c):
    print(f"{b} num is middle")
else:
    print(f"{c} num is middle")