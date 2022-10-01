#Write a Python script to remove all non int values from a list.
l=["kajal",9,"puja",4,8,"deepak"]
l2=[]
for a in l:
    if type(a)==int:
      l2.append(a)

print(l2)