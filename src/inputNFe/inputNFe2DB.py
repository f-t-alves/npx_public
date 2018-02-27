import traceback

def inputNFe2DB(inDict,db):
    cursor = db.cursor()
    inList = []
    length = len(inDict['prodEAN'])
    for i in range(length):
        inList.append((inDict['prodEAN'][i],inDict['prodQuantity'][i]))
    try:
        cursor.executemany('''
        INSERT OR IGNORE INTO StockControl(EAN,Quantity)
           VALUES(?,?)''', inList)
        db.commit()
    except:
        db.rollback()
        print('inputNFe failed')
        traceback.print_exc()
