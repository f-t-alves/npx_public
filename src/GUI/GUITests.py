import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)

# root=Tk()
# root.title('New Pharma eXperience')
# root.iconbitmap('clinic.ico')
# root.geometry("356x270")
# root.resizable(width=False, height=True)


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default='clinic.ico')

        master = tk.Frame(self)
        master.grid_rowconfigure(0,weight=1)
        master.grid_columnconfigure(0,weight=1)
        master.grid()

        self.frames = {}

        for F in(StartPage,PageOne, PageTwo,PageThree):

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

        button = ttk.Button(self, text="Visit Page 1",command=lambda: controller.show_frame(PageOne))
        button.pack()
        button2 = ttk.Button(self, text="To Page 2",command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="To Graph Page",command=lambda: controller.show_frame(PageThree))
        button3.pack()

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Page One', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="To Page 2",command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Page Two', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page One",command=lambda: controller.show_frame(PageOne))
        button2.pack()

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Graph Page', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize)



app = MainApp()
app.mainloop()

# class Toolbar:
#
#     def __init__(self,MainWindow):
#
#         self.MainWindow = MainWindow
#         self.toolbar = Frame(self.MainWindow, relief=RAISED, bd=2, bg='sky blue2')
#         self.toolbar.pack(side=TOP, fill=X)
#         self.toolbarButton1 = Button(self.toolbar, text='Laboratories',anchor=E,
#          command= lambda:InputBoxes(Lab,MainFrame))
#         self.toolbarButton1.pack(side=LEFT,anchor=NW)
#         self.toolbarButton1 = Button(self.toolbar, text='Provider Company',
#          command=lambda:InputBoxes(Provider,MainFrame))
#         self.toolbarButton1.pack(side=RIGHT,anchor=NW)
#         self.toolbarButton1 = Button(self.toolbar, text='Med Product',
#          command=lambda:InputBoxes(Product,MainFrame))
#         self.toolbarButton1.pack(anchor=N)
#         self.toolbarButton1 = Button(self.toolbar, text='PLACEHOLDER')
#         self.toolbarButton1.pack(anchor=NE)
#


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




class InputBoxes:

    def __init__(self,InputNames,Window):

        self.InputNames = InputNames
        self.EntryNumbers = len(InputNames)
        self.entries = []
        self.master = Window

        # if int(self.grid_info()["row"]) > 0:


        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def clear(self,master):
        L = self.master.grid_slaves()
        for l in L:
            l.destroy()

    def create_entry_widgets(self,EntryNumbers,InputNames,entries,master):

        self.ctrl = int(EntryNumbers)
        self.List = InputNames

        # for i in range(self.ctrl):
        #
        #     if int(self.SubmitButton.grid_info()["row"]) > 0:
        #         self.SubmitButton.grid_remove()
        #     self.text = Label(text = self.List[i],bg='sky blue')
        #
        #     self.text.grid_forget()



        for i in range(self.ctrl):

            self.text = Label(text = self.List[i],bg='sky blue')

            self.text.master.grid(row=2+i, column = 1, sticky = W)

        for i in range(self.ctrl):
            self.entr = Entry(bg='azure')
            self.entr.master.grid(row=2+i, column = 2, sticky = W)
            self.entries.append(self.entr)

        self.SubmitButton = Button(text='Submit',command = self.submit,
         width = 30)

        self.SubmitButton.master.grid(row=self.ctrl+3,column=1, columnspan = 3)
        # print('',self.SubmitButton.grid_info())

    def submit(self):
        self.Content =[]
        for self.entry in self.entries:
            self.Content.append(self.entry.get())
        self.clear()
        return(self.Content)


#
# Lab = ['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
# 'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2', 'LabContactFax']
# Product = ['EAN','ProdName','LabID','PrinAtivo','CodGGREM','Registro',
# 'Description','TeraClassID','ProdType','PF0p','PF12p','PF17p','PF17p_ALC',
# 'PF17p5','PF17p5_ALC','PF18p','PF18p_ALC','PF20p','PMC0p','PMC12p','PMC17p',
# 'PMC17p_ALC','PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC','PMC20p','RestHosp',
# 'CAP','CONFAZ87','AnalRecur','ListaTribID','Comerc2016','Tarja']
# Provider = ['ProvCompName','ProvCompCNPJ','ProvOfficeAddress',
# 'ProvContactEmail1','ProvContactEmail2','ProvContactPhone1','ProvContactPhone2',
# 'ProvContactFax']

# toolbar = Toolbar(root)
# root.mainloop()
# print('', me.Content)
