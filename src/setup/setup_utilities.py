import pandas as pd

def readCSV(filecsv):
    reader = pd.read_csv(filecsv,na_values=None,encoding='utf-8')
    return reader

def insertTable(tableName,inHeaders,inData,cursor):
    nColumns = len(inHeaders)
    parenthesis = '''(''' + '''?,''' * (nColumns-1) + '''?)'''
    targets = tableName + '''('''
    for i in range(nColumns-1):
        targets = targets + inHeaders[i] + ''','''
    targets = targets + inHeaders[-1] + ''')'''
    commandString = '''INSERT INTO ''' + targets + ''' VALUES''' + parenthesis
    cursor.executemany(commandString,inData)

def selectTable(tableName,inHeaders,cursor):
    outDict = {}
    targets = ''''''
    nColumns = len(inHeaders)
    for i in range(nColumns-1):
        header = inHeaders[i]
        outDict[header] = []
        targets = targets + header + ''', '''
    outDict[inHeaders[-1]] = []
    targets = targets + inHeaders[-1]

    commandString = '''SELECT ''' + targets + ''' FROM ''' + tableName

    cursor.execute(commandString)
    all_rows = cursor.fetchall()
    for row in all_rows:
        index = row[0]
        for i in range(nColumns):
            outDict[inHeaders[i]].append(row[i])

    return outDict
