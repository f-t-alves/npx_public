class SQLTable:
    def __init__(self):
        self.name = ''
        self.fields = {}
        self.foreignkeys = {}

def findLink(inTable):
    tableLinks = {}
    linkedTables = list(inTable.foreignkeys.keys())
    for key in linkedTables:
        fks = {}
        tName = inTable.name
        fks[tName] = inTable.foreignkeys[key][0]
        fks[key] = inTable.foreignkeys[key][1]
        sortList = [inTable.name,key]
        sortList.sort()
        linkKey = sortList[0] + '-' + sortList[1]
        tableLinks[linkKey] = sortList[0] + '''.''' + fks[sortList[0]] + ''' = ''' + sortList[1] + '''.''' + fks[sortList[1]]
    return tableLinks

def findAllLinks(allTables):
    tempDict = {}
    allLinks = {}
    for tableKey in allTables:
        table = allTables[tableKey]
        tempDict = findLink(table)
        for key in tempDict:
            allLinks[key] = tempDict[key]
    return allLinks


allTables = {}
allLinks = {}

labsTable = SQLTable()
labsTable.name = 'Laboratories'
labsTable.fields['LabID'] = 'INTEGER PRIMARY KEY NOT NULL'
labsTable.fields['LabName'] = 'TEXT NOT NULL'
labsTable.fields['LabCNPJ'] = 'TEXT NOT NULL'
labsTable.fields['LabOfficeAddress'] = 'TEXT'
labsTable.fields['LabContactEmail1'] = 'TEXT'
labsTable.fields['LabContactEmail2'] = 'TEXT'
labsTable.fields['LabContactPhone1'] = 'TEXT'
labsTable.fields['LabContactPhone2'] = 'TEXT'
labsTable.fields['LabContactFax'] = 'TEXT'

allTables[labsTable.name] = labsTable

provsTable = SQLTable()
provsTable.name = 'ProviderCompany'
provsTable.fields['ProvCompID'] = 'INTEGER PRIMARY KEY NOT NULL'
provsTable.fields['ProvCompName'] = 'TEXT NOT NULL'
provsTable.fields['ProvCompCNPJ'] = 'TEXT NOT NULL'
provsTable.fields['ProvOfficeAddress'] = 'TEXT'
provsTable.fields['ProvContactEmail1'] = 'TEXT'
provsTable.fields['ProvContactEmail2'] = 'TEXT'
provsTable.fields['ProvContactPhone1'] = 'TEXT'
provsTable.fields['ProvContactPhone2'] = 'TEXT'
provsTable.fields['ProvContactFax'] = 'TEXT'

allTables[provsTable.name] = provsTable

teraClassTable = SQLTable()
teraClassTable.name = 'TerapeuticClass'
teraClassTable.fields['TeraClassRowID'] = 'INTEGER PRIMARY KEY NOT NULL'
teraClassTable.fields['TeraClassID'] = 'TEXT UNIQUE'
teraClassTable.fields['TeraClassDescription'] = 'TEXT'
teraClassTable.fields['TeraClassFull'] = 'TEXT'

allTables[teraClassTable.name] = teraClassTable

listTribTable = SQLTable()
listTribTable.name = 'ListaTributaria'
listTribTable.fields['ListaTribID'] = 'INTEGER PRIMARY KEY NOT NULL'
listTribTable.fields['ListDescription'] = 'TEXT NOT NULL'

allTables[listTribTable.name] = listTribTable

NFeTable = SQLTable()
NFeTable.name = 'NFeControl'
NFeTable.fields['NFeID'] = 'TEXT PRIMARY KEY NOT NULL'
NFeTable.fields['EmissionDate'] = 'TEXT'
NFeTable.fields['DueDate'] = 'TEXT'
NFeTable.fields['DueTotal'] = 'REAL'
NFeTable.fields['TaxTotal'] = 'REAL'
NFeTable.fields['XMLFile'] = 'TEXT NOT NULL'

allTables[NFeTable.name] = NFeTable

stockTable = SQLTable()
stockTable.name = 'StockControl'
stockTable.fields['StockID'] = 'INTEGER PRIMARY KEY NOT NULL'
stockTable.fields['StockEAN'] = 'INTEGER NOT NULL'
stockTable.fields['StockLotNumber'] = 'TEXT'
stockTable.fields['StockQuantity'] = 'INTEGER NOT NULL'
stockTable.fields['StockLocation1'] = 'TEXT'
stockTable.fields['StockLocation2'] = 'TEXT'
stockTable.fields['StockManufactureDate'] = 'TEXT'
stockTable.fields['StockExpireDate'] = 'TEXT'
stockTable.foreignkeys['Products'] = ['StockEAN','ProdEAN']

allTables[stockTable.name] = stockTable

prodsTable = SQLTable()
prodsTable.name = 'Products'
prodsTable.fields['ProdEAN'] = 'INTEGER PRIMARY KEY NOT NULL'
prodsTable.fields['ProdName'] = 'TEXT NOT NULL'
prodsTable.fields['ProdLabID'] = 'INTEGER NOT NULL'
prodsTable.fields['PrinAtivo'] = 'TEXT NOT NULL'
prodsTable.fields['CodGGREM'] = 'INTEGER NOT NULL'
prodsTable.fields['Registro'] = 'INTEGER NOT NULL'
prodsTable.fields['ProdDescription'] = 'TEXT NOT NULL'
prodsTable.fields['ProdTeraClassID'] = 'INTEGER'
prodsTable.fields['ProdType'] = 'TEXT NOT NULL'
prodsTable.fields['PF0p'] = 'TEXT'
prodsTable.fields['PF12p'] = 'REAL'
prodsTable.fields['PF17p'] = 'REAL'
prodsTable.fields['PF17p_ALC'] = 'REAL'
prodsTable.fields['PF17p5'] = 'REAL'
prodsTable.fields['PF17p5_ALC'] = 'REAL'
prodsTable.fields['PF18p'] = 'REAL'
prodsTable.fields['PF18p_ALC'] = 'REAL'
prodsTable.fields['PF20p'] = 'REAL'
prodsTable.fields['PMC0p'] = 'REAL'
prodsTable.fields['PMC12p'] = 'REAL'
prodsTable.fields['PMC17p'] = 'REAL'
prodsTable.fields['PMC17p_ALC'] = 'REAL'
prodsTable.fields['PMC17p5'] = 'REAL'
prodsTable.fields['PMC17p5_ALC'] = 'REAL'
prodsTable.fields['PMC18p'] = 'REAL'
prodsTable.fields['PMC18p_ALC'] = 'REAL'
prodsTable.fields['PMC20p'] = 'REAL'
prodsTable.fields['RestHosp'] = 'INTEGER NOT NULL'
prodsTable.fields['CAP'] = 'INTEGER NOT NULL'
prodsTable.fields['CONFAZ87'] = 'INTEGER NOT NULL'
prodsTable.fields['AnalRecur'] = 'INTEGER'
prodsTable.fields['ProdListaTribID'] = 'INTEGER NOT NULL'
prodsTable.fields['Comerc2016'] = 'INTEGER'
prodsTable.fields['Tarja'] = 'TEXT NOT NULL'
prodsTable.foreignkeys[labsTable.name] = ['ProdLabID','LabID']
prodsTable.foreignkeys[teraClassTable.name] = ['ProdTeraClassID','TeraClassID']
prodsTable.foreignkeys[listTribTable.name] = ['ProdListaTribID','ListaTribID']

allTables[prodsTable.name] = prodsTable

allLinks = findAllLinks(allTables)
