#!/usr/bin/python
# coding=UTF-8 
# Copyright 2016 Edson Gustavo Santiago Silva
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
# install numpy and plotly

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
	
	NB1 = Simulator.Simulator("B", e=0.0005, N=5000, B=50)
	NB2 = Simulator.Simulator("B", e=0.0005, N=1000, B=50)
	NB3 = Simulator.Simulator("B", e=0.0005, N=5000, B=500)
	NB4 = Simulator.Simulator("B", e=0.0005, N=1000, B=500)
	
	NB1.call_methods()
	NB2.call_methods()
	NB3.call_methods()
	NB4.call_methods()
	#B = Simulator.Simulator("B")
	#NB2 = Simulator.Simulator("I")
	#B2 = Simulator.Simulator("B")
	
	#B.call_methods()
	#NB2.call_methods()
	#B2.call_methods()
	
	BurstTime = go.Bar(
    	x=['(N=5000,B=50)', '(N=1000,B=50)', '(N=5000,B=500)', '(N=1000,B=500)'],
    	y=[NB1.thput, NB2.thput, NB3.thput, NB4.thput],
    	name='Throughput'
	)
	c1 = go.Bar(
    	x=['(N=5000,B=50)', '(N=1000,B=50)', '(N=5000,B=500)', '(N=1000,B=500)'],
    	y=[NB1.tc1, NB2.tc1, NB3.tc1, NB4.tc1],
    	name='c1'
	)
	c2 = go.Bar(
    	x=['(N=5000,B=50)', '(N=1000,B=50)', '(N=5000,B=500)', '(N=1000,B=500)'],
    	y=[NB1.tc2, NB2.tc2, NB3.tc2, NB4.tc2],
    	name='c2'
	)	
	data = [ c2, BurstTime, c1]

	layout = go.Layout(barmode='group')
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig)



		

