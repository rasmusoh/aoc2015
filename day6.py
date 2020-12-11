import re
import numpy as np
import fileinput

r = re.compile(r'(.*) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')
lights = np.zeros((1000, 1000))
for line in fileinput.input("./data/day6.txt"):
    parsed = r.match(line)
    command, x_from, y_from, x_to, y_to = parsed.groups()
    x_from = int(x_from)
    x_to = int(x_to)
    y_from = int(y_from)+1
    y_to = int(y_to)+1
    if command == 'turn on':
        lights[x_from:x_to, y_from:y_to] += 1
    elif command == 'turn off':
        lights[x_from:x_to, y_from:y_to] -= 1
        lights = np.clip(lights, 0, None)
    else:
        lights[x_from:x_to, y_from:y_to] += 2
print(lights.sum())
