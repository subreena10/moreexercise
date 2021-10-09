numberofstudent=int(input("Enter the number no.of students: "))
studentexpenses=int(input("Enter the expenses of student: "))
totalexpense=numberofstudent * studentexpenses 
if studentexpenses<=50000:
    print("we are in budget")
else:
    print("out of budget")