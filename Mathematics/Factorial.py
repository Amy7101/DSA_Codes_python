def fact(n):
    res=1
    for i in range(2,n+1):
        res=res*i
        return res
        if __name__=='main__':
            number=5
            print(fact(number))