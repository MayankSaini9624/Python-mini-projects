import time

print("THIS IS A TIMER THAT I HAVE BUILT IN PYTHON")
timeinsec=int(input("ENTER THE TIME IN SEC:"))
def timer():
    n=1
    while True:
        if n<=timeinsec:
            print(n)
            time.sleep(1) 
            n+=1
        else:
         print("TIMES UP TIME COUNT=",timeinsec,"SEC")
         break
    return
timer()