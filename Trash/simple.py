import numpy as np
from scipy.optimize import brentq

#code specifically for Fc = z^2 + c with c = 0 julia set

n = 1

T = (1/2)*np.zeros((2**n, 2**n))
for i in range(2**n):
    T[i, i] = 1/2
    T[i, (i+1)%2**n] = 1/2
    
    
f = lambda a : np.max(np.abs(np.linalg.eigvals(T**a))) - 1
mu = brentq(f, 0, 2)
print(mu)