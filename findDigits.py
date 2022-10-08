def findDigits(n):
    # Write your code here
    t=n
    c=0
    while(n!=0):
        rem=n%10
        if(rem!=0 and t%rem==0):
            c+=1
        n//=10
    return c
