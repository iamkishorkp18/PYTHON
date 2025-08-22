a=["raj","suri","john","roc"]
mark=[[10,20,30,27],[30,20,40,40],[47,83,98,49],[37,48,23,98]]
per=[]
for i in mark:
    d=sum(i)/4
    per.append(d)
for i in range(4):
    print("{}. {} : {} %".format(i+1,a[i],per[i]))
