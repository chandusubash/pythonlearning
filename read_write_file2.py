f = open("/Users/chandussubash/Documents/Data Analyst/roughdocs/funny.txt", "r")
f_out = open("/Users/chandussubash/Documents/Data Analyst/roughdocs/funny_out.txt", "w")
for line in f:
    tokens = line.split(" ")
    f_out.write(' : ' + str(len(tokens))+line) 
    # print(len(tokens))
f.close()
f_out.close()
