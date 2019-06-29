# Expectation Calculation for question 2.3 and 2.4
# It is assuming that only the first non solved task will be attempted again. after that no non-solved tasks will be attempted again. hence maximum number of attempts is 8
def expectedReturnFirstNonSolvedTask(policy,attempts,first_task_nonsolved):
	if len(policy) > 0 and attempts <= 8 :  # Max number of attempts is 8 
		# we take the next task and increase attempts
		task = policy[0]
                if  first_task_nonsolved == False:
			second_attempt_pass = task[1] + expectedReturnFirstNonSolvedTask(policy[1:], attempts+2,True)	
			second_attempt_fail = 0 + expectedReturnFirstNonSolvedTask(policy[1:], attempts+2,True)
			first_attempt_pass  =      task[2]     * ( task[1] +  expectedReturnFirstNonSolvedTask(policy[1:], attempts+1,False) )
			first_attempt_fail  =  (1-task[2])     * (    0    +  (task[2]/2)*second_attempt_pass + (1-task[2]/2)*second_attempt_fail )         
			return first_attempt_pass + first_attempt_fail
		if first_task_nonsolved == True : #This means that once task has already been failed and tried. No more second tries
			first_attempt_pass  =      task[2]     * ( task[1] +  expectedReturnFirstNonSolvedTask(policy[1:], attempts+1,True) )
			first_attempt_fail  =  (1-task[2])     * (    0    +  expectedReturnFirstNonSolvedTask(policy[1:], attempts+1,True) )                
			return first_attempt_pass + first_attempt_fail               
	else:
		return 0


#Task 2.3 
# Find expectations of Policy A and B 
tasks = [(1, 12, 0.25), (2, 4, 0.4), (3, 10, 0.35), (4, 5, 0.6), (5, 7, 0.45), (6, 3, 0.5), (7, 50, 0.15)]

policyA = tasks #Policy A, sequential order
policyB = sorted(tasks, key=lambda task: task[2], reverse=True) # Policy B, order of increasing difficulty
print "Policy A:",policyA
print "Expected return of policy A :",expectedReturnFirstNonSolvedTask(policyA,0,False) 

print "Policy B",policyB
print "Expected return of policy B :",expectedReturnFirstNonSolvedTask(policyB,0,False) 

#Task 2.4
# Randomly shuffle the order of tasks to generate all policies. Check the expected return of each policy and find the best 
import itertools
maxer = 0
for policy in list(itertools.permutations(tasks)) :
	#print("Current Policy :",policy)
	er = expectedReturnFirstNonSolvedTask(policy,0,False)
	if er > maxer :
		maxer = er
		policyC = policy		
	#print("Expected return of current policy :",er )
	

print "Improved policy C :",policyC
print "Expected Return of policy C :",maxer
