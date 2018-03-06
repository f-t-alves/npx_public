from tkinter import *
import tkinter.messagebox


MainWindow = Tk()
MainWindow.geometry("356x270")
MainWindow.title('New Pharma eXperience')
MainWindow.resizable(width=False, height=True)
MainWindow.config(bg='sky blue')
MainWindow.iconbitmap('clinic.ico')
TopMenu = Menu(MainWindow)
toolbar = Frame(MainWindow, bg='sky blue2')
toolbar.grid(columnspan=5)
toolbarButton1 = Button(toolbar, text='Laboratories',
 command= lambda:InputBoxes(Lab))
toolbarButton1.grid(row=0,column=1)
toolbarButton1 = Button(toolbar, text='Provider Company',
 command=lambda:InputBoxes(Provider))
toolbarButton1.grid(row=0,column=2)
toolbarButton1 = Button(toolbar, text='Med Product',
 command=lambda:InputBoxes(Product))
toolbarButton1.grid(row=0,column=3)
toolbarButton1 = Button(toolbar, text='PLACEHOLDER')
toolbarButton1.grid(row=0)

MainWindow.config(menu=TopMenu)

File = Menu(TopMenu)
Edit = Menu(TopMenu)
View = Menu(TopMenu)
PLACEHOLDER = Menu(TopMenu)
TopMenu.add_cascade(label='File', menu=File)
TopMenu.add_cascade(label='Edit', menu=Edit)
TopMenu.add_cascade(label='View', menu=View)
TopMenu.add_cascade(label='PLACEHOLDER', menu=PLACEHOLDER)
File.add_command(label='BlaBla', command=quit)
File.add_separator()
File.add_command(label='LoL')




class InputBoxes:

    def __init__(self,InputNames):

        self.InputNames = InputNames
        self.EntryNumbers = len(InputNames)
        self.entries = []
        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl):

            self.text = Label(text = self.List[i],bg='sky blue')

            self.text.grid(row=2+i, column = 1, sticky = W)

        for i in range(self.ctrl):
            self.entr = Entry(bg='azure')
            self.entr.grid(row=2+i, column = 2, sticky = W)
            self.entries.append(self.entr)

        self.SubmitButton = Button(text='Submit',command = self.submit,
         width = 30)
        self.SubmitButton.grid(row=self.ctrl+3,column=1, columnspan = 3)


    def submit(self):
        self.Content =[]
        for self.entry in self.entries:
            self.Content.append(self.entry.get())

        return(self.Content)



Lab = ['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2', 'LabContactFax']
Product = ['EAN','ProdName','LabID','PrinAtivo','CodGGREM','Registro',
'Description','TeraClassID','ProdType','PF0p','PF12p','PF17p','PF17p_ALC',
'PF17p5','PF17p5_ALC','PF18p','PF18p_ALC','PF20p','PMC0p','PMC12p','PMC17p',
'PMC17p_ALC','PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC','PMC20p','RestHosp',
'CAP','CONFAZ87','AnalRecur','ListaTribID','Comerc2016','Tarja']
Provider = ['ProvCompName','ProvCompCNPJ','ProvOfficeAddress',
'ProvContactEmail1','ProvContactEmail2','ProvContactPhone1','ProvContactPhone2',
'ProvContactFax']

MainWindow.mainloop()
# print('', me.Content)
