# write a python programe to check given umber is "positive" "nagative" or "zero"

# number=int(input("Enter number: "))
# if number > 0:
#     print("positive number")
# elif number<0:
#     print("nagative number")
# else:
#     print("Zero")
 

 # 2. write a programe to find middle number in a group of three numbers
# a=int(input("Enter first number: "))
# b= int(input("Enter 2nd number: "))
# c= int(input("Enter 3rd number: "))

# if (a > b and a < c) or (a < b and a > c):
#     print (f"{a} num is middle number")
# elif (b > a and b < c) or (b < a and b > c):
#     print(f"{b} num is middle")
# else:
#     print(f"{c} num is middle")


# 3. write a programe to calculate total marks in five subjects (full marks =100) 
# as well as percentage of marks and  division as per the following condition.
# percentage>=80 - grade A              percentage>=60 - grade B 
# percentage>=40 - grade C              percentage <40 -grade D

hindi= int(input("enter Hindi marks= "))
english= int(input("Enter English Marks= "))
Maths= int(input("Enter Maths Marks= "))
Pol_sci= int(input("Enter Pol_sci marks= "))
science= int(input("enter science marks= "))

total=hindi+english+Maths+Pol_sci+science
percentage=(total/500)*100
print(percentage)

if percentage>=80:
    print("grade A")
elif percentage>60:
    print("Grade B")
elif percentage>=40:
    print("Grade c")
else:
    print("Grade D")

    