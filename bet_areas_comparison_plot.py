import numpy as np
import matplotlib.pyplot as plt

bet_areas = [676, 449, 592, 409, 624, 469]
# refine_ls_wR_factor_ref = [0.0980, 0.1097, 0.0912]
# refine_ls_goodness_of_fit_ref = [1.045, 1.060, 1.038]
labels = ['With PIL under shear (our data)',
          'No PIL, no shear (synthesized as in Ref. S6) (our data)',
          '[S10], fast growth with 77% crystallinity',
          '[S10], slow growth with 93% crystallinity',
          '[Ref. S6]',
          '[Ref. S11]']
colors=['red', 'black', 'grey', 'grey', 'grey', 'grey']
ind = np.arange(len(bet_areas))  # the x locations for the groups
width = 0.35  # the width of the bars

figscalefactor = 0.7
fig, (ax1) = plt.subplots(1,1, sharey=True, figsize=(figscalefactor*12,figscalefactor*2.5))
# rects1 = ax.bar(ind - width/2, refine_ls_R_factor_all, width,
#                 label='R-factor for all reflections')
# rects2 = ax.bar(ind + width/2, refine_ls_wR_factor_ref, width,
#                 label='Weighted residual factors for all reflections')
# rects3 = ax.bar(ind + width/2, refine_ls_goodness_of_fit_ref, width,
#                 label='Least-squares goodness-of-fit parameter for all reflections')
ax1.barh(ind, bet_areas, color=colors)
ax1.set_xlabel('BET surface area, $m^2/g$')
ax1.set_yticks(ind)
ax1.set_yticklabels(labels)

plt.tight_layout()
plt.savefig('figures/BET_areas_CC3R_1.png', dpi=500)


# ===== COF ====

bet_areas = [148, 98, 330, 692, 329]
# refine_ls_wR_factor_ref = [0.0980, 0.1097, 0.0912]
# refine_ls_goodness_of_fit_ref = [1.045, 1.060, 1.038]
labels = ['With PIL under shear (our data)',
          'No PIL, no shear (our data)',
          '[Ref. S14]',
          '[Ref. S13]',
          '[Ref. S12]']
# colors=['#2ca02c', '#1f77b4', 'grey', 'grey', 'grey']
colors=['red', 'black', 'grey', 'grey', 'grey']
ind = np.arange(len(bet_areas))  # the x locations for the groups
width = 0.35  # the width of the bars

figscalefactor = 0.7
fig1, (ax2) = plt.subplots(1,1, sharey=True, figsize=(figscalefactor*12,figscalefactor*2.5))
# rects1 = ax.bar(ind - width/2, refine_ls_R_factor_all, width,
#                 label='R-factor for all reflections')
# rects2 = ax.bar(ind + width/2, refine_ls_wR_factor_ref, width,
#                 label='Weighted residual factors for all reflections')
# rects3 = ax.bar(ind + width/2, refine_ls_goodness_of_fit_ref, width,
#                 label='Least-squares goodness-of-fit parameter for all reflections')
ax2.barh(ind, bet_areas, color=colors)
ax2.set_xlabel('BET surface area, $m^2/g$')
ax2.set_yticks(ind)
ax2.set_yticklabels(labels)

plt.tight_layout()
plt.savefig('figures/BET_areas_COF_1.png', dpi=500)

# ======= MOF ======

bet_areas = [1671, 1348, 0, 0] # Basolite® C 300 produced by BASF: 1500-2100 m2/g
misc_lit_dict = {
    'S15':575,
    'S16':1055,
    'S17':1590,
    'S18':1716,
    'S19':855,
    'S20':1075,
    'S21':1150,
    'S22':1251.1
}
import operator
print(sorted(misc_lit_dict.items(), key=operator.itemgetter(1)))
misc_lit_labels = misc_lit_dict.keys()
misc_lit = [misc_lit_dict[x] for x in misc_lit_dict.keys()]
labels = ['With PIL under shear (our data)',
          'No PIL, no shear (our data)',
          'Literature (Refs. S15-S22)',
          'Basolite® C 300 (prod. by BASF)']
colors=['red', 'black', 'grey', 'grey', 'grey']
ind = np.arange(len(bet_areas))  # the x locations for the groups
ind[-1] = ind[-1] + 1
width = 0.35  # the width of the bars

figscalefactor = 0.7
fig2, (ax3) = plt.subplots(1,1, sharey=True, figsize=(figscalefactor*12,figscalefactor*2.5))
# rects1 = ax.bar(ind - width/2, refine_ls_R_factor_all, width,
#                 label='R-factor for all reflections')
# rects2 = ax.bar(ind + width/2, refine_ls_wR_factor_ref, width,
#                 label='Weighted residual factors for all reflections')
# rects3 = ax.bar(ind + width/2, refine_ls_goodness_of_fit_ref, width,
#                 label='Least-squares goodness-of-fit parameter for all reflections')
ax3.barh(ind, bet_areas, color=colors)
ys = misc_lit
xs = [ind[-2] for x in misc_lit]
ax3.scatter(ys, xs, marker="x")

ax3.errorbar(y=ind[-1],x=1800, xerr=300, linewidth=2)
ax3.scatter(1500, ind[-1], marker="|", color='#1f77b4')
ax3.scatter(2100, ind[-1], marker="|",color='#1f77b4')

ax3.set_xlabel('BET surface area, $m^2/s$')
ax3.set_yticks(ind)
ax3.set_yticklabels(labels)

plt.tight_layout()
plt.savefig('figures/BET_areas_MOF_1.png', dpi=500)
plt.legend()
plt.show()