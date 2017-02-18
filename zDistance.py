import numpy as np


def zDistance(A,B):
    [M, t] = (A.size);
    [N, s] = (B.size);

    a = sum(np.multiply(A,A))
    b = sum(np.multiply(B,B))

    if M < 150:
        X =  np.matmul(np.transpose(a) , np.ones(1,N));
        Y = np.ones(M, 1) * b;
    else
        X = np.repeat(b, M, 1);
        Y = np.repeat(np.transpose(a),1,N);

    D = np.sqrt(X + Y - 2 * A * np.transpose(B));

    return D
