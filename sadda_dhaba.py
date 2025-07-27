print("OII WELCOME TO SADDA DHABA OII")
menu={   "Sprouts":50,
        "Poha":50,
        "Idli-Sambhar":75,
        "Dahi-Roti":50, 
        "COCA-COLA":30,
        "PEPSI":30,
        "Tea-Regular":40,
        "Tea-Lemon":50,
        "Cofee":50,
        "Cold-Cofee":60,
        "Pasta":100,
        "Noodles":70,
        "Lassi":40,
        "Dhokla":15,}
print("Sprouts:50\nPoha:50\nIdli-Sambhar:75\nDahi-Roti:50\nCOCA-COLA:30\nPEPSI:30\nTea-Regular:40\nTea-Lemon:50\nCofee:50\nCold-Cofee:60\nPasta:100\nNoodles:70\nLassi:40\nDhokla:15")
TOTAL=0
item1=input("ENTER YOUR ORDER:")
if item1 in menu:
    print("YOU'R ORDER IS GONNA READY SOON PLEAES WAIT!")
    TOTAL+=menu.get(item1)
else:
    print("PLESE ENTER SOMTHNG FROM THE MENU ")

choice=input("Do Your Want to Anything Else(YES/NO)")
if choice=="YES":
    item2=input("ENTER YOU'R SECOND ORDER:")
    if item2 not in menu:
        print("PLEAS ORDER FROM THE MENU")
    else:
        print("YOU'R ORDER WILL BE READY SOON")
        TOTAL+=menu.get(item2)

print("NET TOTAL=",TOTAL,"₹")
print("THANKS FOR VISITING US")