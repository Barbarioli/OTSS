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


def empirical_bernstein(epsilon, delta, variable_range, sample, block_size = 1):

    epsilon = epsilon
    delta = delta
    t = 1
    k = 0
    upper_bound = 10000000000000
    lower_bound = -1000000000000
    beta = 1.5
    p = 1.1
    c = delta * (p-1)/p
    last = None
    values = pd.Series(sample[0:1])

    #Checking for stopping condition
    while ((epsilon + 1) * lower_bound < (1 - epsilon) * upper_bound):

        initial_value = randint(0,len(sample)-(block_size+1))
        values = pd.concat([values, sample[initial_value:initial_value+block_size]])
        t += block_size

        #Adding new value

        if t > np.floor(beta ** k):
            k += 1
            alpha = np.floor(beta ** k) / np.floor(beta ** (k - 1))
            dk = c / (0.00000000000001 + (math.log(k, p) ** p))
            x = -alpha * np.log(dk)/3

        ct = np.std(values) * np.sqrt(2 * x / t) + 3 * variable_range * x / t
        lower_bound = max(lower_bound, np.abs(np.mean(values))-ct)
        #print('lower bound: ', lower_bound)
        upper_bound = min(upper_bound, np.abs(np.mean(values))+ct)
        #print('upper bound: ', upper_bound)
    values = pd.concat([values, sample[(len(sample)-1):len(sample)]])
    values = values.loc[~values.index.duplicated(keep = 'first')]
    
    return values