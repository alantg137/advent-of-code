import re
score = 0
r = r'(\d+)\|(\d+)'
rules = []
r2 = r'\,'
file = open("data.txt")
for line in file:
    line = line.strip()
    good = True
    for match in re.finditer(r,line):
        x = int(match.group(1))
        y = int(match.group(2))
        rules.append((x,y))
    if re.search(r2,line):
        blob = line.split(',')
        for sh in range(len(blob)):
            blob[sh] = int(blob[sh])
        for rule in rules:
            x = rule[0]
            y = rule[1]
            if x in blob and y in blob:
                if blob.index(x) > blob.index(y):
                    good = False
        if good:
            score = score + blob[len(blob)//2]
print(score)


