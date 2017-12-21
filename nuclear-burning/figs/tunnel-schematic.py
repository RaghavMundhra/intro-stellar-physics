import numpy as np
import matplotlib.pyplot as plt

# wavefunctions (for plotting, just do simple barrier penetration into well)
ri = 0.5
rt = 3.0
ki = 9.0*np.pi
kappa = 1.0
ko = 1.0

C = 0.5*np.exp(-kappa*ri)*(np.sin(ki*ri) + ki/kappa*np.cos(ki*ri))
D = 0.5*np.exp(kappa*ri)*(np.sin(ki*ri) - ki/kappa*np.cos(ki*ri))
B = C*np.exp(kappa*rt)*(np.sin(ko*rt) + kappa/ko*np.cos(ko*rt)) +\
    D*np.exp(-kappa*rt)*(np.sin(ko*rt) - kappa/ko*np.cos(ko*rt))
A = C*np.exp(kappa*rt)*(np.cos(ko*rt) - kappa/ko*np.sin(ko*rt)) +\
    D*np.exp(-kappa*rt)*(np.cos(ko*rt) - kappa/ko*np.sin(ko*rt))

x_i = np.linspace(0.05,ri,50)
psi_i = 0.5*np.sin(ki*x_i)
x_t = np.linspace(ri,rt,50)
psi_t = 0.5*(C*np.exp(kappa*x_t) + D*np.exp(-kappa*x_t))
x_o = np.linspace(rt,8.0,50)
psi_o = 0.5*(A*np.cos(ko*x_o) + B*np.sin(ko*x_o))

plt.style.use('text-sans')
textwidth=2
ax = plt.figure(figsize=(textwidth,textwidth*0.618)).add_subplot(111)
ax.set_xlim(0.0,8.0)
ax.set_ylim(-5.0,6.0)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_xlabel(r'$r$')
ax.set_ylabel(r'$E$, $\psi$')

# Coulomb
rc = np.linspace(0.3,8.0)
Ec = 3.0/rc
plt.plot(rc,Ec,color='r',linewidth=1,solid_capstyle='round',solid_joinstyle='round')
# nuclear
plt.plot([0.05,0.05,0.5,0.5],[6.0,-5.0,-5.0,6.0],color='b',linewidth=1,solid_capstyle='round',solid_joinstyle='round')

# energy
plt.plot([0.05,0.5],[1.0,1.0],color='k',linestyle='-')
plt.plot([0.5,3.0],[1.0,1.0],color='k',linestyle=':')
plt.plot([3.0,8.0],[1.0,1.0],color='k',linestyle='-')

# wavefunction
plt.plot(x_i,psi_i,color='0.2',linewidth=0.5)
plt.plot(x_t,psi_t,color='0.2',linewidth=0.5)
plt.plot(x_o,psi_o,color='0.2',linewidth=0.5)
plt.savefig('tunnel-schematic.pdf',format='pdf')