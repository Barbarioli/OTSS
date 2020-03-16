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
	upper_bound.fill(10000000000000)
	lower_bound = np.empty(number_variables)
	lower_bound.fill(-1000000000000)
	beta = 1.5
	p = 1.1
	c = delta * (p-1)/p
	last = None
	initial_values = randint(0,len(sample)-(block_size+1))
	values = sample[int(initial_values):int(initial_values+block_size)]

	#Checking for stopping condition
	while (((epsilon + 1) * lower_bound < (1 - epsilon) * upper_bound).all):

		#initial_values = [randint(0,len(sample)-(block_size+1)) for i in range(number_variables)]
		initial_values = randint(0,len(sample)-(block_size+1))

		if (t % 10 == 0):
			print('sample size: ', t)
		#print(initial_values, initial_values+block_size)
		print(sample[int(initial_values):int(initial_values+block_size)])
		#np.concatenate(values, sample[int(initial_values):int(initial_values+block_size)])
		print(values)
		t += block_size

		#Adding new value

		if t > np.floor(beta ** k):
			k += 1
			alpha = np.floor(beta ** k) / np.floor(beta ** (k - 1))
			dk = c / (0.00000000000001 + (math.log(k, p) ** p))
			x = -alpha * np.log(dk)/3

		
		ct = np.std(values, axis = 0) * np.sqrt(np.absolute(2 * x / t)) + 3 * variable_ranges * x / t
		print(ct)
		lower_bound = np.maximum(lower_bound, np.abs(np.mean(values,axis = 0))-ct)
		print('lower bound: ', lower_bound)
		upper_bound = np.minimum(upper_bound, np.abs(np.mean(values, axis = 0))+ct)
		print('upper bound: ', upper_bound)


	return values
