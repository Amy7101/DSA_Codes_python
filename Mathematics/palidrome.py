def ispal(n):
    rev=0
    temp=0
    while temp!=0:
        ld=temp % 10
        rev=rev*10+ld
        temp=temp//10
        return rev==n
if __name__=='__main__':
    number=4553
    print(ispal(number))
