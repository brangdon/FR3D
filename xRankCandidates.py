import numpy as np

from xDiscrepancyFast import xDiscrepancyFast

def xRankCandidates(File, Model, Cand, Verbose):

    #if nargin < 4:
     #   Verbose = 0;

    if Verbose > 0:
     print('Calculating discrepancy\n');

    N = Model.NumNT;
    s = len(Cand[:, 1]);

    Discrepancy = np.zeros(65000, 1);

    Candidates = np.uint16(np.zeros(65000, len(Cand[0,:])));

    count = 0;

    #tic

   #  if Verbose > 0:
#        print('Seconds remaining:');

    for i in range(1,s):
        A = xDiscrepancyFast(Model,  File(Cand(i, N + 1)).NT(Cand(i, [N]))     )

        if A >= 0:
            count = count + 1;

            Discrepancy[count, 1] = A;

            Candidates[count,:]  = Cand[i,:];

#    if Verbose > 0:
 #       printf('\n');

    Candidates = Candidates[1:count,:];
    Discrepancy = np.sqrt(Discrepancy[1:count, 1]) / Model.NumNT;
    y, i = np.sort(Discrepancy);
    Candidates = Candidates[i,:];
    Discrepancy = Discrepancy(i);
#    if Verbose > 1:
 #       printf('Calculating discrepancy took        %8.3f seconds\n', toc);

    
    return (Candidates, Discrepancy)