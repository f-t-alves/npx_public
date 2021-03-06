import traceback

def inputNFe2DB(inDict,db):
    cursor = db.cursor()
    prepDict = prepInputNFe2DB(inDict)

    NFeID = prepDict['nfeTuple'][0]
    flagDupe = checkDuplicateNFe(NFeID,cursor)

    if flagDupe==True:
        print('Duplicate NFe, operation cancelled')
    else:
        writeNFe2DB(prepDict,db)



def writeNFe2DB(inDict,db):
    cursor = db.cursor()

    stockList = inDict['stockList']
    nfeTuple = inDict['nfeTuple']

    listLen = len(stockList)

    try:
        cursor.execute('''INSERT INTO NFeControl(NFeID,XMLFile) VALUES(?,?)''', nfeTuple)

        for i in range(listLen):
            cursor.execute('''SELECT StockID,EAN,LotNumber,Quantity FROM StockControl WHERE EAN = ? AND LotNumber = ?''',(stockList[i][0],stockList[i][1]))
            selectRow = cursor.fetchone()
            if selectRow == None:
                cursor.execute('''INSERT INTO StockControl(EAN,LotNumber,Quantity,ManufactureDate,ExpireDate) VALUES(?,?,?,?,?)''', stockList[i])
            else:
                rowID = selectRow[0]
                oldQuantity = selectRow[3]
                newQuantity = oldQuantity + stockList[i][2]
                cursor.execute('''UPDATE StockControl SET Quantity = ? WHERE StockID = ?''', (newQuantity,rowID))
        db.commit()
    except:
        db.rollback()
        print('inputNFe failed')
        traceback.print_exc()

def prepInputNFe2DB(inDict):
    outDict = {}
    stockList = []

    length = len(inDict['prodEAN'])
    NFeID = str(inDict['NFeID'])
    NFeFile = str(inDict['NFeFile'])

    nfeTuple = (NFeID,NFeFile)
    for i in range(length):
        stockList.append((inDict['prodEAN'][i],inDict['prodLot'][i],inDict['prodQuantity'][i],inDict['prodFabDate'][i],inDict['prodExpDate'][i]))

    outDict['stockList'] = stockList
    outDict['nfeTuple'] = nfeTuple

    return outDict

def checkDuplicateNFe(checkID,cursor):
    cursor.execute('''SELECT NFeID FROM NFeControl''')
    checkList = cursor.fetchall()
    flag = False
    for cell in checkList:
        flag = checkID in cell
        if flag==True:
            break
    return flag
