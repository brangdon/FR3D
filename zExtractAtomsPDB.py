

def zExtractAtomsPDB(Filename,Outputname,Verbose):
    # print "hej"
    outputFile = open(Outputname, 'w')

    with open(Filename, "r") as ins:
        # array = []
        for line in ins:
            if  line.startswith("ATOM") :
                outputFile.write(line)
            if line.startswith("HETATM"):
                line = line.replace("HETATM", "HETA  ")
                outputFile.write(line)
                # print line
            # array.append(line)

    outputFile.close()
    return ""

zExtractAtomsPDB('1S72.pdb', "out.txt", 1)