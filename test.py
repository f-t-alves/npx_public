import sqlite3
import os

from src.setup.HighCommands import *
from src.inputNFe.readNFe import *
from src.inputNFe.inputNFe2DB import *
from src.GUI import MainApp as MaP

os.makedirs('data',exist_ok=True)
db = sqlite3.connect('data/testdb.db')
createDB(db)
df = populateDB(db)

filename = 'data/xml_test.xml'
NFeDict = readNFe(filename)

inputNFe2DB(NFeDict,db)

app = MaP.MainApp()
app.geometry("940x270")
app.resizable(width=True, height=True)
app.mainloop()
