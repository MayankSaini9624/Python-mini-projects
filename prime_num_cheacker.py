n= int(input("ENTER  THE  NUMBER:"))
def prime(n):
    if n<2:
        print("NOT A PRIME NUMBER")
        return
    
    for x in range (2,n):
        if n%x==0:
            print("NOT A PRIME NUMBER")
            return  
    print("A PRIME NUMBER")
prime(n)