import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

base_folder = 'data/crystal_growth/Size distribution data for 18 crystals/'
def get_sizes_from_file(target_folder, file, is_in_nm=False):
    data = np.zeros(shape=(2,2))
    target_file = target_folder + file
    with open(target_file) as oldfile:
        for i, line in enumerate(oldfile):
            if 'Particle size' in line:
                foo = 1
            if 'Statistical report' in line:
               uptoline = i
               break
    temp_data = np.genfromtxt(target_file, delimiter='\t', skip_header=8, max_rows=uptoline - 8)
    if is_in_nm:
        temp_data = temp_data/1000
    return temp_data

from pylab import plot, show, savefig, xlim, figure, \
                ylim, legend, boxplot, setp, axes

def setBoxColors(bp):
    setp(bp['boxes'][0], color='blue')
    setp(bp['caps'][0], color='blue')
    setp(bp['caps'][1], color='blue')
    setp(bp['whiskers'][0], color='blue')
    setp(bp['whiskers'][1], color='blue')
    plt.setp(bp['fliers'][0], markeredgecolor='blue')
    setp(bp['medians'][0], color='blue')

    setp(bp['boxes'][1], color='red')
    setp(bp['caps'][2], color='red')
    setp(bp['caps'][3], color='red')
    setp(bp['whiskers'][2], color='red')
    setp(bp['whiskers'][3], color='red')
    plt.setp(bp['fliers'][1], markeredgecolor='red')
    setp(bp['medians'][1], color='red')

N = 19
data_stirring = []
data_nostirring = []

data_stirring.append(get_sizes_from_file('data/crystal_growth/'
                                         'TA-time-dependence-PIL-under-shear/Stirring-SD/',
                                         '10 min-SD.txt')[:,1])
data_nostirring.append(get_sizes_from_file('data/crystal_growth/'
                                         'TA-time-dependence-PIL-no-shear/',
                                         '10 min-SD.txt')[:,1])
print('Numbers of crystals: ')
print(len(data_stirring[0]))
print(len(data_nostirring[0]))

filenames_list_stirring = ['SD-Crystal {0}-stirring.txt'.format(i+1) for i in range(N)]
for nn, f in enumerate(filenames_list_stirring):
    if nn == 18:
        is_in_nm = True
    else:
        is_in_nm = False
    data_stirring.append(get_sizes_from_file(base_folder, f, is_in_nm)[:,1])

filenames_list_nostirring = ['SD-Crystal {0}-non-stirring.txt'.format(i+1) for i in range(N)]
for nn,f in enumerate(filenames_list_nostirring):
    if nn == 18:
        is_in_nm = True
    else:
        is_in_nm = False
    data_nostirring.append(get_sizes_from_file(base_folder, f, is_in_nm)[:,1])


N = 20


fig = figure(figsize=(11,2.5))
ax = axes()
the_ratios = []
pvalues = []
for i in range(N):
    bp = boxplot([data_nostirring[i], data_stirring[i]], positions = [1.2+3*i, 1.8+3*i], widths = 0.6, whis=1000)
    the_ratio = np.mean(data_stirring[i])/np.mean(data_nostirring[i])
    ks_here = stats.ks_2samp(data_stirring[i], data_nostirring[i])[1]
    tt_here = stats.ttest_ind(data_stirring[i], data_nostirring[i], equal_var=True)[1]
    mw_here = stats.mannwhitneyu(data_stirring[i], data_nostirring[i], alternative='greater')[1]
    pvalues.append(ks_here)
    pvalues.append(tt_here)
    pvalues.append(mw_here)
    print('#{0}\t{1:.2f}\t{2:.2f}\t{3:.2e}\t{4:.2e}\t{5:.2e}'.format(
        i+1, the_ratio,
        np.median(data_stirring[i]) / np.median(data_nostirring[i]),
        ks_here,
        tt_here,
        mw_here))
    the_ratios.append(the_ratio)
    setBoxColors(bp)
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

print('Avg. ratio: {0}'.format(np.mean(np.array(the_ratios))))
print('Highest p-value: {0}'.format(np.max(np.array(pvalues))))

for x in range(N):
    plt.axvline(x=3 + 3*x, color = 'black', alpha=0.15)

# set axes limits and labels
labels = ['1']
labels.extend([2+i for i in range(N)])
ax.set_xticklabels(labels)
theticks = [1.5 + 3*i for i in range(N)]
ax.set_xticks(theticks)
ax.set_yscale('log')
ax.set_xlim(-0.5,(N-1)*3+3)
ax.set_ylim(0.5, 1000)

# draw temporary red and blue lines and use them to create a legend
hB, = plt.plot([1,1],'b-')
hR, = plt.plot([1,1],'r-')
legend((hR, hB),('With shear', 'Without shear'))
hB.set_visible(False)
hR.set_visible(False)
plt.ylabel('Crystal size, µm')
ax.xaxis.set_tick_params(length=0)
plt.tight_layout()

plt.savefig('figures/boxcompare11_.png', dpi=300)
ax.yaxis.tick_right()
ax.set_ylim(0.01, 0.3)
plt.tight_layout()

plt.savefig('figures/boxcompare12_.png', dpi=300)
plt.show()