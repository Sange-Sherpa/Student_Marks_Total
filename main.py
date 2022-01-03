num = int(input("Enter number of students whose value is to be entered: "))


def marks(names):
    js = int(input("Enter marks of " + names + " for JavaScript: "))
    dbms = int(input("Enter marks of " + names + " for DBMS: "))
    os = int(input("Enter marks of " + names + " for OS: "))
    maths = int(input("Enter marks of " + names + " for Maths: "))
    se = int(input("Enter marks of " + names + " for SE: "))
    print("Total Marks of " + names + " is:", js + dbms + os + maths + se)


for i in range(num):
    if i != (num-1):
        marks(str(input("Enter name of student: ")))
        print("\n")
    else:
        marks(str(input("Enter name of another student: ")))
