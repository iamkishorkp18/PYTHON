student=["A","B","C","D","E","F"]
cgpa=[59,66,47,88,78,69]
arrer=[0,1,2,1,0,0]
for i in range(6):
    if arrer[i]==0 and cgpa[i] >60 :
        print(student[i])
    
