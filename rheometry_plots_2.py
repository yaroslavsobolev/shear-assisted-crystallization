import numpy as np
import matplotlib.pyplot as plt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

sr_0 = 9

def get_eta_0(sr, viscosity, sr_0 = sr_0):
    array = np.asarray(sr)
    idx = (np.abs(array - sr_0)).argmin()
    return viscosity[idx]

f1 = plt.figure(1, figsize=(2.45,4.9))
plt.axhline(y=1, linestyle='--', color='black', alpha=0.8)

data = np.loadtxt('data/rheometry/PIL1_849k__13.4equiv.txt', skiprows=2, usecols=[0,1,2,3,4])
sr = data[:,2]
viscosity = data[:,4]/1000
eta_0 = get_eta_0(sr, viscosity)
plt.semilogx(sr, viscosity/eta_0, color='#ff7f0e', linewidth=3)

data = np.loadtxt('data/rheometry/PIL1_402k__26.8equiv_3h.txt', skiprows=2, usecols=[0,1,2,3,4])
sr = data[:,1]
viscosity = data[:,3]/1000
eta_0 = get_eta_0(sr, viscosity)
plt.semilogx(sr, viscosity/eta_0, color='#1f77b4', linewidth=2, alpha=0.5)

data = np.loadtxt('data/rheometry/PIL1_402k__13.4equiv_3h_C.txt', skiprows=2, usecols=[0,1,2])
sr = data[:,1]
viscosity = data[:,2]/1000
eta_0 = get_eta_0(sr, viscosity)
plt.semilogx(sr, viscosity/eta_0, color='#1f77b4', linewidth=3)
idx = 4
pfit = np.polyfit(np.log10(sr[1:idx]), viscosity[1:idx]/eta_0, 1)
intersection = 10**((1-pfit[1])/pfit[0])
print(intersection)
visc_fit = pfit[0]*np.log10(sr) + pfit[1]
plt.semilogx(sr, visc_fit, '--', label='fit', color='black', alpha=0.6)
plt.semilogx(intersection, 1, 'o', markersize=4, color='black', alpha=1, markeredgecolor='black')

data = np.loadtxt('data/rheometry/PIL1_402k__6.7equiv_3h.txt', skiprows=2, usecols=[0,1,2,3,4])
sr = data[:,1]
viscosity = data[:,3]/1000
eta_0 = get_eta_0(sr, viscosity)
plt.semilogx(sr, viscosity/eta_0, color='#1f77b4', linewidth=4, alpha=0.5)
idx = 4
pfit = np.polyfit(np.log10(sr[:idx]), viscosity[:idx]/eta_0, 1)
intersection = 10**((1-pfit[1])/pfit[0])
print(intersection)
visc_fit = pfit[0]*np.log10(sr) + pfit[1]
plt.semilogx(sr, visc_fit, '--', label='fit', color='black', alpha=0.6)
plt.semilogx(intersection, 1, 'o', markersize=4, color='black', markeredgecolor='black', alpha=1)

plt.xlim([9, 1e3])
plt.ylim([0.52, 1.07])
plt.xlabel('Shear rate, $s^{-1}$')
plt.ylabel('$\eta/\eta_{0}$')
plt.tight_layout()
plt.savefig('rheometry_2.png', dpi=500)

plt.show()