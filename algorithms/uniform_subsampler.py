import numpy as np

def uniform_sampler(data, rate = 2):
    
    subsample = []
    for i in range(0,len(data)):
        if i % rate == 0:
            subsample.append(data[i])
    
    return subsample