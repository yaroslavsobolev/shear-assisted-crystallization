import numpy as np
import matplotlib.pyplot as plt

base_folder = 'data/crystal_growth/'

#Lifshits-Slyozov_distribution
def LS_distr(input):
    x = np.copy(input)
    x[x>1.5] = 0
    return 4/9*x**2*(3/(3 + x))**(7/3) * (1.5/(1.5-x))**(11/3) * np.exp(-1.5/(1.5-x))

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

def plot_file(target_folder, target_files, alpha=0.5, axis=False, thebins=np.linspace(0,900,18),
              in_mm=False, no_vertlines=False, um_to_mm=False, add_LS=False, fillcolor='#1f77b4',
              edgecolor2=False):
    data = np.zeros(shape=(2,2))
    for k, file in enumerate(target_files):
        target_file = target_folder + file
        with open(target_file) as oldfile:
            for i, line in enumerate(oldfile):
                if 'Statistical report' in line:
                   uptoline = i
                   break
        temp_data = np.genfromtxt(target_file, delimiter='\t', skip_header=8, max_rows=uptoline - 8)
        if k == 0:
            data = temp_data
        else:
            data = np.concatenate((data, temp_data), axis=0)
    if in_mm:
        data[:,1] = data[:,1]*1000
    if um_to_mm:
        data[:, 1] = data[:, 1] / 1000
    if no_vertlines:
        lw = 0
    else:
        lw = 0.6
    if axis:
        axis.hist(data[:,1], alpha=alpha, density=True, edgecolor='grey',linewidth=lw, bins=thebins,color=fillcolor)
        if edgecolor2:
            axis.hist(data[:, 1], histtype='step', stacked=True, density=True,
                      fill=False, color='black', linewidth=1.5, bins=thebins, edgecolor=edgecolor2)
        else:
            axis.hist(data[:,1], histtype='step', stacked=True, density=True,
                     fill=False, color = 'black', linewidth=1.5, bins=thebins)
    else:
        plt.hist(data[:,1], alpha=alpha, density=True, bins=thebins, color=fillcolor)
        plt.hist(data[:,1], histtype='step', stacked=True, density=True,
                 fill=False, color = 'black', linewidth=1.5, bins=thebins)
    if add_LS:
        meanshift = 1
        LS_points = np.linspace(0,900,180)
        LS_y = LS_distr(LS_points/(meanshift*np.mean(data[:, 1])))
        # meanls = np.mean(LS_y)
        axis.plot(LS_points[LS_y > 0], 0.4*LS_y[LS_y>0]/((LS_points[1]-LS_points[0])*np.sum(LS_y))) #
    print('Mean: {0}, Mean cubed: {1}'.format(np.mean(data[:, 1]), np.mean(data[:, 1])**3))

def plot_RPMs():
    f1, (ax0, ax1, ax2, ax3) = plt.subplots(4, sharex=True, sharey=False, figsize=(2,5))
    plot_file(base_folder + \
                  'Growth in PIL without shear/',
              ['size distribution-008.txt'],
              alpha=0.5,
              axis=ax0)
    ax0.text(.90, .75, '$\dot{\gamma} = 0 \enspace s^{-1}$',
            horizontalalignment='right',
            transform=ax0.transAxes)
    plot_file(base_folder + \
                  'Stirring speed dependent crystallization-with PIL/'
                  '60 rpm/',
              ['size distribution-007.txt', 'size distribution-007.txt'],
              alpha=0.5,
              axis=ax1)
    ax1.text(.98, .75, '$\dot{\gamma} = 25 \enspace s^{-1}$',
            horizontalalignment='right',
            transform=ax1.transAxes)
    plot_file(base_folder + \
                  'Stirring speed dependent crystallization-with PIL/'
                  '200 rpm/',
              ['size distribution 014.txt', 'size distribution 024.txt', 'size distribution 026.txt'],
              alpha=0.5,
              axis=ax2)
    ax2.text(.98, .75, '$\dot{\gamma} = 85 \enspace s^{-1}$',
            horizontalalignment='right',
            transform=ax2.transAxes)
    plot_file(base_folder + \
                  'Stirring speed dependent crystallization-with PIL/'
                  '400 rpm/',
              ['size distribution-004.txt', 'size distribution-008.txt'],
              alpha=0.5,
              axis=ax3)
    ax3.text(.98, .75, '$\dot{\gamma} = 167 \enspace s^{-1}$',
            horizontalalignment='right',
            transform=ax3.transAxes)
    f1.subplots_adjust(hspace=0)
    ax0.get_yaxis().set_ticks([])
    ax1.get_yaxis().set_ticks([])
    ax2.get_yaxis().set_ticks([])
    ax3.get_yaxis().set_ticks([])
    ax3.get_xaxis().set_ticks([0, 200, 400, 600, 800])
    plt.xlabel('Crystal size, $\mu$m')
    # plt.savefig('figures/RPM_graph.png', dpi=300)
    plt.show()

def plot_MW(add_LS=False):
    f1, (ax0, ax1, ax2, ax3) = plt.subplots(4, sharex=True, sharey=False, figsize=(2,5))

    # plot_file(base_folder + \
    #               'Crystallization without PIL or Monomer/',
    #           ['size distribution-002.txt'],#, 'size distribution-009.txt'],
    #           alpha=0.5,
    #           axis=ax0)
    # ax1.text(.98, .62, '(crystals in\nsolvent alone)',
    #         horizontalalignment='right',
    #         transform=ax0.transAxes)
    #
    # plot_file(base_folder + \
    #               'Crystallization with monomer/',
    #           ['size-distribution-004.txt', 'size-distribution-006.txt'],
    #           alpha=0.5,
    #           axis=ax1)
    # ax1.text(.98, .65, '414 g/mol\n(monomer)',
    #         horizontalalignment='right',
    #         transform=ax1.transAxes)

    plot_file(base_folder + \
                  'TA with and without monomer - 200 rpm/',
              ['trimesic-acid-in-pure-DMD-200rpm.txt'],#, 'size distribution-009.txt'],
              alpha=0.5,
              axis=ax0,
              add_LS=add_LS,
              fillcolor='grey')
    ax1.text(.98, .62, '(crystals in\nsolvent alone)',
            horizontalalignment='right',
            transform=ax0.transAxes)

    plot_file(base_folder + \
                  'TA with and without monomer - 200 rpm/',
              ['trimesic-acid-with-PILmonomer-200rpm.txt'],
              alpha=0.5,
              axis=ax1,
              add_LS=add_LS,
              fillcolor='#2ca02c')
    ax1.text(.98, .65, '414 g/mol\n(monomer)',
            horizontalalignment='right',
            transform=ax1.transAxes)


    plot_file(base_folder + \
                  'PIL molecular weight dependent crystallziation-200 rpm/'
                  '402k molecular weight/200 rpm/',
              ['size distribution 014.txt', 'size distribution 024.txt', 'size distribution 026.txt'],
              alpha=0.7,
              axis=ax2,
              add_LS=add_LS)
    ax2.text(.80, .65, '402 000\ng/mol',
            horizontalalignment='center',
            transform=ax2.transAxes, fontsize=10)

    plot_file(base_folder + \
                  'PIL molecular weight dependent crystallziation-200 rpm/'
                  '849k-molecular-weight/size-distributions/',
              ['size distribution-009.txt', 'size distribution-010.txt'],
              alpha=0.7,
              axis=ax3,
              add_LS=add_LS,
              fillcolor='#ff7f0e')
    ax3.text(.80, .65, '849 000\ng/mol',
            horizontalalignment='center',
            transform=ax3.transAxes)

    f1.subplots_adjust(hspace=0)
    ax0.get_yaxis().set_ticks([])
    ax1.get_yaxis().set_ticks([])
    ax2.get_yaxis().set_ticks([])
    ax3.get_yaxis().set_ticks([])
    ax3.get_xaxis().set_ticks([0, 200, 400, 600, 800])
    plt.xlabel('Crystal size, $\mu$m')
    if add_LS:
        plt.savefig('figures/MW_graph_withLS_1.png', dpi=300)
    else:
        plt.savefig('figures/MW_graph_update.png', dpi=300)
    plt.show()

def plot_MW_revision_compare(add_LS=False):
    f1, (ax0, ax1, ax2, ax3) = plt.subplots(4, sharex=True, sharey=False, figsize=(2,5))

    plot_file(base_folder + \
                  'Data for Figure 4b/',
              ['TA without PIL-200 rpm- 3h.txt'],#, 'size distribution-009.txt'],
              alpha=0.1,
              axis=ax2,
              add_LS=add_LS,
              fillcolor='white',
              edgecolor2='red')
    ax2.text(.98, .62, '(crystals in\nsolvent alone)',
            horizontalalignment='right',
            transform=ax2.transAxes)

    plot_file(base_folder + \
                  'Data for Figure 4b/',
              ['TA + Monomer-200 rpm-3h- Size distribution.txt'],
              alpha=0.1,
              axis=ax3,
              add_LS=add_LS,
              fillcolor='white',
              edgecolor2='red')
    ax3.text(.98, .65, '414 g/mol\n(monomer)',
            horizontalalignment='right',
            transform=ax3.transAxes)



    plot_file(base_folder + \
                  'TA with and without monomer - 200 rpm/',
              ['trimesic-acid-in-pure-DMD-200rpm.txt'],#, 'size distribution-009.txt'],
              alpha=0.1,
              axis=ax2,
              add_LS=add_LS,
              fillcolor='white')
    ax2.text(.98, .62, '(crystals in\nsolvent alone)',
            horizontalalignment='right',
            transform=ax2.transAxes)

    plot_file(base_folder + \
                  'TA with and without monomer - 200 rpm/',
              ['trimesic-acid-with-PILmonomer-200rpm.txt'],
              alpha=0.1,
              axis=ax3,
              add_LS=add_LS,
              fillcolor='white')
    ax3.text(.98, .65, '414 g/mol\n(monomer)',
            horizontalalignment='right',
            transform=ax3.transAxes)

    #old


    f1.subplots_adjust(hspace=0)
    ax0.get_yaxis().set_ticks([])
    ax1.get_yaxis().set_ticks([])
    ax2.get_yaxis().set_ticks([])
    ax3.get_yaxis().set_ticks([])
    ax3.get_xaxis().set_ticks([0, 200, 400, 600, 800])
    plt.xlabel('Crystal size, $\mu$m')
    if add_LS:
        plt.savefig('figures/MW_review_comparison_graph_withLS_1.png', dpi=300)
    else:
        plt.savefig('figures/MW_review_comparison_graph_1.png', dpi=300)
    plt.show()

def plot_PMMA():
    f1, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False, figsize=(2,4))

    # plot_file(base_folder + \
    #               'Crystallization with monomer/',
    #           ['size-distribution-004.txt', 'size-distribution-006.txt'],
    #           alpha=0.5,
    #           axis=ax1)
    # ax1.text(.98, .65, '414 g/mol\n(monomer)',
    #         horizontalalignment='right',
    #         transform=ax1.transAxes)

    # plot_file(base_folder + \
    #               'TA-with-PVDF-or-PMMA-at-400rpm/'
    #               'PMMA-120 k/',
    #           ['008-size distribution.txt'],
    #           alpha=0.5,
    #           axis=ax2)
    # ax2.text(.81, .65, '402\nkg/mol',
    #         horizontalalignment='center',
    #         transform=ax2.transAxes, fontsize=10)

    plot_file(base_folder + \
                  'TA-with-PVDF-or-PMMA-at-400rpm/'
                  'PMMA-996 k/',
              ['size distribution-002.txt'],
              alpha=0.5,
              axis=ax3)
    ax3.text(.7, .82, 'PMMA',
            horizontalalignment='left',
            transform=ax3.transAxes)

    f1.subplots_adjust(hspace=0)
    # ax0.get_yaxis().set_ticks([])
    ax1.get_yaxis().set_ticks([])
    ax2.get_yaxis().set_ticks([])
    ax3.get_yaxis().set_ticks([])
    ax3.get_xaxis().set_ticks([0, 200, 400, 600, 800])
    plt.xlabel('Crystal size, $\mu$m')
    plt.savefig('figures/PMMA_graph.png', dpi=300)
    plt.show()

def plot_PMMA_PVDF():
    f1, (ax0, ax1, ax2, ax3) = plt.subplots(4, sharex=True, sharey=False, figsize=(2,4))

    # plot_file(base_folder + \
    #               'Crystallization with monomer/',
    #           ['size-distribution-004.txt', 'size-distribution-006.txt'],
    #           alpha=0.5,
    #           axis=ax1)
    # ax1.text(.98, .65, '414 g/mol\n(monomer)',
    #         horizontalalignment='right',
    #         transform=ax1.transAxes)

    plot_file(base_folder + \
                  'TA-with-PVDF-or-PMMA-at-400rpm/'
                  'PMMA-996 k/',
              ['size distribution-002.txt'],
              alpha=0.5,
              axis=ax2)
    ax2.text(.68, .75, 'PMMA',
            horizontalalignment='left',
            transform=ax2.transAxes)

    # plot_file(base_folder + \
    #               'TA-with-PVDF-or-PMMA-at-400rpm/'
    #               'PVDF-/',
    #           ['005-size distribution.txt'],
    #           alpha=0.5,
    #           axis=ax3)
    # ax3.text(.68, .75, 'PVDF',
    #         horizontalalignment='left',
    #         transform=ax3.transAxes)

    plot_file(base_folder + \
                  'TA-with-different-polymers-under-shear-400rpm/',
              ['TA-75 mg PVDF-0.75 ml DMF-200 rpm-3h.txt'],
              alpha=0.5,
              axis=ax3)
    ax3.text(.68, .75, 'PVDF',
            horizontalalignment='left',
            transform=ax3.transAxes)

    f1.subplots_adjust(hspace=0)
    # ax0.get_yaxis().set_ticks([])
    ax1.get_yaxis().set_ticks([])
    ax2.get_yaxis().set_ticks([])
    ax3.get_yaxis().set_ticks([])
    ax3.get_xaxis().set_ticks([0, 200, 400, 600, 800])
    plt.xlabel('Crystal size, $\mu$m')
    plt.savefig('figures/PVDF_graph.png', dpi=300)
    plt.show()

def plot_CS():
    f1, (ax0, ax1, ax2) = plt.subplots(3, sharex=True, sharey=False, figsize=(6,4))
    # plot_file(base_folder + \
    #               'Crystallization with monomer/',
    #           ['size-distribution-004.txt', 'size-distribution-006.txt'],
    #           alpha=0.5,
    #           axis=ax1)
    # ax1.text(.98, .65, '414 g/mol\n(monomer)',
    #         horizontalalignment='right',
    #         transform=ax1.transAxes)
    thebins = np.linspace(0, 10000, 10)
    plot_file(base_folder + \
                  'Stirring in small cell for one week/'
                  '200 rpm for one week/',
              ['30 size distribution.txt', '34-size distribution.txt'],
              alpha=0.5,
              axis=ax0,
              thebins=np.linspace(0,1,10),
              no_vertlines=True,
              um_to_mm=True)
    ax0.text(.90, .60, '1 mm gap,\n200 RPM',
            horizontalalignment='center',
            transform=ax0.transAxes, fontsize=10)
    plot_file(base_folder + \
                  'Stirring in small cell for one week/'
                  '460 rpm for one week/',
              ['34-size distribution.txt', '37-size distribution.txt'],
              alpha=0.5,
              axis=ax1,
              thebins=np.linspace(0,1,10),
              no_vertlines=True,
              um_to_mm=True)
    ax1.text(.90, .60, '1 mm gap,\n460 RPM',
            horizontalalignment='center',
            transform=ax1.transAxes, fontsize=10)

    plot_file(base_folder + \
                  '',
              ['size distribution in large couette cell.txt'],
              alpha=0.5,
              axis=ax2,
              thebins=np.linspace(0, 10, 20))
    ax2.text(.89, .60, '8.7 mm gap,\n1200 RPM',
            horizontalalignment='center',
            transform=ax2.transAxes)

    f1.subplots_adjust(hspace=0)
    ax0.get_yaxis().set_ticks([])
    ax1.get_yaxis().set_ticks([])
    ax2.get_yaxis().set_ticks([])
    ax2.get_xaxis().set_ticks([0, 2, 4, 6, 8, 10])
    plt.xlabel('Crystal size, mm')
    plt.savefig('figures/CS_graph.png', dpi=300)
    plt.show()

def plot_simulation_shear():
    f1, ax1 = plt.subplots(1, sharex=True, sharey=False, figsize=(3.5*0.9, 3*0.9))

    data = np.array([[0.005, 340], [0.02, 643], [0.05, 1100], [0.1, 1585]])
    ax1.plot(data[:,0]*2, data[:,1], color = 'blue', label='Freely rotating, $r_c$ = 0.2 $\mu$m')

    data = np.loadtxt('data/simulation/rad_200nm.txt', skiprows=1)
    line1 = ax1.plot(data[:,0]*2*1000, data[:,2], dashes=[4,4], color='blue', label='Fixed, $r_c$ = 0.2 $\mu$m')

    data = np.array([[0.25, 1460], [0.2, 1000], [0.17, 816], [0.15, 710], [0.1, 525], [0.05, 346.8], [0.01, 165]])
    ax1.plot(data[:,0]*2, data[:,1], color = 'black', label='Freely rotating, $r_c$ = 2.0 $\mu$m')

    data = np.loadtxt('data/simulation/rad_2um.txt', skiprows=1)
    ax1.plot(data[:,0]*2*1000, data[:,2], dashes=[4,4], color = 'black', label='Fixed, $r_c$ = 2.0 $\mu$m')

    data = np.array([[0, 41.868], [0.88, 41.868]])
    line1 = ax1.plot(data[:,0], data[:,1], dashes=[1,1], color='green', label='Mean shear (bulk)')
    plt.xlim([0,0.5])
    plt.ylim([0, 1600])
    # ax1.get_xaxis().set_ticks([0, 0.1, .2, .3, .4, .5])
    # ax1.get_yaxis().set_ticks([0, 200, 400, 600, 800, ])
    plt.ylabel('Local shear rate max., 1/s')
    plt.xlabel('Crystal size (edge length), mm')
    # plt.legend(loc=(0.55, 0.4))
    plt.tight_layout()
    plt.savefig('figures/theor_graph.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    # plot_PMMA_PVDF()
    plot_PMMA()
    # plot_MW()
    # plot_RPMs()
    # plot_CS()
    # plot_simulation_shear()