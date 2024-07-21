d = {"Tom": 12345666, "chandu": 8884788342}
d["nimi"] = 9742199032
Total = 0
del d["Tom"]
for key in d:
    print("Key :", key, " Value is :", d[key])
    Total = Total + d[key]
print(Total)
for k, v in d.items():
    print('hi', k, v)
print("chandu" in d)
d.clear()
print(d)
