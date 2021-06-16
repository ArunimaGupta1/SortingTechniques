l= [1,1,2,5,6,8,3,5,0]
print(l)
for i in range(len(l)):
    min_val = min(l[i:])
    idx = l.index(min_val,i)
    if l[i]>min_val:
        l[i],l[idx] = l[idx],l[i]
    print(l)

        
