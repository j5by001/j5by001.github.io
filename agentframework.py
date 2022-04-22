# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:25:28 2022

@author: odett
"""

import random


class Agent:
    
    # Constructor 
    
    def __init__ (self, y, x, store, agents, environment):
        
               
     def __init__ (self, distance, neighbourhood, average): 
         
      #
               
      self.y = y
      self.x = x
      self.distance = distance
      self.store = store
      self.agents = agents
      self.environment = environment   
     # self.neighbourhood = neighbourhood
        #self.distance_between = distance_between
      self.average = average
        
       
    # converting the agents into string    
    def __str__(self):
        return "y=" + str(self.y) + ", x=" + str(self.x) + ", store=" + str(self.store)
    
            
        def distance_between(self, agent, neighbourhood):
            return ((self.x - agent.x)**2) + ((self.y - agent.y)**2)**0.5
            print(distance_between)
        
       
        def average(agent, store):
            average = (self.store + self.agent) / 2
            print(average)
            
        def share_with_neighbours(self, neighbourhood):
            for agent in self.agents:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    avg = sum / 2
                    self.store = avg
                    agent.store = avg
                    print("sharing" + str(dist) + " " + str(avg))
                           
        
        
             
    def move(self):
        # self.y = y
        # self.x = x
        """
        Randomly increases or decreases the x and y coordinate values.

        Returns
        -------
        None.

        """
        # Change x
        if(random.random() < 0.5):
            self.x = self.x + 1
            print("Increases x")
        else:
            self.x = self.x - 1
            #print("Decreases x")
        # Change y
        if(random.random() < 0.5):
            #print("Increases y")
            self.y = self.y + 1
        else:
            self.y = self.y - 1
            #print("Decreases y")
            
       
    def eat(self): # eat what is left
                 if self.environment[self.y][self.x] > 10:
                     self.environment[self.y][self.x] -= 10
                     self.store += 10
                 print(self.store) 
                 
                 
    # # distance between the 2 agents in the first 2 rows
    # def distance_between(agents_row_a, agents_row_b):
    #     return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5
    # print(distance_between)
    # #print(a.y, a.x)
    
        