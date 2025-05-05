def equipt(arr):
    leftsum=0
    rightsum=0
    n=len(arr)
    for i in range(n):
        leftsum=0
        rightsum=0
        for j in range(i):
            leftsum+=arr[j]
        for j in range (i+1,n):
            rightsum+=arr[j]
        if leftsum == rightsum:
            return i
    return-1
a=[-4,6,2,0,1,0,1]
print(equipt(a))