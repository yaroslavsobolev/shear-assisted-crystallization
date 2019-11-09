import numpy as np
import matplotlib.pyplot as plt

refine_ls_R_factor_all = [0.0440, 0.0472, 0.0368]
refine_ls_wR_factor_ref = [0.0980, 0.1097, 0.0912]
refine_ls_goodness_of_fit_ref = [1.045, 1.060, 1.038]
labels = ['With PIL under shear', 'Recrystallization', 'Solvent evaporation']
colors=['#2ca02c', '#1f77b4', '#1f77b4']


ind = np.arange(len(refine_ls_goodness_of_fit_ref))  # the x locations for the groups
width = 0.35  # the width of the bars

figscalefactor = 0.7
fig, (ax1, ax2, ax3) = plt.subplots(1,3, sharey=True, figsize=(figscalefactor*10,figscalefactor*2.5))
# rects1 = ax.bar(ind - width/2, refine_ls_R_factor_all, width,
#                 label='R-factor for all reflections')
# rects2 = ax.bar(ind + width/2, refine_ls_wR_factor_ref, width,
#                 label='Weighted residual factors for all reflections')
# rects3 = ax.bar(ind + width/2, refine_ls_goodness_of_fit_ref, width,
#                 label='Least-squares goodness-of-fit parameter for all reflections')
ax1.barh(ind, refine_ls_R_factor_all, color=colors)
ax1.set_xlabel('R-factor\nfor all reflections')
ax1.set_yticks(ind)
ax1.set_yticklabels(labels)

ax2.barh(ind, refine_ls_wR_factor_ref, color=colors)
ax2.set_xlabel('Weighted residual factors\nfor all reflections')
ax2.set_yticks(ind)

ax3.barh(ind, refine_ls_goodness_of_fit_ref, color=colors)
ax3.set_xlabel('Least-squares\ngoodness-of-fit\nparameter\n for all reflections')
ax3.set_yticks(ind)
# ax1.set_yticklabels(labels)


plt.tight_layout()
plt.savefig('SC_XRD__Rvalues_1.png', dpi=500)
plt.show()