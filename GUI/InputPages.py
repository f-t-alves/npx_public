
import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

def popupmsg(msg):
    popup =tk.Tk()



    popup.wm_title('NPX')
    label = ttk.Label(popup, text =msg, font=NORM_FONT,anchor='center')
    label.pack(side='top', fill='x', pady=10,anchor='center')
    B1 = ttk.Button(popup, text='Ok',command=popup.destroy)
    B1.pack()
    popup.geometry("200x80")
    popup.resizable(width=False, height=False)
    popup.mainloop()

class StrInputBoxes(tk.Frame):

    def __init__(self,InputNames,EntryNumbers,ColumnNumber,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = EntryNumbers
        self.ColumnNumber = ColumnNumber
        self.entries = []

        self.create_entry_widgets(self.EntryNumbers,self.ColumnNumber,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,ColumnNumber,InputNames,entries):

        self.ctrl1 = int(EntryNumbers)
        self.ctrl2 = int(ColumnNumber)
        self.List = InputNames

        for i in range(self.ctrl1):

            self.text = tk.Label(self,text = self.List[i],)

            self.text.grid(row=i, column = self.ctrl2, sticky = 'E',pady=2)
            self.text.grid_columnconfigure(1,weight=1)

        for i in range(self.ctrl1):

            self.entr = tk.Entry(self,bg='azure')
            self.entr.grid(row=i, column = self.ctrl2+1, sticky = 'E',pady=2)
            self.entries.append(self.entr)



class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self,'New Pharma eXperience')
        tk.Tk.iconbitmap(self, default='clinic.ico')

        master = tk.Frame(self)
        master.pack(expand=1)

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save Settings", command = lambda:popupmsg('Not Suppoerted Yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = quit)
        menubar.add_cascade(label='File', menu=filemenu)


        # button = ttk.Button(self, text="Med Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(PageOne))
        # button.pack(ipady=10,fill ='x')



        tk.Tk.config(self,menu=menubar)

        self.frames = {}

        for F in(StartPage,MedPage1,MedPage2,MedPage3,PageTwo,PageThree):

            frame = F(master, self)

            self.frames[F] = frame

            frame.grid(row=5,column=5,columnspan=10,rowspan=10,sticky='NSEW')
            frame.grid_rowconfigure(0,weight=1)
            frame.grid_columnconfigure(0,weight=1)
            a= frame.grid_size()
            b=frame.grid_location(6,4)
            print(a,b)

        self.show_frame(StartPage)

    def show_frame(self, ctrl):

        frame = self.frames[ctrl]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        tk.Frame.pack(self,fill='both')
        label = tk.Label(self, text='Welcome to Input Window', font = LARGE_FONT)
        label.pack(pady=10,padx=10,fill='both')

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)

        button = ttk.Button(self, text="Med Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(MedPage1))
        button.pack(ipady=10,fill ='x')
        button2 = ttk.Button(self, text="Lab Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(PageTwo))
        button2.pack(ipady=10,fill ='x')
        button3 = ttk.Button(self, text="Provider Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(PageThree))
        button3.pack(ipady=10,fill ='x')


class MedPage1(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        label = tk.Label(self, text='Products 1', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        Product = ['ProdName','PrinAtivo','Description','TeraClassID','ProdType']
        Product2 = ['PF0p','PF12p','PF17p','PF17p_ALC',
        'PF17p5','PF17p5_ALC','PF18p','PF18p_ALC','PF20p','PMC0p','PMC12p','PMC17p',
        'PMC17p_ALC','PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC','PMC20p']
        Product3 =['RestHosp','CAP','CONFAZ87','AnalRecur','ListaTribID',
        'Comerc2016','Tarja']

        a = StrInputBoxes(Product,1,1,self)
        b = StrInputBoxes(Product2,2,1,self)

        a.pack()
        b.pack()
        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Next",command=lambda: controller.show_frame(MedPage2))
        button2.pack()

class MedPage2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        label = tk.Label(self, text='Products 2', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        Product = ['EAN','ProdName','LabID','PrinAtivo','CodGGREM','Registro',
        'Description','TeraClassID','ProdType']
        Product2 = ['PF0p','PF12p','PF17p','PF17p_ALC',
        'PF17p5','PF17p5_ALC','PF18p','PF18p_ALC','PF20p','PMC0p','PMC12p','PMC17p',
        'PMC17p_ALC','PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC','PMC20p']
        Product3 =['RestHosp','CAP','CONFAZ87','AnalRecur','ListaTribID',
        'Comerc2016','Tarja']

        button1 = ttk.Button(self, text="Next",command=lambda: controller.show_frame(MedPage3))
        button1.pack()

class MedPage3(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        label = tk.Label(self, text='Products 3', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        Product = ['EAN','ProdName','LabID','PrinAtivo','CodGGREM','Registro',
        'Description','TeraClassID','ProdType']
        Product2 = ['PF0p','PF12p','PF17p','PF17p_ALC',
        'PF17p5','PF17p5_ALC','PF18p','PF18p_ALC','PF20p','PMC0p','PMC12p','PMC17p',
        'PMC17p_ALC','PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC','PMC20p']
        Product3 =['RestHosp','CAP','CONFAZ87','AnalRecur','ListaTribID',
        'Comerc2016','Tarja']




        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text='Laboratories', font = LARGE_FONT)
        label.pack()


        LabName =['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
        'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2',
        'LabContactFax']


        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Provider Company', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        ProviderComp = ['ProvCompName','ProvCompCNPJ','ProvOfficeAddress',
        'ProvContactEmail1','ProvContactEmail2','ProvContactPhone1','ProvContactPhone2',
        'ProvContactFax']


        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()



app = MainApp()
app.geometry("500x350")
app.resizable(width=True, height=True)
app.mainloop()








class IntInputBoxes(tk.Frame):

    def __init__(self,InputNames,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = len(self.InputNames)
        self.entries = []

        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl):

            self.text = tk.Label(self,text = self.List[i],)

            self.text.grid(row=i, column = 1, sticky = 'E',pady=2)
            self.text.grid_columnconfigure(1,weight=1)

        for i in range(self.ctrl):

            self.entr = tk.Entry(self,bg='azure',textvariable = tk.IntVar())
            self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
            self.entries.append(self.entr)




class FloatInputBoxes(tk.Frame):

    def __init__(self,InputNames,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = len(self.InputNames)
        self.entries = []

        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl):

            self.text = tk.Label(self,text = self.List[i],)

            self.text.grid(row=i, column = 1, sticky = 'E',pady=2)
            self.text.grid_columnconfigure(1,weight=1)

        for i in range(self.ctrl):

            self.entr = tk.Entry(self,bg='azure',textvariable = tk.DoubleVar())
            self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
            self.entries.append(self.entr)



class submit(StrInputBoxes,IntInputBoxes,FloatInputBoxes):

        self.SubmitButton = ttk.Button(self,text='Submit',command = self.submit,
         width = 30)
        self.SubmitButton.grid(row=self.ctrl+3,column=1, columnspan = 3,pady=10,padx=10)

        self.Content =[]

        for self.entry in self.entries:
            self.Content.append(self.entry.get())

        print(self.Content)

        for i in range(self.ctrl):
            self.entr = tk.Entry(self,bg='azure')
            #self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
            self.entr.delete(0, 'end')

        (self.Content)
