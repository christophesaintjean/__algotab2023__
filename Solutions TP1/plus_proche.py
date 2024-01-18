# TD1 Exo 3
# TP1 Exo 2

from time import perf_counter_ns
from random import randint
import matplotlib.pyplot as plt
from tqdm import tqdm

def tableau(n, a=0, b=100):
    T = []
    for _ in range(n):
        T.append(randint(a, b))
    return T

def diss(a, b):
    return abs(a-b)

def plus_proche(T, req, d=diss):
    i_min = 0
    d_min = d(req, T[i_min])
    if d_min == 0:
        return i_min
    for i in range(1, len(T)):
        d_i = d(req, T[i])
        if d_i == 0:
            return i
        if d_i < d_min:
            d_min = d_i
            i_min = i
    return i_min

def tps_plus_proche(n):
    T = tableau(n)
    req = randint(0, n)
    debut = perf_counter_ns()
    _ = plus_proche(T, req, diss)
    fin = perf_counter_ns()
    duree = fin - debut
    return duree


if __name__ == "__main__":
    #print(diss(3, 3), diss(3, 4), diss(3, 2))
    T  = [3, 5, 0, 3, -1, 2]
    req = -2
    print(plus_proche(T, req, diss))
    
    n = 10**1  # petit
    T = tableau(n)
    req = randint(0, 100)
    debut = perf_counter_ns()
    _ = plus_proche(T, req, diss)
    fin = perf_counter_ns()
    duree = fin - debut
    print("Duree (petit): ", duree)
    
    n = 10**3 # moyen
    T = tableau(n)
    req = randint(0, 10**3)
    debut = perf_counter_ns()
    _ = plus_proche(T, req, diss)
    fin = perf_counter_ns()
    duree = fin - debut
    print("Duree (moyen): ", duree)
        
    
    n = 10**6 # grand
    T = tableau(n)
    req = randint(0, 10**5)
    debut = perf_counter_ns()
    _ = plus_proche(T, req, diss)
    fin = perf_counter_ns()
    duree = fin - debut
    print("Duree (grand): ", duree)
    
    print(f"Duree (grand): {tps_plus_proche(n)}")
    
    N = []
    Tps = []
    for n in tqdm(range(10, 10**5, 200)):
        N.append(n)
        # calcul
        Tps.append(tps_plus_proche(n))
        
    #affichage de la courbe N vs Tps
    plt.figure()
    plt.plot(N, Tps)
    plt.show()
    
        
    
    
    

    
    
    

