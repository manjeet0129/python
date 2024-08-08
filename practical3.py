#practical3a:all latters of alphabets
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
print(ispangram("The quick brown fox jumps over the lazy dog"))

#practical3b:print the elements of the list that of the list that are less than5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

