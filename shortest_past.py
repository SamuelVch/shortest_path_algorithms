import sys
import numpy as np
import os

matrix = None
algo = 0


def Djisktra(arr):
    path = np.zeros(len(arr), dtype=int)
    path.fill(10**12)

def Bellman_Ford(arr):
    distance = np.matrix(np.zeros((len(arr), len(arr))))  # initialisation de la matrice D à zero partout
    for ligne in range(len(arr)):
        for colonne in range(arr[ligne].size):
            if ligne != colonne:  # lorsque le nœud source et le nœud d'arrivé ne sont pas les mêmes (a vers a, b vers b, etc.)
                distance[ligne, colonne] = 10**12  # mettre la distance entre les deux nœuds = inf

    for source in range(len(arr)):  # permettra d'itérer sur la même ligne plusieurs fois
        for _ in range(len(arr) - 1):  # permettra de comparer tous les chemins possibles dans les autres lignes de la matrice d'adjacence
            for node in range(len(arr)):
                for neighbour in range(arr[node].size):
                    distance[source, neighbour] = min(distance[source, neighbour], distance[source, node] + arr[node, neighbour])  # si la distance entre le nœud et son voisin est plus faible que celle actuelle, la remplacer

    return distance


def Floyd_Warshall(arr):
    return


if __name__ == '__main__':
    n = len(sys.argv)
    if n < 2:
        print("Please insert the path of the adjacency matrix as an argument")
        sys.exit("Program end")
    print("Adjacency matrix path: " + sys.argv[1])
    arr = np.loadtxt(sys.argv[1], delimiter=",", dtype=float)
    print(arr)
    print("By default, the shortest path of every pair will be calculated using Djisktra, Bellman-Ford and "
          "Floyd_Warshall")
    try:
        if n == 3:
            Djisktra(arr)
        else:
            print(Djisktra(arr))
            print(Bellman_Ford(arr))
            print(Floyd_Warshall(arr))
        print("Shortest path computation done !")
    except:
        print("Shortest path computation error !")
