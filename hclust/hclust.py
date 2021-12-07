#!/usr/bin/env python3

#Importing libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram , linkage
from skbio.tree import TreeNode as TN

def arrayify(data: list) -> np.ndarray:
    return np.array(data)

def link(data: np.ndarray) -> np.ndarray:
    return linkage(data, metric = 'cityblock', optimal_ordering = True)

def dendro(linkage_matrix: np.ndarray) -> dict:
    return dendrogram(linkage_matrix)

def plot_dendro(a_dendrogram: dict) -> None:
    plt.title('Dendrogram')
    plt.ylabel('City block distance')
    plt.show()

def tree(linkage_matrix: np.ndarray, original_data: np.ndarray) -> TN:
    return TN.from_linkage_matrix(linkage_matrix, [str(x) for x in range(original_data.shape[0])])

def data2tree(data: list) -> TN:
    return tree(link(arrayify(data)), arrayify(data))
 
def main():
    data = [[1, 2, 3, 4],
            [5, 22, 7, 8],
            [9, 10, 11, 12]]
    print(data)
    print(data2tree(data))
    plot_dendro(dendro(link(arrayify(data))))
    

if __name__ == "__main__":
    main()
