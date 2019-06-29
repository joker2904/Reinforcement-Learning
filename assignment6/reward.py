from cartpole import calculateIteration
import numpy as np
import math



#returns reward (int), terminate condition(bool), and goal reached(bool)
def R(position,velocity,angle,angular,k1,k2,k3,k4,N,t):
	F = k1*position+k2*velocity+k3*angle+k4*angular
	#print(k1,k2,k3,k4,position,velocity,angle,angular,F)
	if F <= -100.0:
		F = -100.0		
	elif F >= 100.0:
		F = 100.0
	
	position,velocity,angle,angular = calculateIteration(position,velocity,angle,angular,F)
	print(position,velocity,angle,angular)
	if position > 5.0 or angle > 1.0:
		return -(N-t),True,False
	if position >= -0.1 and position <= 0.1 and angle >= -0.05 and angle <= 0.05:
		return 0,True,True
	return -1,False,False


def randomWeights():
	a = np.random.rand(4)
	k1 = a[0]
	k2 = a[1]
	k3 = a[2]
	k4 = a[3]
	return k1,k2,k3,k4	

def ZeroWeights():
	return 0.0001,0.0001,0.0001,0.0001

def UpdateWeights(position,velocity,angle,angular,k1,k2,k3,k4,G,t):
	alpha = 0.01
	discount = 0.001
	#calculate gradient of log of policy
	policy = k1*position+k2*velocity+k3*angle+k4*angular
	if policy <= -100.0 or policy >= 100.0: #gradient will be 0, so no change in weights
		return k1,k2,k3,k4 
	coefficient = (alpha*math.pow(discount,t)*G)/policy
	# d(log(policy))/d(weights)
	#updating components of weights according to partial derivative of policy wrt weights
	k1_new = k1 + coefficient*position  #   d(policy)/d(k1)
	k2_new = k2 + coefficient*velocity  #   d(policy)/d(k2)
	k3_new = k3 + coefficient*angle     #   d(policy)/d(k3)
	k4_new = k4 + coefficient*angular   #   d(policy)/d(k4)
	return k1_new,k2_new,k3_new,k4_new


#Function to calculate a basic initial policy based on random initialization of weights and finding the rewards
def CalculateBasicPolicy(Weights):
	N = 1000
	position = -1.0
	velocity = 0.25
	angle = 0.3
	angular = -0.7
	maxreward = 0.0
	k1,k2,k3,k4 = Weights()
	for t in range(N):
		# One episode
		print('Episode -',t,' ::')
		terminate = False
		reward = 0.0
		goal = False
		
		while terminate == False:
			r,terminate,success = R(position,velocity,angle,angular,k1,k2,k3,k4,N,t)
			reward += r
			goal |= success
			#print(r,terminate,success,goal)
		maxreward += reward
		print('Reward from episode -',maxreward)
	return maxreward



#Implement monte carlo policy gradient
def MonteCarloPolicyGradient(InitializeWeights,UpdateWeights):
	N = 1000
	position = -1.0
	velocity = 0.25
	angle = 0.3
	angular = -0.7
	maxreward = 0.0
	#Initialize the weights randomly
	k1,k2,k3,k4 = InitializeWeights()
	for t in range(N):
		# One episode
		print('Episode No-',t,' ::')
		terminate = False
		reward = 0.0
		goal = False
		step = 0
		while terminate == False:
			#Run one step of the episode and get the returns 
			r,terminate,success = R(position,velocity,angle,angular,k1,k2,k3,k4,N,t)
			reward += r
			goal |= success
			k1t,k2t,k3t,k4t = UpdateWeights(position,velocity,angle,angular,k1,k2,k3,k4,r,step)
			step += 1
			# terminating condition for episode . If goal is reached and weights do not change beyond a threshold
			if goal == True and np.abs(k1t-k1) <= 0.0001 and np.abs(k2t-k2) <= 0.0001 and np.abs(k3t-k3) <= 0.0001 and np.abs(k4t-k4) <= 0.0001:
				break
			print(r,terminate,success,goal)
			k1 = k1t
			k2 = k2t
			k3 = k3t
			k4 = k4t
		maxreward += reward
		print('Reward from episode -',reward)
	return maxreward




print('Training - ')
r = MonteCarloPolicyGradient(ZeroWeights,UpdateWeights)

#My current implementation is not converging
	
	
				
			
			
		
