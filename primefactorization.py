def kishor(a,b):
    if a==1:
        return
    while(a%b!=0):
        b+=1
    print(b,end=" ")
    kishor(a//b,b)


n=int(input("enter any number"))
kishor(n,2)
