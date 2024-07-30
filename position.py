def remove_chars(ch,n):
    for i in range(n):
        if (ch[i]=='n'):
            return i

ch=str(input("donner une chaine "))
n=len(ch)
x=remove_chars(ch,n)
print("la position",x)
