def minimumNumber(n, password):
    cn=cl=cu=cc=0
    num='0123456789'
    sp='!@#$%^&*()-+'
    for i in password:
        if(i in num and cn==0):
            cn=1
        if(i.islower() and cl==0):
            cl=1
        if(i.isupper() and cu==0):
            cu=1
        if((i in sp) and cc==0):
            cc=1
    res=cn+cl+cu+cc
    if(res==4 and n>=6):
        return 0
    else:
        if((4-res)+n>=6):
            return (4-res)
        else:
            return 6-n
