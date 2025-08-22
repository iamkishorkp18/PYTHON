import random
l=[]
a=0
while (a!=5):
    d=random.randint(1,10)
    if d  not in l:
       l.append(d)
       a+=1
print(l)
