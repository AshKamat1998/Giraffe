### This code was written for reference purpose only. nostarchpress/pythoncrashcourse###
# Initial Program
print("Hello World")
msg = "Hello World"
print(msg)
# Concatenation
print("Hello " + "World")
print("You have " + str(1000000) + " USD")

# LIST STRUCTURES'
bikes = ['A', 'B', 'C', 'D', 'E']
newbikes = bikes.reverse()
print(newbikes)
for bike in bikes:
    print(bike)
print(bikes[1])
print(bikes[:2])
print(bikes[2:])    # Print last 3 items in the list
print(bikes[1:4])   # Print sliced items in the list
print(bikes[-1])    # Print last item in the list
bikes.append('G')  # append takes only one argument
    ## Numerical Lists
squares=[]
for x in range(1,10):
    squares.append(x**x)
print(squares)
reversesquares=sorted(squares,reverse=True)
print(reversesquares)
newlist = squares[:]  # Copying a list
print(newlist)
## This code removes duplicate items from a list
origlist = bikes[:]
origlist.append("A")
origlist.append("C")
print(origlist)
cleanedbikes = []
for bike in bikes:
    if cleanedbikes.__contains__(bike):
        pass
    else:
        cleanedbikes.append(bike)
print(cleanedbikes)
cleanedbikes = []
for bike in bikes:
    if bike not in cleanedbikes:
        cleanedbikes.append(bike)
print(cleanedbikes)
##-------------------------------------------------
## TUPLE:
dimensions = (1200, 1300)
##================================================
## if statement
##yourage = float(input("What is your age:  "))             ##  int(input("What is your age:  "))
##yoursex = input("What is your sex:  ").capitalize()
###
yourage = 5
yoursex="M"
if yourage < 5 and yoursex == "M":
    print("You are male kid")
elif yourage <= 10 and yoursex == "M":
    print("You are male adult")
elif yourage >=25 or yoursex == "F":
    print("You are female")
else:
    print("You are female kid")
###
## DICTIONARIES:
alien = {'color': 'green', 'points': 5}
alien['xpos'] = 23
print(alien)
resulttable = {'A': 17, 'B': 23, 'C': 28, 'D': 24, 'E': 18, 'F': 18, 'G': 16, 'H': 17}
resulttable["I"] = 45
#student = input("Student Name: ")
student = "A"
print("Student  " + student + "secured  " + str(resulttable[student]))
for student, marks in resulttable.items():
    print(student, marks)
for student in resulttable.keys():
    print("Student " + student + " secured " + str(resulttable[student]))
print(resulttable.values())

###         LOOPING
### WHILE
x=0
while x <= 10:
    print(x)
    x += 1
### Data Structures nesting
### Creating a list of dictioneries:
### creates an empty list, adds two dictioneries to the list and prints it
users = []
resulttable2 = {'i': 17, 'j': 23, 'k': 28, 'l': 24, 'm': 18, 'n': 18, 'o': 16, 'p': 17}
users.append(resulttable)
users.append(resulttable2)
print(users)
for result_dict in users:
    for name,marks in result_dict.items():
        print(name + " : " + str(marks))
        print("\n")
users = []
users = [resulttable,resulttable2]
for result_dict in users:
    for name,marks in result_dict.items():
        print(name + " : " + str(marks))
###
stu1 = "xxx"
stu1l = ["Eng", "Math", "Progr"]
stu2 = "yyy"
stu2l = ["Geog","Hist"]
studict = {stu1 : stu1l, stu2 : stu2l}

for stu, langs in studict.items():
    print(stu +" : ")
    for lang in langs:
        print("-" + lang)


import UserFunctions as UF
user = ["X", "Y", "Z"]
UF.greet_users(user)
em_user=[]
UF.print_model(user,em_user)
print(user)
print(em_user)

user = ["X", "Y", "Z"]
UF.greet_users(user)
em_user=[]
UF.print_model(user[:],em_user)  ## Passing a list with [:] prevents function from modifying it.
print(user)
print(em_user)
import Class
car_1 = Car("Toyota", "Camry", 2015)
