def theLoveLetterMystery(s):
    # Write your code here
    l=list('abcdefghijklmnopqrstuvwxyz')
    j=len(s)-1
    i=c=0
    while(i<j):
        ii=l.index(s[i])
        ji=l.index(s[j])
        if(ii!=ji):
            c+=abs(ii-ji)
        i+=1
        j-=1
    return c
