# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\guilh\Desktop\NewPharmaExperience\npx_mock\src\GUI\DistInput.ui'
#
# Created: Mon Apr  2 22:46:30 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DistInput(QtGui.QWidget):
    def __init__(self, master):
        QtGui.QWidget.__init__(self,master)
        self.gridLayout_4 = QtGui.QGridLayout(self)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LabFrame = QtGui.QFrame(self)
        self.LabFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LabFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.LabFrame.setObjectName("LabFrame")
        self.gridLayout = QtGui.QGridLayout(self.LabFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.InputWidget = QtGui.QWidget(self.LabFrame)
        self.InputWidget.setObjectName("InputWidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.InputWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Email2Entry = QtGui.QLineEdit(self.InputWidget)
        self.Email2Entry.setObjectName("Email2Entry")
        self.gridLayout_3.addWidget(self.Email2Entry, 5, 2, 1, 1)
        self.Phone2Label = QtGui.QLabel(self.InputWidget)
        self.Phone2Label.setObjectName("Phone2Label")
        self.gridLayout_3.addWidget(self.Phone2Label, 7, 1, 1, 1)
        self.Phone1Label = QtGui.QLabel(self.InputWidget)
        self.Phone1Label.setObjectName("Phone1Label")
        self.gridLayout_3.addWidget(self.Phone1Label, 6, 1, 1, 1)
        self.FaxLabel = QtGui.QLabel(self.InputWidget)
        self.FaxLabel.setObjectName("FaxLabel")
        self.gridLayout_3.addWidget(self.FaxLabel, 8, 1, 1, 1)
        self.Phone1Entry = QtGui.QLineEdit(self.InputWidget)
        self.Phone1Entry.setObjectName("Phone1Entry")
        self.gridLayout_3.addWidget(self.Phone1Entry, 6, 2, 1, 1)
        self.FaxEntry = QtGui.QLineEdit(self.InputWidget)
        self.FaxEntry.setObjectName("FaxEntry")
        self.gridLayout_3.addWidget(self.FaxEntry, 8, 2, 1, 1)
        self.Phone2Entry = QtGui.QLineEdit(self.InputWidget)
        self.Phone2Entry.setObjectName("Phone2Entry")
        self.gridLayout_3.addWidget(self.Phone2Entry, 7, 2, 1, 1)
        self.NameLabel = QtGui.QLabel(self.InputWidget)
        self.NameLabel.setObjectName("NameLabel")
        self.gridLayout_3.addWidget(self.NameLabel, 1, 1, 1, 1)
        self.CNPJLabel = QtGui.QLabel(self.InputWidget)
        self.CNPJLabel.setObjectName("CNPJLabel")
        self.gridLayout_3.addWidget(self.CNPJLabel, 2, 1, 1, 1)
        self.CNPJEntry = QtGui.QLineEdit(self.InputWidget)
        self.CNPJEntry.setObjectName("CNPJEntry")
        self.gridLayout_3.addWidget(self.CNPJEntry, 2, 2, 1, 1)
        self.NameEntry = QtGui.QLineEdit(self.InputWidget)
        self.NameEntry.setObjectName("NameEntry")
        self.gridLayout_3.addWidget(self.NameEntry, 1, 2, 1, 1)
        self.EnderEntry = QtGui.QLineEdit(self.InputWidget)
        self.EnderEntry.setObjectName("EnderEntry")
        self.gridLayout_3.addWidget(self.EnderEntry, 3, 2, 1, 1)
        self.Email1Label = QtGui.QLabel(self.InputWidget)
        self.Email1Label.setObjectName("Email1Label")
        self.gridLayout_3.addWidget(self.Email1Label, 4, 1, 1, 1)
        self.Email1Entry = QtGui.QLineEdit(self.InputWidget)
        self.Email1Entry.setObjectName("Email1Entry")
        self.gridLayout_3.addWidget(self.Email1Entry, 4, 2, 1, 1)
        self.Email2Label = QtGui.QLabel(self.InputWidget)
        self.Email2Label.setObjectName("Email2Label")
        self.gridLayout_3.addWidget(self.Email2Label, 5, 1, 1, 1)
        self.EnderLabel = QtGui.QLabel(self.InputWidget)
        self.EnderLabel.setObjectName("EnderLabel")
        self.gridLayout_3.addWidget(self.EnderLabel, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 8, 1)
        spacerItem1 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 8, 1)
        self.gridLayout.addWidget(self.InputWidget, 4, 1, 1, 3)
        self.LogoLabel = QtGui.QLabel(self.LabFrame)
        self.LogoLabel.setObjectName("LogoLabel")
        self.gridLayout.addWidget(self.LogoLabel, 1, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 4, 4, 1)
        self.ButtonWidget = QtGui.QWidget(self.LabFrame)
        self.ButtonWidget.setObjectName("ButtonWidget")
        self.gridLayout_5 = QtGui.QGridLayout(self.ButtonWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.CancelarButton = QtGui.QPushButton(self.ButtonWidget)
        self.CancelarButton.setObjectName("CancelarButton")
        self.gridLayout_5.addWidget(self.CancelarButton, 0, 2, 1, 1)
        self.SalvarButton = QtGui.QPushButton(self.ButtonWidget)
        self.SalvarButton.setObjectName("SalvarButton")
        self.gridLayout_5.addWidget(self.SalvarButton, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(350, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.ButtonWidget, 5, 1, 1, 3)
        self.TitleLabel = QtGui.QLabel(self.LabFrame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout.addWidget(self.TitleLabel, 1, 1, 1, 3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 8, 1, 1, 3)
        spacerItem6 = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 6, 1)
        self.gridLayout_4.addWidget(self.LabFrame, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, DistInput):
        DistInput.setWindowTitle(QtGui.QApplication.translate("DistInput", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.Phone2Label.setText(QtGui.QApplication.translate("DistInput", "Telefone 2", None, QtGui.QApplication.UnicodeUTF8))
        self.Phone1Label.setText(QtGui.QApplication.translate("DistInput", "Telefone 1", None, QtGui.QApplication.UnicodeUTF8))
        self.FaxLabel.setText(QtGui.QApplication.translate("DistInput", "Fax", None, QtGui.QApplication.UnicodeUTF8))
        self.NameLabel.setText(QtGui.QApplication.translate("DistInput", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.CNPJLabel.setText(QtGui.QApplication.translate("DistInput", "CNPJ", None, QtGui.QApplication.UnicodeUTF8))
        self.Email1Label.setText(QtGui.QApplication.translate("DistInput", "E-mail 1", None, QtGui.QApplication.UnicodeUTF8))
        self.Email2Label.setText(QtGui.QApplication.translate("DistInput", "E-mail 2", None, QtGui.QApplication.UnicodeUTF8))
        self.EnderLabel.setText(QtGui.QApplication.translate("DistInput", "Endereço", None, QtGui.QApplication.UnicodeUTF8))
        self.LogoLabel.setText(QtGui.QApplication.translate("DistInput", "<html><head/><body><p><img src=\":/NPX ICO/clinic (2).png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelarButton.setText(QtGui.QApplication.translate("DistInput", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.SalvarButton.setText(QtGui.QApplication.translate("DistInput", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.TitleLabel.setText(QtGui.QApplication.translate("DistInput", "<html><head/><body><p align=\"center\">Cadastro de Distribuidores</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

from src.GUI import npx_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DistInput = QtGui.QFrame()
    ui = Ui_DistInput()
    ui.setupUi(DistInput)
    DistInput.show()
    sys.exit(app.exec_())
