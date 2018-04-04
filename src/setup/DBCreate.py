def createTableCommand(tableObj):
    createCommand = '''CREATE TABLE IF NOT EXISTS'''

    tableName = tableObj.name
    createCommand += ''' ''' + tableName + '''('''

    fieldName = list(tableObj.fields.keys())
    fLen = len(fieldName)
    for i in range(fLen):
        fName = fieldName[i]
        line = ''' '''
        line += fName + ''' '''
        line += tableObj.fields[fName]
        if i != fLen-1:
            line += ''','''
        createCommand = createCommand + line

    foreignTables = list(tableObj.foreignkeys.keys())
    ftLen = len(foreignTables)
    for i in range(ftLen):
        line = ''', '''
        ftName = foreignTables[i]
        fkLocal = tableObj.foreignkeys[ftName][0]
        fkForeign = tableObj.foreignkeys[ftName][1]
        #fkName = tableObj.foreignkeys[ftName]
        line += '''FOREIGN KEY (''' + fkLocal + ''')'''
        line += ''' REFERENCES ''' + ftName + '''(''' + fkForeign + ''')'''
        createCommand = createCommand + line

    createCommand += ''')'''

    #print(createCommand)
    return createCommand
