file = open("data.txt")
score=0
a1=[]
a2=[]
for line in file:
    p = (line.rstrip().split('   '))
    a1.append(p[0])
    a2.append(p[1])

#24931009
for x in a1:
    for y in a2:
        if x==y:
            score= score + int(x)
print(score)