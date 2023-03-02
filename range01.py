from combinatorial import Hdim
import numpy as np


#symbol function
S = lambda x : '1' if x.imag >= 0 else '0' 


for c in np.linspace(0,1,100):
    print("                ------            ")
    print("C = " + str(c))

    Xs = [-1 + 0j]
    F = lambda x : x**2 + c
    Fi = [lambda x : np.sqrt(x - c), lambda x : -1*np.sqrt(x-c)]
    Fd = lambda x : 2*x

    for k in range(10,11):
        print(Hdim(k, Xs, S, F, Fi, Fd)) 