import sqlite3
import os

from src.setup.HighCommands import *
from src.inputNFe.readNFe import *
from src.inputNFe.inputNFe2DB import *

os.makedirs('data',exist_ok=True)
db = sqlite3.connect('data/testdb.db')
createDB(db)

filename = 'data/xml_test.xml'
NFeDict = readNFe(filename)

inputNFe2DB(NFeDict,db)
