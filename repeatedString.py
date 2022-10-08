def repeatedString(s, n):
    # Write your code here
    l=len(s)
    ac=l-len(s.replace('a',''))
    ac*=(n//l)
    for i in s[0:(n-((n//l)*l))]:
        if(i=='a'):
            ac+=1
    return ac
