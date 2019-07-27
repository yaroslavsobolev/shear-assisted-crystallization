import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker

f1, ax = plt.subplots(1, figsize=(4,6))
plt.axvline(x=1, linestyle='-.', color='black', alpha=0.6)

data = np.loadtxt('data/rheometry/dynamic_relaxation/PIL1_402k_strain_test.txt', skiprows=2)
strain = data[:,0]
storage_modulus = data[:,1]
loss_modulus = data[:,2]
plt.loglog(strain, storage_modulus, color='#1f77b4', alpha=0.8, label='''G\', MW 402k g/mol''')
plt.loglog(strain, loss_modulus, '--', color='#1f77b4', linewidth=2, alpha=0.8, label='''G\", MW 402k g/mol''')

data = np.loadtxt('data/rheometry/dynamic_relaxation/PIL1_849k_strain_test.txt', skiprows=2)
strain = data[:,0]
storage_modulus = data[:,1]
loss_modulus = data[:,2]
plt.loglog(strain, storage_modulus, color='#ff7f0e', alpha=0.8, label='''G\', MW 849k g/mol''')
plt.loglog(strain, loss_modulus, '--', color='#ff7f0e', linewidth=2, alpha=0.8, label='''G\", MW 849k g/mol''')

# plt.xlim([0.5, 1e3])
# ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
# ax.xaxis.set_major_formatter(mticker.FormatStrFormatter('%f'))
ax.set_xticklabels(['0.0001', '0.001', '0.01', '0.1', '1', '10', '100'])
plt.ylim([1e-4, 1e2])
plt.xlabel('Shear strain, %')
plt.ylabel('Dynamic modulus, Pa')
plt.legend()
plt.tight_layout()
plt.savefig('rheometry_4.png', dpi=500)
plt.show()