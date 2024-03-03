import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
L=2
M=1 #M = 1 => mu = m

def model(y,t,m):
    if y[0] > L: #Stop calculating when fallen length is longer than rope
        return [0,0]
    return [y[1] , 9.81 * (1 + m*y[0] * ( 4*M*L + 2*m*L - m*y[0] ) / ( 2*(m*L - m*y[0] + 2*M*L)**2 ))]

y0 = 0

# time points
time = np.linspace(0,0.7,200)

plt.figure(figsize = (5,7))
plt.ylim([0,2])

position, velocity = odeint(model, [0,0], time,(100,)).T   
plt.plot(time, position, label = "$\mu = 100$")

position, velocity = odeint(model, [0,0], time,(10,)).T   
plt.plot(time, position, label = "$\mu = 10$")

position, velocity = odeint(model,[0,0], time,(1,)).T   
plt.plot(time, position, label = "$\mu = 1$")

position, velocity = odeint(model,[0,0], time,(0,)).T   
plt.plot(time, position,label = "$\mu = 0$")

plt.plot(time, 1/2*9.81*time**2,linestyle=(0, (5, 5)),linewidth=3,label= "standard free-fall")

plt.legend()
plt.xlabel('time $(s)$')
plt.ylabel('position $(m)$')

plt.show()