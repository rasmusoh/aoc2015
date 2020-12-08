import fileinput

for line in fileinput.input():
    floor = 0
    basement_char = None
    for i in range(len(line.rstrip())):
        floor += 1 if line[i] == '(' else -1
        if basement_char is None and floor < 0:
            basement_char = i+1
    print(basement_char)
