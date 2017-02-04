

visited = {}
for line in open('1qrs.pdb'):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        type = list[2]
        if type == 'CA':
            residue = list[3]
            type_of_chain = list[4]
            atom_count = int(list[5])
            position = list[6:8]
            if atom_count >= 0:
                if type_of_chain not in visited:
                    visited[type_of_chain] = 1
                    print residue,type_of_chain,atom_count,' '.join(position)