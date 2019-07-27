import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

f1,ax = plt.subplots(1, figsize=(2.5,1.2))
satlevels = np.array([587.23, 281.97, 164.85, 167.17])/1000
errors = np.array([7.613971638, 7.725291982, 3.177756779, 2.779545779])/1000
xticklabels = ['DMF','mono','402k','849k']
barlist=plt.bar(xticklabels, satlevels, yerr=errors)
ax.set_xticklabels(xticklabels, rotation = 20)#, ha="right")
barlist[0].set_color('grey')
barlist[0].set_alpha(0.8)
barlist[1].set_color('green')
barlist[1].set_alpha(0.5)
barlist[2].set_color('#1f77b4')
barlist[3].set_color('#ff7f0e')

# plt.xlim([6e-5, 1e3])
# plt.ylim([0.5e-3, 2e3])
# plt.xlabel('Shear rate, $s^{-1}$')
plt.ylabel('$c_{s}$, M')
plt.tight_layout()
# ax.set_xticks([1e-3, 1e-1, 1e1, 1e3])
plt.savefig('sat_conc_1.png', dpi=500)
plt.show()