#import xml.etree.ElementTree as eTree
import xmltodict
from src.inputNFe.cleanNFe import *

#def tags(tree,tagDict):
#    for node in tree:
#        nodeName = node.tag
#        nodeAttrib = node.attrib
#        nodeText = node.text
#        #fullTag = nodeName + nodeAttrib
#        tagDict[nodeName] = {'value':nodeText,'attrib':nodeAttrib}

#xml_tree = eTree.parse(filename)
#xml_root = xml_tree.getroot()

filename = 'data/xml_test.xml'

filename = cleanNFe(filename)
fileclean = open(filename)

dict_tree = xmltodict.parse(fileclean.read())

prodEAN = []

NFeID = dict_tree['nfeProc']['protNFe']['infProt']['chNFe']
for iprod in range(len(dict_tree['nfeProc']['NFe']['infNFe']['det'])):
    prodEAN.append(dict_tree['nfeProc']['NFe']['infNFe']['det'][iprod]['prod']['cEAN'])
