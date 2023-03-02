from .combinatorial import Hdim
import numpy as np


#symbol function
S = lambda x : '1' if x.imag >= 0 else '0' 

Xs = [-1 + 0j]
F = lambda x : x**2
Fi = [np.sqrt, lambda x : -1*np.sqrt(x)]
Fd = lambda x : 2*x

for k in range(2, 6):
    print(Hdim(k, Xs, S, F, Fi, Fd))
