        
while(1):
    
    print("1.square")
    print("2.rectangle")
    print("3.circle")
    print("4.triangle")
    print("1.exit")
    a=int(input("enter a hoice"))
    
    def square(a):
        print("area of square",a*a)
    def rectangle(a,b):
        print("area of rectangle",a*b)
    def circle(r):
        print("area of circle",3.14*r*r)
    def triangle(a,b):
        print("area of triangle",2*a+b)
        
    if a==1:
        a=int(input("enter a side of square "))
        square(a)
    elif a==2:
        rectangle(10,20)
    elif a==3:
        r=int(input("enter radius"))
        return circle(r)
    elif a==4:
        triangle(2,3)
    else :
        print("exit")









        
