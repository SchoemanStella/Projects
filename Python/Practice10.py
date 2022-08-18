1# a program that recieves the raduis of a circle and shows the diameter
from math import pi
r = float(input("enter raduis of circle"))
print("radius of circle:" + str(r) + "is:" + str(pi * r**2))

print("....................................................")

2# 3 integres and says "biggest" and "lowest"
num1= float(input("enter 1st number"))
num2=float(input("enter 2nd number"))
num3=float(input("enter 3rd number"))

if num1 > num2 : 
    highest = num1
else: 
    high = num2
if num3 > high: 
    high = num3

    print("The highest number/n is: " + str(high))

3# Write a program that generates a random integer number between 1 and 10, and through conditional tests you have to guess what number this is. 
import random 
from tkinter.messagebox import showerror

print("")
selected_guessed_number =random.randint(1,10)
guessed_number= int(int("Enter your guess of number"))
print("")

if guessed_number != selected_random_ : 
 print("Sorry you are wrong")
 print ("The correct answer was " : +str(selected_random_number))
else:
    print("Congratulations you were right <3")

4# Write a program that asks the user how many students are in his classroom
students_count= 0
students_grades_sum= 0
average = 0

number_of_students = int(input("How many students are in class?"))

print("")
while students_count < number_of_students : 
    students_grades = int(input("Enter the student grades: "))
    students_grades_sum = students_grades_sum +students_grades
    student_count = students_count + 1

avrage = students_grades_sum / number_of_students
print(str(avrage))
print("")

5#Write a program called PrintNumberInWord which prints "ONE", "TWO",... , "NINE", "OTHER" if the int variable "number" is 1, 2,... , 9, or other, respectively
print("")

mark =float(input("pEnter your mark : "))

print("")

if mark >= 50 :
    print("PASS")
else:
    print("FAIL")

print("")
print("Done")
print("")

6# Write a program called PrintNumberInWord which prints "ONE", "TWO",... , "NINE", "OTHER" if the int variable "number" is 1, 2,... , 9, or other, respectively. 

from ast import match_case

print("")
number = int(input("Any number :"))

print("")

match number : 

    case 1: print("One")

    case 2:print("Two")

    case 3:print("Three")

    case 4:print("Four")

    case 5:print("Five")

    case 6:print("Six")

    case 7:print("Seven")

    case 8:print("Eight")
    
    case 9:print("Nine")

    case _:  print("Other")

print("")

9# Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s raise should also be reported
print("")
#get rating
rating = float(input("Eneter rating : "))
employe_raise = 2400.00

#test what rating is

if rating == 0.0 :
    employe_raise = 2400.00* rating
    print("Unaccepable performance")
    print("Employes raise; $" str(employe_raise))

if rating ==0.4: 
    employe_raise = 2400.00* rating
    print("Unaccepable performance")
    print("Employes raise; $" str(employe_raise))

if rating>=0.6
    employe_raise = 2400.00* rating
    print("Unaccepable performance")
    print("Employes raise; $" str(employe_raise))

if (rating < 0.4 ) and (rating > 0.0) :
    print ("Invalid")

if (rating < 0.6 ) and (rating > 0.4)
    print("Invalid ")


