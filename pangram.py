def pangrams(s):
    st=list('abcdefghijklmnopqrstuvwxyz')
    s=s.replace(' ','')
    s=s.lower()
    for i in s:
        if i in st:
            st.remove(i)
        if(len(st)==0):
            return "pangram"
    return "not pangram"
