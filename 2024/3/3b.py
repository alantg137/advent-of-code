import re
file = open("data.txt")
s= file.read()
p = 0
dont = False
r = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"
for s in re.finditer(r,s):
    if s.group(0) == "don't()":
        dont = True
        continue
    if s.group(0) == "do()":
        dont = False
        continue
    if dont == False:
        p = p + int(s.group(1))*int(s.group(2))
print(p)