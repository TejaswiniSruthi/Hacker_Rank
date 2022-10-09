def hackerrankInString(s):
    # Write your code heren=len(s)
    n=len(s)
    l=list('hackerrank')
    for i in range(n):
        if(s[i]==l[0]):
            l.remove(l[0])
        if(len(l)==0):
            return "YES"
    return "NO"
