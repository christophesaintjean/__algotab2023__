from plus_proche import plus_proche
from supp_tp1 import levenshteinDistance as lev_diss
from tqdm import tqdm

def my_map_tqdm(fun, L):
    """ vue en S1 """
    R = []
    for Li in tqdm(L):
        R.append(fun(Li))
    return R

if __name__ == "__main__":
    L = ["le", "petito", "chat"]
    dico = []
    with open('dico.txt', 'r') as f:
        for ligne in f:
            dico.append(ligne.rstrip('\n'))
    plus_proche_l1 = dico[plus_proche(dico, L[1], lev_diss)]
    print(f"{L[1]} -> {plus_proche_l1}")

    def mot_plus_proche(mot):
        return dico[plus_proche(dico, mot, lev_diss)]
    
    print(my_map_tqdm(mot_plus_proche, L))
    
    phrase = "Le petito chat se promeni jur le muré"
    print(' '.join(my_map_tqdm(mot_plus_proche, phrase.split(" "))))
    
    """
    Problemes/discutions:
    * difference maj/minuscules: lev_diss("le", "he") = lev_diss("Le", "he")
    * ordre importe peu
    * on pourrait trier les mots par fréquence d'utilisation dans la langue
    
    """
    
        