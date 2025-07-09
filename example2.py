n=list(map(int,input("Enter 5 numbers : ").split()))
for j in range(len(n)-1,-1,-1):
    print(n[j],end=" ")
print()
l=0
for i in n:
    l=l+i
print("The sum of the numbers :",l)
y=l/len(n)
print("The average of the numbers :",y)