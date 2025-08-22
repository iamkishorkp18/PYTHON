a=[[" " for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if (j==0 or j==9):
            a[i][j]="*"
        elif(j==i and i<5):
            a[i][j]="*"
        elif(i+j==8 and i<5):
            a[i][j]="*"
    print()

for i in range(10):
    for j in range(10):
        print(a[i][j],end=" ")
    print()
