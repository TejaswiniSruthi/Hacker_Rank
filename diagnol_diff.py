def diagonalDifference(arr):
    # Write your code here
    l=r=0
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if(i==j):
                l+=arr[i][j]
            if((i+j)==(n-1)):
                r+=arr[i][j]
    return abs(l-r)
