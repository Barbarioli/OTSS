import numpy as np
import pandas as pd

def uniform_sampler(data, rate = 5):
    
    subsample = data[0:1]
    for i in range(0,len(data)):
        if i % rate == 0:
            subsample = pd.concat([subsample, data[i:i+1]])
    subsample = pd.concat([subsample, data[(len(data)-1):len(data)]])
    return subsample
