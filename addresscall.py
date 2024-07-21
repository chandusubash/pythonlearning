import json

f = open("/Users/chandussubash/Documents/book.txt")
s = f.read()
print(s)
book = json.loads(s)
print(book) 
print(type(book))
for v in book:
    for i in book[v]:
        print(i, ':', book[v][i])
