# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:04:43 2017

@author: Huntrer
"""
print("-----it starts here---")
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
from scipy.spatial import distance
 
vector1 = [3.0, 104.0]
vector2 = [18.0, 90.0]
vectorOther = [1.0, 2.0, 3.0]
 
v1 = np.array(vector1)
v2 = np.array(vector2)
vOther = np.array(vectorOther)
 
def diff_Length_Error():
raise RuntimeWarning("The length of the two vectors are not the same!")
 
def euclidean0_0 (vector1, vector2):
''' calculate the euclidean distance
    input: numpy.arrays or lists
    return: 1. quard distance, 2. euclidean distance
'''
quar_distance = 0
try:
if(len(vector1) != len(vector2)):
diff_Length_Error()
zipVector = zip(vector1, vector2)
 
for member in zipVector:
quar_distance += (member[1] - member[0]) ** 2
 
return quar_distance, math.sqrt(quar_distance)
 
except Exception, err:
sys.stderr.write('WARNING: %s\n' % str(err))
return -1, -1
 
def euclidean0_1(vector1, vector2):
    '''calculate the euclidean distance, no numpy
    input: numpy.arrays or lists
    return: euclidean distance
    '''
dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
dist = math.sqrt(sum(dist))
return dist
 
def euclidean2(vector1, vector2):
    '''calculate the euclidean distance, use numpy.dot() function
    input: numpy.arrays or lists
    return: euclidean distance
    '''
try:
        if type(vector1) == list:
            vector1 = np.array(vector1)
        if type(vector2) == list:
            vector2 = np.array(vector2)
        diff = vector2 - vector1
        squareDistance = np.dot(diff.T, diff)
        return squareDistance, math.sqrt(squareDistance)
    except TypeError as e:
        print "Type error: {}".format(e.message)
        raise
    except ValueError as e:
        print "Value error: {}".format(e.message)
        raise
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
 
def euclidean3(vector1, vector2):
    ''' use numpy.linalg.norm to calculate the euclidean distance. '''
    vector1, vector2 = list_to_npArray(vector1, vector2)
    distance = np.linalg.norm(vector1-vector2, 2, 0) # the third argument "0" means the column, and "1" means the line.
    return distance
 
def euclidean4(vector1, vector2):
    ''' use scipy to calculate the euclidean distance. '''
dist = distance.euclidean(vector1, vector2)
return dist
 
def euclidean5(vector1, vector2):
    ''' use matplotlib.mlab to calculate the euclidean distance. '''
vector1, vector2 = list_to_npArray(vector1, vector2)
dist = plt.mlab.dist(vector1, vector2)
return dist
 
def list_to_npArray(vector1, vector2):
    '''convert the list to numpy array'''
if type(vector1) == list:
vector1 = np.array(vector1)
if type(vector2) == list:
vector2 = np.array(vector2)
return vector1, vector2