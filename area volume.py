
print("THIS IS A AREA AND VOLUME CALCUKATOR")
print("----------------------")
print("""SELECT=
1.AREA
2.VOLUME""")
print("----------------------")
aov=int(input("ENTER YOU PREFRENCE="))
while True:
    if(aov==1):
        print("----------------------")
        print("SELECT=\n1.RECTANGLE\n2.SQUARE\n3.TRIANGLE\n4.CIRCLE\n5.CUBOIDE\n6.CUBE\n7.EXIT")
        print("----------------------")
        area=int(input("ENTER ="))
        if(area==1):
            print("----------------------")
            print("YOU CHOOSE TO FIND THE AREA OF RECTANGLE")
            print("----------------------")
            length=float(input("LENGTH (in cm)= "))
            width=float(input("WIDTH (in cm)= "))
            print("----------------------")
            print("THE AREA = ",(length*width),"sq centimeters")
            print("----------------------")
            break
        elif(area==2):
            print("----------------------")
            print("YOU CHOOSE TO FIND THE AREA OF SQUARE")
            print("----------------------")
            length=float(input("LENGTH(in cm) = "))
            print("----------------------")
            print("THE AREA = ",(length*length),"sq centimeter")
            print("----------------------")
            break
        elif(area==3):
            print("----------------------")
            print("YOU CHOOSE TO FIND THE AREA OF TRIANGLE")
            base=float(input("BASE (in cm) = "))
            height=float(input("HEIGHT (in cm) = "))
            print("----------------------")
            print("THE AREA = ",(height*base)/2,"sq centimeters")
            print("----------------------")
            break
        elif(area==4):
            print("----------------------")
            print("YOU CHOOSE TO FIND THE AREA OF CIRCLE")
            print("----------------------")
            radius=float(input("RADIUS (in cm) = "))
            print("----------------------")
            print("THE AREA = ",(3.14*radius*radius),"sq centimeters")
            print("----------------------")
            break
        elif(area==5):
            print("----------------------")
            print("YOU CHOOSE TO FIND THE AREA OF CUBOIDE")
            print("----------------------")
            length=float(input("LENGTH (in cm) = "))
            width=float(input("WIDTH (in cm) = "))
            height=float(input("HEIGHT (in cm) = "))
            print("----------------------")
            print("THE AREA = ",(2*(length*width+width*height+height*length)),"sq centimeters")
            print("----------------------")
            break
        elif(area==6):
            print("----------------------")
            print("YOU CHOOSE TO FIND THE AREA OF CUBE")
            length=float(input("LENGTH (in cm) = "))
            print("THE AREA = ",(6*length*length),"sq centimeters")
            print("----------------------")
            break
        elif(area==7):
            print("----------------------")
            print("YOU CHOOSE TO EXIT")
            print("----------------------")
            exit()
        else:
            print("----------------------")
            print("INVALID COMMAND")
            print("----------------------")
            exit()
    elif(aov==2):
        print("----------------------")
        print("SELECT = \n1.CUBOIDE\n2.CUBE\n3.CYLINDER\n4.SPHERE\n5.EXIT")
        print("----------------------")
        vol=int(input("ENTER YOUR PREFRENCE = "))
        if (vol==1):
            print("----------------------")
            print("YOU CHOOSE TO CALCULATE THE VOLUME OF CUBOIDE")
            print("----------------------")
            length=float(input("LENGTH (in cm) = "))
            width=float(input("WIDTH (in cm) = "))
            height=float(input("HEIGHT (in cm) = "))
            print("----------------------")
            print("THE VOLUME = ",(length*width*height),"centimeter cube")
            print("----------------------")
            break
        elif (vol==2):
            print("----------------------")
            print("YOU CHOOSE TO CALCULATE THE VOLUME OF CUBE")
            print("----------------------")
            length=float(input("LENGTH (in cm) = "))
            print("----------------------")
            print("THE VOLUME = ",(length*length*length),"centimeter cube")
            print("----------------------")
            break
        elif (vol==3):
            print("----------------------")
            print("YOU CHOOSE TO CALCULATE THE VOLUME OF CYLINDER")
            print("----------------------")
            radius=float(input("ENTER THE RADIUS (in cm) =  "))
            height=float(input("ENTER THE HEIGHT (in cm) =  "))
            print("----------------------")
            print("THE VOLUME = ",(3.14*radius*radius*height),"centimeter cube")
            print("----------------------")
            break
        elif (vol==4):
            print("----------------------")
            print("YOU CHOOSE TO CALCULATE THE VOLUME OF SPHERE")
            print("----------------------")
            radius=float(input("ENTER THE RADIUS (in cm) =  "))
            print("----------------------")
            print("THE VOLUME = ",(4.18*radius*radius*radius),"centimeter cube")
            print("----------------------")
            break
        elif(vol==5):
            print("----------------------")
            print("YOU CHOOSE TO EXIT")
            print("----------------------")
            exit()
        else:
            print("----------------------")
            print("INVALID COMMAND")
            print("----------------------")
            exit()
    else:
        print("INVALID COMMAND")
        exit()