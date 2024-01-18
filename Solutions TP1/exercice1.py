import matplotlib.pyplot as plt
from tqdm import tqdm
#from tqdm.gui import tqdm     #On peut auddi lancer une fenetre mais il y a rien à voir ici 

L = [3, 4.5, -2, 1, -4, 3, 6, 3, -2, 8]

for i in tqdm(L):
    pass

plt.plot(L)
plt.show()
