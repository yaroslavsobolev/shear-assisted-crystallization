import numpy as np
import matplotlib.pyplot as plt

base_folder = 'D:/Docs/Science/UNIST/Projects/shear_crystal_growth/Data/Size distribution data for 18 crystals/'
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
    # data = temp_data
    # if in_mm:
    #     data[:,1] = data[:,1]*1000
    # if um_to_mm:
    #     data[:, 1] = data[:, 1] / 1000
    # if no_vertlines:
    #     lw = 0
    # else:
    #     lw = 0.6
    # if axis:
    #     axis.hist(data[:,1], alpha=alpha, density=True, edgecolor='grey',linewidth=lw, bins=thebins)
    #     axis.hist(data[:,1], histtype='step', stacked=True, density=True,
    #              fill=False, color = 'black', linewidth=1.5, bins=thebins)
    # else:
    #     plt.hist(data[:,1], alpha=alpha, density=True, bins=thebins)
    #     plt.hist(data[:,1], histtype='step', stacked=True, density=True,
    #              fill=False, color = 'black', linewidth=1.5, bins=thebins)

# data = np.random.rand(2,3)
# plt.boxplot(data)
# plt.show()

# function for setting the colors of the box plots pairs
from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes

# def setBoxColors(bp):
    # setp(bp['boxes'][0], color='blue')
    # setp(bp['caps'][0], color='blue')
    # setp(bp['caps'][1], color='blue')
    # setp(bp['whiskers'][0], color='blue')
    # setp(bp['whiskers'][1], color='blue')
    # plt.setp(bp['fliers'][0], markeredgecolor='blue')
    # plt.setp(bp['fliers'][1], markeredgecolor='blue')
    # setp(bp['medians'][0], color='blue')

    # setp(bp['boxes'][1], color='red')
    # setp(bp['caps'][2], color='red')
    # setp(bp['caps'][3], color='red')
    # setp(bp['whiskers'][2], color='red')
    # setp(bp['whiskers'][3], color='red')
    # plt.setp(bp['fliers'][1], markeredgecolor='red')
    # plt.setp(bp['fliers'][3], markeredgecolor='blue')
    # setp(bp['medians'][1], color='red')

# Some fake data to plot

N = 3
data_stirring = []
# data_nostirring = []
# THIS IS FOR GROWTH FROM POWDER
# data_stirring.append(get_sizes_from_file('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/'
#                                          'Data/Stirring speed dependent crystallization-with PIL/'
#                                          '400 rpm/', 'size distribution-008.txt')[:,1])
# data_nostirring.append(get_sizes_from_file('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/'
#                                          'Data/Growth in PIL without shear/', 'size distribution-008.txt')[:,1])

data_stirring.append(get_sizes_from_file('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/'
                                         'Data/Data for Figure 2c/',
                                         'TA without PIL-200 rpm- 3h.txt')[:,1])
data_stirring.append(get_sizes_from_file('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/'
                                         'Data/Data for Figure 2c/',
                                         'TA-75 mg PIL-0.75 ml DMF-200 rpm- 3h- Size distribution.txt')[:,1])
data_stirring.append(get_sizes_from_file('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/'
                                         'Data/Data for Figure 2c/',
                                         'TA-75 mg PMMA-0.75 ml DMF-200 rpm-3h.txt')[:,1])
data_stirring.append(get_sizes_from_file('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/'
                                         'Data/Data for Figure 2c/',
                                         'TA-75 mg PVDF-0.75 ml DMF-200 rpm-3h.txt')[:,1])
# data_nostirring.append(get_sizes_from_file('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/'
#                                          'Data/Time dependent growth from solution/No stirring -SD/',
#                                          '10 min-SD.txt')[:,1])
print(data_stirring)
# print(data_nostirring)

# filenames_list_stirring = ['SD-Crystal {0}-stirring.txt'.format(i+1) for i in range(N)]
# for f in filenames_list_stirring:
#     data_stirring.append(get_sizes_from_file(base_folder, f)[:,1])

# filenames_list_nostirring = ['SD-Crystal {0}-non-stirring.txt'.format(i+1) for i in range(N)]
# for f in filenames_list_nostirring:
#     data_nostirring.append(get_sizes_from_file(base_folder, f)[:,1])

# add data for trimesic acid

# N = 3

# data_stirring = np.random.rand(10,18)
# data_nostirring = np.random.rand(10,18)
# A= [[1, 2, 5,],  [7, 2]]
# B = [[5, 7, 2, 2, 5], [7, 2, 5]]
# C = [[3,2,5,7], [6, 7, 3]]

fig = figure(figsize=(3,2.5))
ax = axes()
hold(True)

# first boxplot pair
# for i in range(N):
bp = boxplot([data_stirring[0], data_stirring[1], data_stirring[2], data_stirring[3]],
             positions = [1.5+3*i for i in range(4)], widths = 0.6, whis=1000)
# print('Number {0}, factor {1}'.format(i, np.mean(data_stirring[i])/np.mean(data_nostirring[i])))
# print(np.mean(data_stirring[i])/np.mean(data_nostirring[i]))
# setBoxColors(bp)
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


# # second boxplot pair
# bp = boxplot(B, positions = [4, 5], widths = 0.6)
# setBoxColors(bp)
#
# # thrid boxplot pair
# bp = boxplot(C, positions = [7, 8], widths = 0.6)
# setBoxColors(bp)

# set axes limits and labels
# ylim(0,9)
labels = ['No\npolymer', 'PIL-1', 'PMMA', 'PVDF']
labels.extend([1+i for i in range(N)])
# labels.append('TA')
ax.set_xticklabels(labels)
theticks = [1.5 + 3*i for i in range(N+1)]
# theticks.append(20)
ax.set_xticks(theticks)
ax.set_yscale('log')
ax.set_xlim(0,N*3+3)

# draw temporary red and blue lines and use them to create a legend
# hB, = plt.plot([1,1],'b-')
# hR, = plt.plot([1,1],'r-')
# legend((hR, hB),('With shear', 'Without shear'))
# hB.set_visible(False)
# hR.set_visible(False)
# plt.xlabel('Substance index')
plt.ylabel('Crystal size, µm')
ax.xaxis.set_tick_params(length=0)
plt.tight_layout()

plt.savefig('polymer_compare.png', dpi=300)
plt.show()