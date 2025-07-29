import math
print("-"*30)
print("THIS IS A CALCULATOR THAT I HAVE BULID USING PYTHON")
print("-"*30)    
while True:
    print("-"*30)
    print("""SELECT:
1.NUMERIC EXPRESSION,
2.SQUARE AND SQUARE ROOT,
3.CUBE AND CUBE ROOT,
4.FACTORIAL,
5.EXIT THE CALCULATOR""")
    print("-"*30)
    print("-"*30)
    option=int(input("INPUT THE PREFRENCE:"))
    if(option==1):
        while True:
            n=str(input("ENTER THE VALUE TO EVALUATE(or done to stop) :"))
            if(n=="done"):
                print("YOU CHOOSE TO EXIT")
                break
            else:
                try:
                    print(eval(n)) 
                except:
                    print("invalid expression")
    elif(option==2):
        while True:
            s=int(input("SELECT:\n1.SQUARE,\n2.SQUARE ROOT,\n3.EXIT:"))
            if(s==1):
                while True:
                    print("-"*30)
                    a=int(input("ENTER:\n1.SQUARE,\n2.EXIT:"))
                    if(a==1):
                        print("-"*30)
                        print("YOU CHOOSE TO EVALUATE SQUARE")
                        n=int(input("ENTER THE VALUE TO EVALUATE :"))
                        try:
                                print(n*n) 
                                print("-"*30)
                        except:
                                print("-"*30)
                                print("invalid expression")
                                print("-"*30)   
                    elif(a==2):
                            print("-"*30)
                            print("YOU CHOOSE TO EXIT")
                            print("-"*30)
                            break
                    else:
                        print("-"*30)
                        print("somthing went wrong")
                        print("-"*30)
                        break
            elif(s==2):
                while True:
                    b=int(input("ENTER:\n1.SQUARE ROOT,\n2.EXIT\n:"))
                    if(b==1):
                        print("-"*30)
                        print("YOU CHOOSE TO EVALUATE SQUARE ROOT")
                        n=float(input("ENTER THE VALUE TO EVALUATE(or done to stop) :"))
                        try:
                                if n < 0:
                                     print("Square root of negative number is not defined (real numbers).")
                                else:
                                     print(math.sqrt(n)) 
                                     print("-"*30)
                        except:
                                print("-"*30)
                                print("invalid expression")
                                print("-"*30)                        
                    elif(b==2):
                        print("-"*30)
                        print("YOU CHOOSE TO EXIT")
                        print("-"*30)
                        break
                    else:
                        print("-"*30)
                        print("SOMTHING WENT WRONG")
                        print("-"*30)
                        break
            elif(s==3):
                 print("-"*30)
                 print("YOU CHOOSE TO EXIT")
                 print("-"*30)
                 break
            else:
                 print("-"*30)
                 print("invalid command")
                 print("-"*30)
                 break

    elif(option==3):
        while True:
            t=int(input("SELECT:\n1.CUBE,\n2.CUBE ROOT,\n3.EXIT:"))
            if(t==1):
                while True:
                    print("-"*30)
                    a=int(input("ENTER:\n1.CUBE,\n2.EXIT:"))
                    if(a==1):
                        print("-"*30)
                        print("YOU CHOOSE TO EVALUATE CUBE")
                        n=int(input("ENTER THE VALUE TO EVALUATE :"))
                        try:
                                print(n*n*n) 
                                print("-"*30)
                        except:
                                print("-"*30)
                                print("invalid expression")
                                print("-"*30)   
                    elif(a==2):
                            print("-"*30)
                            print("YOU CHOOSE TO EXIT")
                            print("-"*30)
                            break
                    else:
                        print("-"*30)
                        print("somthing went wrong")
                        print("-"*30)
                        break
            elif(t==2):
                while True:
                    b=int(input("ENTER:\n1.CUBE ROOT,\n2.EXIT\n:"))
                    if(b==1):
                        print("-"*30)
                        print("YOU CHOOSE TO EVALUATE CUBE ROOT")
                        n=float(input("ENTER THE VALUE TO EVALUATE(or done to stop) :"))
                        try:
                                print(round(n**(1/3),3)) 
                                print("-"*30)
                        except:
                                print("-"*30)
                                print("invalid expression")
                                print("-"*30)                        
                    elif(b==2):
                        print("-"*30)
                        print("YOU CHOOSE TO EXIT")
                        print("-"*30)
                        break
                    else:
                        print("-"*30)
                        print("SOMTHING WENT WRONG")
                        print("-"*30)
                        break
            elif(t==3):
                 print("-"*30)
                 print("YOU CHOOSE TO EXIT")
                 print("-"*30)
                 break
            else:
                 print("-"*30)
                 print("invalid command")
                 print("-"*30)
                 break

    elif(option==4):
        n = str(input("ENTER THE VALUE TO EVALUATE (or done to stop): "))
        if n.lower() == "done":
            print("YOU CHOSE TO EXIT")
            break
        else:
            try:
                num = int(n)
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("THE FACTORIAL WILL BE =", math.factorial(num))
            except:
                print("-"*30)
                print("Invalid input! Only non-negative integers are allowed.")
                print("-"*30)
                
    elif(option==5):
        print("-"*30)
        print("YOU CHOOSE TO EXIT THE CALCULATOR")
        print("-"*30)
        exit()
    else:
        print("-"*30)
        print("invalid command")
        print("-"*30)
        exit()