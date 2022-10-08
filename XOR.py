def maximizingXor(l, r):
    # Write your code here
    m=0
    for i in range(l,r+1):
        for j in range(i,r+1):
            res=i^j
            if(m<res):
                m=res
    return m
