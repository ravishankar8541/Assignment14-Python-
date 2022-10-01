#  Write a python script to sort a list.
l=[6,7,3,2,0,2,9,57]
print(len(l))
for a in range(0,len(l)): 
    for b in range(a+1,len(l)):    
        if l[a]>=l[b]:
            temp=l[a]
            l[a]=l[b]
            l[b]=temp
         
print(l)         