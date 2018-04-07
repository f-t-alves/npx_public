import pandas as pd

def readCSV(filecsv):
    reader = pd.read_csv(filecsv,na_values=None,encoding='utf-8')
    return reader

def selectQuery(commandString,cursor):
    outDict = {}
    all_rows = cursor.fetchall()
    for row in all_rows:
        index = row[0]
        for i in range(nColumns):
            outDict[inHeaders[i]].append(row[i])
    return outDict

def insertTable(tableName,inHeaders,inData,cursor):
    nColumns = len(inHeaders)
    parenthesis = '''(''' + '''?,''' * (nColumns-1) + '''?)'''
    targets = tableName + '''('''
    for i in range(nColumns-1):
        targets += inHeaders[i] + ''','''
    targets += inHeaders[-1] + ''')'''
    commandString = '''INSERT INTO ''' + targets + ''' VALUES''' + parenthesis
    cursor.executemany(commandString,inData)

def selectTable(tableName,inHeaders,cursor):
    outDict = {}
    targets = ''''''
    nColumns = len(inHeaders)
    for i in range(nColumns-1):
        header = inHeaders[i]
        outDict[header] = []
        targets += header + ''', '''
    outDict[inHeaders[-1]] = []
    targets += inHeaders[-1]

    commandString = '''SELECT ''' + targets + ''' FROM ''' + tableName

    outDict = selectQuery(commandString,cursor)

    return outDict

def removeDuplicates(inList):
    outList = []
    for item in inList:
        if item not in outList:
            outList.append(item)
    return outList

def findHeader(allTables,target):
    foundCount = 0
    for key in allTables:
        table = allTables[key]
        fields = list(table.fields.keys())
        for field in fields:
            if target == field:
                return table.name
    return None

def advancedSelect(allTables,allLinks,headerDict,cursor):
    #allLinks => {'Products-Laboratories': 'Products.ProdLabID = Laboratories.LabID'}
    #headerDict => {'col1':{'visible': True, filters:{'operation':'equal', 'values': [1,5]}}}
    #operations => equal, greater, less, gequal, lequal, between, not, in
    tableList = []

    selectList = []
    fromList = []
    whereDict = {}
    linkDict = {}
    for key in headerDict:
        tableList.append(findHeader(allTables,key))
        if headerDict[key]['visible']:
            selectList.append(key)
        if headerDict[key]['filters']:
            whereDict[key] = headerDict[key]['filters']
    tableList = removeDuplicates(tableList)
    tableList.sort()

    slLen = len(selectList)
    flLen = len(tableList)
    wdLen = len(whereDict)

    existingLinks = list(allLinks.keys())

    for i in range(0,flLen-1):
        for j in range(i,flLen):
            sortList = []
            sortList.append(tableList[i])
            sortList.append(tableList[j])
            sortList.sort()
            pairString = sortList[0] + '-' + sortList[1]
            if pairString in existingLinks:
                linkDict[pairString] = allLinks[pairString]

    keyList = list(linkDict.keys())
    klLen = len(keyList)
    for i in range(klLen):
        tableList = keyList[i].split('-')
        fromList.append(tableList[0])
        fromList.append(tableList[1])
    fromList = removeDuplicates(fromList)

    selectString = '''SELECT '''
    for i in range(0,slLen-1):
        selectString += selectList[i] + ''', '''
    selectString += selectList[-1]

    fromString = ''' FROM ''' + fromList[0]
    for i in range(1,flLen):
        table = fromList[i]
        fromString += ''' INNER JOIN ''' + table + ''' ON'''
        for j in range(0,i):
            sortList = [table]
            sortList.append(fromList[j])
            sortList.sort()
            pairString = sortList[0] + '-' + sortList[1]
            if pairString in keyList:
                fromString += ''' ''' + linkDict[pairString] + ''','''
        if fromString[-1:] == ''',''':
            fromString = fromString[:-1]

    whereString = ''''''
    if wdLen>0:
        whereString = ''' WHERE '''
    for key in whereDict:
        op = whereDict[key]['operation']
        val = whereDict[key]['values']
        if len(val)>0:
            if op == 'equal':
                whereString += ''' ''' + key + ''' LIKE ''' + str(val[0]) + ''' AND '''
            elif op == 'greater':
                whereString += ''' ''' + key + ''' > ''' + str(val[0]) + ''' AND '''
            elif op == 'less':
                whereString += ''' ''' + key + ''' < ''' + str(val[0]) + ''' AND '''
            elif op == 'gequal':
                whereString += ''' ''' + key + ''' >= ''' + str(val[0]) + ''' AND '''
            elif op == 'lequal':
                whereString += ''' ''' + key + ''' <= ''' + str(val[0]) + ''' AND '''
            elif op == 'between':
                whereString += ''' ''' + key + ''' BETWEEN ''' + str(val[0]) + ''' AND ''' + str(val[1]) + ''' AND '''
            elif op == 'outside':
                whereString += ''' ''' + key + ''' NOT BETWEEN ''' + str(val[0]) + ''' AND ''' + str(val[1]) + ''' AND '''
            elif op == 'in':
                whereString += ''' ''' + key + ''' IN (''' + str(val[0])
                for i in range(1,len(val)):
                    whereString += ''', ''' + str(val[i])
                whereString +=  ''') AND '''
            elif op == 'not':
                whereString += ''' ''' + key + ''' NOT IN (''' + str(val[0])
                for i in range(1,len(val)):
                    whereString += ''', ''' + str(val[i])
                whereString +=  ''') AND '''
    if whereString[-4:] == '''AND ''':
        whereString = whereString[:-4]

    commandString = selectString + fromString + whereString

    outDict = selectQuery(commandString,cursor)

    return outDict
