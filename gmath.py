import math
from display import *

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    squared = 0
    for x in vector:
        squared += x**2
    magnitude = squared**0.5
    for i in range(len(vector)):
        vector[i] /= magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] * b[i])
    return sum

def subtract_vectors(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]-b[i])
    return c

#only works for vectors of size 3
def cross_product(a, b):
    c = []
    c.append(a[1]*b[2]-a[2]*b[1])
    c.append(a[2]*b[0]-a[0]*b[2])
    c.append(a[0]*b[1]-a[1]*b[0])
    return c

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    a = subtract_vectors(polygons[i+1],polygons[i])
    b = subtract_vectors(polygons[i+2],polygons[i])
    n = cross_product(a, b)
    return n
