from combinatorial import Hdim
import numpy as np
import time

#symbol function
S = lambda x : '1' if x.imag >= 0 else '0' 

Xs = [-1 + 0j]
F = lambda x : x**2
Fi = [np.sqrt, lambda x : -1*np.sqrt(x)]
Fd = lambda x : 2*x

for k in range(2, 6):
    print(Hdim(k, Xs, S, F, Fi, Fd))



print(" --------- ")  #c = -1
#expected output is 1.28635
c = -1

Xs = [0+1j, 0-1j]
F = lambda x : x**2 + c
Fi = [lambda x : np.sqrt(x - c), lambda x : -1*np.sqrt(x - c)]
Fd = lambda x : 2*x
st = time.time()
for k in range(9, 14):
    print(Hdim(k, Xs, S, F, Fi, Fd))
et = time.time()

print("time taken = ", et - st)