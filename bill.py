print("DORA DORA STORE")
print("YOUR BILL")

item1=str(input("NAME OF THE ITEM1:"))
item2=str(input("NAME OF THE ITEM2:"))
item3=str(input("NAME OF THE ITEM3:"))
item4=str(input("NAME OF THE ITEM4:"))
item5=str(input("NAME OF THE ITEM5:"))
item6=str(input("NAME OF THE ITEM6:"))
item7=str(input("NAME OF THE ITEM7:"))

cost1=int(input("THE COST OF ITEM1:"))
cost2=int(input("THE COST OF ITEM2:"))
cost3=int(input("THE COST OF ITEM3:"))
cost4=int(input("THE COST OF ITEM4:"))
cost5=int(input("THE COST OF ITEM5:"))
cost6=int(input("THE COST OF ITEM6:"))
cost7=int(input("THE COST OF ITEM7:"))

intdis=int(input("OFFERED DISCOUNT:"))
discount=intdis/100

TOTAL_AMMOUNT_WO_GST=cost1+cost2+cost3+cost4+cost5+cost6+cost7

discount_ammount=discount*TOTAL_AMMOUNT_WO_GST
rest_ammount=TOTAL_AMMOUNT_WO_GST-discount_ammount
gst=0.18*rest_ammount

net_ammount=rest_ammount+gst

print("TOTAL =", TOTAL_AMMOUNT_WO_GST)
print("DISCOUNT=",intdis,"%")
print("DISCOUNTED MONEY=", discount_ammount)
print("TOTAL AFTER DISCOUNT=", rest_ammount)
print("GST=", gst)
print("NET AMMOUNT TO PAY=",net_ammount)
print("""
        PAYMENT METHOD
                        1.CREDIT CARD
                        2.UPI
                        3.CASH""")


print("THANKS FOR VISITING US")
print("HAVE A GOOD DAY")