def reverse(x):
    if (x%10==0):
        x//=10
    rev=str(x)[::-1]
    return int(rev)

    def beautifulDays(i, j, k):
    # Write your code here
    bd=0
    for x in range(i,j+1):
        res=reverse(x)
        res=abs(res-x)
        if(res%k==0):
            bd+=1
    return bd
            
