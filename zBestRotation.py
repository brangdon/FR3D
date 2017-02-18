import numpy as np
from numpy import linalg as LA

def zBestRotation(A, B):
    n = len(A[:, 1])
    M = np.zeros(3,3)

    for i in range(1, n + 1):

        M = M + np.matmul(A[i,:].transpose(), B[i,:])

    v, d = LA.eig(np.matmul(M.transpose(),M))
    e,i = np.multiply(np.diag(d), (-1))



    a = v[:, i(1)] # eigenvectorwith largest eigenvalue
    b = v[:, i(2)]
    c = v[:, i(3)]

    np.sqrt([1, 4, 9])

    Ma = np.multiply(M, a) / np.sqrt((e[0]) * (-1))
    Mb = np.multiply(M, b) / np.sqrt((e[1]) * (-1))

    if(np.linalg.det([1,b,c]) > 0):
        g = np.cross(Ma, Mb)
    else:
        g = np.multiply(np.cross(Ma, Mb), -1)

    R = np.matmul([a,b,c], np.transpose([Ma, Mb, g]))

    return R
