a=[0,1,1,0,0,0,0,1]
zero=0
one=0
for i in range(len(a)):
    if a[i]==0:
        zero+=1
    if a[i]==1:
        one+=1
print("It would take",zero,"flips to change all the values to one.\nIt would take",one,"flips to change all values to zero.")