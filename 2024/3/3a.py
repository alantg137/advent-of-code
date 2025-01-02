import re
file = open("data.txt")
s= file.read()
p = 0
r = r"mul\((\d+),(\d+)\)"
for s in re.finditer(r,s):
    p = p + int(s.group(1))*int(s.group(2))
print(p)