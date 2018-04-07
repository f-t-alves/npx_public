import sqlite3
import os
import sys
from PySide import QtGui

from src.setup.HighCommands import *
from src.inputNFe.readNFe import *
from src.inputNFe.inputNFe2DB import *
from src.GUI import MainWindow as MaW

os.makedirs('data',exist_ok=True)
db = sqlite3.connect('data/testdb.db')
createDB(db)
df = populateDB(db)

filename = 'data/xml_test.xml'
NFeDict = readNFe(filename)

inputNFe2DB(NFeDict,db)

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = MaW.Ui_MainWindow(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
