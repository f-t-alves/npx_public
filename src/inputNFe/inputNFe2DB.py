import traceback

def inputNFe2DB(inDict,db):
    cursor = db.cursor()
    stockList = []

    length = len(inDict['prodEAN'])
    NFeID = str(inDict['NFeID'])
    NFeFile = str(inDict['NFeFile'])

    nfeTuple = (NFeID,NFeFile)
    for i in range(length):
        stockList.append((inDict['prodEAN'][i],inDict['prodQuantity'][i]))

    flagDupe = checkDuplicateNFe(NFeID,cursor)
    if flagDupe==True:
        print('Duplicate NFe, operation cancelled')
        return

    try:
        cursor.execute('''
        INSERT INTO NFeControl(NFeID,XMLFile)
           VALUES(?,?)''', nfeTuple)

        cursor.executemany('''
        INSERT INTO StockControl(EAN,Quantity)
           VALUES(?,?)''', stockList)
        db.commit()
    except:
        db.rollback()
        print('inputNFe failed')
        traceback.print_exc()

def checkDuplicateNFe(checkID,cursor):
    cursor.execute('''SELECT NFeID FROM NFeControl''')
    checkList = cursor.fetchall()
    flag = False
    for cell in checkList:
        flag = checkID in cell
        if flag==True:
            break
    return flag
