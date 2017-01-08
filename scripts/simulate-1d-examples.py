#!/usr/bin/env python

import numpy as np
import numpy.random as rand


def savetxt_noisy(filename, arr):
    np.savetxt(filename, arr)
    print 'wrote', filename

def gaussian_random_walk(n):
    steps = rand.standard_normal(size=n)
    steps -= np.mean(steps)
    return np.cumsum(steps)

def noisy_sine_wave(n, p):
    assert n % p == 0
    return np.sin(2*np.pi/p * np.arange(n)) + rand.standard_normal(size=n)

def noisy_square_wave(n, p):
    assert n % p == 0
    assert p % 2 == 0

    a = np.ones((n//p, 2, p//2))
    a[:,1,:] = -1
    a = np.reshape(a, (-1,))

    return a + rand.standard_normal(size=n)

def noisy_von_mises(n, p, d):
    # von Mises concentration parameter
    kappa = np.log(2) / (2 * np.sin(np.pi*d/2.)**2)

    # pulse phase (pulses occur at multiples of 2pi)
    phi = (2*np.pi/p) * np.arange(n)

    # this is the von Mises time series
    s = np.exp(-2*kappa * np.sin(phi/2.)**2)
    
    # normalize to <s>=1
    s /= np.mean(s)

    return s + rand.standard_normal(size=n)


N = 2**20    # total timestream length
P = 64       # period used for sine waves etc.

savetxt_noisy('gaussian_white_noise.txt', rand.standard_normal(size=N))
savetxt_noisy('gaussian_random_walk.txt', gaussian_random_walk(N))
savetxt_noisy('noisy_sine_wave.txt', noisy_sine_wave(N,P))
savetxt_noisy('noisy_square_wave.txt', noisy_square_wave(N,P))

savetxt_noisy('noisy_von_mises_0.1.txt', noisy_von_mises(N,P,0.1))
savetxt_noisy('noisy_von_mises_0.066.txt', noisy_von_mises(N,P,0.066))
savetxt_noisy('noisy_von_mises_0.033.txt', noisy_von_mises(N,P,0.033))
