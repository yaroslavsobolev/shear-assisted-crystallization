from histograms_2 import *

# ========================= FIGURE 1 TIME GRAPH ======================
ms = 4
f1, ax1 = plt.subplots(1, sharex=True, sharey=False, figsize=(2.65, 2.85))
ax1.axhline(y=0, color = 'grey', alpha=0.7, dashes=[2,2])

# no_stirring_with_pil
no_shear_pil = [[0, 0, 0]]
s = get_sizes_from_file(base_folder+
                    'No stirring -SD-updated/', '4 min-SD.txt')[:, 1]
no_shear_pil.append([4, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    'No stirring -SD-updated/', '10 min-SD.txt')[:, 1]
no_shear_pil.append([10, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    'No stirring -SD-updated/', '30 min-SD.txt')[:, 1]
no_shear_pil.append([30, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    'No stirring -SD-updated/', '60 min-SD.txt')[:, 1]
no_shear_pil.append([60, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    'No stirring -SD-updated/', '120 min-SD.txt')[:, 1]
no_shear_pil.append([120, np.mean(s), np.std(s)])
no_shear_pil = np.array(no_shear_pil)
ax1.errorbar(no_shear_pil[:,0], no_shear_pil[:,1], no_shear_pil[:,2], fmt='-o',
             markersize=ms*0.7, color='black', alpha=0.8, label='With PIL, no shear',
             capthick=1, capsize=3)

# stirring_with_pil
do_shear_pil = [[0, 0, 0]]
s = get_sizes_from_file(base_folder+
                    'Stirring-SD-updated/Stirring-SD/', '4 min- SD.txt')[:, 1]
do_shear_pil.append([4, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    'Stirring-SD-updated/Stirring-SD/', '10 min-SD.txt')[:, 1]
do_shear_pil.append([10, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    'Stirring-SD-updated/Stirring-SD/', '30 min-SD.txt')[:, 1]
do_shear_pil.append([30, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    'Stirring-SD-updated/Stirring-SD/', '60 min-SD.txt')[:, 1]
do_shear_pil.append([60, np.mean(s), np.std(s)])
print([60, np.mean(s), np.std(s)])
do_shear_pil = np.array(do_shear_pil)
ax1.errorbar(do_shear_pil[:,0], do_shear_pil[:,1], do_shear_pil[:,2], fmt='-o',
             markersize=ms*0.7, color='#1f77b4', alpha=0.8, label='With PIL, with shear',
             capthick=1, capsize=3)

# stirring_without_pil
shear_no_pil = [[0, 0, 0]]
s = get_sizes_from_file(base_folder+
                    "Shearing TA without PIL IN DMF/"
                    'TA-108 mg+without pil- 400 rpm -time dependent/10 min/', '007-size distribution.txt')[:, 1]
shear_no_pil.append([10, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    "Shearing TA without PIL IN DMF/"
                    'TA-108 mg+without pil- 400 rpm -time dependent/30 min/', '005-size distribution.txt')[:, 1]
shear_no_pil.append([30, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    "Shearing TA without PIL IN DMF/"
                    'TA-108 mg+without pil- 400 rpm -time dependent/1 h/', '020-size distribution.txt')[:, 1]
shear_no_pil.append([60, np.mean(s), np.std(s)])
s = get_sizes_from_file(base_folder+
                    "Shearing TA without PIL IN DMF/"
                    'TA-108 mg+without pil- 400 rpm -time dependent/2 h/', '018-size distribution.txt')[:, 1]
shear_no_pil.append([120, np.mean(s), np.std(s)])

shear_no_pil = np.array(shear_no_pil)
ax1.errorbar(shear_no_pil[:,0], shear_no_pil[:,1], shear_no_pil[:,2], fmt='-o',
             markersize=ms*0.7, color='green', alpha=0.8, label='No PIL, with shear',
             capthick=1, capsize=3)

# NO PIL, WITH HEATING-OVERSATURATING-COOLING
s = get_sizes_from_file(base_folder+
                    "Shearing TA without PIL IN DMF/"
                    'ta-108 mg dissovle at 36 degree- then-stirring 400 rpm without pil-10 min/',
                        '010-size distribution.txt')[:, 1]
ax1.errorbar(10, np.mean(s), np.std(s), color='#bcbd22', linestyle="None", capsize=3, alpha = 0.5)
ax1.scatter(10, np.mean(s), marker='o', facecolors='white', edgecolors='#bcbd22', zorder=30)

s = get_sizes_from_file(base_folder+
                    "Shearing TA without PIL IN DMF/"
                    'TA-85 mg+23mg - without pil-400 rpm- 10 min/',
                        '017-Size distribution.txt')[:, 1]
ax1.scatter(10, np.mean(s), marker='s', facecolors='none', edgecolors='green')
# ax1.get_xaxis().set_ticks([0, 1, 2, 3, 4, 5, 6])
# ax1.get_yaxis().set_ticks([0, 200, 400, 600])

plt.ylim([-100, 980])
plt.xlim([-5, 125])
plt.ylabel('Average size, $\mu$m')
plt.xlabel('Time, minutes')
plt.tight_layout()
plt.savefig('figures/figure1_time_dependence.png', dpi=300)
# plt.show()