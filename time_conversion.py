 # Write your code here
    if(s[0:2]=='12' and s[-2:]=='AM'):
        n='00'
    elif(s[-2:]=='PM' and s[0:2] !='12'):
        n=int(s[0:2])+12
    else:
        n=s[0:2]
    s=str(n)+s[2:8]
    
    return s
