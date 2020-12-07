import re
import fileinput

nice_1 = 0
nice_2 = 0
for line in fileinput.input():
    line = line.rstrip()
    threevowels = len(re.findall(r'([aeiou])', line)) >= 3
    double = re.search(r'([a-z])\1', line) is not None
    noforbidden = re.search(r'(ab)|(cd)|(pq)|(xy)', line) is None
    if threevowels and double and noforbidden:
        nice_1 += 1

    double_pair = re.search(r'(..).*\1', line) is not None
    xyx = re.search(r'([a-z])[^\1]\1', line) is not None
    if double_pair and xyx:
        nice_2+=1

print(nice_1)
print(nice_2)
