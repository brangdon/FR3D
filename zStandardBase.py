import numpy as np

def column(matrix, i):
    return [row[i] for row in matrix]

def zStandardBase(Base):
    P = []
    A = []

    if Base == 'A':
        A.append('N9') ; P.append([-2.150224, 0.126891, 0.000000]);
        A.append('C4');        P.append([-0.924859, - 0.501213,    0.000000])

        A.append('N3');        P.append([-0.658718 ,- 1.815294 ,   0.000000]);
        A.append('N1');        P .append(     [1.670931, - 1.131398   , 0.000000]);
        A.append('C6');        P .append (   [1.360416,    0.171881 ,   0.000000]);
        A.append('N6');        P .append  (      [2.355297  ,  1.088060 ,   0.000000]);
        A.append('C8');        P .append   (     [-1.906564   , 1.477225,    0.000000]);
        A.append('C5');        P .append   (   [0.000000,    0.549452  ,  0.000000]);
        A.append('C2');        P .append  (   [0.661274, - 2.029533   , 0.000000]);
        A.append('N7');        P .append  (   [-0.617269,    1.782995 ,   0.000000]);
        A.append('H2');        P .append  (   [0.973364, - 3.070824 ,   0.000000]);
        A.append('H8');        P .append  (  [-2.711953   , 2.199653 ,   0.000000]);
        A.append('H9');        P .append   ( [-3.048083 ,- 0.334168,    0.000000]);
        A.append('1H6');        P .append  (   [3.309197 ,   0.770943,    0.000000]);
        A.append('2H6');        P .append   (  [2.135761  ,  2.068742 ,   0.000000]);
    #
    #

    if Base == 'C':
        A.append('N1');        P .append([-1.201400, - 0.988797   , 0.000000]);
        A.append('C2');        P .append   (    [-1.228703 ,   0.432731  ,  0.000000]);
        A.append('O2')        ;        P.append   (     [-2.305800  ,  0.997479  ,  0.000000]);
        A.append('N3')        ;        P .append  (     [0.000000   , 1.058136  ,  0.000000]);
        A.append('C4')        ;        P.append  (    [1.103523   , 0.340863  ,  0.000000]);
        A.append('N4')        ;        P .append  (     [2.277717   , 1.023318  ,  0.000000]);
        A.append('C6')     ;        P .append   (    [-0.063948 ,- 1.726544 ,   0.000000]);
        A.append('C5')     ;        P .append   (    [1.143491 ,- 1.100074    ,0.000000]);
        A.append('H1')       ;        P .append  (      [-2.109196 ,- 1.432113   , 0.000000]);
        A.append('H6')        ;        P .append   (    [-0.176374 ,- 2.806043   , 0.000000]);
        A.append('H5')       ;        P .append (    [2.070986 ,- 1.657412   , 0.000000]);
        A.append('1H4')    ;        P.append    (  [3.165717 ,   0.556293 ,   0.000000]);
        A.append('2H4')      ;        P .append   (    [2.234862  ,  2.028988 ,   0.000000]);

    if Base == 'G':
        A.append('N9');        P .append   (     [2.172210   , 0.729189 ,   0.000000]);
        A.append('C4');        P .append     (   [1.001237  ,  0.019938  ,  0.000000]);
        A.append('N3');        P .append   (   [0.900356 ,- 1.338904   , 0.000000]);
        A.append('N1')       ;        P .append  (    [-1.421194 ,- 0.866938   , 0.000000]);
        A.append('C6')      ;        P .append   (    [-1.379129 ,   0.565543 ,   0.000000]);
        A.append('O6')     ;        P .append     (  [-2.414453 ,   1.201631 ,   0.000000]);
        A.append('C8')       ;        P .append    (   [1.834646   , 2.063338   , 0.000000]);
        A.append('C5')       ;        P .append   (  [0.000000  ,  0.992618  ,  0.000000]);
        A.append('C2')       ;        P .append   (    [-0.351059 ,- 1.727424  ,  0.000000]);
        A.append('N7')      ;        P .append   (   [0.527998   , 2.264153   , 0.000000]);
        A.append('N2')   ;        P .append    ( [-0.636748 ,- 3.060725   , 0.000000]);
        A.append('H1')        ;        P.append (     [-2.363856 ,- 1.237500   , 0.000000]);
        A.append('H8')      ;        P .append  (     [2.585708  ,  2.841187   , 0.000000]);
        A.append('H9')       ;        P .append  (    [3.097888  ,  0.326363  ,  0.000000]);
        A.append('1H2')       ;        P .append  (     [0.138301 ,- 3.699602  ,  0.000000]);
        A.append('2H2')        ;        P .append  (    [-1.574938 ,- 3.414999  ,  0.000000]);

    if Base == 'U':
        A.append('N1')    ;        P .append     ( [-1.140881 ,- 1.025641 ,   0.000000]);
        A.append('C2')     ;        P .append    ( [-1.240681  ,  0.362011 ,   0.000000]);
        A.append('O2')     ;        P .append    ( [-2.300579  ,  0.952478 ,   0.000000]);
        A.append('N3')    ;        P .append     ( [0.000000  ,  0.980206  ,  0.000000]);
        A.append('C4')    ;        P .append    ( [1.282012   , 0.395645   , 0.000000]);
        A.append('O4')    ;        P .append     (  [2.282917 ,   1.088566  ,  0.000000]);
        A.append('C6')     ;        P .append     ( [0.052878 ,- 1.708082   , 0.000000]);
        A.append('C5')     ;        P .append     (  [1.243058 ,- 1.064709   , 0.000000]);
        A.append('H5')     ;        P .append      (  [2.179366 ,- 1.605340   , 0.000000]);
        A.append('H1')    ;        P .append    ([-2.021852 ,- 1.517438  ,  0.000000]);
        A.append('H3')      ;        P .append   (  [-0.025642 ,   1.993008 ,   0.000000]);
        A.append('H6')      ;        P .append(    [-0.028009, - 2.789726  ,  0.000000]);

    A = np.transpose(A)

    X = column(P, 0)
    Y = column(P, 1)
    Z = column(P, 2)

    # print Z
    return (A, X, Y, Z)

# zStandardBase('A')
