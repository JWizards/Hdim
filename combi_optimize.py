import numpy as np
from scipy.optimize import brentq
from scipy.sparse import coo_matrix
from scipy.sparse import csr_array

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
    
    pos_i = []
    pos_j = []
    pos_vals = []
    for x in Xs:
        y, symb = x
        i = int(symb[1:], 2)
        j = int(symb[:-1], 2)
        T = 1/np.abs(Fd(y))
        pos_i.append(i)
        pos_j.append(j)
        pos_vals.append(T)


    vec_size = len(OldXs)
    T = csr_array(coo_matrix((pos_vals, (pos_i, pos_j)), shape=(vec_size, vec_size)))

    #T assumed to be csr_array
    #vec_size is size of vector
    def dom_eig(T, vec_size, e = 0.001):
        #euclidean norm
        def norm(v):
            return np.sqrt(np.sum(v**2))
        def norm_2(v):
            return np,sum(v)

        v = (np.ones(vec_size))
        v = v/norm(v)
        
        eig = 0
        ratios = []
        while ratios.len() >= 2 and np.abs(np.min(ratios) - np.max(ratios)) > e:
            A = 3

        return eig


    f = lambda a : np.abs(dom_eig(T.power(a), vec_size)) - 1

    for x in np.linspace(0,2, 300):
        print("f at ", x, " is ", f(x))

    mu = brentq(f, 0, 2)

    return mu 
      



# #T assumed to be csr_array
# #vec_size is size of vector
# def dom_eig(T, vec_size, e = 0.001):
#     #euclidean norm
#     def norm(v):
#         return np.sqrt(np.sum(v**2))

#     v = (np.ones(vec_size))
#     v = v/norm(v)

#     eig = 0
#     old_eig = 100000 #infinity
#     while( np.abs(eig - old_eig) > e):
#         v = T@v

#         old_eig = eig
#         eig = norm(v)

#         v = v/norm(v)

#     return eig