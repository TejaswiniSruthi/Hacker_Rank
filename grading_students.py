def gradingStudents(grades):
    # Write your code here
    arr=[]
    for i in grades:
        if(i%5>2):
            ele=((i//5)+1)*5
            if(ele>=40):
                arr.append(ele)
            else:
                arr.append(i)
        else:
            arr.append(i)
    return arr
            
