F_NAME = "data.csv"
f = open(F_NAME, "r")
f_name = open("names.txt", "r") 
data = []

for x in f: 
    record = x.split(',')
    name = "\"" + record[0] + "\""
    value = "(" + name + "," + record[1] + "," + record[2].replace("\n","") + ")" + "," + "\n"
    data.append(value)

output = open("sqldata.txt", "w")
for x in data: 
    output.write(x)
   








