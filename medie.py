f = open("solutions.txt","r")

m = 0
for line in f:
    m += len(line.split()) - 1

m/=11454

print(m)