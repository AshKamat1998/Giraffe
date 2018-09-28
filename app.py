# THIS IS STRING CLASS
testString = "Akshaya"
print(testString.upper())
print(testString.lower())
print(testString.islower())
print(testString.isupper())
print(testString.count("a"))
print(testString.casefold())
print(testString[3])
print(testString.index("sh"))
print(testString.replace("sh","KK"))
newString="Akshay is of age:"
age=30
print(newString + " " + str(age))
print(len(newString))
# THESE WERE VARIOUS STRING METHODS
print(testString.isalpha())
testStr2="Akshay123"
print(testStr2.isalpha)
print(testStr2.isspace())
print(testStr2.isdigit())
print(testStr2.isdigit())
print(testStr2.startswith("A"))
print(testStr2.endswith("3"))
print(testStr2.find("p"))
testStr3 = "THIS IS STRING CLASS"
print(testStr3.split())
print(testStr3.split("I"))
p= pow(2,4)
from math import *
print(sqrt(29))
#uName=input("Your Name Please: ")
#uName2=input("Your last Name Please:")
#print(uName +" "+ uName2)
#LISTS
#friends[1]=input("Friends Name: ")
def SayHi():
    print("Say Hi")
SayHi()
def CubeANumber(i):
    return pow(i,3)
s=CubeANumber(98)
print(s)
# Functions:
"""
num1 = float(input("enter first Number:"))
operation=str(input("enter operation:" ))
num2 = float(input("enter second Number:"))
"""
def MyCalc(op1,op2,op3):
    anser=5.98
    if op2 == "+":
        answer = op1+op3
    elif op2 == "-":
        answer = op1-op3
    elif op2 == "X":
        answer = op1 * op3
    elif op2 == "/":
        answer = op1 / op3
    return round(answer)
"""
outnum=MyCalc(num1,operation,num2)
print(MyCalc(num1,operation,num2))
"""
#DICTIONARIES
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}
print(monthConversions["Jan"])
print(monthConversions.get("Feb","Not a valid key"))
# while loop
p=1
while p<=10:
    print(p)
    p=p+1
def RaisedTo(baseNumber,power):
    res=1
    for index in range(power):
        res=res*baseNumber
    return res
print(RaisedTo(3,4))
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10]
]
print(number_grid[0][2])
for row in number_grid:
    for col in row:
        print(col)
'''
Block comment

'''
try:
    res = int(input("Enter a number:"))
    print(res)
except ValueError as err:
    print(err)