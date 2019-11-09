import numpy as np
import matplotlib.pyplot as plt

def couette_shear(R1, R2, omega, r):
    a = -1*omega*R1**2/(R2**2 - R1**2)
    b = omega*R1**2*R2**2/(R2**2 - R1**2)
    return -2*b/r**2

def couette_shear_noderiv(R1, R2, omega, r):
    a = (-1*omega*R1**2)/(R2**2 - R1**2)
    b = (omega*R1**2*R2**2)/(R2**2 - R1**2)
    return a*r + b/r

print(couette_shear_noderiv(4e-3, 5e-3, 400*2*np.pi/(60), 4e-3))
f1 = plt.figure(1, figsize=(6,4))

R1 = 4e-3
R2 = 5e-3
rpm = 200
rs = np.linspace(R1, R2, 50)
ys = [couette_shear(R1, R2, rpm*2*np.pi/(60), r)for r in rs]
plt.plot((rs-R1)*1000, np.abs(np.array(ys)), label='small cell, 200 RPM')
volavg = np.mean(np.abs(np.array(ys)) * 2 * np.pi * rs) / np.mean(2 * np.pi * rs)
print('rpm = {0}, avg shear={1}, volume average shear={2}, variation={3}-{4}'.format(rpm, np.mean(np.abs(np.array(ys))),
                                                                    volavg,
                                                                                     (volavg - np.min(np.abs(np.array(ys))))/volavg,
                                                                                     (-1*volavg + np.max(
                                                                                         np.abs(np.array(ys)))) / volavg))
R1 = 4e-3
R2 = 5e-3
rpm = 460
rs = np.linspace(R1, R2, 50)
ys = [couette_shear(R1, R2, rpm*2*np.pi/(60), r) for r in rs]
plt.plot((rs-R1)*1000, np.abs(np.array(ys)), label='small cell, 460 RPM')
volavg = np.mean(np.abs(np.array(ys)) * 2 * np.pi * rs) / np.mean(2 * np.pi * rs)
print('rpm = {0}, avg shear={1}, volume average shear={2}, variation={3}-{4}'.format(rpm, np.mean(np.abs(np.array(ys))),
                                                                    volavg,
                                                                                     (volavg - np.min(np.abs(np.array(ys))))/volavg,
                                                                                     (-1*volavg + np.max(
                                                                                         np.abs(np.array(ys)))) / volavg))

R1 = 4e-3
R2 = (25.5e-3)/2
rs = np.linspace(R1, R2, 50)
rpm = 1200
ys = [couette_shear(R1, R2, rpm*2*np.pi/(60), r)for r in rs]
plt.plot((rs-R1)*1000, np.abs(np.array(ys)), label='large cell, 1200 RPM', alpha=0.5)
volavg = np.mean(np.abs(np.array(ys)) * 2 * np.pi * rs) / np.mean(2 * np.pi * rs)
print('rpm = {0}, avg shear={1}, volume average shear={2}, variation={3}-{4}'.format(rpm, np.mean(np.abs(np.array(ys))),
                                                                    volavg,
                                                                                     (volavg - np.min(np.abs(np.array(ys))))/volavg,
                                                                                     (-1*volavg + np.max(
                                                                                         np.abs(np.array(ys)))) / volavg))
# plt.ylim(0, 160)
plt.legend()
plt.xlabel('Radial distance from the inner (moving) wall, mm')
plt.ylabel('Shear rate, s$^{-1}$')
plt.savefig('couette_uniformity.png', dpi=300)
plt.show()

