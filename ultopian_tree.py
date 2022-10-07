def utopianTree2(n,x):
    if(n!=0):
        x+=1
        return utopianTree(n-1,x)
    return x

def utopianTree(n,x):
    # Write your code here
    if(n!=0):
        x*=2
        return utopianTree2(n-1,x)
    return x
