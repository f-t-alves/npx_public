def createProductTable(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
       EAN INTEGER PRIMARY KEY NOT NULL,
       ProdName TEXT NOT NULL,
       LabID INTEGER NOT NULL,
       PrinAtivo TEXT NOT NULL,
       CodGGREM INTEGER,
       Registro INTEGER NOT NULL,
       ProdDescription TEXT NOT NULL,
       TeraClassID TEXT,
       ProdType TEXT NOT NULL,
       PF0p REAL,
       PF12p REAL,
       PF17p REAL,
       PF17p_ALC REAL,
       PF17p5 REAL,
       PF17p5_ALC REAL,
       PF18p REAL,
       PF18p_ALC REAL,
       PF20p REAL,
       PMC0p REAL,
       PMC12p REAL,
       PMC17p REAL,
       PMC17p_ALC REAL,
       PMC17p5 REAL,
       PMC17p5_ALC REAL,
       PMC18p REAL,
       PMC18p_ALC REAL,
       PMC20p REAL,
       RestHosp INTEGER NOT NULL,
       CAP INTEGER NOT NULL,
       CONFAZ87 INTEGER NOT NULL,
       AnalRecur INTEGER,
       ListaTribID INTEGER NOT NULL,
       Comerc2016 INTEGER NOT NULL,
       Tarja INTEGER NOT NULL,
       FOREIGN KEY (LabID) REFERENCES Laboratories(LabID),
       FOREIGN KEY (TeraClassID) REFERENCES TerapeuticClass(TeraClassID),
       FOREIGN KEY (ListaTribID) REFERENCES ListaTributaria(ListaTribID)
    )''')

def createLaboratoryTable(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Laboratories(
       LabID INTEGER NOT NULL PRIMARY KEY,
       LabName TEXT NOT NULL,
       LabCNPJ TEXT NOT NULL,
       LabOfficeAddress TEXT,
       LabContactEmail1 TEXT,
       LabContactEmail2 TEXT,
       LabContactPhone1 TEXT,
       LabContactPhone2 TEXT,
       LabContactFax TEXT
    )''')

def createProviderTable(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProviderCompany(
       ProvCompID INTEGER PRIMARY KEY NOT NULL,
       ProvCompName TEXT NOT NULL,
       ProvCompCNPJ TEXT NOT NULL,
       ProvOfficeAddress TEXT,
       ProvContactEmail1 TEXT,
       ProvContactEmail2 TEXT,
       ProvContactPhone1 TEXT,
       ProvContactPhone2 TEXT,
       ProvContactFax TEXT
    )''')

def createTerapeuticClassTable(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TerapeuticClass(
       TeraClassID INTEGER PRIMARY KEY NOT NULL,
       Description TEXT NOT NULL
    )''')

def createListaTributaria(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ListaTributaria(
       ListaTribID INTEGER PRIMARY KEY NOT NULL,
       ClassDescription TEXT NOT NULL
    )''')

def createStockTable(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS StockControl(
       StockID INTEGER PRIMARY KEY NOT NULL,
       EAN INTEGER NOT NULL,
       LotNumber TEXT,
       Quantity INTEGER NOT NULL,
       Location1 TEXT,
       Location2 TEXT,
       ManufactureDate TEXT,
       ExpireDate TEXT,
       FOREIGN KEY (EAN) REFERENCES Products(EAN)
    )''')

def createNFeTable(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS NFeControl(
       NFeID TEXT PRIMARY KEY NOT NULL,
       EmissionDate TEXT,
       DueDate TEXT,
       DueTotal REAL,
       TaxTotal REAL,
       XMLFile TEXT NOT NULL
    )''')

#TEST AREA
def populateListaTributaria(cursor):
    pop = [(1,'Positiva'),
           (2,'Neutra'),
           (3,'Negativa')]
    cursor.executemany('''
    INSERT OR IGNORE INTO ListaTributaria(ListaTribID,ClassDescription)
       VALUES(?,?)''', pop)
