import multiprocessing as mp
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from random import randint
import sys
import warnings

from algorithms.online_subsampler import *
from algorithms.analytics import *
from algorithms.breakpoint_detection import *
from algorithms.empirical_bernstein import *
from algorithms.uniform_subsampler import *
from algorithms.queries import *
from algorithms.size_optimizer import *
from algorithms.automated_subsampler import *

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def classification_sampling_online(dataframe, name, save = False, interpolation = False, zero_input = False, comparison = False):

	size = len(dataframe.T)
	number_series = len(dataframe.iloc[:,])

	dti = pd.date_range('2018-01-01', periods=size-1, freq='S')
	classes = dataframe.iloc[:,0]

	df = dataframe.T 
	df = df[1:]
	#print(df.head())

	df_subsample = pd.DataFrame()

	if comparison == True:

		df_uniform_sample = pd.DataFrame()
		df_eb = pd.DataFrame()

	for j in range(0,number_series):

		df_intermediate = df.iloc[:, j:j+1]
		#print(df_intermediate)
		values = [number for number in df_intermediate[j]]
		series = pd.Series(values, index = dti)
		minimum = np.abs(min(series.values))
		maximum = np.abs(max(series.values))
		#series = series + minimum
		variable_range = maximum - minimum

		#subsampling

		queue = mp.Queue()
		return_queue = mp.Queue()
		index_queue = mp.Queue()

		print("series " + str(j))

		p1 = mp.Process(target = detection, args = (series, queue, 0.025, 0.025, False, True))
		p2 = mp.Process(target = online_subsampler, args = (0.1,0.01,variable_range,25,series, queue, return_queue,index_queue, 200))

		p1.start()
		p2.start()
		p1.join()
		p2.join()
		
		print('finished')
		online_subsample = retrieve_data(return_queue)
		online_subsample_size = len(online_subsample)
		online_subsample = online_subsample - minimum
		online_subsample = online_subsample.resample('S').mean()

		df_subsample['series_' + str(j)] = online_subsample

		if comparison == True:

			uniform_sample, eb_sample = size_optimizer(series, online_subsample_size, 3, error = 0.25)
			uniform_sample = uniform_sample - minimum
			eb_sample = uniform_sample - minimum
			uniform_sample = uniform_sample.resample('S').mean()
			eb_sample = eb_sample.resample('S').mean()
			df_uniform_sample['series_' + str(j)] = uniform_sample
			df_eb['series_' + str(j)] = eb_sample

		if save == True and j % 100 == 0:

			df_subsample.to_csv('/Users/brunobarbarioli/Documents/Research/OTSS/subsamples/' + name + '.tsv',sep="\t", index=False)

			if comparison ==  True:

				df_uniform_sample.to_csv('/Users/brunobarbarioli/Documents/Research/OTSS/subsamples/' + name + '_uniform.tsv',sep="\t", index=False)
				df_eb.to_csv('/Users/brunobarbarioli/Documents/Research/OTSS/subsamples/' + name + '_eb.tsv',sep="\t", index=False)				



	if interpolation:

		df_subsample = df_subsample.interpolate(method = 'linear', direction = 'both')

	if zero_input:

		df_subsample = df_subsample.fillna(0)

	if save == True:

		df_subsample.to_csv('/Users/brunobarbarioli/Documents/Research/OTSS/subsamples/' + name + '.tsv',sep="\t", index=False)

		if comparison == True:

			df_uniform_sample.to_csv('/Users/brunobarbarioli/Documents/Research/OTSS/subsamples/' + name + '_uniform.tsv',sep="\t", index=False)
			df_eb.to_csv('/Users/brunobarbarioli/Documents/Research/OTSS/subsamples/' + name + '_eb.tsv',sep="\t", index=False)				


	return df_subsample
