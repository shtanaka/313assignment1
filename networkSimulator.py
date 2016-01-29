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
import math

class simulator:
    


	def nonburst(self, sentBlocks=0):
		
		# recursive code to nonburst. it receive as 
		# parameters how many blocks were sent. starts at 0
		
		msgSize = self.sizeBlock + self.r
		# for each block not sent yet
		for i in range(sentBlocks, self.K) :
			# for each bit of the block, including the checkbits
			for j in range(0, int(msgSize)):
				# if error occurs, count++
				if random.random() <= self.e:
					self.numErr += 1
			# if after send the block there's more than 1 error, go for next trial
			if self.numErr > 1 :
				break
			# else mark the block as sent
			else :
				self.numErr = 0
				sentBlocks += 1
		# check if it reached the limit of trials. if not, call nonburst()
		# passing as param how many blocks were sent. else increases as
		# not worthy	
		if self.numErr > 1 :
			self.numErr = 0
			self.trials += 1

			if self.trials < self.T :
				self.runtime += msgSize + 50
				self.nonburst(sentBlocks)
			else :
				print  "Not worthy"
				self.runtime += msgSize + 50
				self.notWorthy += 1
				self.totalTrials += self.trials
				self.trials = 0
		# if low # of errors or 0 blocks divided, increase worthy
		else :
			print str(self.trials + 1) + " Trials"
			self.runtime += self.F + 50
			self.totalTrials += self.trials + 1
			self.trials = 0 
			self.worthy += 1

	def burst(self, sentBlocks=0):
		
		# recursive code to burst. it receive as 
		# parameters how many blocks were sent. starts at 0
		# values to call the burst time

		msgSize = self.sizeBlock + self.r
		for i in range(sentBlocks, self.K) :
			for j in range(0, int(msgSize)):
				# increment burstTime
				if self.burstTime is False :
					self.count += 1
					if self.count == self.N :
						print "Burst"
						self.count = 0
						self.burstTime = not self.burstTime
				else :
					self.count += 1
					if self.count == self.B :
						print "End of Burst"
						self.count = 0
						self.burstTime = not self.burstTime

				if self.burstTime :	
					if random.random() <= self.e * ( self.N + self.B ) / self.B:
						self.numErr += 1
				else :
					if random.random() <= self.e:
						self.numErr += 1		
				
			if self.numErr > 1 :
				break
			else :
				self.numErr = 0
				sentBlocks += 1
		
		if self.numErr > 1 :
			self.numErr = 0
			self.trials += 1
			if self.trials < self.T :
				self.runtime += msgSize + 50
				self.nonburst(sentBlocks)
			else :
				print  "Not worthy"
				self.runtime += msgSize + 50
				self.notWorthy += 1
				self.totalTrials += self.trials
				self.trials = 0
		else :
			print str(self.trials + 1) + " Trials"
			self.runtime += self.F + 50
			self.totalTrials += self.trials + 1
			self.trials = 0 
			self.worthy += 1
			

	def call_methods(self):
		# while runtime is not 5 * 10**6 ms
		while self.runtime < self.R:
			if self.M == 'I' :
				self.nonburst()
			elif self.M == 'B' :
				self.burst()
		else :
			print "Delivered blocks: " + str(self.worthy) + " in " + str(self.totalTrials) + " trials."

	def __init__(self, M, K=4, F=4000, e=0.0001, B=50, N=5000):
		self.M = M
		self.A = 50
		self.K = int(K)
		self.F = int(F)
		self.e = float(e)
		self.B = float(B)
		self.N = float(N)
		self.R = 5 * (10**6)
		self.T = 5

		self.burstTime = False
		self.count = 0
		self.numErr = 0
		self.trials = 0
		self.totalTrials = 0
		self.notWorthy = 0
		self.worthy = 0
		self.runtime = 0
		self.tput = 0
		self.ttf = 0
		self.sizeBlock = self.F/self.K
		self.r = math.ceil(math.log (self.sizeBlock, 2))

		self.call_methods()


if __name__ == "__main__":
	
	print "Standard Simulator: "
	print "M = choosen"
	print "A = 50"
	print "K = 4"
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
		x = simulator(M, K, F, e, B, N)