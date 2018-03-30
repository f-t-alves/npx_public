import npx_rc
import sys
from PySide import QtGui

import StartPage_v2 as SP2
import InputProdPage as IPP

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = SP2.Ui_MainWindow()
inputProd = IPP.Ui_InputPage()
inputProd.setupUi(MainWindow)
ui.setupUi(MainWindow,inputProd)
MainWindow.show()
sys.exit(app.exec_())
