# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\guilh\Desktop\NewPharmaExperience\npx_mock\src\GUI\MainWindow.ui'
#
# Created: Wed Mar 28 21:15:10 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import InputFrame as Inp
import StartPageFrame as StP

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)


        self.centralwidget.setObjectName("centralwidget")

        Frame = QtGui.QFrame(self.centralwidget)
        # Frame.setObjectName("Frame")
        # self.gridLayoutFrame = QtGui.QGridLayout(Frame)
        # self.gridLayoutFrame.setObjectName("FrameLayout")
        Frame.show()



        self.frames = {}

        for F in (StP.Ui_Frame,Inp.Ui_Frame):

            Frame = QtGui.QFrame(self.centralwidget)
            self.gridLayout = QtGui.QGridLayout(Frame)
            ui = F()
            ui.setupUi(Frame)
            self.frames[F] = Frame
            Frame.setVisible(False)

        def show_frame(ctrl):

            for F in self.frames:
                self.frames[F].setVisible(False)
            frame = self.frames[ctrl]
            frame.setVisible(True)

        show_frame(Inp.Ui_Frame)


        MainWindow.setCentralWidget(self.centralwidget)


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/NPX ICO/clinic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/NPX ICO/clinic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuBlop = QtGui.QMenu(self.menubar)
        self.menuBlop.setObjectName("menuBlop")
        self.menuBlop2 = QtGui.QMenu(self.menubar)
        self.menuBlop2.setObjectName("menuBlop2")
        self.menuBlop3 = QtGui.QMenu(self.menubar)
        self.menuBlop3.setObjectName("menuBlop3")
        self.menuBlop4 = QtGui.QMenu(self.menubar)
        self.menuBlop4.setObjectName("menuBlop4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLo = QtGui.QAction(MainWindow)
        self.actionLo.setObjectName("actionLo")
        self.actionBackup = QtGui.QAction(MainWindow)
        self.actionBackup.setObjectName("actionBackup")
        self.actionAlguma_Coisa = QtGui.QAction(MainWindow)
        self.actionAlguma_Coisa.setObjectName("actionAlguma_Coisa")
        self.menuMenu.addAction(self.actionLo)
        self.menuBlop.addAction(self.actionBackup)
        self.menuBlop3.addAction(self.actionAlguma_Coisa)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuBlop.menuAction())
        self.menubar.addAction(self.menuBlop2.menuAction())
        self.menubar.addAction(self.menuBlop3.menuAction())
        self.menubar.addAction(self.menuBlop4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBlop.setTitle(QtGui.QApplication.translate("MainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBlop2.setTitle(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBlop3.setTitle(QtGui.QApplication.translate("MainWindow", "Alguma Coisa", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBlop4.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLo.setText(QtGui.QApplication.translate("MainWindow", "lo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBackup.setText(QtGui.QApplication.translate("MainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlguma_Coisa.setText(QtGui.QApplication.translate("MainWindow", "Alguma Coisa", None, QtGui.QApplication.UnicodeUTF8))

import npx_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
