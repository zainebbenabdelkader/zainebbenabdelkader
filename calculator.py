def somme(x,y):
    z=x+y
    return z
def difference(x,y):
    z=x-y
    return z
def multip(x,y):
    z=x*y
    return z
def divis(x,y):
    if (y==0):
        return "error"
    else:
        z=x/y
        return z
x=float(input("donner x  :"))
y=float(input("donner y :"))
n=input("_:")
if (n=='+'):
    print("la somme : ",somme(x,y))
else :
    if (n=='-'):
         print("la diif : ",difference(x,y))
    else :
        if (n=='*'):
            print("la multi : ",multip(x,y))
        else :
            if (n=='/'):
                print("la div : ",divis(x,y))
            else:
                if(n=='c'):
                    x=0
                    y=0
                    print("clear")

