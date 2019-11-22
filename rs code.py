# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:59:57 2018

@author: Huntrer
"""
points = 0
for level in range(1,100):
    diff = int(level + 300 * math.pow(2, float(level)/7) )
points += diff
str = "Level %d = %d" % (level + 1, points / 4)
print(str)