# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\guilh\Desktop\NewPharmaExperience\npx_mock\src\GUI\MainWindow.ui'
#
# Created: Wed Mar 28 21:15:10 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from src.GUI.InputFrame import Ui_InputPage
from src.GUI.StartPageFrame import Ui_StartPage
from src.GUI.NFeInput import Ui_NFe_Frame
from src.GUI.LabInput import Ui_LabInput
from src.GUI.DistInput import Ui_DistInput
from src.GUI.ClienteInput import Ui_ClienteFrame
from src.GUI.SearchBox import Ui_SearchBoxAlfa


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 720)

        self.centralwidget = QtGui.QWidget(MainWindow)


        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("CentralLayout")


        self.frames = {}

        for F in (Ui_StartPage,Ui_InputPage,Ui_NFe_Frame,Ui_LabInput,Ui_DistInput,Ui_ClienteFrame,Ui_SearchBoxAlfa):

            Frame = F(self.centralwidget)

            self.frames[F] = Frame
            Frame.setVisible(False)
            self.gridLayout.addWidget(Frame, 0, 0, 1, 1)


        self.frames[Ui_StartPage].setVisible(True)

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

        def show_frame(ctrl):

            for F in self.frames:
                self.frames[F].setVisible(False)
            frame = self.frames[ctrl]
            frame.setVisible(True)


        def LabCons():

            inDict =  {
                "Headers":{
                    "ID":{
                        "HeadName":"LabID",
                        "HeadWidth":50
                    },
                    "Nome":{
                        "HeadName":"LabName",
                        "HeadWidth":250
                    },
                    "CNPJ":{
                        "HeadName":"LabCNPJ",
                        "HeadWidth":150
                    },
                    "Endereço":{
                        "HeadName":"LabOfficeAddress",
                        "HeadWidth":400
                    },
                    "Telefone 1":{
                        "HeadName":"LabContactPhone1",
                        "HeadWidth":150
                    },
                    "Telefone 2":{
                        "HeadName":"LabContactPhone2",
                        "HeadWidth":150
                    },
                    "E-Mail 1":{
                        "HeadName":"LabContactEmail1",
                        "HeadWidth":300
                    },
                    "E-Mail 2":{
                        "HeadName":"LabContactEmail2",
                        "HeadWidth":300
                    },
                    "Fax":{
                        "HeadName":"LabContactFax",
                        "HeadWidth":150
                    }
                },
                "Buttons":{
                    "ExitButton":None
                },
                "EntryBox":{
                    "Nome do Laboratório":{
                        "HeadName":"LabName",
                        "Context":True

                    }
                }
            }

            self.frames[Ui_SearchBoxAlfa].BuildWidget(inDict)

            show_frame(Ui_SearchBoxAlfa)

        def DistCons():

            inDict =  {
                "Headers":{
                    "ID":{
                        "HeadName":"ProvCompID",
                        "HeadWidth":50
                    },
                    "Nome":{
                        "HeadName":"ProvCompName",
                        "HeadWidth":250
                    },
                    "Fax":{
                        "HeadName":"ProvContactFax",
                        "HeadWidth":150
                    }
                },
                "Buttons":{
                    "ExitButton":None
                },
                "EntryBox":{
                    "Nome do Distribuidor":{
                        "HeadName":"ProvCompName",
                        "Context":True

                    }
                }
            }

            self.frames[Ui_SearchBoxAlfa].BuildWidget(inDict)

            show_frame(Ui_SearchBoxAlfa)



        # Bloco com os comandos que dão link entre as frames

        self.frames[Ui_StartPage].Produto_Button.clicked.connect(lambda: show_frame(Ui_InputPage) )
        self.frames[Ui_StartPage].NFe_Button.clicked.connect(lambda: show_frame(Ui_NFe_Frame) )
        self.frames[Ui_StartPage].Laboratorios_Button.clicked.connect(lambda: show_frame(Ui_LabInput) )
        self.frames[Ui_StartPage].Distribuidor_Button.clicked.connect(lambda: show_frame(Ui_DistInput) )
        self.frames[Ui_StartPage].Clientes_Button.clicked.connect(lambda: show_frame(Ui_ClienteFrame) )
        self.frames[Ui_StartPage].LabCons_Button.clicked.connect(LabCons)
        self.frames[Ui_StartPage].DistCons_Button.clicked.connect(DistCons)
        self.frames[Ui_SearchBoxAlfa].SearchButton.clicked.connect(lambda: self.frames[Ui_SearchBoxAlfa].SelectCall())
        self.frames[Ui_InputPage].Back_Button.clicked.connect(lambda: show_frame(Ui_StartPage) )
        self.frames[Ui_NFe_Frame].CancelarButton.clicked.connect(lambda: show_frame(Ui_StartPage) )
        self.frames[Ui_LabInput].CancelarButton.clicked.connect(lambda: show_frame(Ui_StartPage) )
        self.frames[Ui_DistInput].CancelarButton.clicked.connect(lambda: show_frame(Ui_StartPage) )
        self.frames[Ui_ClienteFrame].Cancelar_Button.clicked.connect(lambda: show_frame(Ui_StartPage) )
        self.frames[Ui_SearchBoxAlfa].ExitButton.clicked.connect(lambda: show_frame(Ui_StartPage) )




from src.GUI import npx_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
