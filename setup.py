from src.setup.HighCommands import *
from src.setup.setup_utilities import advancedSelect
from src.setup.SQLTables import *
import sqlite3
import os

os.makedirs('data',exist_ok=True)

db = sqlite3.connect('data/testdb.db')
cursor = db.cursor()

createDB(db)
df = populateDB(db)

testDict = {
    'ProdName':{'visible':True,'filters':{'operation':'equal','values':['%LOSAR%']}},
    'PrinAtivo':{'visible':True,'filters':None},
    'LabName':{'visible':True,'filters':None},
    'TeraClassFull':{'visible':True,'filters':None},
    'ListDescription':{'visible':True,'filters':None},
    'LabID':{'visible':False,'filters':{'operation':'gequal','values':[100]}}
    }

td = advancedSelect(allTables,allLinks,testDict,cursor)
