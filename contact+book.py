print("THIS IS A CONTACT BOOK ")
name1=input("NAME OF THE PERSON:")
number=input("ENTER THE NUMBER:")
strnum=str(number)
if (len(strnum)!=10):
    print("invalid no only sim card no. are been valid here")
    exit()
if (number.isdecimal()):
    pass
else:
    print("INVALID")
    exit()
email=input("ENTER THE EMAIL:")
if "@" not in email and ".com" not in email :
    print("INVALID EMAIL")
if " " in email:
    print("INVALID EMAIL NO SPACE ALLOW")
    exit()
else:
    print("name:",name1,"\n mob.:",number,"\n email:",email)
print("THIS THE DATA THAT IS ONE TIME ONLY STORED IN THE CONTACT BOOK")