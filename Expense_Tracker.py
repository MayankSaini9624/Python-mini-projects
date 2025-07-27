print("THIS IS AN EXPENSE TRACKER")
print("""
SELECT FROM THE FOLLOWING -
1. ADD AN EXPENSE
2. SUMMARY OF EXPENSE
3. COMMENT ON EXPENSE
4. EXIT
""")

education_exp = 0
grocery_exp = 0
merchandise_exp = 0
bill_exp = 0
oth_exp = 0

while True:
    pref = int(input("ENTER YOUR PREFERENCE: "))

    if not (1 <= pref <= 4):
        print("INVALID PREFERENCE\n")
        continue

    if pref == 1:
        print("""
SELECT THE EXPENSE CATEGORY
1. EDUCATION
2. GROCERY
3. MERCHANDISE
4. BILLS
5. OTHERS
6. GO BACK TO MAIN MENU
""")
        while True:
            cat_choice = int(input("ENTER THE CATEGORY OF EXPENSE: "))

            if cat_choice == 1:
                print("YOU HAVE CHOSEN THE EDUCATION CATEGORY")
                exp = int(input("ENTER THE EXPENSE FOR EDUCATIONAL PURPOSE: ₹"))
                education_exp += exp
            elif cat_choice == 2:
                print("YOU HAVE CHOSEN THE GROCERY CATEGORY")
                exp = int(input("ENTER THE EXPENSE FOR GROCERY PURPOSE: ₹"))
                grocery_exp += exp
            elif cat_choice == 3:
                print("YOU HAVE CHOSEN THE MERCHANDISE CATEGORY")
                exp = int(input("ENTER THE EXPENSE FOR MERCHANDISE PURPOSE: ₹"))
                merchandise_exp += exp
            elif cat_choice == 4:
                print("YOU HAVE CHOSEN THE BILLS CATEGORY")
                exp = int(input("ENTER THE EXPENSE FOR BILL PURPOSE: ₹"))
                bill_exp += exp
            elif cat_choice == 5:
                print("YOU HAVE CHOSEN THE OTHERS CATEGORY")
                exp = int(input("ENTER THE EXPENSE FOR OTHER PURPOSE: ₹"))
                oth_exp += exp
            elif cat_choice == 6:
                break
            else:
                print("INVALID CATEGORY. TRY AGAIN.")

    elif pref == 2:
        print("\n--- SUMMARY OF EXPENSE ---")
        print("EDUCATIONAL EXPENSE:",education_exp,"₹")
        print("GROCERY EXPENSE:",grocery_exp,"₹")
        print("MERCHANDISE EXPENSE:",merchandise_exp,"₹")
        print("BILLS: ",bill_exp,"₹")
        print("OTHER EXPENSE:",oth_exp,"₹")
        total = education_exp + grocery_exp + merchandise_exp + bill_exp + oth_exp
        print("TOTAL EXPENSE:","₹",total)

    elif pref == 3:
        print("\n--- PYTHON GENERATED COMMENT ---")
        if education_exp > 10000:
            print("DO YOU NEED A SCHOLARSHIP? YOU CAN SEARCH FOR ONE ONLINE.")
        if grocery_exp > 10000:
            print("YOU'RE SPENDING A LOT ON GROCERY. ONLY BUY NECESSARY ITEMS AND SAVE MONEY.")
        if merchandise_exp > 10000:
            print("KISI KI SHAADI HAI KYA?  ITNA KYU KHARCH RHA HAI MERCHANDISE PE?")
        if bill_exp > 2000:
            print("ITNE SUBSCRIPTION HAI TERE PAAS? USE A 5G PLAN OR CHEAPER BROADBAND OPTIONS.")
        if oth_exp > 3000:
            print("MEHNAT LAGTI HAI KAMANE ME, NALLE!")
        print()

    elif pref == 4:
        print("THANK YOU FOR USING THE EXPENSE TRACKER.")
        break
