import math
print("College Bunking Assistant")
n=int(input("Enter total no.of subjects: "))
limit=int(input("Enter the minimum required attendance(in %): "))
subjects=[]
Classes={}
for i in range(1,n+1):
    sub=input(f"Enter subject {i}: ")
    subjects.append(sub)
for i in range(1,n+1):
    sub=subjects[i-1]
    hours=int(input(f"Enter total no.of hours for subject {subjects[i-1]}: "))
    Classes[sub]=hours
attendance={}
for i in range(1,n+1):
    present=int(input(f"Enter the number of classes attended for subject {subjects[i-1]}: "))
    sub=subjects[i-1]
    attendance[sub]=math.ceil((present/Classes[sub])*100)
print("These are the subjects present: ")
print(subjects)
user_sub=input("Enter the subject you need assistance in bunking: ")


def bunking(course):
    current_attendance=attendance.get(course)
    bunk=limit-current_attendance
    if(limit<=0):
        print("Sorry!You cannot bunk any more classes in this subject.")
    else:
        res=math.floor((bunk/100)*Classes.get(course))
        print(f"You can bunk {res} more classes in {user_sub} this semester")


bunking(user_sub)
