a=int(input("enter a first number"))
b=int(input("enter a second number"))
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(a)
