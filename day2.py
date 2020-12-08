import fileinput

tot_area = 0
tot_ribbon = 0
for line in fileinput.input():
    [l, w, h] = map(lambda x: int(x), line.split('x'))
    sides_sorted = [l, w, h]
    sides_sorted.sort()
    area = 2*l*w + 2*w*h + 2*h*l + sides_sorted[0]*sides_sorted[1]
    ribbon = 2*sides_sorted[0] + 2*sides_sorted[1] + l*w*h
    tot_area += area
    tot_ribbon += ribbon
    print(ribbon)
print('tot:'+str(tot_ribbon))
