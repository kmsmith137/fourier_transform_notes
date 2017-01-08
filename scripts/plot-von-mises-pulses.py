#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# index range used in plots (global)
(I,J) = (32, 224)


def plot_file(filename, label):
    a = np.loadtxt(filename)
    print 'read', filename

    plt.plot(np.arange(I,J), a[I:J], label=label)


plt.figure(figsize=(6,3))
plot_file('noisy_von_mises_0.033.txt', r'$D=0.033$')
plot_file('noisy_von_mises_0.066.txt', r'$D=0.066$')
plot_file('noisy_von_mises_0.1.txt', r'$D=0.1$')

plt.xlim(I,J)

# remove axes
ax = plt.gca().axes
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

out_filename = 'von_mises_pulses.png'
plt.savefig(out_filename)
print 'wrote', out_filename
