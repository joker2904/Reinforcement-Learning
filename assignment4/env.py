#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:06:06 2018

@author: jannogga
modified by manzil
"""
import numpy as np

gridworld = np.load('gridworld.npy')
coordinateActions = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
                    #[NW,      N,      NE,     E,     SE,    S,     SW,     W]

class env:
    
	def __init__(self,startingState):
		self.state = startingState
    
	def reset(self):
		self.state = startingState
    
	def step(self, a):
		deviation = np.random.choice([-1, 0, 1], p = [0.2, 0.6, 0.2])
		action = (a + deviation) % 8
		tmp = tuple(map(sum, zip(self.state, coordinateActions[action])))
		self.state = tuple([np.clip(tmp[0], 0, 4), np.clip(tmp[1], 0, 6)])
		reward = gridworld[self.state]
		return (reward, 0) if reward == -1 else (reward, 1)
    


