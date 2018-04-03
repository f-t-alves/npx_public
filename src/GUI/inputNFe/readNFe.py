import xml.etree.ElementTree as eTree

def readNFe(filename):
    cleanDict = cleanNFe(filename)
    fileclean = open(cleanDict['filename'])

    xml_tree = eTree.parse(fileclean)
    xml_root = xml_tree.getroot()

    readDict = {}

    prodEAN = []
    prodLot = []
    prodFabDate = []
    prodExpDate = []
    prodQuantity = []

    for prot in xml_root.iter('infProt'):
        NFeID = prot.find('chNFe').text

    for product in xml_root.iter('prod'):
        prodEAN.append(int(product.find('cEAN').text))

        med = product.find('med')
        prodLot.append(med.find('nLote').text)
        prodFabDate.append(med.find('dFab').text)
        prodExpDate.append(med.find('dVal').text)
        prodQuantity.append(int(float(med.find('qLote').text)))

    fileclean.close()

    readDict['NFeID'] = NFeID
    readDict['prodEAN'] = prodEAN
    readDict['prodLot'] = prodLot
    readDict['prodFabDate'] = prodFabDate
    readDict['prodExpDate'] = prodExpDate
    readDict['prodQuantity'] = prodQuantity
    readDict['NFeFile'] = cleanDict['filein']

    return readDict





def cleanNFe(filename):
    outDict = {}

    filein = open(filename)
    outDict['filein'] = filein.read()
    filein.seek(0,0)

    temp = filename.split('.')
    temp.insert(-1,'_clean.')
    filename = ''.join(temp)
    outDict['filename'] = filename
    fileout = open(filename,mode='w+')

    del_list = [' xmlns="http://www.portalfiscal.inf.br/nfe"',' xmlns="http://www.w3.org/2000/09/xmldsig#"']
    for line in filein:
        for substr in del_list:
            line = line.replace(substr, "")
        fileout.write(line)

    filein.close()
    fileout.close()

    return outDict
