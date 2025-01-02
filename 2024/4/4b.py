l = []
first_time = True

xmas = 0
file = open("data.txt")
for line in file:
    line = line.strip()
    if first_time:
        l.append("0"*len(line)+6*"0")
        l.append("0"*len(line)+6*"0")
        l.append("0"*len(line)+6*"0")
    l.append("000"+line.strip()+"000")
    first_time = False
l.append("0"*len(line)+6*"0")
l.append("0"*len(line)+6*"0")
l.append("0"*len(line)+6*"0")   
print("\n".join(l))
for x in range(len(l[0])):  
    for y in range(len(l)):    
        if l[y][x] != 'M':
            continue
            
        if l[y-1][x-1] == 'A' and l[y-2][x-2] == 'S' and l[y][x-2] == 'M' and l[y-2][x] == 'S':  
            xmas = xmas+1
            
        if l[y-1][x+1] == 'A' and l[y-2][x+2] == 'S' and l[y][x+2] == 'S' and l[y-2][x] == 'M':
            xmas = xmas + 1
        
        if l[y+1][x-1] == 'A' and l[y+2][x-2] == 'S' and l[y][x-2] == 'M' and l[y+2][x] == 'S':  
            xmas = xmas+1
            
        if l[y-1][x-1] == 'A' and l[y-2][x-2] == 'S' and l[y][x-2] == 'S' and l[y-2][x] == 'M':
            xmas = xmas + 1
print(xmas)
