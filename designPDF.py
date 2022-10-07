def designerPdfViewer(h, word):
    # Write your code here
    s='abcdefghijklmnopqrstuvwxyz'
    res = {}
    for key in s:
        for value in h:
            res[key] = value
            h.remove(value)
            break
    m=res[word[0]]
    for i in word:
        if res[i]>m:
            m=res[i]
    return m*len(word)
