def getMoneySpent(keyboards, drives, b):
    arr=[]
    for i in keyboards:
        for j in drives:
            if(i+j<=b):
                arr.append(i+j)
    if(sum(arr)==0):
        return -1
    else:
        return max(arr)
