with open('data.txt', 'r') as file:
    print(file)
    for line in file.readlines():
        print(line)