print("This is the report card for GOVT SR. SEC. SCHOOL ,JAIPUR (RAJ.)")
marks_of_hindi=int(input("ENTER THE MARKS OF HINDI:"))
if(marks_of_hindi not in range(0,101)):
    print("INVALID MARKS")
    exit()
marks_of_eng=int(input("ENTER THE MARKS OF ENGLISH:"))
if(marks_of_eng not in range(0,101)):
    print("INVALID MARKS")
    exit()
marks_of_phy=int(input("ENTER THE MARKS OF PHYSICS:"))
if(marks_of_phy not in range(0,101)):
    print("INVALID MARKS")
    exit()
marks_of_chem=int(input("ENTER THE MARKS OF CHEMISTRY:"))
if(marks_of_chem not in range(0,101)):
    print("INVALID MARKS")
    exit()
marks_of_math=int(input("ENTER THE MARKS OF MATHS:"))
if(marks_of_math not in range(0,101)):
    print("INVALID MARKS")
    exit()
obtained=marks_of_chem+marks_of_eng+marks_of_hindi+marks_of_phy+marks_of_math
percentage=(obtained/500)*100
print("Marks obtained in Hindi",marks_of_hindi)
print("Marks obtained in English",marks_of_eng)
print("Marks obtained in Physics",marks_of_phy)
print("Marks obtained in Chemistry",marks_of_chem)
print("Marks obtained in Math",marks_of_math)
print("Group name - Science")
print(percentage,"%")
print("TOTAL",obtained)
if (marks_of_chem < 30 or marks_of_eng < 30 or marks_of_hindi < 30 or 
    marks_of_math < 30 or marks_of_phy < 30):
    print("FAILED","GRADE-F")
else:
    if percentage >= 60:
        print("Passed by 1st division","GRADE- A")
    elif 45 <= percentage < 60:
        print("Passed by 2nd division","GRADE-B")
    elif 33 <= percentage < 45:
        print("Passed by 3rd division","GRADE-C")
    else:
        print("IMPROVEMENT NEEDED","GRADE-D")

print("""SIGN
            SIGNATURE VALID""")
