def breakingRecords(scores):
    # Write your code here
    ma=mi=scores[0]
    mac=mic=0
    for i in scores:
        if(i>ma):
            mac+=1
            ma=i
        if(i<mi):
            mic+=1
            mi=i
    return mac,mic
