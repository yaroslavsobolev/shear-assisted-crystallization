import numpy as np
import matplotlib.pyplot as plt

def plot_simulation_shear():
    f1, ax1 = plt.subplots(1, sharex=True, sharey=False, figsize=(3.5*0.9, 3*0.9))

    fuckup_correction_coeff = 1/42*167/1000

    data = np.array([[0.005, 340], [0.02, 643], [0.05, 1100], [0.1, 1585]])
    ax1.plot(data[:,0]*2, data[:,1]*fuckup_correction_coeff, color = 'blue', label='Freely rotating, $r_c$ = 0.2 $\mu$m')

    data = np.loadtxt('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/simulation/rad_200nm.txt', skiprows=1)
    line1 = ax1.plot(data[:,0]*2*1000, data[:,2]*fuckup_correction_coeff, dashes=[4,4], color='blue', label='Fixed, $r_c$ = 0.2 $\mu$m')

    data = np.array([[0.25, 1460], [0.2, 1000], [0.17, 816], [0.15, 710], [0.1, 525], [0.05, 346.8], [0.01, 165]])
    ax1.plot(data[:,0]*2, data[:,1]*fuckup_correction_coeff, color = 'black', label='Freely rotating, $r_c$ = 2.0 $\mu$m')

    data = np.loadtxt('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/simulation/rad_2um.txt', skiprows=1)
    ax1.plot(data[:,0]*2*1000, data[:,2]*fuckup_correction_coeff, dashes=[4,4], color = 'black', label='Fixed, $r_c$ = 2.0 $\mu$m')

    data = np.array([[0, 41.868], [0.88, 41.868]])
    line1 = ax1.plot(data[:,0], data[:,1]*fuckup_correction_coeff, dashes=[1,1], color='green', label='Mean shear (bulk)')
    plt.xlim([0,0.5])
    plt.ylim([0, 6])
    # ax1.get_xaxis().set_ticks([0, 0.1, .2, .3, .4, .5])
    # ax1.get_yaxis().set_ticks([0, 200, 400, 600, 800, ])
    plt.ylabel('Local shear rate max., $10^3 $s$^{-1}$')
    plt.xlabel('Crystal size (edge length), mm')
    # plt.legend(loc=(0.55, 0.4))
    plt.tight_layout()
    plt.savefig('theor_graph_1.png', dpi=300)
    plt.show()

def plot_simulation_shear_dimensionless():
    f1, ax1 = plt.subplots(1, sharex=True, sharey=False, figsize=(3.5*0.9, 3*0.9))

    data = np.array([[0.005, 340], [0.02, 643], [0.05, 1100], [0.1, 1585]])
    ax1.plot(data[:,0]*2/1000/0.2, data[:,1], color = 'blue', label='Freely rotating, $r_c$ = 0.2 $\mu$m')

    data = np.loadtxt('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/simulation/rad_200nm.txt', skiprows=1)
    line1 = ax1.plot(data[:,0]*2/0.2, data[:,2], dashes=[4,4], color='blue', label='Fixed, $r_c$ = 0.2 $\mu$m')

    data = np.array([[0.25, 1460], [0.2, 1000], [0.17, 816], [0.15, 710], [0.1, 525], [0.05, 346.8], [0.01, 165]])
    ax1.plot(data[:,0]*2/1000/2, data[:,1], color = 'black', label='Freely rotating, $r_c$ = 2.0 $\mu$m')

    data = np.loadtxt('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/simulation/rad_2um.txt', skiprows=1)
    ax1.plot(data[:,0]*2/2, data[:,2], dashes=[4,4], color = 'black', label='Fixed, $r_c$ = 2.0 $\mu$m')

    data = np.array([[0, 41.868], [0.88, 41.868]])
    # line1 = ax1.plot(data[:,0], data[:,1], dashes=[1,1], color='green', label='Mean shear (bulk)')
    # plt.xlim([0,0.5])
    plt.ylim([0, 1600])
    # ax1.get_xaxis().set_ticks([0, 0.1, .2, .3, .4, .5])
    # ax1.get_yaxis().set_ticks([0, 200, 400, 600, 800, ])
    plt.ylabel('Local shear rate max., $10^3 s^{-1}$')
    plt.xlabel('$L/r_{c}$')
    # plt.legend(loc=(0.55, 0.4))
    plt.tight_layout()
    plt.savefig('theor_graph_2.png', dpi=300)
    plt.show()

def plot_relaxation():
    major_fuckup_correction = 1/42*167
    f1, ax1 = plt.subplots(1, sharex=True, sharey=False, figsize=(6, 4))
    data = np.loadtxt('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/simulation/max_speed_vs_time.txt', skiprows=49)
    ax1.plot((data[:,0]-data[0,0])*1000, data[:,1]/(0.1E-3*np.sqrt(2))*major_fuckup_correction, color = 'black', label='Simulation')
    plt.axhline(y=42/2*major_fuckup_correction, linestyle='--', label='$\dot{\gamma}_0/2$')
    print('V={0} mm/s'.format(41*0.1*np.sqrt(2)))
    plt.xlabel('t, ms')
    plt.ylabel('Angular velocity, rad/s')
    plt.ylim(0, 80*major_fuckup_correction)
    plt.tight_layout()
    plt.legend()
    plt.savefig('theor_relaxation.png')
    plt.show()


f1, ax1 = plt.subplots(1, sharex=True, sharey=False, figsize=(8.9, 2.6))
data = np.loadtxt('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/simulation/max_shear_vs_time_propergammazero.txt', skiprows=233)
ax1.plot((data[:,0]-data[0,0])*1000, data[:,1], label='Newtonian', alpha=0.7)
# plt.axhline(y=42/2, linestyle='--', label='$\dot{\gamma}_0/2$')
print('V={0} mm/s'.format(41*0.1*np.sqrt(2)))
plt.xlabel('t, ms')
plt.ylabel('Highest shear rate, 1/s')
# plt.yticks([0, 100, 200, 300, 400, 500, 600])
plt.ylim(-0.1, 2800)
plt.tight_layout()
# plt.legend()
# plt.savefig('theor_shear_rate_1.png')
# plt.show()



data2 = np.loadtxt('D:/Docs/Science/UNIST/Projects/shear_crystal_growth/simulation/max_shear_vs_time_nonnewtonian_1.txt', skiprows=1)

dydx = np.gradient(data2[:,1], data2[:,0])
# f2 = plt.figure(2)
# plt.plot((data[:,0]-data[0,0])*1000, dydx)
# f1, ax1 = plt.subplots(1, sharex=True, sharey=False, figsize=(8.9, 2.6))
# ax1.plot((data[:,0]-data[0,0])*1000, data[:,1], color = 'black', label='Simulation2')
thresh = 5e5
todel = np.abs(dydx)<thresh
y2 = data2[todel,1]
x1 = (data2[:,0]-data2[0,0])*1000
x2 = x1[todel]
ax1.plot(x2[x2>10]+0.1, y2[x2>10], label='Non-newtonian', alpha=0.7)
# plt.axhline(y=42/2, linestyle='--', label='$\dot{\gamma}_0/2$')
print('V={0} mm/s'.format(41*0.1*np.sqrt(2)))
plt.xlabel('t, ms')
plt.ylabel('Highest shear rate, 1/s')
# plt.yticks([0, 100, 200, 300, 400, 500, 600])
plt.ylim(-0.1, 2800)
plt.xlim(0, 45)
plt.tight_layout()
plt.legend()
plt.savefig('theor_shear_rate_nn1.png', dpi=300)
plt.show()