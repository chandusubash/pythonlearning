import json

book = {}
book["nimmi"] = {
    "name": "Nimitha Rai",
    "address": "305 bilden",
    "phone": 9986054089
}
book["chandu"] = {
    "name": "Chandu subash",
    "address": "305 bilden",
    "phone": 8884788342
}

jsonstring = json.dumps(book)
print(jsonstring)
with open("/Users/chandussubash/Documents/book.txt", "w") as f:
    f.write(jsonstring)
