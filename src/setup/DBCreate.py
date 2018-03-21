def createTableCommand(tableObj):
    createCommand = '''CREATE TABLE IF NOT EXISTS'''

    tableName = tableObj.name
    createCommand = createCommand + ''' ''' + tableName + '''('''

    fieldName = list(tableObj.fields.keys())
    fLen = len(fieldName)
    for i in range(fLen):
        fName = fieldName[i]
        line = ''' '''
        line = line + fName + ''' '''
        line = line + tableObj.fields[fName]
        if i != fLen-1:
            line = line + ''','''
        createCommand = createCommand + line

    foreignTables = list(tableObj.foreignkeys.keys())
    ftLen = len(foreignTables)
    for i in range(ftLen):
        line = ''', '''
        ftName = foreignTables[i]
        fkName = tableObj.foreignkeys[ftName]
        line = line + '''FOREIGN KEY (''' + fkName + ''')'''
        line = line + ''' REFERENCES ''' + ftName + '''(''' + fkName + ''')'''
        createCommand = createCommand + line

    createCommand = createCommand + ''')'''

    #print(createCommand)
    return createCommand
