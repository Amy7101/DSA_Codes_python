#count digits
x=int(input("enter x:"))
res=0
while x>0:
    x=x//10
    res=res+1
    print("count of digits is"+str(res))