def rcheck(arr):
    n=len(arr)
    for i in range(n-2):
        r=abs(arr[i]-arr[i+1])
        if(abs((arr[(n-i)-1])-(arr[(n-i)-2]))!=r):
            return False
    return True

def funnyString(s):
    # Write your code here
    arr=[]
    for i in s:
        arr.append(ord(i))
    if(rcheck(arr)):
        return "Funny"
    else:
        return "Not Funny"
