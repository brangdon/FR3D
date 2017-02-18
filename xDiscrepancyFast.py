import numpy as np
import math

from zAngleOfRotation import zAngleOfRotation
from zBestRotation import  zBestRotation

def xDiscrepancyFast(Model, Cand):

    L = len(Cand)

    if L == 2:

        C = np.matmul(np.transpose(Cand[1].Rot), Cand(2).Rot)

        r1 = np.matmul(Model.R, C)

        ang1 = zAngleOfRotation(r1)

        r2 = np.matmul(np.transpose(Model.R), np.transpose(C))
        ang2 = zAngleOfRotation(r2)

        t1 = Model.T1 - np.matmul(Cand[1].Center - Cand[0].Center, Cand[0].Rot)
        t2 = Model.T2 - np.matmul(Cand[0].Center - Cand[2].Center, Cand[1].Rot)

        v = Model.AngleWeight[0]

        #Disc = (np.sqrt(np.matmul(t1,np.transpose(t1))) + (v^2)*ang1^2) + np.sqrt(np.matmul(t2,np.transpose(t2)) + (v ^ 2) * ang2 ^ 2)) / 4;

        Disc = (np.sqrt(np.matmul(t1,np.transpose(t1)) + (v^2)*ang1^2) + np.sqrt(np.matmul(t2,np.transpose(t2)) + (v^2)*ang2^2))/4
        if(Disc > Model.LDiscCutoff):
            Disc = -1


    else:
        MCC = Model.CenteredCenters;
        MWC = Model.WeightedCenteredCenters;

        CandiCenters =  np.concatenate(1, Cand.Center);
        CMean = Model.LocWeight * CandiCenters / Model.NumNT;

        CC = CandiCenters - np.matmul(np.ones(L, 1), CMean)

        R = zBestRotation(CC, MWC)

        S = np.matmul(Model.LocWeight, sum(((MCC - CC * R)^2)))
        n = 1;

        while (S <= Model.LDiscCutoff) & (n <= L):
            ang = zAngleOfRotation(R * Cand(n).Rot * np.transpose((Model.NT(n).Rot)));
            S = S + (ang ^ 2) * Model.AngleWeight(n) ^ 2;
            n = n + 1;

        if (n > 1) & (S <= Model.LDiscCutoff):
            Disc = S;
        else:
            Disc = -1;

    return Disc