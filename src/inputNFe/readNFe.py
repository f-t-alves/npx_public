import xml.etree.ElementTree as eTree

def readNFe(filename):
    filename = cleanNFe(filename)
    fileclean = open(filename)

    xml_tree = eTree.parse(filename)
    xml_root = xml_tree.getroot()

    readDict = {}

    prodEAN = []
    prodQuantity = []

    for prot in xml_root.iter('infProt'):
        NFeID = prot.find('chNFe').text

    for product in xml_root.iter('prod'):
        prodEAN.append(int(product.find('cEAN').text))
        prodQuantity.append(int(float(product.find('qCom').text)))

    fileclean.close()

    readDict['prodEAN'] = prodEAN
    readDict['prodQuantity'] = prodQuantity

    return readDict





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
