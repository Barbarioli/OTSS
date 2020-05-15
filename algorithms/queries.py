import numpy as np
from scipy.interpolate import interp1d
import pandas as pd

def threshold_query(data, threshold):

	result = []
	for point in data:
		if point > threshold:
			result.append(point)

	return result


def interpolation_query(data, point, type = 'linear'):

	result

	if data[point] != 'nan':
		return data[point]

	elif type == 'linear':
		return
	
	return	result

