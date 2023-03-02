from .combinatorial import Hdim

for c in np.linspace(0,1,100):
    print("                ------            ")
    print("C = " + str(c))

    Xs = [-1 + 0j]
    F = lambda x : x**2 + c
    Fi = [lambda x : np.sqrt(x - c), lambda x : -1*np.sqrt(x-c)]
    Fd = lambda x : 2*x

    for k in range(10,11):
        print(Hdim(k, Xs, S, F, Fi, Fd)) 