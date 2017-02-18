import numpy as np

from zBestRotation import zBestRotation


def zBestTransformation(X, Y):
    n = len(X[:, 1]);

    mX = np.mean(X);
    mY = np.mean(Y);

    A = X - np.matmul(np.ones(n, 1), mX)
    B = Y - np.matmul(np.ones(n, 1), mY)

    R = zBestRotation(A, B);

    scale = np.sqrt(sum(sum(np.multiply(B, B))) / sum(sum(np.multiply(A, A))));

    shift = np.transpose(mY - np.matmul(mX , np.transpose(R)))

    sshift = np.transpose(mY - np.matmul(scale , np.matmul(mX , np.transpose(R))))

    return (R, scale, shift, sshift)
