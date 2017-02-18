from zAxisAngleRadians import zAxisAngleRadians


def zAxisAngle(R):
    tuple = zAxisAngleRadians(R);

    axis = tuple[0]
    angle = tuple[1]

    angle = angle * 57.29577951308232;

    if axis(3) < 0:
        axis = axis * (-1)
        angle = angle * (-1)

    if angle < -90:
        angle = angle + 360;

    return (axis, angle)
