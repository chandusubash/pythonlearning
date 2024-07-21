indian=['samosa','daal','biriyani','paratha','paneer masala']
chinese=['noodles','fried rice','chilly chicken','sushi','momos']
italian=['pizza','penne pasta','lasagne','pasta','italian chicken curry']
dish=input("enter a dish name :")
if dish in indian:
    print("You selected Indian food")
elif dish in chinese:
    print("You selected Chinese food")
elif dish in italian:
    print("You selected Italian")
else:
    print("Dude i dont have the information u are looking for")

