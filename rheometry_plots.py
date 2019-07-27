import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

f1,ax = plt.subplots(1, figsize=(2.7,5))
data = np.loadtxt('data/rheometry/PIL1_849k__13.4equiv.txt', skiprows=2, usecols=[0,1,2,3,4])
sr = data[:,2]
viscosity = data[:,4]/1000
plt.loglog(sr, viscosity, color='#ff7f0e', linewidth=3)

data = np.loadtxt('data/rheometry/PIL1_402k__26.8equiv_3h.txt', skiprows=2, usecols=[0,1,2,3,4])
sr = data[:,1]
viscosity = data[:,3]/1000
plt.loglog(sr, viscosity, color='#1f77b4', linewidth=2, alpha=0.5)

data = np.loadtxt('data/rheometry/PIL1_402k__13.4equiv_3h_C.txt', skiprows=2, usecols=[0,1,2])
sr = data[:,1]
viscosity = data[:,2]/1000
plt.loglog(sr, viscosity, color='#1f77b4', linewidth=3)

data = np.loadtxt('data/rheometry/PIL1_402k__6.7equiv_3h.txt', skiprows=2, usecols=[0,1,2,3,4])
sr = data[:,1]
viscosity = data[:,3]/1000
plt.loglog(sr, viscosity, color='#1f77b4', linewidth=4, alpha=0.5)

data = np.loadtxt('data/rheometry/monomer_2equiv.txt', skiprows=2, usecols=[0,1])
sr = data[:,0]
viscosity = data[:,1]/1000
plt.loglog(sr, viscosity, color='green', linewidth=3, alpha=0.5)

plt.axhline(9.2E-4, linestyle='--', color='black', linewidth=3, alpha=0.5)

plt.xlim([6e-5, 1e3])
plt.ylim([0.5e-3, 2e3])
plt.xlabel('Shear rate, $s^{-1}$')
plt.ylabel('Viscosity ($\eta$), Pa$\cdot$s')
plt.tight_layout()

locmaj = tck.LogLocator(base=100,numticks=10)
ax.xaxis.set_major_locator(locmaj)
locmin = tck.LogLocator(base=1000.0,subs=(0.01,0.1,1),numticks=30)
ax.xaxis.set_minor_locator(locmin)
ax.xaxis.set_minor_formatter(tck.NullFormatter())
ax.set_xticks([1e-3, 1e-1, 1e1, 1e3])
plt.savefig('rheometry_1.png', dpi=500)
print(1)

# f2 = plt.figure(2, figsize=(2,2))
# data = np.loadtxt('data/rheometry/PIL1_849k__13.4equiv.txt', skiprows=3, usecols=[0,1,2,3,4])
# sr = data[:,2]
# viscosity = data[:,4]/1000
# plt.loglog(sr, viscosity, color='#ff7f0e', linewidth=3)
#
# data = np.loadtxt('data/rheometry/PIL1_402k__13.4equiv_3h_corr.txt', skiprows=3, usecols=[0,1])
# sr = data[:,0]
# viscosity = data[:,1]/1000
# plt.loglog(sr, viscosity, color='#1f77b4', linewidth=3)
#
# plt.xlim([1, 1e3])
# plt.ylim([0.09, 1.1])
# # plt.xlabel('Shear rate, $s^{-1}$')
# # plt.ylabel('Viscosity, Pa$\cdot$s')
# plt.tight_layout()
# plt.savefig('rheometry_1_inset.png', dpi=500)
plt.show()