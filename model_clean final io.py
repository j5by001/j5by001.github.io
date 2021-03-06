# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:22:44 2022

@author: odett
Learning python
This code is used to create An ABM with agents, with functions, lists as well as plot the values of y and x
"""

# import requests
import random
import operator
import matplotlib
import matplotlib.pyplot
import agentframework
import csv


random.seed(0)

# # defining function for distance between x and y
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5



#start_time = time.time()
  
# # creating list
num_of_agents = 100
num_of_iterations = 10
agents = []
neighbourhood = 20

#Initialize the environment
environment = []
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    row_list = []
    for value in row: # A list of value
        print(int(value)) # print list
        row_list.append(int(value))
    #print(row_list)
    environment.append(row_list)
f.close() 

# # return the number of rows and columns in the list
nrows = len(environment)
ncols = len(environment)
print("nrows 300", nrows)
print("ncols 300", ncols)

#print("time taken to execute lines 27 to 48" % (time.time() - start_time)) 

# #retrieve constructor from agentframework and passed through all the agents at random
for i in range(num_of_agents):
    agents.append(agentframework.Agent(random.randint(0, nrows),
                                       random.randint(0, ncols),
                                       environment, agents))    #agents.append(agentframework.Agent())
for i in range(num_of_agents):
    print(agents[i])

# Move the agents.
for j in range(num_of_iterations):
    #print("Iteration", j)
    for i in range(num_of_agents):
        agents[i].move() # The issue here was that the Agent class did not yet
                         # have a function called move defined. I have added 
                         # this.
        agents[i].eat()

            
        agents[i].share_with_neighbours(neighbourhood)


for i in range(num_of_agents):
    agents.append(agentframework.Agent())   
     
print(agents[i])              
print(neighbourhood)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()



# # Calculate the distance, maximum and minimum distance between all the agents.
distance = distance_between(agents[0], agents[1])
mind = distance
maxd = distance
for a in agents:
    for b in agents:
        if (a != b):
            distance = distance_between(a, b)
            mind = min(mind, distance)
            maxd = max(maxd, distance)
            print(distance, mind, maxd)
            
# # Calculate the distance, maximum and minimum distance between the agents.
distance = distance_between(agents[0], agents[1])
mind = distance
maxd = distance
for i in range(num_of_agents):
    for j in range(i + 1, num_of_agents, 1):
        a = agents[i]
        b = agents[j]
        #if (a != b):
        #if (i != j):
        #if (i < j):
        distance = distance_between(a, b)
        mind = min(mind, distance)
        maxd = max(maxd, distance)
        #print(i, j, distance, mind, maxd)
            




   

       
            
            
            
            
            
            
            
