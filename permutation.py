def permutationEquation(p,n):
    # Write your code here
    res=[]
    for i in range(1,n+1):
        y=p.index(i)+1
        ym=p.index(y)+1
        res.append(ym)
    return res
