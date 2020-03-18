import math
import time
import numpy as np
from random import randint

def ms_subsampler(epsilon, delta, number_variables, variable_ranges, block_size, sample):

	epsilon = epsilon
	delta = delta
	t = 1
	k = 0
	upper_bound = np.empty(number_variables)
	upper_bound.fill(1000000000)
	lower_bound = np.empty(number_variables)
	lower_bound.fill(-1000000000)
	beta = 1.5
	p = 1.1
	c = delta * (p-1)/p
	last = None
	initial_values = randint(0,len(sample)-(block_size+1))
	values = np.array(sample[int(initial_values):int(initial_values+block_size)])


	#Checking for stopping condition
	while (np.all((epsilon + 1) * lower_bound < (1 - epsilon) * upper_bound)):
		#print(((epsilon + 1) * lower_bound < (1 - epsilon) * upper_bound).all)
		#initial_values = [randint(0,len(sample)-(block_size+1)) for i in range(number_variables)]
		initial_values = randint(0,len(sample)-(block_size+1))

		if (t % 10 == 0):
			print('number of blocks: ', t)
			
		values = np.append(values, sample[int(initial_values):int(initial_values+block_size)], axis = 0)
		print('number of samples: ', values.size)
		t += block_size

		#Adding new value
		
		if t > np.floor(beta ** k):
			k += 1
			alpha = np.floor(beta ** k) / np.floor(beta ** (k - 1))
			dk = c / (0.00000000000001 + (math.log(k, p) ** p))
			x = -alpha * np.log(dk)/3
		
		#print('x: ', np.sqrt(2 * x / t))
		ct = np.std(values, axis = 0) * np.sqrt(2 * x / t) + 3 * variable_ranges * x / t
		#print('ct: ', ct)
		lower_bound = np.nanmax([lower_bound, np.abs(np.mean(values,axis = 0))-ct], axis = 0)
		print('lower bound: ', lower_bound)
		print('upper bound: ', upper_bound)
		#print('new values:', np.abs(np.mean(values,axis = 0))-ct)
		upper_bound = np.nanmin([upper_bound, np.abs(np.mean(values, axis = 0))+ct], axis = 0)
		print('convergence criteria: ', (epsilon + 1) * lower_bound, (1 - epsilon) * upper_bound)


	return values
