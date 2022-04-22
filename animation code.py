# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 02:35:11 2022

@author: odett
"""
import requests
import bs4
import matplotlib
matplotlib.use('TkAgg') 


root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1

# def run() 
#     animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#     canvas.draw() 
#     pass

# pulling data from external source

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs) 

    
num_of_agents = 10
num_of_iterations = 100
agents = []

root = tkinter.Tk() 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, y, x))   
    
def run(): 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()   


 
             
     # Make the agents.
 for i in range(num_of_agents):
         agents.append([random.randint(0,100),random.randint(0,100)])

 for i in range(num_of_agents):
     y = int(td_ys[i].text)
     x = int(td_xs[i].text)
     agents.append(agentframework.Agent(environment, agents, y, x)) 

 carry_on = True	
    	
 def update(frame_number):
        
         fig.clear()   
         global carry_on
        
         for i in range(num_of_agents):
             if random.random() < 0.5:
                 agents[i][0]  = (agents[i][0] + 1) % 99 
             else:
                 agents[i][0]  = (agents[i][0] - 1) % 99
            
             if random.random() < 0.5:
                 agents[i][1]  = (agents[i][1] + 1) % 99 
             else:
                 agents[i][1]  = (agents[i][1] - 1) % 99 
            
         if random.random() < 0.1:
             carry_on = False
             print("stopping condition")
        
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


    ax.set_autoscale_on(False)

  
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
            #print(agents[i][0],agents[i][1])

   		
def gen_function(b = [0]):
        a = 0
        global carry_on #Not actually needed as we're not assigning, but clearer
        while (a < 10) & (carry_on) :
            yield a			# Returns control and waits next call.
            a = a + 1


for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    
    
 # run animaation and create menu and draw on canvas

  def run(): 
#    #animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()   
   
root = tkinter.Tk() 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

  tkinter.mainloop()       
            