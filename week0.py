# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hellow world")

"""
There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 13 miles. 
    Miles to feet template --- Miles to feet solution --- Miles to feet (Checker)
"""
print(13*5280)

"""Write a single Python statement that combines the three strings "My name is", "Joe" and "Warren" (plus a couple of other small strings) into one larger string "My name is Joe Warren."
 and prints the result. Name tag template --- Name tag solution --- Name tag (Checker)"""

a="My name is"
b="Warren"
c="Vasu"

print ("{0} {1} {2}".format(a,b,c))

"""Write a Python expression that combines the string "Joe Warren is 52 years old." from the string "Joe Warren" and the number 52 and then prints the result (Hint: Use the function str to convert the number into a string.)
 Name and age template --- Name and age solution --- Name and age (Checker)""" 

name="vasu H S"
age=27
print(type(age))
print("{0} is {1} years old.".format(name,str(age)))

"""The distance between two points (x0,y0) and (x1,y1) is (x0−x1)2+(y0−y1)2−−−−−−−−−−−−−−−−−−√.
 Write a Python statement that calculates and prints the distance between the points (2,2) and (5,6).
 Point distance template --- Point distance solution --- Point distance (Checker)"""
import math
a=(2,2)
b=(5,6)
print(type(a),type(b))

first=pow((a[0]-b[0]),2)

sec=pow((a[1]-b[1]),2)
    
print (math.sqrt(first + sec))



                                                                