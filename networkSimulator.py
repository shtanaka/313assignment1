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

import plotly
import plotly.graph_objs as go
import Simulator

if __name__ == "__main__":
	
	# print "Standard Simulator: "
	# print "M = choosen"
	# print "A = 50"
	# print "K = 4"
	# print "F = 4000"
	# print "e = 0.0001"
	# print "B = 50"
	# print "N = 5000"
	# M = raw_input("Type the error model:")
	# K = raw_input("Type the # of blocks:")
	# F = raw_input("Type the size of the frame:")
	# e = raw_input("Type the probability of error:")
	# B = raw_input("Type the burst length:")
	# N = raw_input("type the non-burst length:")
	# Simulator(M, K, F, e, B, N)
	
	NB = Simulator.Simulator("I")
	B = Simulator.Simulator("B")
	NB.call_methods()
	B.call_methods()
	graph_out = [
    	go.Bar(
       		x=['no bursts', 'bursts'],
       		y=[float(NB.worthy)/float(NB.totalTrials), float(B.worthy)/float(B.totalTrials)]
    		)
	]
	plotly.offline.plot(graph_out)



		

