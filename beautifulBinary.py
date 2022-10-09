def beautifulBinaryString(b,n):
    # Write your code here
    c=i=0
    while(i<(n-2)):
        if(b[i:i+3]=='010'):
            c+=1
            i+=3
        else:
            i+=1
    return c
