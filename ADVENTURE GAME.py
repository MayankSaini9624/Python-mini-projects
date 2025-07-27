
print("ADVENTURE GAME")
username=input("enter a good username:")
print(username,", YOU ARE IN A UNKNOWN PLACE. CHOOSE YOUR PATH WISELY!")
print("""SELECT THE FOLLOWING CHOICE:
1.TAKE A LEFT 
2.TAKE A RIGHT
""")
first=input("LEFT OR RIGHT:").upper()

print("DON'T INPUT INVALID COMMAND BECAUSE EVEY TIME YOU ENTER INCORRECT ANSWER YOU HAVE TO START FROM BEGINING")
if first=="LEFT":
    print("NOW YOU SEE 3 DOORS")
    print("""SELECT-
    1.DOOR(1)
    2.DOOR(2)
    3.DOOR(3)
    """)
    firstD=int(input("ENTER THE DOOR NO.:"))
    if firstD==1:
        print("YOU SEE 3 WAYS:\n1. wayA\n2. wayB\n3. wayC")

        firstDway=int(input("WHICH WAY ?"))
        if firstDway==1:
            print(username,"See Desert\n,You enter the Desert\n, YOU Get dehydrate,\nDEATH.")
            exit()
        if firstDway==2:
            print("YOU SEE A CHEAST .\n THERE ARE 2 MAPS IN CHEAST.")
            print("SELECT ONE OF 2 MAPS.\n1. MAP 1\n2. MAP 2")
            firstDwaymap=int(input("WHICH MAP:"))
            if firstDwaymap==1:
                print("SEE ANYWHERE DOOR.\n AND ESCAPED")
                print("congrats")
                exit()
            if firstDwaymap==2:
                print("YOU SEE A DRAGON.\nIT BURNT YOU.\nDEATH")
                exit()
        if firstDway==3:
            print("YOU SEE A HAUNTED HOUSE.\nYOU ENTER THE HOUSE")
            print("YOOUSAW TWO ROOMS")
            print("""SELECT THE ROOM
            1.ROOM 1
            2.ROOM 2""")
            firstDwayhouseroom=int(input("THE ROOM NO.:"))
            if firstDwayhouseroom ==1 :
                print("THERE ARE 2 WAYS.\n1.way1.\n2.way2")
                firstDwayhouseroomway=int(input("ENTER THE WAY:"))
                if firstDwayhouseroomway==1:
                    print("THERE IS A GHOST.\nDEATH")
                    exit()
                if firstDwayhouseroomway==2:
                    print("THERE ARE 2 WINDOWS:")
                    print("""SELECT:
                    1.STORE ROOM
                    2.ANYWHERE DOOR """)
                    firstDwayhouseroomwaywin=int(input("WHICH WINDOW:"))
                    if firstDwayhouseroomwaywin==1:
                        print("GET HALLUCINATE.\n get Nausea.\nDEATH")
                        exit()
                    if firstDwayhouseroomwaywin==2:
                        print("SEE ANYWHERE DOOR.\nESCAPED")    
                        exit()
                    if firstDwayhouseroomwaywin>2 or firstDwayhouseroomwaywin<1:
                        print("INVALID COMMAND")
                if firstDwayhouseroomway>2 or firstDwayhouseroomway<1:
                    print("INVALID COMMAND")        
            if firstDwayhouseroom==2:
                print("SAW A GHOST.\n DEATH")
                exit()
            if firstDwayhouseroom >2 or firstDwayhouseroom<1 :
                print("INVALID COMMAND")    
        if firstDway >3 or firstDway<1 :
            print("INVALID COMMAND")
    if firstD==2:
        print("GET TRAVELLED IN PAST OR FUTURE")        
        print("THERE ARE 3 TIME PASSAGES:\n1. First\n2. Second\n3. Third")
        firstDtp=int(input("WHICH TIME PASSAGE:"))
        if firstDtp==1:
            print("IN THIS TIME LINE THE EARTH IS IN FUTURE.\n AND HUMANS STARTED A WAR AND NUKE EACH OTHER.\n AND YOU ALSO GET IN TO THE EATRH WHICH IS ALSO A BALL OF LAVA.\n DEATH")
            exit()
        if firstDtp==2:
            firstDtpH=int(input("CHOOSE THE WAY:\n1.way1.\n2.way2"))
            if firstDtpH==1:
                print("IN THIS TIMELINE THE EARTH IS BEEN WELL MAINTAIN BY THE HUMANS AND YOU ARE STUCK IN HEAVEN.\nBECAUSE YOU CAN'T ESCAPE .\nTHIS WILL NOT COUNT AS ESCAPE.\nBUT BECAUSE YOU AR I HEAVEN YOU ARE \nFAILED")
                exit()
            if firstDtpH==2:
                print("NOW YOU ARE GOING BACK TO THE 21th CENTUARY")
            if firstDtpH not in range (1,3):
                print("INVALID COMMAND")  
        if firstDtp==3:
            print("IN THIS TIME LINE YOU ARE IN THE ERA OF DINO'S ")
            print("SELECT:\n1.A\n2.B")
            firstDtpstuck=int(input("ENTER THE SELECTED OPTION:"))
            if firstDtpstuck==1:
                print("YOU ARE LIVING LIKE A NORMAL STONE AGE PERSON AND THAT IS ACCEPTABLE AS ESCAPE")
                print("ESCAPED")
                exit()
            if firstDtpstuck==2:
                print("WHAT WHAT WHAT IS THAT .........\n OHH NO THAT'S A ASTROIDE AND THAT IS HOW YOU AND ALL DINO GET VANISHED AWAY")    
                print("DEATH")
                exit()
            if firstDtpstuck not in range(1,3):
                print("INVALID COMMAND")
                exit()
    if firstD==3:
        print("THERE ARE 4 DOORS INSIDE THE 3RD DOOR ")
        print("SELECT THE DOORS:\n1.1st.\n2.2nd.\n3.3rd.")
        firstDd=int(input("ENTER THE ONE YOU WANT TO CHOOSE:"))
        if firstDd==1:
            print("THERE IS A DEMON THERE.\n IT WILL ASK YOU 3 QUESTION")
            q1=input("DEOMON :\n1. WHAT IS THAT THING WHICH IS EXTREMLY HOT AND HAVING THE SHAPE OF A BALL:").lower()
            if q1=="sun":
                print("DEMON:SHARP BRAIN.")
                q2=input("2. WHAT FRUIT DON'T HAVE SEEDS:").lower()
                if q2=="banana":
                    print("DEMON : NICE.")
                    q3=input("DOES ANY PART OF APPLE IS FATEL(YES/NO):").lower()
                    if q3 =="yes":
                        print("YOU ARE FREE TO GO .\nESCAPED")
                        exit()
                    else:
                        print("DEATH")    
                        exit()
                else:
                    print("DEATH")    
                    exit()     
            else:
                print("DEATH")    
                exit()        
        if firstDd==2:
            print("In this door there are doreamon .\n But somehoe he had lost his memory.\n But he know about the escape root.\n but you have to let him remind me of some of his gadgets.")        
            print("DOREAMON SAID:\n 1.I can't remember the use of big light what it do make think big or small.\nBut be carefull because he had his air cannon and he know how to use it and aslo he is in anger.")
            d1=input("ANS(BIG/SMALL)").lower()
            if d1=="big":
                print("YAHH I REMEMBER")
                d2=input("2.WHAT DOES THAT BAMBOCOPTER DOES (FLY / DIG)").lower()
                if d2=="fly":
                    print("THANK YOU LAST ONE LAST ONE")
                    d3=input("3.WHAT IS THE USE OF THIS POKET ON MY BELLY TO(STORE/COOK):").lower()
                    if d3 =="store":
                        print("THANKS ALOT \n I CAN SHOW YOU THE PATH THERE IT IS")
                        print("ESCAPED")
                        exit()
                    else:
                        print("AHHH....\nYOU ARE MAKING ME ANGRY \nBOOOOOOOM")
                        print("DEATH")
                        exit()
                else:
                    print("AHHH....\nYOU ARE MAKING ME ANGRY \nBOOOOOOOM")
                    print("DEATH")
                    exit()        
            else:
                print("AHHH....\nYOU ARE MAKING ME ANGRY \nBOOOOOOOM")
                print("DEATH")
                exit()
        if firstDd==3:
            print("BEHIND THIS DOOR THERE ARE 2 DORAMI ONE OF THEM IS EVIL AND ONE OF THEM IS GOOD")
            print("BUT YOU DON'T KNOW WHO IS WHO")
            print("IF YOU CHOOSE EVIL ONE YOU DIED AND IF COOSE NORMAL ONE SHE WILL GONNA HELP YOU TO ESCAPE")
            print("""WHO IS REALL DORAMI:
            1.LEFT ONE
            2.RIGHT ONE""")
            dorami=int(input("TELL WHO IS REAL (1/2):"))
            if(dorami==1):
                print("SICK ................")
                print("DEATH")
                exit()
            if(dorami==2):
                print("DORAMIN:THANKS FOR CHOOSING ME AND BELIVING ME  THAT I AM REAL")
                print("DORAMIN:I WILL SHOW THE ESCAPE PATH")
                print("ESCAPED")
                exit()
            else:
                print("INVALID COMMAND")
                exit()
if first=="RIGHT":
    print("THERE IS A ROOM AND IN THAT ROOM THERE ARE 2 VENTS ")
    print("SELECT THE VENT :\n1.VENT 1.\n2.VENT 2.")
    firstvent=int(input("ENTER THE VENT NO.:"))
    if firstvent==1:
        print("BY THIS VENT YOU ENTERED A ROOM IN THA TROOM THERE AR 3 WINDOWS")
        print("""SELECT THE WINDOW NO.:
            1.WINDOW NO. 1
            2.WINDOW NO. 2
            3.WINDOW NO. 3""")
        firstventwin=int(input("ENTER THE WINDOW NO.:"))
        if firstventwin==1:
            print("you see a bear there .\n and it vanished you")
            print('DEATH')
            exit()
        if firstventwin==2:
            print("YOU SEE A MAGICIAN THERE ")
            print("HE HELP YOU ")
            print("ESCAPED")
            exit()
        if firstventwin==3:
            print("ahh.. it just escape window ")
            print("Escaped")
            exit()
        else:
            print("INVALID COMMAND")    
    if firstvent==2:
        print("BY THIS VENT YOU ENTERED A ROON WHICH HAVE 3 DOOR .\nBY HEARING YOU CAN SENSE THAT THERE ARE HULK SPIDEY AND RED-SKULL IN THOES ROOM .\nCHOOSE WISELY")
        firstventm=int(input("ENTER TEH DOOR NO. YOU DO WANT TO ENTER INTO :"))
        if firstventm==1:
            print("IT'S SPIDEY HE IS GONNA HELP YOU")
            print("ESCAPED")
            exit()
        if firstventm==2:
            print("IT IS THE ROOM OF RED-SKULL")
            print("WHAT ARE YOU WAITING FOR HE MUST HAD KILLED YOU")
            print("DEATH")
            exit()
        if firstventm==3:
            print("IT IS THE ROOM OF OUR GREEN MONSTER HULKKK")
            print("HE SMASHED THE WALL AND YOU ESCAPED")
            exit()
        else:
            print("INVALID COMMAND")
            exit()


