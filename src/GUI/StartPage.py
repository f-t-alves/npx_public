
import sqlite3

import tkinter as tk
from tkinter import ttk
from src.GUI import LabPage as LabP
from src.GUI import ProviderPage as ProvP
from src.GUI import MedPage2 as MedP
from src.GUI import MedSearchPage as MSP
from src.GUI import MainApp as MaP
from tkinter import filedialog as fd
from src.inputNFe import readNFe as rNFe
from src.inputNFe import inputNFe2DB as iNFe

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)
#TestFont = font.Font(family='Verdana' , size= 10,weight='bold', slant='italic')


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        PageFrame=ttk.Frame(self,width=940,borderwidth=30)
        PageFrame.grid(ipady=300)

        label = tk.Label(PageFrame, text='Welcome to NPX', font = LARGE_FONT)
        label.grid(row = 0,pady=10,padx=340,sticky = 'we')
        # label2 = tk.Label(PageFrame, text='Menu', font = NORM_FONT)
        # label2.grid(row = 1,pady=10,padx=23,sticky = 'w')

        menuframe = ttk.LabelFrame(PageFrame,text='Menu',labelanchor='n',padding=10)
        menuframe.grid(sticky = 'nw')

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)
        s.layout('TEntry')
        # print(s.layout('TButton'))

        button = ttk.Button(menuframe, text="Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(Input),width=10)
        button.grid(row = 2,ipady=3,sticky = 'nw')
        button2 = ttk.Button(menuframe, text="Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(Search),width=10)
        button2.grid(row = 3,ipady=3,sticky = 'nw')
        button3 = ttk.Button(menuframe, text="NFe Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(ImportNFe),width=10)
        button3.grid(row = 4,ipady=3,sticky = 'nw')
        button4 = ttk.Button(menuframe, text="PlaceHolder",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=10)
        button4.grid(row = 5,ipady=3,sticky = 'nw')
        button5 = ttk.Button(menuframe, text="PlaceHolder",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=10)
        button5.grid(row = 6,ipady=3,sticky = 'nw')
        button6 = ttk.Button(menuframe, text="PlaceHolder",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=10)
        button6.grid(row = 7,ipady=3,sticky = 'nw')
        # button4 = ttk.Button(self, text="Med Input 2.0",style='Front Page Button.TButton',command=lambda: controller.show_frame(MedP2.MedPage))
        # button4.pack(ipady=10,fill ='x')


class Input(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940,relief='solid')

        PageFrame=ttk.Frame(self,width=940,relief='solid')
        PageFrame.grid(padx=300,sticky='nwse')

        label = tk.Label(PageFrame, text='Input Page', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)

        button = ttk.Button(PageFrame, text="Med Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(MedP.MedPage),width=30)
        button.grid(ipady=10)
        button2 = ttk.Button(PageFrame, text="Lab Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(LabP.LabPage),width=30)
        button2.grid(ipady=10)
        button3 = ttk.Button(PageFrame, text="Provider Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(ProvP.ProviderPage),width=30)
        button3.grid(ipady=10)
        button4 = ttk.Button(PageFrame, text="Back Home",style='Front Page Button.TButton',command=lambda: controller.show_frame(StartPage))
        button4.grid(pady=10)


class Search(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        PageFrame=ttk.Frame(self,width=940,relief='solid')
        PageFrame.grid(padx=300)


        label = tk.Label(PageFrame, text='Search Page', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)

        button = ttk.Button(PageFrame, text="Med Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(MSP.SearchMedPage),width=30)
        button.grid(ipady=10)
        button2 = ttk.Button(PageFrame, text="Lab Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=30)
        button2.grid(ipady=10)
        button3 = ttk.Button(PageFrame, text="Provider Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=30)
        button3.grid(ipady=10)
        button4 = ttk.Button(PageFrame, text="Back Home",style='Front Page Button.TButton',command=lambda: controller.show_frame(StartPage))
        button4.grid(pady=10)


class PlaceHolder(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        PageFrame=ttk.Frame(self,borderwidth=1,relief='solid')
        PageFrame.grid(padx=300)

        label = tk.Label(PageFrame, text='PlaceHolder', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        button = ttk.Button(PageFrame, text="Back Home",style='Front Page Button.TButton',command=lambda: controller.show_frame(StartPage))
        button.grid(pady=10)


class ImportNFe(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        PageFrame=ttk.Frame(self,borderwidth=1,relief='solid')
        PageFrame.grid(padx=120)

        label = tk.Label(PageFrame, text='Import NFe', font = LARGE_FONT)
        label.grid(pady=10,padx=10,columnspan=3)

        entr1 = tk.Entry(PageFrame)
        entr1.grid(row=1,column=1,ipadx=130,padx=10,ipady=2)

        def getFilename():

            filename =  fd.askopenfilename(initialdir = "C:/Users/%s",title = "Select XML",filetypes = (("XML Files","*.xml"),("all files","*.*")))
            entr1.insert(0,filename)

            #return(filename)

        def submitNFe():
            msgDict = {}
            msgList = []

            db = sqlite3.connect('data/testdb.db')
            cursor = db.cursor()

            filepath = entr1.get()

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
            MaP.popupmsg(msgDict)
            db.close()

            print(NFeID)
            print(outDict['Error'])
            return(filepath)

        button = ttk.Button(PageFrame, text="Back Home",style='Front Page Button.TButton',command=lambda: controller.show_frame(StartPage))
        button.grid(row=2,pady=10,padx=10)
        button1 = ttk.Button(PageFrame, text="Open",style='Front Page Button.TButton',command=getFilename)
        button1.grid(row=1,column=2,pady=10,padx=10)
        button2 = ttk.Button(PageFrame, text="Submit",style='Front Page Button.TButton',command=submitNFe)
        button2.grid(row=2,column=2,pady=10,padx=10)
