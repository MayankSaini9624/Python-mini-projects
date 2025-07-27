import time
from time import sleep
print("THIS IS THE STUDENT MANAGEMENT RECORD")
studata={}
while 1==1:
    print("""CHOOSE FROM THE FOLLOWING:
1.ADD A STUDENT,AND HIS/HER MARKS
2.VIEW DATA
3.EXIT""")
    op=int(input("CHOOSE THE PREFRENCE:"))
    time.sleep(3)
    if op==1:
        name=str(input("NAME OF THE STUDENT:"))
        if name.isalpha():
            marks=float(input("ENTER THE MARKS"))
            studata[name]=marks
            print(name,"is added in student database with the marks of",marks)
        else:
            print("ENETR A VALID NAME")
            exit()
        time.sleep(4)    
      
    
    elif op==2:
        print("STUDENT DATABASE")
        for student, marks in studata.items():
            print(f"{student}:{marks}")
    elif op ==3:
        exit() 
    else:
        print("INAVLID CHOICE")              
        exit()



print("THANKS")