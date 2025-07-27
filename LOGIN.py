print("THIS IS A LOGIN WINDOW")
username="Mayank"
password="mayanksaini@123."
inputusername=input("ENTER USERNAME: ")
inputpassword=input("ENETR PASSWORD: ")
if username==inputusername:
    if password==inputpassword:
        print("LOGIN SUCCESSFULLY")
    else:
        print("INCORRECT PASSWORD")
else:
    if username!=inputusername:
        if password==inputpassword:
            print("INCORRECT USERNAME")
        else:
            print("INCORRECT USERNAME AND PASSWORD")
    else:
        pass