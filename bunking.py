import math
print("College Bunking Assistant")
n=int(input("Enter total no.of subjects: "))
f=True
limit=int(input("Enter the minimum required attendance(in %): "))
subjects=[]
Classes={}
Current={}

for i in range(1,n+1):
    sub=input(f"Enter subject {i}: ")
    subjects.append(sub)


for i in range(1,n+1):
    sub=subjects[i-1]
    hours=int(input(f"Enter total no.of hours for subject {subjects[i-1]}: "))
    Classes[sub]=hours


for i in range(1,n+1):
    sub=subjects[i-1]
    hours=int(input(f"Enter no.of hours completed for subject {subjects[i-1]}: "))
    Current[sub]=hours

attendance={}


for i in range(1,n+1):
    present=int(input(f"Enter the number of classes attended for subject {subjects[i-1]}: "))
    sub=subjects[i-1]
    attendance[sub]=present


def bunking(course):

    print("These are the subjects present: ")
    print(subjects)
    user_sub=input("Enter the subject you need assistance in bunking: ")

    current_attendance=attendance.get(course)
    bunk=int(Current.get(course))-int(current_attendance)
    total_bunk=math.floor((100-limit)*Classes.get(course)/100)
    res=total_bunk-bunk
    if(res>0):
        print(f"You can bunk {res} more hours in this subject!")
    else:
        print("Sorry! You cannot bunk any more for this subject")



while(f==True):
    flag=input("Do you need any assistance(Y/N): ")
    if(flag=="Y"):
        f=True
    else:
        f=False
        break
    print("These are the subjects present: ")
    print(subjects)
    user_sub=input("Enter the subject you need assistance in bunking: ")
    bunking(user_sub)
