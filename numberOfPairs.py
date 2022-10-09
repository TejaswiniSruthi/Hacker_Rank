def sockMerchant(n, ar):
    # Write your code here
    arr=[]
    c=0
    for i in ar:
        if i in arr:
            arr.remove(i)
            c+=1
        else:
            arr.append(i)
    return c
