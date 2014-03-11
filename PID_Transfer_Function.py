from numpy import *
from matplotlib import pyplot as plt
from scipy import signal

time_input = arange(0.0 , 100, 0.1)

m=100
c=10
k=10

#Simple Spring Mass System
sys = signal.lti(1,[m,c,k])

#Calculate a ramp input
u=[]
for i in range(1000):
	u=time_input+100

#Calculate the Spring Mass System from a combination step + ramp input
time1 , response, stateVector = signal.lsim(sys,u,time_input)

#Calculate Spring Mass System response for a step input
time2 , responseStep = sys.step(T=time_input)

plt.figure(1)
plt.plot(time1,response)

plt.figure(2)
plt.plot(time2,responseStep)
plt.show()
