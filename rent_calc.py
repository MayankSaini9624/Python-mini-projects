print("THE IS A RENT CALC")
room=float(input("ENTER THE AMMOUNT FOR ROOM $: "))
elec_unit=float(input("ENTER THE AMMOUNT FOR ELCETRICITY UNITS YOU USE:"))
puc=float(input("ENTER WHAT IS THE PER UNIT CHARGE FOR ELECTRICITY:"))
water=float(input("ENTER THE AMMOUNT FOR WATER $:"))
foodngrocery=float(input("ENTER THE SPENDING FOR FOOD AND GROCERY $:"))
total=room+elec_unit*puc+water+foodngrocery
person=int(input("NO. OF PEOPLE IN ROOM WHO IS ABLE TO PAY:"))
total_person=total/person
if person == 0:
    print("Number of people cannot be zero!")
else:
    total_per_person = total / person
    print("\n-----------------------------------")
    print("Total Amount to Pay per Person: $", round(total_per_person, 2))
    print("-----------------------------------")