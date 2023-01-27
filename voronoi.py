import numpy as np
from scipy.optimize import brentq



"""
Key assumptions:
    
    all supplied inverses in Fi produce original samples of refinement.
    samples are used as representatives of markov partitions
    voronoi style nearest representative is used to determine the partition a sample is in
    i.e:
        As per the paper we need an entry in our transition matrix wherever i->j holds
        I calculate refinements by applying all inverse functions to a sample to generate new list of samples.
        then I locate i and j as the indice of the nearest sample in the previous iteration,
        both w.r.t the sample and f(sample) (as new sample is supposed to be an inverse)
"""


"""
    ref_level is refinement level (number of iterations)
    combi is an array of tuples specifying markov partitiion combinatorics (i->j in paper)
    Xs is samples in markov partition
    F is func (for all partitions) 
    Fi is ARRAY of relevant inverse functions
    Fd is derivative func (for all partitions)
"""
def Hdim(ref_level , Xs, F, Fi, Fd):
    
    #refine and save most recent iterate
    OldXs = []    
    for i in range(ref_level):
        temp = []
        for x in Xs:
            for f in Fi:
                temp.append(f(x))
        OldXs = Xs[:]
        Xs = temp[:]
    
    #a is element
    #list of representatives to find closest from
    #voronoi style!
    def repIndice(a, reps):
        return np.argmin(np.abs(np.array(reps)-a))
    
    T = np.zeros((len(OldXs), len(OldXs)))
    for x in Xs:
        i = repIndice(x, OldXs)
        j = repIndice(F(x), OldXs)
        T[i, j] = 1/np.abs(Fd(x))
        
    f = lambda a : np.max(np.abs(np.linalg.eigvals(T**a))) - 1
    mu = brentq(f, 0, 2)
    
    return mu


Xs = [1j, -1j]
F = lambda x : x**2
Fi = [np.sqrt, lambda x : -1*np.sqrt(x)]
Fd = lambda x : 2*x

for k in range(1, 4):
    print(Hdim(k, Xs, F, Fi, Fd))

#okay now with c = -1

Xs = [1j, -1j]
F = lambda x : x**2
Fi = [np.sqrt, lambda x : -1*np.sqrt(x)]
Fd = lambda x : 2*x

for k in range(1, 4):
    print(Hdim(k, Xs, F, Fi, Fd))

    
        