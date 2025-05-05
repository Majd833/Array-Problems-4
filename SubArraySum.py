def subarraysum(arr,n,sum):
    for i in range(n):
        currsum=arr[i]
        j=i+1
        while j<=n:
            if currsum==sum:
                print("sum found between")
                print("indexes %d and %d"%(i,j-1))
                return 1
            if currsum>sum or j==n:
                break
            currsum=currsum+arr[j]
            j+=1
    print("No subarray found")
    return 0
arr=[3,6,2,2,12,0,9,1]
n=len(arr)
sum=10
subarraysum(arr,n,sum)