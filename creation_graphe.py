import networkx as nx
import os


def create_G(edge_list):
    """
    Crée la matrice d'adjacence de G
    à partir d'une liste d'arc
    """
    G = nx.Graph()

    G.add_edges_from(edge_list)

    A = nx.adjacency_matrix(G)

    G_matrice = A.todense()

    return ((G_matrice.len(), G_matrice))


def create_F_matrices(number):
    """
    Crée un certain nombres de chaine à enregistrer
    et ressort une liste de matrice d'adjacence
    """
    if number == 0:
        return []

    F_matrices = []

    for i in range(1, number+1):
        F_temp = nx.Graph()
        for j in range(1, i+1):
            F_temp.add_node(j)
            if j != 1:
                F_temp.add_edge(j-1, j)
        F_matrices.append((i ,(nx.adjacency_matrix(F_temp)).todense()))

    return F_matrices


def create_folders(G, F_matrices):
    """
    Crée un dossier contenant 
    """
    os.makedirs(graphe_repertory)
    os.makedirs(graphe_repertory)


# Temporaire

edge_list = [(1, 2),
             (2, 1), (2, 3), (2, 4),
             (3, 2),
             (4, 2), (4, 5), (4, 6),
             (5, 4),
             (6, 4)]

F = int(input("nombre de chaines à crée"))