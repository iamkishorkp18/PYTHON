def isprime(n):
    if n<2:
        return False
    if n%2==0:
        return n==2
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    return True
primedigits=[3,5,7]
re=[]
for h in primedigits:
    for t in primedigits:
        for u in primedigits:
            num=100*h+10*t+u
            digitsum=h+t+u
            if isprime(digitsum):
                re.append(num)
print(re)
print(len(re))
