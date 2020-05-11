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

def subsample_analysis(return_queue, index_queue):
    """function to analyze the subsample in terms of accuracy and sample size

    Input: 
    return_queue:
    index_queue"

    Output:
    subsample_average:
    relative_size:
    """
    
    subsample = return_queue.get()
    indexes = index_queue.get()
    subsample_average = np.full((indexes[1]-indexes[0]),np.mean(subsample))
    relative_size = np.full((indexes[1]-indexes[0]),len(subsample)/(indexes[1]-indexes[0]))
    
    while return_queue.empty() == False:
        
        subsample = return_queue.get()
        indexes = index_queue.get()
        size = indexes[1]-indexes[0]
        subsample_average = np.concatenate((subsample_average, np.full(size,np.mean(subsample))), axis = None)
        relative_size = np.concatenate((relative_size, np.full(size,len(subsample)/size)), axis = None)
    
    return subsample_average, relative_size