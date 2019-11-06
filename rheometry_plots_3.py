import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# def find_nearest(array, value):
#     array = np.asarray(array)
#     idx = (np.abs(array - value)).argmin()
#     return array[idx]
#
# sr_0 = 9
#
# def get_eta_0(sr, viscosity, sr_0 = sr_0):
#     array = np.asarray(sr)
#     idx = (np.abs(array - sr_0)).argmin()
#     return viscosity[idx]

f1 = plt.figure(1, figsize=(4,6))
# plt.axhline(y=1, linestyle='--', color='black', alpha=0.8)

data = np.loadtxt('data/rheometry/dynamic_relaxation/PIL1_402k_1percent.txt', skiprows=2)
freq = data[:,0]
storage_modulus = data[:,1]
loss_modulus = data[:,2]
plt.loglog(freq, storage_modulus, color='#1f77b4', alpha=0.8, label='''G\', MW 402k g/mol''')
plt.loglog(freq, loss_modulus, '--', color='#1f77b4', linewidth=2, alpha=0.8, label='''G\", MW 402k g/mol''')

ida = 10
idb = 30
pfit = np.polyfit(np.log10(freq[ida:idb]), np.log10(storage_modulus[ida:idb]), 1)
print(pfit)
# line_fit = 10**(pfit[0]*np.log10(freq[ida:idb]) + pfit[1])
line_fit = 10**(2*np.log10(freq[15:20]) - 3.2)
plt.loglog(freq[15:20], line_fit, color='black', alpha=0.6)

line_fit = 10**(1*np.log10(freq[8:15]) - 0.7)
plt.loglog(freq[8:15], line_fit, color='black', alpha=0.6)

def fitfunction(f, a):
    return a*f

ida = 1
idb = 15
popt, pcov = curve_fit(fitfunction, freq[ida:idb], loss_modulus[ida:idb])
print('nu_zero = {0}'.format(popt))

ida = 2
idb = 10
def fitfunction(f, a):
    return a*f**(1/2)

popt, pcov = curve_fit(fitfunction, freq[ida:idb], storage_modulus[ida:idb])
print(popt)
fit_sampled = popt[0]*freq**(1/2)
freq1 = np.copy(freq)

data = np.loadtxt('data/rheometry/dynamic_relaxation/PIL1_849k_1percent.txt', skiprows=2)
freq = data[:,0]
storage_modulus = data[:,1]
loss_modulus = data[:,2]
plt.loglog(freq, storage_modulus, color='#ff7f0e', alpha=0.8, label='''G\', MW 849k g/mol''')
plt.loglog(freq, loss_modulus, '--', color='#ff7f0e', linewidth=2, alpha=0.8, label='''G\", MW 849k g/mol''')

# plt.loglog(freq1[:-15], fit_sampled[:-15], color='black', alpha=0.5) #label='$G\'=\\alpha\\omega^{1/2}$'
# orange

plt.xlim([0.5, 1e3])
# plt.ylim([0.52, 1.07])
plt.xlabel('Frequency, rad/s')
plt.ylabel('Dynamic modulus, Pa')
plt.legend()
plt.tight_layout()
plt.savefig('figures/rheometry_3a.png', dpi=500)

# # plt.xlabel('Shear rate, $s^{-1}$')
# # plt.ylabel('Viscosity, Pa$\cdot$s')
# plt.tight_layout()
# plt.savefig('figures/rheometry_2.png', dpi=500)
plt.show()