import pandas as pd

def readCSV(filecsv):
    reader = pd.read_csv(filecsv,na_values=None)
    return reader

def readProduct(filename):
    filecsv = open(filename)
    productDF = readCSV(filecsv)
    productDF = productDF.infer_objects()
    productDF.REGISTRO = pd.to_numeric(productDF.REGISTRO, errors='coerce').fillna(0).astype('int64')
    productDF.EAN = productDF.EAN.fillna(0).astype('int64')
    return productDF

def populateProduct(cursor):
    pop = []

    filename = 'data/test_product.csv'
    productDF = readProduct(filename)

    for row in productDF.iterrows(): #iterrows() retorna uma tupla com o indice da row e a row em si
        index = row[0]
        rowBuffer = row[1].tolist()
        pop.append(tuple(rowBuffer))

    #cursor.executemany('''INSERT INTO Products VALUES(?,?)''', pop) #falta filtrar os dados e converter as foreign keys
    return pop #TEST

#TEST AREA
def populateListaTributaria(cursor):
    pop = [(1,'Positiva'),
           (2,'Neutra'),
           (3,'Negativa')]
    cursor.executemany('''
    INSERT OR IGNORE INTO ListaTributaria(ListaTribID,ClassDescription)
       VALUES(?,?)''', pop)
