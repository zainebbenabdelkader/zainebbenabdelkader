def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

word=str(input("donner une chaine : "))
n=int(input("the place of n :"))
print("removing character",remove_chars(word, n))