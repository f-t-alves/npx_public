import xml.etree.ElementTree as eTree
from src.inputNFe.readNFe import *

#def tags(tree,tagDict):
#    for node in tree:
#        nodeName = node.tag
#        nodeAttrib = node.attrib
#        nodeText = node.text
#        #fullTag = nodeName + nodeAttrib
#        tagDict[nodeName] = {'value':nodeText,'attrib':nodeAttrib}

filename = 'data/xml_test.xml'

#dict_tree = xmltodict.parse(fileclean.read())

#prodEAN = []
#
#NFeID = dict_tree['nfeProc']['protNFe']['infProt']['chNFe']
#for iprod in range(len(dict_tree['nfeProc']['NFe']['infNFe']['det'])):
#    prodEAN.append(dict_tree['nfeProc']['NFe']['infNFe']['det'][iprod]['prod']['cEAN'])

NFeDict = readNFe(filename)
