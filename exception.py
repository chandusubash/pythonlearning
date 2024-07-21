x = input("Enter a number :")
y = input("Enter another number :")
try:
    z = int(x) / int(y)
except Exception as e:
    print("Zero division exception", e)
    z = None
print(z)
