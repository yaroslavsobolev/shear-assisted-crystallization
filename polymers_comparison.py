import numpy as np
import matplotlib.pyplot as plt

def get_sizes_from_file(target_folder, file):
    data = np.zeros(shape=(2,2))
    target_file = target_folder + file
    with open(target_file) as oldfile:
        for i, line in enumerate(oldfile):
            if 'Particle size' in line:
                print(line)
            if 'Statistical report' in line:
               uptoline = i
               break
    temp_data = np.genfromtxt(target_file, delimiter='\t', skip_header=8, max_rows=uptoline - 8)
    return temp_data

from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
N = 3
data_stirring = []

data_stirring.append(get_sizes_from_file('data/crystal_growth/'
                                         'TA-with-different-polymers-under-shear-400rpm/',
                                         'TA without PIL-200 rpm- 3h.txt')[:,1])
data_stirring.append(get_sizes_from_file('data/crystal_growth/'
                                         'TA-with-different-polymers-under-shear-400rpm/',
                                         'TA-75 mg PIL-0.75 ml DMF-200 rpm- 3h- Size distribution.txt')[:,1])
data_stirring.append(get_sizes_from_file('data/crystal_growth/'
                                         'TA-with-different-polymers-under-shear-400rpm/',
                                         'TA-75 mg PMMA-0.75 ml DMF-200 rpm-3h.txt')[:,1])
data_stirring.append(get_sizes_from_file('data/crystal_growth/'
                                         'TA-with-different-polymers-under-shear-400rpm/',
                                         'TA-75 mg PVDF-0.75 ml DMF-200 rpm-3h.txt')[:,1])
print(data_stirring)

fig = figure(figsize=(3,2.5))
ax = axes()
bp = boxplot([data_stirring[0], data_stirring[1], data_stirring[2], data_stirring[3]],
             positions = [1.5+3*i for i in range(4)], widths = 0.6, whis=1000)
alpha = 0.3
for x in bp['boxes']:
    x.set(alpha=alpha)
for x in bp['caps']:
    x.set(alpha=alpha)
for x in bp['whiskers']:
    x.set(alpha=alpha)
for x in bp['fliers']:
    x.set(alpha=alpha)
for median in bp['medians']:
    median.set(linewidth=2)
    # for b in bp['boxes']:
    #     b.set_alpha(0.1)

for x in range(N):
    plt.axvline(x=3 + 3*x, color = 'black', alpha=0.15)

labels = ['No\npolymer', 'PIL-1', 'PMMA', 'PVDF']
labels.extend([1+i for i in range(N)])
ax.set_xticklabels(labels)
theticks = [1.5 + 3*i for i in range(N+1)]
ax.set_xticks(theticks)
ax.set_yscale('log')
ax.set_xlim(0,N*3+3)
plt.ylabel('Crystal size, µm')
ax.xaxis.set_tick_params(length=0)
plt.tight_layout()
plt.savefig('figures/polymer_compare.png', dpi=300)
plt.show()