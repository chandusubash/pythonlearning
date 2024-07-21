key_location="chair"
locations=["garage","sofa","chair","train"]
for i in locations:
    if i==key_location:
        print("Key found in : ",i)
        break
    else:
        print("Key not found in ",i)
