# Write a Python script to create a list of first N odd natural numbers.
n=int(input("How many odd numbers you want to print :"))
l=[x for x in range(1,2*n+1,2)]
print(l)