#! /usr/bin/env python

import json
# Importing the matplotlib library
import matplotlib.pyplot as plt

with open('data.txt') as json_file:
    data = json.load(json_file)

numberList = []
for i in range(0,1000):
	numberList.append(i)

# Passing the parameters to the bar function, this is the main function which creates the bar plot
plt.bar(numberList, data)
# Displaying the bar plot
plt.show()