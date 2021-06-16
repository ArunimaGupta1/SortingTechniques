l= [1,1,2,5,6,8,3,5,0]
print(l)
for i in range(len(l)-1):
    min_val = l[i]
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            min_val = l[j]
    idx = l.index(min_val,i)
    if l[i]>min_val:
        l[i],l[idx] = l[idx],l[i]
    print(l)
        
