# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import time
import math
import random
from random import randint
import matplotlib.pyplot
import matplotlib.pyplot as plt
import operator




    

"creating a list to assign coordinates a represents x and b represents y"


num_of_coordinates = 100  # "limiting  number of coordinates to 100"
num_of_iterations = 50
coordinates = []

a=[0,0]
b= [3,4]
mdistance = []

"finding the distance between a and b"

calc_dist = ((a[1] - b[1])**2 + (a[0] - b[0])**2)**0.5   

print("distance between", a, "and", b, "=", calc_dist);

"finding the time it takes to execute the distance code"

#start = time.process_time()

x=[]
y=[]

"selecting random numbers between 0 and 100 for x and y coordinates in the list "
"for 100 to be inclusive in the list using raandom.randint"

start =  time.time()

#generate random coordinates between 0 and 100 and append to a list

for i in range(0,100):
 
 x = random.randint(0,100)
 y = random.randint(0,100)  
 
 coordinates.append((x,y))

print(coordinates)

"getting max and min coordinates" 

print('maximum coordinates', max(coordinates, key=operator.itemgetter(1)))
print('minimum coordinates', min(coordinates, key=operator.itemgetter(1)))

 
"finding the distance between coordinates for random points"

    
# for j in range(num_of_iterations):
#     for i in range(num_of_coordinates):
        
#         answer= (((coordinates[0][0] - coordinates[1][0])**2)+((coordinates[0][1] - coordinates[1][1])**2))**0.5

# print("distance", answer)


start = time.time()
"finding maximum distance between random min and max coordinates"

def mdistance():
    return(((coordinates[0][0] - coordinates[1][0])**2)+((coordinates[0][1] - coordinates[1][1])**2))**0.5

# retrieving maximum and minimum coordinates 
min = (min(coordinates, key=operator.itemgetter(1)))
max = (max(coordinates, key=operator.itemgetter(1)))

#calculating maximum distance

print("max distance", math.dist(min,max))

end = end = time.time()
print(end-start, "seconds to get max distance")
# writing coordinates further from each other to text file

# lines = ['Answer', 'which 2 coordinates are further from each other']
# with open('Answer.txt', 'w') as f:
#     f.write('The 2 cooridnates further from each other are ' + str(min,max)+ "\n")
#     f.close()



matplotlib.pyplot.xlim(0,150)# 150 used to accommodate the edge limits within range 100
matplotlib.pyplot.ylim(0,150) # 150 used to accommodate the edge limits within range 100
for i in range(num_of_coordinates):
    matplotlib.pyplot.scatter(x,y)
    matplotlib.pyplot.scatter(min,max, color="black")
matplotlib.pyplot.show()
matplotlib.pyplot.savefig('show.png')#saving the plot to.png file


end = time.time()

print(end-start, "seconds to execute entire code")

# stackoverflow.com and geekforgeeks.org were used to reference code where necessary

