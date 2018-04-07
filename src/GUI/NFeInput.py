# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\guilh\Desktop\NewPharmaExperience\npx_mock\src\GUI\NFeInput.ui'
#
# Created: Mon Apr  2 13:06:45 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QFileDialog

import sqlite3
from src.inputNFe import inputNFe2DB as iNFe
from src.inputNFe import readNFe as rNFe
from config import dbPath

class Ui_NFe_Frame(QtGui.QWidget):
    def __init__(self, master):
        QtGui.QWidget.__init__(self,master)
        self.gridLayout_2 = QtGui.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.InputNFe_Frame = QtGui.QFrame(self)
        self.InputNFe_Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.InputNFe_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.InputNFe_Frame.setObjectName("InputNFe_Frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.InputNFe_Frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.SalvarButton = QtGui.QPushButton(self.InputNFe_Frame)
        self.SalvarButton.setObjectName("SalvarButton")
        self.gridLayout_3.addWidget(self.SalvarButton, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.CancelarButton = QtGui.QPushButton(self.InputNFe_Frame)
        self.CancelarButton.setObjectName("CancelarButton")
        self.gridLayout_3.addWidget(self.CancelarButton, 2, 1, 1, 1)
        self.WidgetHeader = QtGui.QWidget(self.InputNFe_Frame)
        self.WidgetHeader.setObjectName("WidgetHeader")
        self.gridLayout = QtGui.QGridLayout(self.WidgetHeader)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Label = QtGui.QLabel(self.WidgetHeader)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 0, 0, 1, 1)
        self.FilePath_Entry = QtGui.QLineEdit(self.WidgetHeader)
        self.FilePath_Entry.setObjectName("FilePath_Entry")
        self.gridLayout.addWidget(self.FilePath_Entry, 0, 1, 1, 1)
        self.UploadButton = QtGui.QPushButton(self.WidgetHeader)
        self.UploadButton.setObjectName("UploadButton")
        self.gridLayout.addWidget(self.UploadButton, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.WidgetHeader, 0, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 0, 1, 3)
        self.gridLayout_2.addWidget(self.InputNFe_Frame, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def selectFile(self):
        filename = QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.', filter='*.XML')[0]
        self.FilePath_Entry.setText(filename)

    def submitNFe(self):
        msgDict = {}
        msgList = []

        filepath = self.FilePath_Entry.text()
        print(filepath)

        db = sqlite3.connect(dbPath)
        cursor = db.cursor()
        NFeDict = rNFe.readNFe(filepath)
        prepDict = iNFe.prepInputNFe2DB(NFeDict)
        NFeID = prepDict['nfeTuple'][0]
        flagDupe = False
        flagDupe = iNFe.checkDuplicateNFe(NFeID,cursor)
        if flagDupe:
            msgDict['msgTitle'] = ' Operation cancelled:'
            msgList.append('Duplicate NFe')
        else:
            outDict = iNFe.writeNFe2DB(prepDict,db)
            if len(outDict['missingProd']) > 0:
                msgDict['msgTitle'] = ' Operation cancelled:'
                msgList.append('Product(s) with EAN')
                for i in outDict['missingProd']:
                    msgList.append(i)
                msgList.append('not found in registered products table')
            elif outDict['Error']:
                msgDict['msgTitle'] = ' Operation cancelled:'
                msgList.append(outDict['Error'])
            else:
                msgDict['msgTitle'] = 'Import successful'
        msgDict['msgList'] = msgList
        #MaP.popupmsg(msgDict)
        db.close()
        print(NFeID)
        print(msgDict)
        return(filepath)

    def retranslateUi(self, NFe_Frame):
        NFe_Frame.setWindowTitle(QtGui.QApplication.translate("NFe_Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.SalvarButton.setText(QtGui.QApplication.translate("NFe_Frame", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelarButton.setText(QtGui.QApplication.translate("NFe_Frame", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.Label.setText(QtGui.QApplication.translate("NFe_Frame", "Arquivo NFe", None, QtGui.QApplication.UnicodeUTF8))
        self.UploadButton.setText(QtGui.QApplication.translate("NFe_Frame", "Upload", None, QtGui.QApplication.UnicodeUTF8))

        self.UploadButton.clicked.connect(self.selectFile)
        self.SalvarButton.clicked.connect(self.submitNFe)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NFe_Frame = QtGui.QFrame()
    ui = Ui_NFe_Frame()
    ui.setupUi(NFe_Frame)
    NFe_Frame.show()
    sys.exit(app.exec_())
