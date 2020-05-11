import multiprocessing as mp
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from random import randint
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

def online_subsampler(epsilon, delta, variable_range, block_size, data, queue, return_queue, index_queue, max_iteration = 100):
    
    """ Online subsampler for time series per Barbarioli, Bruno and Krishnan, Sanjay. 
    
    Inputs:
    epsilon : 
    delta : 
    variable_range : 
    block_size :
    data : time series being analyzed
    queue :
    result_queue:
    index_queue:
    max iteration: 
    
    Returns:
    it updates result_queue and index_queue in a multiprocess environment
    """

    epsilon = epsilon
    delta = delta  
    beta = 1.5
    p = 1.1
    c = delta * (p-1)/p
    last = None
    indexes = queue.get()

    #Checking for stopping condition
    print('subsampler started')
    time.sleep(3)
    while indexes:
        if (indexes[1] - indexes[0]) < block_size:
            print('Block size greater than data interval')
            print("----*----")
            indexes = queue.get()
            continue
            
        sample = data[indexes[0]:indexes[1]]
        print('Interval size: ', indexes[1] - indexes[0])
        upper_bound = 10000000000000
        lower_bound = -1000000000000
        t = 1
        k = 0
        values = np.empty(1)
        iteration = 0
        
        while ((epsilon + 1) * lower_bound < (1 - epsilon) * upper_bound):

            initial_value = randint(0,len(sample)-(block_size+1))
            values = np.concatenate((values,sample[initial_value:initial_value+block_size]), axis = None)
            t += block_size

            #Adding new value

            if t > np.floor(beta ** k):
                k += 1
                alpha = np.floor(beta ** k) / np.floor(beta ** (k - 1))
                dk = c / (0.00000000000001 + (math.log(k, p) ** p))
                x = -alpha * np.log(dk)/3
            

            ct = np.std(values) * np.sqrt(2 * x / t) + 3 * variable_range * x / t
            lower_bound = max(lower_bound, np.abs(np.mean(values))-ct)
            upper_bound = min(upper_bound, np.abs(np.mean(values))+ct)
            iteration += 1
            if iteration == max_iteration or len(values) >= len(sample):
                break
                
        if iteration == max_iteration or len(values) >= len(sample):
            return_queue.put(sample)
        else:
            return_queue.put(values)
        
        if iteration == max_iteration or len(values) >= len(sample):
            print('Relative sample size: ', '100%')
        else:
            print('Relative sample size: ', str(round(((block_size * iteration)/len(sample))*100,2)) +' %')
        
        print("----*----")
        index = indexes
        index_queue.put(index)
        indexes = queue.get()
        
    return
