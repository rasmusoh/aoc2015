import re
from fileinput import input

lines = {line.rstrip().split(' ')[-1]: line.rstrip().split(' ')[:-2]
         for line in input("data/day7.txt") if line.rstrip()}


def get_value(wire):
    values = {}

    def get(symbol):
        if symbol.isnumeric():
            return int(symbol)
        elif symbol in values:
            return values[symbol]

        tokens = lines[symbol]
        value = None
        if len(tokens) == 1:
            value = get(tokens[0])
        elif tokens[1] == 'AND':
            value = get(tokens[0]) & get(tokens[2])
        elif tokens[1] == 'OR':
            value = get(tokens[0]) | get(tokens[2])
        elif tokens[1] == 'LSHIFT':
            value = get(tokens[0]) << int(tokens[2])
        elif tokens[1] == 'RSHIFT':
            value = get(tokens[0]) >> int(tokens[2])
        elif tokens[0] == 'NOT':
            value = ~ get(tokens[1])
        values[symbol] = value
        return value

    return get(wire)


a = get_value('a')
print(a)
lines['b'] = [str(a)]
print(get_value('a'))
