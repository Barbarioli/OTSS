import multiprocessing as mp
import matplotlib.pyplot as plt
import sys
import warnings
import bocd
import numpy as np
from datetime import datetime


#Statements


if not sys.warnoptions:
    warnings.simplefilter("ignore")

def bayesian_detection(data, queue, hazard_constant, plot = False):

	start=datetime.now()
	print("breakpoint started")
	# Initialize object
	bc = bocd.BayesianOnlineChangePointDetection(bocd.ConstantHazard(hazard_constant), bocd.StudentT(mu=0, kappa=1, alpha=1, beta=1))

	print('finishing breakpoint')
	# Online estimation and get the maximum likelihood r_t at each time point
	rt_mle = np.empty(data.shape)
	for i, d in enumerate(data):
		bc.update(d)
		rt_mle[i] = bc.rt

	index_changes = np.where(np.diff(rt_mle)<0)[0]
	print(index_changes)
	print('final step')

	for i in range(len(index_changes)):
		print('storing data')
		if i == 0: 
			queue.put((0,index_changes[i]))
			print((0,index_changes[i]))
		elif i == len(index_changes)-1:
			queue.put((index_changes[i-1], index_changes[i]))
			print((index_changes[i-1], index_changes[i]))
			queue.put((index_changes[i], len(data)))
			print((index_changes[i], len(data)))
		else:
			queue.put((index_changes[i-1], index_changes[i]))
			print((index_changes[i-1], index_changes[i]))

	print('time taken', datetime.now()-start)
	return index_changes
