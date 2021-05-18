#! /usr/bin/env python

import random
import json

randomlist = []
for i in range(0,1000):
	n = random.randint(1,100)
	randomlist.append(n)
print(randomlist)

with open('data.txt', 'w') as outfile:
    json.dump(randomlist, outfile)