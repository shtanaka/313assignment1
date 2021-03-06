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
# test

import random
import math

class Simulator:
    
	
	def trial_check(self, numErr, trials) :
		if numErr > 1 : 
			trials += 1
			if trials < self.T[0] :
				self.runtime += self.F + self.K*self.r + 50
				self.nonburst(trials)
			else :
				self.runtime += 50
				self.notWorthy += 1
				self.totalTrials += trials
				self.fth.append([0, trials])
				self.ftr.append(trials)
		else :
			self.runtime += self.F + self.K*self.r + 50
			self.totalTrials += trials + 1
			self.worthy += 1
			self.ftr.append((trials+1))
			self.fth.append([float(self.F) / float((self.F + self.K*self.r + 50)), trials+1])

	def nonburst(self, trials=0): 
		
		# receives trials as parameter. starts at 0
		
		numErr = 0;
		random.seed = self.T[trials+1]
		for i in range(0, self.K) :
			for j in range(0, int(self.sizeBlock + self.r)):
				if random.random() <= self.e:
					numErr += 1
			if numErr > 1 :
				break
			else :
				numErr = 0
		self.trial_check(numErr, trials)	
		

	def burst(self, trials=0):
		
		# receives trials as parameter. starts at 0
		numErr = 0;
		random.seed = self.T[trials+1]
		for i in range(0, self.K) :
			for j in range(0, int(self.sizeBlock + self.r)):
				if self.isBurst is False :
					self.b += 1
					if self.b == self.N :
						self.b = 0
						self.isBurst = not self.isBurst
				else :
					self.b += 1
					if self.b == self.B :
						self.b = 0
						self.isBurst = not self.isBurst
				if self.isBurst :	
					if random.random() <= self.e * ( float(self.N) + float(self.B) ) / float(self.B):
						numErr += 1
				else :
					if random.random() <= self.e:
						numErr += 1
			if numErr > 1 :
				break
			else :
				numErr = 0				
		self.trial_check(numErr, trials)

	def get_results(self) :
		print self.M
		print self.A
		print self.K
		print self.F
		print self.e
		print self.B
		print self.N
		print self.R
		print self.T
		print " "
		print "------------------"
		print "Results"
		print "FRAME TRANSMISSION"
		print str(self.frametx) + " " + str(self.rc1) + " " + str(self.rc2) 
		print "THROUGHPUT"
		print str(self.thput) + " " + str(self.tc1) + " " + str(self.tc2) 
		print "------------------"
		print " "

	def find_throughput(self) :
		fth = []
		fths = 0
		for i in self.fth:
			fth.append(i[0])
			fths += i[0]
		self.thput = fths/self.totalTrials
		s2 = 0.0
		for i in self.fth :
			s2 = s2 + (i[0] - self.thput)**2/i[1]
		s = s2**0.5
		self.tc1 = self.thput - 1.962*s/self.totalTrials
		self.tc2 = self.thput + 1.962*s/self.totalTrials

	def find_frametx(self) :
		ftrs = 0
		for i in self.ftr :
			ftrs += i
		self.frametx = float(ftrs)/self.worthy
		s2 = 0.0
		for i in self.ftr :
			s2 = s2 + (i - self.frametx)**2/i
		s = s2**0.5
		self.rc1 = self.frametx - 1.962*s/self.worthy
		self.rc2 = self.frametx + 1.962*s/self.worthy

	def call_methods(self) :
		# while runtime is not 5 * 10**6 ms
		while self.runtime < self.R:
			if self.M == 'I' :
				self.nonburst()
			elif self.M == 'B' :
				self.burst()
		else :
			self.find_throughput()
			self.find_frametx()
			#self.ftr = float(self.totalTrials)/float(self.worthy)
			self.get_results()

	def __init__(self, M, K=2, F=4000, e=0.0005, B=50, N=5000):
		self.M = M
		self.A = 50
		self.K = int(K)
		self.F = int(F)
		self.e = float(e)
		self.B = int(B)
		self.N = int(N)
		self.R = 5 * (10**6)
		self.T = [5,24, 24, 70, 83, 53]
		self.b = 0
		self.isBurst = False
		self.sizeBlock = self.F/self.K
		self.r = math.ceil(math.log (self.sizeBlock, 2))
		self.fth = []
		self.tc1 = 0
		self.tc2 = 0
		self.thput = 0
		self.ftr = []
		self.rc1 = 0
		self.rc2 = 0
		self.frametx = 0
		self.totalTrials = 0
		self.notWorthy = 0
		self.worthy = 0
		self.runtime = 0 