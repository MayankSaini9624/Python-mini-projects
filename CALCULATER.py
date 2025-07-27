print("THIS A CALCULATOR THAT I HAVE BUILD USING PYTHON")
print("""Press
                1. Addition
                2.Substraction
                3.Multiplication
                4.Divide
                """)
press=int(input("ENTER YOUR PREFFRENCE:"))

if(press>=5):
     print("DON'T YOU HAVE MIND")
else:
     dig1=float(input("digit1:"))
     dig2=float(input("digit2:"))

if(press==1):
    print("ADD=", dig1+dig2)
elif(press==2):
    print("SUB=", dig1-dig2)
elif(press==3):
    print("MULTIPLY=", dig1*dig2)
elif(press==4):
    if(dig2 !=0):
            print("DIVIDE=", dig1/dig2)
    else:
         print("CAN'T DIVIDE BY 0")  


else:
    print("INVALID")


print("END OF THE CODE")