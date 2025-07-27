balance=10000
pin="96240"
epin=input("Enter Your PIN:")
if epin.isdigit and len(epin)==5 :
    if(epin==pin):
        ammount=int(input("Enter Ammount to Deduct:"))
        if(ammount>balance):
            print("INAVALID \n(your balance is lower then that of your input ammount")
        else:
            print("AMMOUNT DEDUCTED:",ammount , "\nREMAINING AMMOUNT:",balance-ammount)
elif(epin.isdigit and len(epin)!=5):
    print("THE LENGTH OF PIN IS NOT APPROPIATE")
else:
    print("INCORRECT PIN")