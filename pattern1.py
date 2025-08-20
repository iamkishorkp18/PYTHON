star=int(input("enter a no. of stars"))
blocks=int(input("enter a no. of blocks"))
lines=int(input("enter a no. of lines"))

for i in range(blocks):
    count=0
    for j in range(lines-i):
        for k in range(star):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    print()
