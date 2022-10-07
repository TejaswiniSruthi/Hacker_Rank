def viralAdvertising(n):
    share=5
    cum=0
    # Write your code here
    while(n!=0):
        liked=share//2
        cum+=liked
        share=liked*3
        n-=1
    return cum
