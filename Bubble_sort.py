l = [10,15,4,23,0]
print("Unsorted list:",end="")
print(l)
for j in range(len(l)-1):
    for i in range(len(l)-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
        print(l)

print("Sorted list:",end="")
print(l)
    
