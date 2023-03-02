import numpy as np
from scipy.optimize import brentq

"""
    Doesn't Work


    combi is an array of tuples specifying markov partitiion combinatorics (i->j in paper)
    Xs is samples in markov partition
    F is array of Fs for markov partition 
    Fi is array of F inverses
    Fd is array of F derivatives
"""
def Hdim(k ,combi, Xs, F, Fi, Fd):
    
    
    for refine in range(k):
        newXs = []
        for link in combi:
            i, j = link
            newXs.append(Fi[i](Xs[j]))
        Xs = newXs
        F = [F[0]]*len(Xs)
        Fi = [Fi[0]]*len(Xs) #Does not work in arbitrary case
        Fd = [Fd[0]]*len(Xs) #Does not work in arbitrary case
        
        
    print(Xs)
    #Transition matrix
    T = np.zeros((len(Xs), len(Xs)))
    for link in combi:
        i, j = link
        #assumes f inverse returns in ith partition
        T[i , j] = 1/np.abs(Fd[i](Fi[i](Xs[j])))
    
    #f for brentq
    f = lambda a : np.max(np.abs(np.linalg.eigvals(T**a))) - 1
    mu = brentq(f, 0, 2)
    
    
    return mu



combi = [(0,1), (1,0)]
Xs = [1j, -1j]
F = [lambda x : x**2, lambda x : x**2]
Fi = [np.sqrt, np.sqrt]
Fd = [lambda x : 2*x, lambda x : 2*x]

for k in range(10):
    print(Hdim(k, combi, Xs, F, Fi, Fd))



"""
print(f(0))

Xs = np.linspace(0,2, 1000)
Ys = [f(x) for x in Xs]
plt.plot(Xs,Ys)
"""