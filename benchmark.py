#!/usr/bin/env python

import sys
import scipy.sparse
import numpy as np


def squarify(X, idx):
    X = X + X.T - scipy.sparse.diags(X.diagonal())
    return X[idx[:, np.newaxis], idx]


def sparse_triangular(X, idx):
    i, j, data = scipy.sparse.find(X[idx[:, np.newaxis], idx])

    ij = np.vstack([np.where(i > j, j, i), np.where(i > j, i, j)])

    # Remove duplicate elements
    ij, ind = np.unique(ij, axis=1, return_index=True)

    # Re-build the matrix
    return scipy.sparse.coo_matrix((data[ind], ij)).tocsr()


if __name__ == "__main__":
    X = scipy.sparse.load_npz("triangular_matrix_800k.npz")
    idx = np.random.choice(np.arange(X.shape[0]), 1000000, replace=True)

    functions = {"squarify": squarify, "sparse_triangular": sparse_triangular}

    res = functions[sys.argv[1]](X, idx)
