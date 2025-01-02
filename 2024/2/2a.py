file = open("data.txt")
score=0
d=0


for line in file:
    p = (line.rstrip().split(' '))
    
    increasing = True
    decreasing = True    
    for i in range(len(p)-1):
        d = int(p[i+1])-int(p[i])
        
        if d > 3 or d < -3 or d == 0:
            decreasing = False
            increasing = False
        if d < 0:
            increasing = False

            
        if d > 0:
            decreasing = False
    if increasing == True and decreasing == False or increasing == False and decreasing == True:
        score = score + 1
print(score)