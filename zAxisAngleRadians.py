import numpy as np

from numpy import linalg as LA


def zAxisAngleRadians(R):
    v, d = LA.eig(np.array(R))

    # print v
    # print d

    y,i = np.sort(np.imag(np.diag(d)))
    # print np.sort((np.diag(d)))

    # print np.sort(np.imag(np.diag(d)))

    axis = v[:, i[1]];

    b = np.zeros(3, 1);

    b[i[1]] = (i[2]);
    b[i[2]] = (-1)*(i[1]);
    angle = 0
    # angle = np.arccos((b'*R*b) / (b' * b)) * sign(det([b R * b axis]));

    return (axis, angle)

# zAxisAngleRadians([[1,4,7],[2,5,8],[3,6,9]])