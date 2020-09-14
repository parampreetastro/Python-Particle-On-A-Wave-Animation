# -*- coding: utf-8 -*-
"""
Parampreet Singh | parampreet_singh@hotmail.com
Simple Python Animation Of A Particle Tracing A Sine Wave Tutorial/Practice
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation




#Define a figure
fig, ax=plt.subplots()

#Define variables of 2pi, time steps, sin function, and plot the sine wave
v=2*np.pi
t=np.arange(0.0, v, 0.001) #This defines a series of times with a specified step increase
sin=np.sin(t)
l=plt.plot(t, sin)

#Define the axes
ax=plt.axis([0, v, -1, 1])

#Define the particle with initial starting point
part, =plt.plot([0], [np.sin(0)], 'ro')

#Define the animate function along the sine wave
def animate(i):
    part.set_data(i, np.sin(i))
    return part,

#Create the animation using the animation function
A=animation.FuncAnimation(fig, animate, frames=np.arange(0.0, v, 0.1), interval=20, blit=True)

#Give a title to the animation and the axes
plt.title("Particle On A Wave Animation")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#Save the animation as an gif file
#You may need to install PillowWriter there are various online resources of how to do this
#If you are using anaconda simply go to the anaconda prompt and type: conda install -c anaconda pillow
A.save('ParticleWave.gif', writer="PillowWriter")

#Show the final results of the animation and plotting
plt.show()