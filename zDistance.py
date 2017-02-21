import numpy as np


def zDistance(A,B):


    [M, t] = (A.size);
    if B == False:
        G = np.matmul(A, np.transpose(A))
        a = np.diag(G);
        X = np.repeat(a, 1, M);
        D = np.sqrt(X + np.transpose(X) - 2*G);            # |u-v| = |u|^2 + |v|^2 - 2 u . v
    else:
        [N, s] = (B.size);

        a = sum(np.multiply(A,A))
        b = sum(np.multiply(B,B))

        if M < 150:
            X =  np.matmul(np.transpose(a) , np.ones(1,N));
            Y = np.ones(M, 1) * b;
        else:
            X = np.repeat(b, M, 1);
            Y = np.repeat(np.transpose(a),1,N);

            D = np.sqrt(X + Y - 2 * A * np.transpose(B));

    return D
