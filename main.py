def findCandidate():
    return ""

def displayCandidates():
    return ""

def rankCandidates():
    return ""

def FR3DSearch():
    return ""

def AddFiletoSearch():
    return ""

def getAtom(file, number):
    visited = {}
    for line in open(file):
        list = line.split()
        type = list[0]
        if type == 'ATOM':
            # type = list[2]
            id = list[1]
            # print number
            if id == str(number):
                # print "gfssgf"
                print line
            # else:
                # print "lipa"
            # if type == 'CA':
            #     residue = list[3]
            #     type_of_chain = list[4]
            #     atom_count = int(list[5])
            #     position = list[6:8]
            #     if atom_count >= 0:
            #         if type_of_chain not in visited:
            #             visited[type_of_chain] = 1
            #             print residue,type_of_chain,atom_count,' '.join(position)

print "hge"
getAtom('1rc7.pdb', 977)