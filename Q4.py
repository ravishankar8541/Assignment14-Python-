"""Write a Python script to find the greatest number in a given list of numbers."""
l=[]
print("Enter a number in list ")
for a in range(5):
    l.append(int(input()))
print(l) 
len=len(l)
i=0
max=0
while i<len:
    if(l[i]>max):
        max=l[i]
    i+=1
print("Greatest number is ",max)        

 