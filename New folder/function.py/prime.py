list1=[]
for i in range(20,40):
    amos=1
    for j in range(2,i):
        if i%j==0:
            amos=0
            break
    if amos==1:
        list1.append(i)
print(list1)
