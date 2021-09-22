def prefix(s, words):
    lis = []
    for i in words:
        if i.startswith(s):
            lis.append(i)
    return lis


s = input("Enter a query string=")
words = []
x = int(input("enter size of list="))
for i in range(x):
    words.append(input('Enter a word='))

print(prefix(s, words))
