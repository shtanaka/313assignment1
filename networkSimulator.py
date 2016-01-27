#!/usr/bin/python
# coding=UTF-8 
# Copyright 2013 Edson Gustavo Santiago Silva
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import random

class simulator:
    
	def nonburst(self):

		print "### Trial " + str(self.trials+1) + "###"
		
		for i in range(0,self.K):
			for j in range(0,self.F):
				if random.random() <= self.e:
					self.numErr += 1
				if j % self.A == 0:
					print 'BLOCK:' + str(i) + '/BIT:' + str(j) + '/NUMERR:' + str(self.numErr)

		if self.numErr > 1:
			self.numErr = 0
			self.trials += 1
			if self.trials != self.T:
				self.nonburst()

	def burst(self):
		
		burst = False
		count = 0
		
		print "### Trial " + str(self.trials+1) + "###"

		for i in range(0,self.K):
			for j in range(0,self.F) :
				if burst is False :
					count += 1
					if count == self.N :
						print "Burst"
						count = 0
						burst = not burst
				else :
					count += 1
					if count == self.B :
						print "End of Burst"
						count = 0
						burst = not burst
					
				if burst :	
					if random.random() <= self.e * ( self.N + self.B ) / self.B:
						self.numErr += 1
				else :
					if random.random() <= self.e:
						self.numErr += 1
				if j % self.A == 0:
					print 'BLOCK:' + str(i) + '/BIT:' + str(j) + '/NUMERR:' + str(self.numErr)

		if self.numErr > 1:
			self.numErr = 0
			self.trials += 1
			if self.trials != self.t:
				self.burst()

	def call_method(self):
		if self.M == 'I' :
			self.nonburst()
		elif self.M == 'B' :
			self.burst()


	def __init__(self, M, K=4, F=4000, e=0.0001, B=50, N=5000):
		self.M = M
		self.A = 50
		self.K = K
		self.F = F
		self.e = e
		self.B = B
		self.N = N
		self.R = 5 * (10**6)
		self.T = 5
		self.numErr = 0
		self.trials = 0

		self.call_method()

if __name__ == "__main__":
	
	print "Standard Simulator: "
	print "M = choosen"
	print "A = 50"
	print "K = 1"
	print "F = 4000"
	print "e = 0.0001"
	print "B = 50"
	print "N = 5000"

	SC = raw_input("Standard or custom Simulator(S or C):")
	if SC == 'S':
		M = raw_input("Type the error model:")
		x = simulator(M)
	elif SC =='C':
		M = raw_input("Type the error model:")
		K = raw_input("Type the # of blocks:")
		F = raw_input("Type the size of the frame:")
		e = raw_input("Type the probability of error:")
		B = raw_input("Type the burst length:")
		N = raw_input("type the non-burst length:")
		x = simulator(M, K, F, e, B, N, x)