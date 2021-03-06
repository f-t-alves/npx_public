import pandas as pd
from src.setup import setup_utilities as utils
from  src.setup import SQLTables as tb

################################################################

def readProducts(filename):
    filecsv = open(filename)
    productsDF = utils.readCSV(filecsv)
    filecsv.close()
    productsDF = productsDF.infer_objects()
    productsDF.Registro = pd.to_numeric(productsDF.Registro, errors='coerce').fillna(0).astype('int64')
    productsDF.ProdEAN = productsDF.ProdEAN.fillna(0).astype('int64')
    return productsDF

def populateProducts(cursor):
    pop = []

    filename = 'data/test_products_nodupes.csv'
    productsDF = readProducts(filename)
    productsDF = replaceProductsCols(productsDF,cursor)

    headers = list(productsDF.columns)

    for row in productsDF.iterrows(): #iterrows() retorna uma tupla com o indice da row e a row em si
        index = row[0]
        rowBuffer = row[1].tolist()
        pop.append(tuple(rowBuffer))

    utils.insertTable(tb.prodsTable.name,headers,pop,cursor)

    #cursor.executemany('''INSERT INTO Products VALUES(?,?)''', pop) #falta filtrar os dados e converter as foreign keys
    return productsDF #TEST

def replaceProductsCols(productsDF,cursor):

    debugDict = {}

    headers = ['LabID', 'LabName']
    labDict = utils.selectTable(tb.labsTable.name,headers,cursor)

    headers = ['TeraClassID', 'TeraClassFull']
    teraDict = utils.selectTable(tb.teraClassTable.name,headers,cursor)

    headers = ['ListaTribID', 'ListDescription']
    listDict = utils.selectTable(tb.listTribTable.name,headers,cursor)

    productsDF.ProdLabID = productsDF.ProdLabID.replace(to_replace=labDict['LabName'],value=labDict['LabID'])
    productsDF.ProdTeraClassID = productsDF.ProdTeraClassID.replace(to_replace=teraDict['TeraClassFull'],value=teraDict['TeraClassID'])
    productsDF.ProdListaTribID = productsDF.ProdListaTribID.replace(to_replace=listDict['ListDescription'],value=listDict['ListaTribID'])

    #productsDF.AnalRecur = productsDF.AnalRecur.fillna(value=0) #Ha apenas Sim e NaN na coluna
    #productsDF.Comerc2016 = pd.to_numeric(productsDF.Comerc2016, errors='coerce').astype('int64') #Ha Sim, Nao e NaN na coluna

    productsDF = productsDF.replace(to_replace=['SIM','Sim'],value=[1,1])
    productsDF = productsDF.replace(to_replace=['NAO','NAo'],value=[0,0])

    debugDict['labDict'] = labDict
    debugDict['teraDict'] = teraDict
    debugDict['listDict'] = listDict

    return productsDF

################################################################

def readLabs(filename):
    filecsv = open(filename)
    labsDF = utils.readCSV(filecsv)
    filecsv.close()
    labsDF = labsDF.infer_objects()
    return labsDF

def populateLabs(cursor):
    pop = []

    filename = 'data/test_labs.csv'
    labsDF = readLabs(filename)

    headers = list(labsDF.columns)

    for row in labsDF.iterrows(): #iterrows() retorna uma tupla com o indice da row e a row em si
        index = row[0]
        rowBuffer = row[1].tolist()
        pop.append(tuple(rowBuffer))

    utils.insertTable(tb.labsTable.name,headers,pop,cursor)

    return labsDF #pop #TEST

################################################################

def readTeraClass(filename):
    filecsv = open(filename)
    teraDF = utils.readCSV(filecsv)
    filecsv.close()
    teraDF = teraDF.infer_objects()
    return teraDF

def populateTeraClass(cursor):
    pop = []

    filename = 'data/test_teraclass.csv'
    teraDF = readTeraClass(filename)

    headers = list(teraDF.columns)

    for row in teraDF.iterrows(): #iterrows() retorna uma tupla com o indice da row e a row em si
        index = row[0]
        rowBuffer = row[1].tolist()
        pop.append(tuple(rowBuffer))

    utils.insertTable(tb.teraClassTable.name,headers,pop,cursor)

    return teraDF #pop #TEST

################################################################

#TEST AREA
def populateListaTributaria(cursor):
    headers = ['ListaTribID','ListDescription']
    pop = [(1,'POSITIVA'),
           (2,'NEUTRA'),
           (3,'NEGATIVA')]
    utils.insertTable(tb.listTribTable.name,headers,pop,cursor)
