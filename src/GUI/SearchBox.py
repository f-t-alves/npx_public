# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\guilh\Desktop\NewPharmaExperience\npx_mock\src\GUI\SearchBoxAlfa.ui'
#
# Created: Tue Mar 20 17:12:33 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import npx_rc
from PySide import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(875, 639)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/NPX ICO/clinic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.verticalLayout = QtGui.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FiliaisCheckBox = QtGui.QCheckBox(Frame)
        self.FiliaisCheckBox.setObjectName("FiliaisCheckBox")
        self.horizontalLayout_2.addWidget(self.FiliaisCheckBox)
        self.ImageSymbol = QtGui.QLabel(Frame)
        self.ImageSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageSymbol.setObjectName("ImageSymbol")
        self.horizontalLayout_2.addWidget(self.ImageSymbol)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LabelText = QtGui.QLabel(Frame)
        self.LabelText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelText.setMargin(0)
        self.LabelText.setIndent(20)
        self.LabelText.setObjectName("LabelText")
        self.horizontalLayout_3.addWidget(self.LabelText)
        self.EntrySearch = QtGui.QLineEdit(Frame)
        self.EntrySearch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EntrySearch.setObjectName("EntrySearch")
        self.horizontalLayout_3.addWidget(self.EntrySearch)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SubmitButton = QtGui.QPushButton(Frame)
        self.SubmitButton.setMaximumSize(QtCore.QSize(127, 16777215))
        self.SubmitButton.setObjectName("SubmitButton")
        self.horizontalLayout.addWidget(self.SubmitButton)
        self.ClearButton = QtGui.QPushButton(Frame)
        self.ClearButton.setObjectName("ClearButton")
        self.horizontalLayout.addWidget(self.ClearButton)
        self.PlaceHolderButton = QtGui.QPushButton(Frame)
        self.PlaceHolderButton.setObjectName("PlaceHolderButton")
        self.horizontalLayout.addWidget(self.PlaceHolderButton)
        self.ExitButton = QtGui.QPushButton(Frame)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.Panel = QtGui.QGroupBox(Frame)
        self.Panel.setObjectName("Panel")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.Panel)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ResultTable = QtGui.QTableWidget(self.Panel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultTable.sizePolicy().hasHeightForWidth())
        self.ResultTable.setSizePolicy(sizePolicy)
        self.ResultTable.setMinimumSize(QtCore.QSize(420, 0))
        self.ResultTable.setShowGrid(True)
        self.ResultTable.setGridStyle(QtCore.Qt.SolidLine)
        self.ResultTable.setColumnCount(3)
        self.ResultTable.setObjectName("ResultTable")
        self.ResultTable.setColumnCount(3)
        self.ResultTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.ResultTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ResultTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ResultTable.setHorizontalHeaderItem(2, item)
        self.ResultTable.horizontalHeader().setCascadingSectionResizes(True)
        self.ResultTable.horizontalHeader().setDefaultSectionSize(250)
        self.ResultTable.horizontalHeader().setSortIndicatorShown(True)
        self.ResultTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.ResultTable)
        self.gridLayout.addWidget(self.Panel, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.FiliaisCheckBox.setText(QtGui.QApplication.translate("Frame", "Todas as filiais", None, QtGui.QApplication.UnicodeUTF8))
        self.ImageSymbol.setText(QtGui.QApplication.translate("Frame", "<html><head/><body><p><img src=\":/NPX ICO/clinic (2).png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelText.setText(QtGui.QApplication.translate("Frame", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.SubmitButton.setText(QtGui.QApplication.translate("Frame", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.ClearButton.setText(QtGui.QApplication.translate("Frame", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.PlaceHolderButton.setText(QtGui.QApplication.translate("Frame", "Whatvs", None, QtGui.QApplication.UnicodeUTF8))
        self.ExitButton.setText(QtGui.QApplication.translate("Frame", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.Panel.setTitle(QtGui.QApplication.translate("Frame", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.ResultTable.setSortingEnabled(True)
        self.ResultTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Frame", "Lab ID", None, QtGui.QApplication.UnicodeUTF8))
        self.ResultTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Frame", "Lab Name", None, QtGui.QApplication.UnicodeUTF8))
        self.ResultTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Frame", "Lab CNPJ", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())