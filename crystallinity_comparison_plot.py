import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

f1, (ax, ax2) = plt.subplots(2, figsize=(8,6))
data = np.loadtxt('data/PXRD/crystallinity/pxrd_crystallinities.txt', skiprows=1, delimiter='\t')
xlabels = ['{0:.0f}'.format(x) for x in data[:,0]]
# plt.bar(xlabels, data[:,1])

# set width of bar
barWidth = 0.3

# set height of bar
bars1 = data[:,1]
bars2 = data[:,2]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

# Make the plot
ax.bar(r1, bars1, width=barWidth, color='#2ca02c', label='Grown with PIL under shear')
ax.bar(r2, bars2, width=barWidth, label='Grown by conventional method')
# plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')

# residual errors
data = np.loadtxt('data/PXRD/residual_errors/pxrd_r_errors.txt', skiprows=1, delimiter='\t')
xlabels = ['{0:.0f}'.format(x) for x in data[:,0]]
# plt.bar(xlabels, data[:,1])

# set width of bar
barWidth = 0.3

# set height of bar
bars1 = data[:,2]
bars2 = data[:,1]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

# Make the plot
ax2.bar(r1, bars1, width=barWidth, color='#2ca02c', label='Grown with PIL under shear')
ax2.bar(r2, bars2, width=barWidth, label='Grown by conventional method')

# Add xticks on the middle of the group bars
# plt.xlabel('group', fontweight='bold')
ax.set_xticks([r + barWidth/2 for r in range(len(xlabels))])
ax.set_xticklabels(xlabels)
ax.set_xlim([-0.5, 16.7])
ax2.set_xticks([r + barWidth/2 for r in range(len(xlabels))])
ax2.set_xticklabels(xlabels)
ax2.set_xlim([-0.5, 16.7])

f1.subplots_adjust(top=0.8)
f1.subplots_adjust(bottom=0.2)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3),
          ncol=3)#, fancybox=True, shadow=True)
plt.xlabel('Substance ID')
ax.set_ylabel('Crystallinity, %')
ax2.set_ylabel('Residual\nerror of fit, %')
# plt.tight_layout()
plt.savefig('figures/crystallinities_1.png', dpi=700)
plt.show()

# barlist=plt.bar(xticklabels, satlevels, yerr=errors)
# ax.set_xticklabels(xticklabels, rotation = 20)#, ha="right")
# barlist[0].set_color('grey')
# barlist[0].set_alpha(0.8)
# barlist[1].set_color('green')
# barlist[1].set_alpha(0.5)
# barlist[2].set_color('#1f77b4')
# barlist[3].set_color('#ff7f0e')
# barlist[3].set_alpha(0.8)
# ax.set_yticks([0, 0.3, 0.6])
# plt.ylim(0,0.7)
# # plt.xlim([6e-5, 1e3])
# # plt.ylim([0.5e-3, 2e3])
# # plt.xlabel('Shear rate, $s^{-1}$')
# plt.ylabel('$c_{s}$, M')
# plt.tight_layout()
# # ax.set_xticks([1e-3, 1e-1, 1e1, 1e3])
