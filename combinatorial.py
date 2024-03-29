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
    Xs is samples in markov partition
    S is symbol selecting func
    F is func (for all partitions) 
    Fi is ARRAY of relevant inverse functions
    Fd is derivative func (for all partitions)
"""

def Hdim(ref_level , Xs, S, F, Fi, Fd, debug = False):
    
    Xs = [(x, "") for x in Xs]

    #refine and save most recent iterate
    OldXs = []
    for i in range(ref_level):
        temp = []
        for x in Xs:
            for i in range(len(Fi)):
                f = Fi[i]
                xnew = f(x[0])
                temp.append((xnew, S(xnew) + x[1]))
        OldXs = Xs[:]
        if debug:
            print(OldXs)
        Xs = temp[:]
    

    T = np.zeros((len(OldXs), len(OldXs)))
    for x in Xs:
        y, symb = x
        i = int(symb[1:], 2)
        j = int(symb[:-1], 2)
        T[i, j] = 1/np.abs(Fd(y))
        
    f = lambda a : np.max(np.abs(np.linalg.eigvals(T**a))) - 1

    print("Solving for ref_level = ", ref_level)
    for x in np.linspace(0,2, 300):
        print("f at ", x, " is ", f(x))

    mu = brentq(f, 0, 2)

    return mu       