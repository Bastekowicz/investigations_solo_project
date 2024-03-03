import numpy as np
import matplotlib.pyplot as plt
L=2
M=1 #M = 1 => mu = m
def func(y,m):
    return 9.81 * (1 + m*y * ( 4*M*L + 2*m*L - m*y ) / ( 2*(m*L - m*y +2*M*L)**2 ))

# time points
y = np.linspace(0,2)
plt.ylim([9,25])

plt.plot(y,func(y,100) , label = "$\mu = 100$")
plt.plot(y,func(y,10) , label = "$\mu = 10$")
plt.plot(y,func(y,1) , label= "$\mu = 1$")
plt.plot(y,func(y,0) , label = "$\mu = 0$") 





plt.legend()
plt.xlabel('position $(m)$')
plt.ylabel('acceleration $(m/s^2)$')
plt.show()