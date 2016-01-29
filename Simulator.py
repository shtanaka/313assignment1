#!/usr/bin/python
import random
import math

class Simulator:
    
	
	def trialCheck(self, numErr, trials) :
		if numErr > 1 : 
			trials += 1
			if trials < self.T :
				self.runtime += self.F + self.K*self.r + 50
				self.nonburst(trials)
			else :
				print  "Not worthy"
				self.runtime += 50
				self.notWorthy += 1
				self.totalTrials += trials
		else :
			self.runtime += self.F + self.K*self.r + 50
			self.totalTrials += trials + 1
			self.worthy += 1

	
	def nonburst(self, trials=0): 
		
		# receives trials as parameter. starts at 0
		
		numErr = 0;
		for i in range(0, self.K) :
			for j in range(0, int(self.sizeBlock + self.r)):
				if random.random() <= self.e:
					numErr += 1
		self.trialCheck(numErr, trials)	
		

	def burst(self, trials=0):
		
		# receives trials as parameter. starts at 0
		numErr = 0;
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
					if random.random() <= self.e * ( self.N + self.B ) / self.B:
						numErr += 1
				else :
					if random.random() <= self.e:
						numErr += 1				
		self.trialCheck(numErr, trials)


		

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

		self.b = 0
		self.isBurst = False
		self.sizeBlock = self.F/self.K
		self.r = math.ceil(math.log (self.sizeBlock, 2))
		
		self.totalTrials = 0
		self.notWorthy = 0
		self.worthy = 0
		self.runtime = 0
		

		self.call_methods()