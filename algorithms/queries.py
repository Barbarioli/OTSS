import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from scipy.stats import linregress

def threshold_query(data, threshold):

	result = []
	for point in data:
		if point > threshold:
			result.append(point)

	return result


def interpolation_query(data, point, method = 'linear'):

	new_data = data.interpolate(method)
	return new_data[point]

def interpolation_distance(real_data, subsample_data, method = 'linear', distance = 'euclidean'):

	interpolated_data = subsample_data.interpolate(method)
	
	if distance == 'euclidean':

		euclidean_distance = np.linalg.norm(real_data-interpolated_data)
		return euclidean_distance

	elif distance == 'dtw':
		distance, path = fastdtw(real_data, interpolated_data, dist=euclidean)
		return distance


def correlation_query(data, number_of_lags = 2, print_lags = True, plot = True):
	
	result = []
	for i in range(number_of_lags):
		value = data.autocorr(lag = i+1)
		if print_lags:
			print('lag ' + str(i) + ": ", value)

		result.append(value)

	if plot:
		plot_acf(data.values, lags=number_of_lags)
	
	return	result

def similarity_query(data, interval):

	return

def comparison_query(data, interval):
	
	return 

