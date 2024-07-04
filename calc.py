def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def substraction(x,y):
    return x-y

def devide(x,y):
    if y==0:
        raise ValueError("The Xero division error raised")
    else:
        return x/y