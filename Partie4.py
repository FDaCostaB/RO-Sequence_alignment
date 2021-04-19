import sys
import Partie3 as p3
from random import randint
import matplotlib.pyplot as plt


def creerGene():
    X = []
    for i in range(100):
        X.append(randint(0, 3) + 1)
    return X


def deletion(X):
    del X[randint(0, len(X) - 1)]
    return X


def insertion(X):
    X.insert(randint(0, len(X)), randint(0, 3) + 1)
    return X


def substitution(X):
    i = randint(0, len(X) - 1)
    n = X.pop(i)
    possible = [p3.A, p3.C, p3.G, p3.T]
    possible.remove(n)
    X.insert(i, possible[randint(0, 2)])
    return X


def mute(X):
    nb = randint(0, 100)
    for i in range(nb):
        mutation = randint(0, 2)
        if mutation == 0:
            deletion(X)
        elif mutation == 1:
            insertion(X)
        elif mutation == 2:
            substitution(X)
    return nb


# MAIN
if len(sys.argv) != 3:
    print("Usage :", sys.argv[0], " DeltaFile <Taille échantillon>")
else:

    # Initialisation
    delta = p3.getDelta(sys.argv[1])
    tailleE = int(sys.argv[2])

    # Affichage des valeurs d'entrées
    print("Delta := ")
    for lignes in delta:
        print(lignes)

    effectue = []
    for i in range(101):
        effectue.append([])

    for i in range(tailleE):
        if (i % 100 == 0):
            print(i)
        X = creerGene()
        Y = X.copy()
        n = mute(Y)
        res, chemin = p3.calculSolution(delta, X, Y)
        n0 = res[len(Y)][len(X)]
        effectue[n].append(int(n0))

    print(effectue)
    moyenne = [0] * 101
    for i in range(101):
        if(len(effectue[i])!=0):
            moyenne[i] = sum(effectue[i]) / len(effectue[i])

    print(moyenne)

    plt.title('Nombres de bases différentes en fonctions du nombre de mutations effectués')
    plt.xlabel('Nombres de mutations effectués')
    plt.ylabel('Nombres de bases différentes')

    plt.plot(moyenne)
    plt.show()
    plt.close()
