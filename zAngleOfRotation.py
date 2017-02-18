import numpy as np
import math


def zAngleOfRotation(R):
    alpha = 2 * math.acos(min(1, math.sqrt(np.trace(R) + 1) / 2));
    return alpha
