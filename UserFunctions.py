def function1(iname="Ash"):
    print(iname)

def returnFullName(fname,lname):
    return fname + " " + lname

def greet_users(names):
    for name in names:
        print("Hello " + name+ "\n")

def print_model(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print("Printing  " + current_model)
        printed.append(current_model)