def joy(arr,s,t,x):
    count=0
    for i in arr:
        if((i+x)>=s and (i+x)<=t):
            count+=1
    return count

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    print(joy(apples,s,t,a))
    print(joy(oranges,s,t,b))
