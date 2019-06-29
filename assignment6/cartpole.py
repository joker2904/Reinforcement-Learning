

import numpy as np
import matplotlib.pyplot as plt
import math




def calculateIteration(position,velocity,angle,angular,F):
	l = 0.8
	mc = 6
	mp = 3
	g = 9.81
	s = np.sin(angle)
	c = np.cos(angle)
	#Calculate angular and linear acceleration
	n = ( g*(mc+mp)*s ) - (F + mp*l*s*(angular * angular))*c
	d = ((4*l)/3)*(mc+mp) - (mp*l*c*c)
	angular_acceleration = n/d
	acceleration =  ( F - mp*l*( (angular_acceleration*c) - (angular*angular*s) ) )/(mp+mc)
	velocity += (acceleration * 0.01)
	position += (velocity *0.01)
	angular += (angular_acceleration * 0.01)
	angle += (angular * 0.01)
	#Apply gaussian noise 
	cov = [[0.004, 0,0,0], [0, 0.04,0,0], [0,0,0.001,0],[0,0,0,0.01] ] 
	mean = [0,0,0,0]
	a,b,c,d = np.random.multivariate_normal(mean, cov)
	position += a
	velocity += b
	angle += c
	angular += d
	return position,velocity,angle,angular

def simulate(F):
	p =[]
	v =[]
	an =[]
	av =[]
	position = -1.0
	velocity = 0.25
	angle = 0.3
	angular = -0.7
	
	interval = np.arange(0,1,0.01)
	
	for _ in interval:		
		p.append(position)
		v.append(velocity)
		an.append(angle)
		av.append(angular)
		#print(interval,position,velocity,theta,angular)
		position,velocity,angle,angular = calculateIteration(position,velocity,angle,angular,0)
	return p,v,an,av


def RunExperiment():
	a,b,c,d = simulate(0)
	interval = np.arange(0,1,0.01)

	#print(a,b,c,d)
	plt.plot(interval,a,label='position')
	plt.plot(interval,b,label='velocity')
	plt.plot(interval,c,label='angle')
	plt.plot(interval,d,label='angular velocity')
	plt.legend()
	plt.show()

RunExperiment()

		
			




