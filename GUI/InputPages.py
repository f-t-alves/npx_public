
import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

# root=Tk()
# root.title('New Pharma eXperience')
# root.iconbitmap('clinic.ico')
# root.geometry("356x270")
# root.resizable(width=False, height=True)

def popupmsg(msg):
    popup =tk.Tk()



    popup.wm_title('!')
    label = ttk.Label(popup, text =msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Ok',command=popup.destroy)
    B1.pack()
    popup.mainloop()




class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self,'New Pharma eXperience')
        tk.Tk.iconbitmap(self, default='clinic.ico')

        master = tk.Frame(self)
        master.grid_rowconfigure(0,weight=1)
        master.grid_columnconfigure(0,weight=1)
        master.grid()

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save Settings", command = lambda:popupmsg('Not Suppoerted Yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = quit)
        menubar.add_cascade(label='File', menu=filemenu)



        tk.Tk.config(self,menu=menubar)

        self.frames = {}

        for F in(StartPage,PageOne,PageTwo,PageThree):

            frame = F(master, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky='NSEW')

        self.show_frame(StartPage)

    def show_frame(self, ctrl):

        frame = self.frames[ctrl]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Start Page', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Med Input",command=lambda: controller.show_frame(PageOne))
        button.pack(ipady=10,ipadx=5)
        button2 = ttk.Button(self, text="Lab Input",command=lambda: controller.show_frame(PageTwo))
        button2.pack(ipady=10,ipadx=5)
        button3 = ttk.Button(self, text="Provider Input",command=lambda: controller.show_frame(PageThree))
        button3.pack(ipady=10,ipadx=2)


class InputBoxes(tk.Frame):

    def __init__(self,InputNames,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = len(self.InputNames)
        self.entries = []
        # self.parent = parent



        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries,)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl):

            self.text = tk.Label(self,text = self.List[i],)

            self.text.grid(row=i, column = 1, sticky = 'W',pady=2)

        for i in range(self.ctrl):
            self.entr = tk.Entry(self,bg='azure')
            self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
            self.entries.append(self.entr)

        self.SubmitButton = ttk.Button(self,text='Submit',command = self.submit,
         width = 30)

        self.SubmitButton.grid(row=self.ctrl+3,column=1, columnspan = 3,pady=10,padx=10)

    def submit(self):
        self.Content =[]
        for self.entry in self.entries:
            self.Content.append(self.entry.get())

        return(self.Content)

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Page One', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        Product = ['EAN','ProdName','LabID','PrinAtivo','CodGGREM','Registro',
        'Description','TeraClassID','ProdType','PF0p','PF12p','PF17p','PF17p_ALC',
        'PF17p5','PF17p5_ALC','PF18p','PF18p_ALC','PF20p','PMC0p','PMC12p','PMC17p',
        'PMC17p_ALC','PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC','PMC20p','RestHosp',
        'CAP','CONFAZ87','AnalRecur','ListaTribID','Comerc2016','Tarja']

        Med = InputBoxes(Product,self)
        Med.grid(row=1,column=0)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0,column=3)
        button2 = ttk.Button(self, text="To Page 2",command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=0,column=4)


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text='Laboratories', font = LARGE_FONT)
        label.grid(row=1,pady=10,padx=10)

        LabName =['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
        'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2',
        'LabContactFax']

        Lab = InputBoxes(LabName,self)
        Lab.grid(row=2)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0,column=0,sticky='NWSE')
        button2 = ttk.Button(self, text="Med",command=lambda: controller.show_frame(PageOne))
        button2.grid(row=0,column=1,sticky='NWSE',ipadx=30)

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Provider Company', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        ProviderComp = ['ProvCompName','ProvCompCNPJ','ProvOfficeAddress',
        'ProvContactEmail1','ProvContactEmail2','ProvContactPhone1','ProvContactPhone2',
        'ProvContactFax']

        Provider = InputBoxes(ProviderComp,self)
        Provider.grid()

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0,column=3)



app = MainApp()
app.geometry("1240x720")
app.mainloop()


# TopMenu = Menu(MainWindow)
# toolbar = Frame(MainWindow, bg='sky blue2')
# toolbar.grid(columnspan=5)
# toolbarButton1 = Button(toolbar, text='Laboratories',
#  command= lambda:InputBoxes(Lab,MainFrame))
# toolbarButton1.grid(row=0,column=1)
# toolbarButton1 = Button(toolbar, text='Provider Company',
#  command=lambda:InputBoxes(Provider,MainFrame))
# toolbarButton1.grid(row=0,column=2)
# toolbarButton1 = Button(toolbar, text='Med Product',
#  command=lambda:InputBoxes(Product,MainFrame))
# toolbarButton1.grid(row=0,column=3)
# toolbarButton1 = Button(toolbar, text='PLACEHOLDER')
# toolbarButton1.grid(row=0)
#
# MainWindow.config(menu=TopMenu)
#
# File = Menu(TopMenu)
# Edit = Menu(TopMenu)
# View = Menu(TopMenu)
# PLACEHOLDER = Menu(TopMenu)
# TopMenu.add_cascade(label='File', menu=File)
# TopMenu.add_cascade(label='Edit', menu=Edit)
# TopMenu.add_cascade(label='View', menu=View)
# TopMenu.add_cascade(label='PLACEHOLDER', menu=PLACEHOLDER)
# File.add_command(label='BlaBla', command=quit)
# File.add_separator()
# File.add_command(label='LoL')




# class InputBoxes:
#
#     def __init__(self,InputNames):
#
#         self.InputNames = InputNames
#         self.EntryNumbers = len(InputNames)
#         self.entries = []
#         self.master = Window
#
#
#
#         self.create_entry_widgets(self.EntryNumbers,self.InputNames,
#         self.entries)
#
#     def create_entry_widgets(self,EntryNumbers,InputNames,entries):
#
#         self.ctrl = int(EntryNumbers)
#         self.List = InputNames
#
#
#         for i in range(self.ctrl):
#
#             self.text = Label(text = self.List[i],bg='sky blue')
#
#             self.text.master.grid(row=2+i, column = 1, sticky = W)
#
#         for i in range(self.ctrl):
#             self.entr = Entry(bg='azure')
#             self.entr.master.grid(row=2+i, column = 2, sticky = W)
#             self.entries.append(self.entr)
#
#         self.SubmitButton = Button(text='Submit',command = self.submit,
#          width = 30)
#
#         self.SubmitButton.master.grid(row=self.ctrl+3,column=1, columnspan = 3)
#
#     def submit(self):
#         self.Content =[]
#         for self.entry in self.entries:
#             self.Content.append(self.entry.get())
#         self.clear()
#         return(self.Content)



LabName = ['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2', 'LabContactFax']
Product = ['EAN','ProdName','LabID','PrinAtivo','CodGGREM','Registro',
'Description','TeraClassID','ProdType','PF0p','PF12p','PF17p','PF17p_ALC',
'PF17p5','PF17p5_ALC','PF18p','PF18p_ALC','PF20p','PMC0p','PMC12p','PMC17p',
'PMC17p_ALC','PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC','PMC20p','RestHosp',
'CAP','CONFAZ87','AnalRecur','ListaTribID','Comerc2016','Tarja']
ProviderComp = ['ProvCompName','ProvCompCNPJ','ProvOfficeAddress',
'ProvContactEmail1','ProvContactEmail2','ProvContactPhone1','ProvContactPhone2',
'ProvContactFax']

# toolbar = Toolbar(root)
# root.mainloop()
# print('', me.Content)
