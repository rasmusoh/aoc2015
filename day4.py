import fileinput
import hashlib
from itertools import count

for line in fileinput.input():
    line = line.rstrip()
    for i in count():
        candidate = line + str(i)
        hexhash = hashlib.md5(candidate.encode('utf8')).digest().hex()
        if hexhash.startswith('000000'):
            print(i)
            break
