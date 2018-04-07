import sys
from PySide import QtGui

from src.GUI import MainWindow as MaW

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = MaW.Ui_MainWindow(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
