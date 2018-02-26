def cleanNFe(filename):
    filein = open(filename)
    temp = filename.split('.')
    temp.insert(-1,'_clean.')
    filename = ''.join(temp)
    fileout = open(filename,mode='w+')

    del_list = [' xmlns="http://www.portalfiscal.inf.br/nfe"',' xmlns="http://www.w3.org/2000/09/xmldsig#"']
    for line in filein:
        for substr in del_list:
            line = line.replace(substr, "")
        fileout.write(line)

    filein.close()
    fileout.close()

    return filename
