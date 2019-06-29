import env  
import numpy as np
import matplotlib.pyplot as plt


# Exercise 4.1 : function to implement TD(0)
def td0(episodes):
	V = np.zeros((5,7))
	discount = 0.9
	alpha = 0.2
	for _ in np.arange(episodes):
		startingState = (3,0)
		grid = env.env(startingState)
		terminate = 0
		while terminate==0:
			a = np.random.choice([1, 3, 5], p = [0.25, 0.5, 0.25])
			s = grid.state			
			(r,terminate) = grid.step(a)
			V[s] = V[s] + alpha * ( r + discount*V[grid.state] - V[s] )
	return V
		

#Exercise 4.2 : Functions to implement Q-learning using epsilon greedy strategy
def QLearningUsingEpsilonGreedy(episodes):
	Q = np.zeros((5,7,8))
	discount = 0.9
	alpha = 0.2
	epsilon = 0.1
	for _ in np.arange(episodes):
		startingState = (3,0)
		grid = env.env(startingState)
		terminate = 0
		while terminate == 0:
			s = grid.state
			if np.random.rand() > epsilon:
				a = np.argmax(Q[s[0],s[1],:])
			else:
				a = np.random.choice([1, 3, 5], p = [0.25, 0.5, 0.25])
			(r,terminate) = grid.step(a)
			Q[s[0],s[1],a] = Q[s[0],s[1],a] + alpha*(r + (discount * np.max(Q[grid.state[0],grid.state[1],:])) - Q[s[0],s[1],a] )
	return Q	
	


#Function to draw policy 

import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

def drawPolicy(pi, cells , startstate, terminalStates ,wstates):
    xticks = np.arange(0,7)
    yticks = np.arange(0,5)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axis([0,7,0,5],'equal')
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    fig.gca().set_aspect('equal')
    fig.gca().invert_yaxis()
    ax.grid(True,color='k')
    for axi in (ax.xaxis, ax.yaxis):
        for tic in axi.get_major_ticks():
            tic.tick1On = tic.tick2On = False
            tic.label1On = tic.label2On = False
    for cell in cells:
        if cell in startstate:
            rect = Rectangle((cell[0],cell[1]),1,1,color='palegreen')
            ax.add_patch(rect)
	    
        if cell in terminalStates:
            rect = Rectangle((cell[0],cell[1]),1,1,color='red')
            ax.add_patch(rect)
	    
        elif cell in wstates:
            rect = Rectangle((cell[0],cell[1]),1,1,color='blue')
            ax.add_patch(rect)
        else:
            if pi[cell[1],cell[0]]==0:
                ax.arrow(cell[0]+0.85,cell[1]+0.85,-0.7,-0.7,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)
            elif pi[cell[1],cell[0]]== 1:
                ax.arrow(cell[0]+0.5,cell[1]+0.9,0,-0.8,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)
            elif pi[cell[1],cell[0]]==2:
                ax.arrow(cell[0]+0.15,cell[1]+0.85,0.7,-0.7,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)
            elif pi[cell[1],cell[0]]==3:
                ax.arrow(cell[0]+0.1,cell[1]+0.5,0.8,0,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)
            elif pi[cell[1],cell[0]]==4:
                ax.arrow(cell[0]+0.15,cell[1]+0.15,0.7,0.7,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)
            elif pi[cell[1],cell[0]]==5:
                ax.arrow(cell[0]+0.5,cell[1]+0.1,0,0.8,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)
            elif pi[cell[1],cell[0]]==6:
                ax.arrow(cell[0]+0.85,cell[1]+0.15,-0.7,0.7,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)
            elif pi[cell[1],cell[0]]==7:
                ax.arrow(cell[0]+0.9,cell[1]+0.5,-0.8,0,head_width=0.2, head_length=0.2,length_includes_head=True,
                        fill = True)

    fig.savefig('optimalpolicy.png')


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('state-value V(s) for each visited state using TD(0) Policy Evaluation :')
print(td0(1000))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Optimal V(s) for each visited state using epsilon greedy Q Learning:')
Q = QLearningUsingEpsilonGreedy(10000)
V_optimal = np.max( Q, axis = 2)
print(V_optimal)

print('Optimal Policy :')
optimalPolicy = np.argmax( Q, axis=2)
print(optimalPolicy)

states = [(y,x) for y in range(len(env.gridworld[0])) for x in range(len(env.gridworld))]
terminalStates = [(5,0)]
startstate = [(0,3)]
wstates =[(3,0),(4,0),(4,1),(4,6),(1,2),(2,2),(4,2),(2,3),(5,3),(2,4),(6,1)]
drawPolicy(optimalPolicy,states,startstate,terminalStates,wstates)



