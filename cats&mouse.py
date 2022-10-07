def catAndMouse(x, y, z):
    #
    # Write your code here.
    if(abs(x-z)>abs(y-z)):
        return("Cat B")
    elif(abs(x-z)<abs(y-z)):
        return("Cat A")
    else:
        return("Mouse C")
