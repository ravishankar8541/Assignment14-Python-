""" Write a Python script to print indices of all occurrences of a given element in a given
list."""
l2=[3,7,4,3,8,5,8]
print(l2)
print("which index of element do you want to find:")
n=int(input())
i=0
while i<len(l2):
    if(l2[i]==n):
        print(i,end=" ")
    i+=1    