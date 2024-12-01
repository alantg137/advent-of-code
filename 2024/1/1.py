file = open("data.txt")
a1=[]
a2=[]
for line in file:
    p = (line.split('   '))
    a1.append(p[0])
    a2.append(p[1])
a1.sort()
a2.sort()

total=0
for i in range(len(a1)):
    total= total + abs(int(a1[i])-int(a2[i]))
print(total)
    