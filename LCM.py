a=int(input("enter a number"))
b=int(input("enter a number"))
m=max(a,b)
while(True):
    if m%a==0 and m%b==0:
        lcm=m
        break
    m+=1
print("LCM",lcm)
