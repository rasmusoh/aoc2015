import fileinput
from operator import add

dirs = {'>': [1, 0], '<': [-1, 0], '^': [0, 1], 'v': [0, -1]}
for line in fileinput.input('data/day3.txt'):
    line = line.rstrip()
    pos = [(0, 0), (0, 0)]
    turn = 0
    houses = {pos[turn]}
    for char in line:
        pos[turn] = tuple(map(add, pos[turn], dirs[char]))
        houses.add(pos[turn])
        turn = (turn + 1) % 2
    print(len(houses))
