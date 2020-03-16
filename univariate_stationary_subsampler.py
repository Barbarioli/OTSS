#import cv2
#from dlcv.utils import *
#from dlcv.struct import Operator, Box
import math
import time
import numpy as np
from random import randint

"""
class EBGS(Operator):
	EBGStop (Empirical Bernstein Stopping) as in the paper:
	Volodymyr Mnih, Csaba Szepesvári, and Jean-Yves Audibert. 2008. Empirical Bernstein stopping. 
	In Proceedings of the 25th international conference on Machine learning (ICML '08). 
	ACM, New York, NY, USA, 672-679. DOI=http://dx.doi.org/10.1145/1390156.1390241
	
	def __init__(self, epsilon, delta, variable_range):
		EBGS is an adaptative sampling algorithm that uses a geometric sampling schedule 
		with a near-optimal stopping rule for relative error estimation on bounded random variable

		Args:
			epsilon (float): 
			delta (float): user definided confidence, i.e., the event happens with 
			probability at least (1-delta)
			variable_range (float): range of the variable being measured
		
		self.epsilon = epsilon
		self.delta = delta
		self.range = variable_range
		self.t = 1
		self.k = 0
		self.upper_bound = 10000000000000
		self.lower_bound = -1000000000000
		self.beta = 1.5
		self.p = 1.1
		self.filter="object"
		self.c = self.delta * (self.p-1)/self.p
		self.indicator = []
		self.region = Box(200,550,350,750)
		self.last = None


	def __iter__(self):
		self.frame_iter = iter(self.video_stream)
		self.super_iter()
		return self


	def __next__(self):
		out = next(self.frame_iter)


		#Checking for stopping condition
		if (self.epsilon + 1) * self.lower_bound < (1 - self.epsilon) * self.upper_bound:
			self.t += 1
			if self.last == None:
				pass
			elif 'bounding_boxes' in self.last:
			#print('number of bounding boxes:',len(self.last['bounding_boxes']))
				cnt = 0
				for label, pt in self.last['bounding_boxes']:
					box = Box(*pt)
					if label == self.filter and self.region.contains(box):
						cnt += 1
					else:
						pass
				if cnt == 0:
					self.indicator.append(0)
					
				else:
					#print('1')
					self.indicator.append(1)
			
			#Adding new value

			if self.t > np.floor(self.beta ** self.k):
				self.k += 1
				self.alpha = np.floor(self.beta ** self.k) / np.floor(self.beta ** (self.k - 1))
				self.dk = self.c / (0.00000000000001 + (math.log(self.k, self.p) ** self.p))
				self.x = -self.alpha * np.log(self.dk) / 3

			values = np.asarray(self.indicator)
			ct = np.std(values)* np.sqrt(2 * self.x / self.t) + 3 * self.range * self.x / self.t
			self.lower_bound = max(self.lower_bound, np.abs(np.mean(values))-ct)
			self.upper_bound = min(self.upper_bound, np.abs(np.mean(values))+ct)
		

			self.last = out
			return out
		else:
			return self.__next__()


	def _serialize(self):
		return {'epsilon': self.epsilon, 'delta': self.delta, 'range': self.range}
"""


class us_subsampler(object):

	def __init__(self, epsilon, delta, variable_range, block_size, block_type, sample):


		self.epsilon = epsilon
		self.delta = delta
		self.range = variable_range
		self.t = 1
		self.k = 0
		self.upper_bound = 10000000000000
		self.lower_bound = -1000000000000
		self.beta = 1.5
		self.p = 1.1
		self.c = self.delta * (self.p-1)/self.p
		self.last = None
		self.block_size = block_size
		self.block_type = block_type
		self.values = []

	def __iter__(self):
		self.iter = iter(self.sample)
		self.super_iter()
		return self


	def __next__(self):
		out = next(self.iter)

				#Checking for stopping condition
		if (self.epsilon + 1) * self.lower_bound < (1 - self.epsilon) * self.upper_bound:
			self.t += 1
			if self.last == None:
				pass
			else:
				self.values.append(self.last)
			#Adding new value

			if self.t > np.floor(self.beta ** self.k):
				self.k += 1
				self.alpha = np.floor(self.beta ** self.k) / np.floor(self.beta ** (self.k - 1))
				self.dk = self.c / (0.00000000000001 + (math.log(self.k, self.p) ** self.p))
				self.x = -self.alpha * np.log(self.dk) / 3


			ct = np.std(values)* np.sqrt(2 * self.x / self.t) + 3 * self.range * self.x / self.t
			self.lower_bound = max(self.lower_bound, np.abs(np.mean(values))-ct)
			self.upper_bound = min(self.upper_bound, np.abs(np.mean(values))+ct)
			print(self.values)

			self.last = out
			return out
		else:
			return self.__next__()

