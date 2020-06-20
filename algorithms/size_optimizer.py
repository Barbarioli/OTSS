import numpy as np
import pandas as pd
from algorithms.empirical_bernstein import *
from algorithms.uniform_subsampler import *

def size_optimizer(data, size_online_subsample, range_series, error = 0.20):

	len_data = len(data)
	uniform_size = int(len_data/size_online_subsample)
	uniform_sample = uniform_sampler(data, uniform_size)

	approximation = 0.25
	eb_sample = empirical_bernstein(approximation,0.01,range_series,data)
	size_eb_sample = len(eb_sample)

	while abs(int(size_online_subsample - size_eb_sample)) > int(error * size_online_subsample):
		#print(int(size_online_subsample - size_eb_sample))
		#print(int(error * size_online_subsample))
		if approximation > 0.01:
			approximation = approximation - 0.01
			eb_sample = empirical_bernstein(approximation,0.01,range_series,data)
			size_eb_sample = len(eb_sample)
		else:
			return uniform_sample, eb_sample

	return uniform_sample, eb_sample