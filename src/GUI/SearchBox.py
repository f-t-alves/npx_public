# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\guilh\Desktop\NewPharmaExperience\npx_mock\src\GUI\SearchBoxAlfa.ui'
#
# Created: Fri Apr  6 00:36:29 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SearchBoxAlfa(QtGui.QWidget):
    def __init__(self, master):
        QtGui.QWidget.__init__(self,master)
        self.gridLayout_5 = QtGui.QGridLayout(self)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget2 = QtGui.QWidget(self)
        self.widget2.setObjectName("widget2")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtGui.QWidget(self.widget2)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
        self.widget_4 = QtGui.QWidget(self.widget2)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SearchButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchButton.sizePolicy().hasHeightForWidth())
        self.SearchButton.setSizePolicy(sizePolicy)
        self.SearchButton.setStyleSheet("image: url(:/NPX ICO/search.png);")
        self.SearchButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/NPX ICO/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon)
        self.SearchButton.setObjectName("SearchButton")
        self.gridLayout_4.addWidget(self.SearchButton, 0, 0, 1, 1)
        self.FiliaisCheckBox = QtGui.QCheckBox(self.widget_4)
        self.FiliaisCheckBox.setObjectName("FiliaisCheckBox")
        self.gridLayout_4.addWidget(self.FiliaisCheckBox, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_4, 0, 2, 1, 1)
        self.ImageSymbol = QtGui.QLabel(self.widget2)
        self.ImageSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageSymbol.setObjectName("ImageSymbol")
        self.gridLayout_2.addWidget(self.ImageSymbol, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget2, 0, 0, 1, 1)
        self.Panel = QtGui.QGroupBox(self)
        self.Panel.setObjectName("Panel")
        self.gridLayout_6 = QtGui.QGridLayout(self.Panel)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5.addWidget(self.Panel, 1, 0, 1, 1)
        self.ResultTable = QtGui.QTableWidget(self.Panel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultTable.sizePolicy().hasHeightForWidth())
        self.ResultTable.setSizePolicy(sizePolicy)
        self.ResultTable.setMinimumSize(QtCore.QSize(420, 0))
        self.ResultTable.setShowGrid(True)
        self.ResultTable.setGridStyle(QtCore.Qt.SolidLine)
        self.widget1 = QtGui.QWidget(self)
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtGui.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.SubmitButton = QtGui.QPushButton(self.widget1)
        self.SubmitButton.setMaximumSize(QtCore.QSize(127, 16777215))
        self.SubmitButton.setObjectName("SubmitButton")
        self.gridLayout.addWidget(self.SubmitButton, 1, 1, 1, 1)
        self.ClearButton = QtGui.QPushButton(self.widget1)
        self.ClearButton.setObjectName("ClearButton")
        self.gridLayout.addWidget(self.ClearButton, 1, 2, 1, 1)
        self.EditButton = QtGui.QPushButton(self.widget1)
        self.EditButton.setObjectName("EditButton")
        self.gridLayout.addWidget(self.EditButton, 1, 3, 1, 1)
        self.ExitButton = QtGui.QPushButton(self.widget1)
        self.ExitButton.setObjectName("ExitButton")
        self.gridLayout.addWidget(self.ExitButton, 1, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget1, 2, 0, 1, 1)
        self.FiliaisCheckBox.setText(QtGui.QApplication.translate("SearchBoxAlfa", "Todas as filiais", None, QtGui.QApplication.UnicodeUTF8))
        self.SubmitButton.setText(QtGui.QApplication.translate("SearchBoxAlfa", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.ClearButton.setText(QtGui.QApplication.translate("SearchBoxAlfa", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.EditButton.setText(QtGui.QApplication.translate("SearchBoxAlfa", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.ExitButton.setText(QtGui.QApplication.translate("SearchBoxAlfa", "Exit", None, QtGui.QApplication.UnicodeUTF8))



        QtCore.QMetaObject.connectSlotsByName(self)


    def ClearFunc(self):
        childrenList = []
        childrenList += self.widget.findChildren(QtGui.QCheckBox)
        childrenList += self.widget.findChildren(QtGui.QLabel)
        childrenList += self.widget.findChildren(QtGui.QLineEdit)
        for child in childrenList:
            child.deleteLater()
        loop = self.ResultTable.columnCount()

        for i in range(loop-1,0,-1):
            self.ResultTable.removeColumn(i)

    def BuildWidget(self, inDict):

        self.ClearFunc()

        self.inDict = inDict

        headerList = list(inDict["Headers"].keys())
        buttonList = list(inDict["Buttons"].keys())
        entryList = list(inDict["EntryBox"].keys())

        hlLen = len(headerList)
        blLen = len(buttonList)
        elLen = len(entryList)

        self.labelList = []
        self.entryBoxList = []
        self.checkBoxList = []
        self.columnList = []

        self.ResultTable.setColumnCount(hlLen)
        self.ResultTable.setRowCount(0)

        self.SubmitButton.setVisible(False)
        self.EditButton.setVisible(False)
        self.ClearButton.setVisible(False)
        self.ExitButton.setVisible(False)

        for i in range(elLen):
            header = entryList[i]
            self.labelList.append(QtGui.QLabel(self.widget))
            self.labelList[i].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.labelList[i].setMargin(0)
            self.labelList[i].setIndent(20)
            self.labelList[i].setText(QtGui.QApplication.translate("SearchBoxAlfa", header, None, QtGui.QApplication.UnicodeUTF8))
            self.gridLayout_3.addWidget(self.labelList[i], i, 0, 1, 1)

            self.entryBoxList.append(QtGui.QLineEdit(self.widget))
            self.entryBoxList[i]
            self.entryBoxList[i].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.entryBoxList[i].setObjectName("EntrySearch")
            self.gridLayout_3.addWidget(self.entryBoxList[i], i, 1, 1, 1)

            self.checkBoxList.append(QtGui.QCheckBox(self.widget))
            self.checkBoxList[i].setObjectName("ContextCheckBox")
            self.gridLayout_3.addWidget(self.checkBoxList[i], i, 2, 1, 1)
            self.checkBoxList[i].setText(QtGui.QApplication.translate("SearchBoxAlfa", "Contexto", None, QtGui.QApplication.UnicodeUTF8))

        for i in range(hlLen):
            header = headerList[i]
            width = inDict["Headers"][header]["HeadWidth"]
            item = QtGui.QTableWidgetItem()
            self.ResultTable.setHorizontalHeaderItem(i, item)
            self.ResultTable.horizontalHeaderItem(i).setText(QtGui.QApplication.translate("SearchBoxAlfa", header, None, QtGui.QApplication.UnicodeUTF8))
            self.ResultTable.setColumnWidth(i, width)

        self.ResultTable.horizontalHeader().setCascadingSectionResizes(True)
        self.ResultTable.horizontalHeader().setSortIndicatorShown(True)
        self.ResultTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.ResultTable, 0, 0, 1, 1)

        childrenList = []
        buttonName = {}
        childrenList = self.widget1.findChildren(QtGui.QPushButton)
        for item in childrenList:
            buttonName[item.objectName()] = item
        for item in buttonName.keys():
            if item in buttonList:
                buttonName[item].setVisible(True)

    def SelectCall(self):

        print("ASUHDIUashd")










from src.GUI import npx_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SearchBoxAlfa = QtGui.QFrame()
    ui = Ui_SearchBoxAlfa()
    ui.setupUi(SearchBoxAlfa)
    SearchBoxAlfa.show()
    sys.exit(app.exec_())
