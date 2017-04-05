import csv
from collections import defaultdict
import matplotlib.pyplot as plt
i = open('directory.csv')
read = csv.reader(i)
states = defaultdict(int)
for l in read:
    if l[7] == 'US':
        states[l[6]] += 1
i.close()
keys = states.keys()
n = open('walmart store_openings.csv')
r = csv.reader(n)
state = defaultdict(int)
for w in r:
    state[w[8]] += 1
state.__delitem__('STRSTATE')
n.close()

ratios = defaultdict(float)
f = open('ratios.csv', 'w')
f.write('state, number of starbucks, number of walmarts, ratio \n')
for key in keys:
    walmart = state[key]
    starbucks = states[key]
    ratio = float(walmart)/starbucks
    ratios[key] = ratio
    # plt.plot(key, ratio)
    f.write(str(key) +', ')
    f.write(str(starbucks) + ',')
    f.write(str(walmart) + ', ')
    f.write(str(ratio))
    f.write('\n')
f.close()
