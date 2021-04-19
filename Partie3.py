import sys

BLANC = 0
A = 1
C = 2
G = 3
T = 4

def getLetter(num):
    if(num==A):
        return 'A'
    if (num == C):
        return 'C'
    if (num == G):
        return 'G'
    if (num == T):
        return 'T'
    if (num == BLANC):
        return '-'
    else:
        exit(0)

def getNum(letter):
    if(letter=='A'):
        return A
    elif (letter == 'C'):
        return C
    elif (letter == 'G'):
        return G
    elif (letter == 'T'):
        return T
    elif (letter == '-'):
        return BLANC
    else:
        exit(0)

def getDelta(name):
    deltaFile = open(name, "r")
    delta = []
    for ligne in deltaFile:
        delta.append(ligne.split())

    for i in range(4):
        for j in range(i+1,5):
            delta[i].append(delta[j][i])

    for i in range(5):
        for j in range(5):
            delta[i][j]= float(delta[i][j])
    deltaFile.close();
    return delta;

def calculSolution(delta,X,Y):
    res = []
    chemin = []
    for i in range(len(Y) + 1):
        res.append([0] * (len(X) + 1))
        chemin.append([(0, 0)] * (len(X) + 1))
    for i in range(len(X)+1):
        for j in range(len(Y)+1):
            if j==0 and i== 0:
                res[j][i] = 0
            if i==0 and j != 0:
                res[j][0]=res[j-1][0] + delta[BLANC][Y[j-1]]
            if j == 0 and i !=0:
                res[0][i]= res[0][i-1] + delta[X[i-1]][BLANC]
            if j!=0 and i!=0:
                minV = min(res[j - 1][i] + delta[BLANC][Y[j - 1]], res[j][i - 1] + delta[X[i - 1]][BLANC],res[j - 1][i - 1] + delta[X[i - 1]][Y[j - 1]])
                if minV == res[j - 1][i] + delta[BLANC][Y[j - 1]]:
                    chemin[j][i] = (i,j-1)
                if minV == res[j][i-1] + delta[X[i - 1]][BLANC]:
                    chemin[j][i] = (i-1,j)
                if minV == res[j - 1][i-1] + delta[X[i - 1]][Y[j - 1]]:
                    chemin[j][i] = (i-1,j-1)
                res[j][i]=min(res[j-1][i]+delta[BLANC][Y[j-1]],res[j][i-1]+delta[X[i-1]][BLANC],res[j-1][i-1]+delta[X[i-1]][Y[j-1]])
    return res,chemin

def dispSolution(chemin,X,Y):
    #Retrouver une valeur qui correspond a la valeur minimum en remontant dans chemin
    actuel = (len(X),len(Y))
    precedent = actuel
    solution = []
    while(precedent != (0,0)):
        precedent=chemin[precedent[1]][precedent[0]]
        if(actuel[0] - precedent[0] == 0 and actuel[1] - precedent[1] == 1):
            solution = [(BLANC, Y[actuel[1]-1])] + solution
        if (actuel[1] - precedent[1] == 0 and actuel[0] - precedent[0] == 1):
            solution = [(X[actuel[0]-1], BLANC)] + solution
        if (actuel[1] - precedent[1] == 1 and actuel[0] - precedent[0] == 1):
            solution = [(X[actuel[0]-1], Y[actuel[1]-1])] + solution
        actuel = precedent

    #Afficher une valeur correspondant au minimum et le min
    for i in range(len(solution)):
        print(getLetter(solution[i][0]),end='')
    print()
    for i in range(len(solution)):
        print(getLetter(solution[i][1]),end='')
    print()
    print("Min value : ",round(res[len(Y)][len(X)],1))

#MAIN
if len(sys.argv) != 4:
    print("Usage :", sys.argv[0]," DeltaFile <Gene X> <Gene Y>")
else :
    # Initialisation

    delta = getDelta(sys.argv[1])
    geneX = sys.argv[2]
    geneY = sys.argv[3]

    X0 = []
    X1 = []

    for i in range(len(geneX)):
        X0.append(getNum(geneX[i]))

    for j in range(len(geneY)):
        X1.append(getNum(geneY[j]))



    #Affichage des valeurs d'entrées
    print("Delta := ")
    for lignes in delta:
        print(lignes)
    print("X :",geneX,"Y :",geneY)

    res,chemin = calculSolution(delta,X0,X1)

    dispSolution(chemin,X0,X1)