list1 = ["Ash", "Aditi", "Akshay"]
list2 = [1.2, 2.3, 3.4]
list3 = ["Ash", 1.2]
list1.append("XXX")

print(list1)
print(list1[1])
print(list2[1:3])
del (list2[1])
print(list2)
print(len(list1))
print(list1 + list2)
for x in (list1 + list2):
    print(x)

print(list1.index("Aditi"))
list1.insert(1, "Shilpa")
print(list1)
squares = []
for x in range(1, 11):
    squares.append(x ** 2)
print(squares)
print(squares[:2])
print(squares[2:])
print(squares[-2:])
kamat_family = {"Ash": 1967, "Aditi": 1996, "Akshay": 2005}
for name in kamat_family.keys():
    print(name)
for values in kamat_family.values():
    print(values)
for name, value in kamat_family.items():
    print(name + " birthyear is:  " + str(value))

writeFile2 = "wFile.txt"
with open(writeFile2, 'w') as file_object:
    for name, value in kamat_family.items():
        file_object.write(name + "   " + str(value))
        file_object.write("\n")
list1 = list(range(1,101))
print(list1)
print(min(list1))
print(list1[:3])
print(list1[2:5])

def returnFullName(fname,lname):
    return fname + " " +  lname
    

y=returnFullName("Ash", "Kamat")
print(y)