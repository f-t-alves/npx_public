
import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)

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



class FloatInputBoxes(tk.Frame):

    def __init__(self,InputNames,EntryNumbers,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = EntryNumbers
        self.entries = []

        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl1 = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl1):

            self.text = tk.Label(self,text = self.List[i],font=SMALL_FONT)

            self.text.grid(row=i, column = 0, sticky = 'E',padx=10,pady=2)
            self.text.grid_columnconfigure(1,weight=1)

        for i in range(self.ctrl1):

            self.entr = tk.Entry(self,bg='azure')
            self.entr.grid(row=i, column = 1,padx=10,pady=2,sticky='e')
            self.entries.append(self.entr)



class IntInputBoxes(tk.Frame):

    def __init__(self,InputNames,EntryNumbers,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = EntryNumbers
        self.entries = []

        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl1 = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl1):

            self.text = tk.Label(self,text = self.List[i],font=SMALL_FONT)

            self.text.grid(row=i, column = 0, sticky = 'E',padx=10,pady=2)
            self.text.grid_columnconfigure(1,weight=1)

        for i in range(self.ctrl1):

            self.entr = tk.Entry(self,bg='azure')
            self.entr.grid(row=i, column = 1,padx=10,pady=2,sticky='e')
            self.entries.append(self.entr)


class StrInputBoxes(tk.Frame):

    def __init__(self,InputNames,EntryNumbers,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = EntryNumbers
        self.entries = []

        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl1 = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl1):

            self.text = tk.Label(self,text = self.List[i],font=SMALL_FONT)

            self.text.grid(row=i, column = 0, sticky = 'E',padx=10,pady=2)
            self.text.grid_columnconfigure(1,weight=1)

        for i in range(self.ctrl1):

            self.entr = tk.Entry(self,bg='azure')
            self.entr.grid(row=i, column = 1,padx=10,pady=2,sticky='e')
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

        tk.Frame.grid_rowconfigure(self,1, weight=0)
        tk.Frame.grid_rowconfigure(self,2, weight=0)
        tk.Frame.grid_columnconfigure(self,1, weight=2)
        tk.Frame.grid_columnconfigure(self,2, weight=3)
        tk.Frame.grid_columnconfigure(self,3, weight=5)

        label = tk.Label(self, text='Products 1', font = LARGE_FONT)
        label.grid(column=1, columnspan = 3,pady=10,padx=10,sticky='n')

        Product = ['ProdName','PrinAtivo','Description','TeraClassID','ProdType']
        Product2 = ['RestHosp','CAP','CONFAZ87','AnalRecur','ListaTribID',
        'Comerc2016','Tarja']
        Product3 = ['EAN','LabID','CodGGREM','Registro']

        a = StrInputBoxes(Product,4,self)
        b = IntInputBoxes(Product2,7,self)
        c = IntInputBoxes(Product3,4,self)

        a.grid(row=1,column=1,sticky='w')
        b.grid(row=1,column=2,rowspan=2,sticky='w')
        c.grid(row=2,column=1,sticky='w')
        c.grid_rowconfigure(1, weight=4)
        c.grid_rowconfigure(2, weight=1)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4,column=1,columnspan = 2, ipadx = 2)
        button2 = ttk.Button(self, text="MedPage1",command=lambda: controller.show_frame(MedPage1))
        button2.grid(row=3,column=1,columnspan = 1,pady=10,sticky='e')
        button3 = ttk.Button(self, text="MedPage2",command=lambda: controller.show_frame(MedPage2))
        button3.grid(row=3,column=2,columnspan = 1,pady=10,sticky='w')
        button4 = ttk.Button(self, text="MedPage3",command=lambda: controller.show_frame(MedPage3))
        button4.grid(row=3,column=3,columnspan = 1,pady=10,sticky='w')

class MedPage2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        tk.Frame.grid_rowconfigure(self,2, weight=0)
        tk.Frame.grid_rowconfigure(self,3, weight=3)
        tk.Frame.grid_columnconfigure(self,0, weight=1)
        tk.Frame.grid_columnconfigure(self,1, weight=3)
        tk.Frame.grid_columnconfigure(self,2, weight=1)

        label = tk.Label(self, text='Products 2', font = LARGE_FONT)
        label.grid(row=0,column=0,columnspan=2,pady=10,padx=10,sticky='n')

        Product = ['PF0p','PF12p','PF17p','PF17p_ALC']
        Product2 = ['PF17p5','PF17p5_ALC','PF18p','PF18p_ALC']
        Product3 = ['PF20p']

        a = FloatInputBoxes(Product,4,self)
        b = FloatInputBoxes(Product2,4,self)
        c = FloatInputBoxes(Product3,1,self)
        a.grid(row=1,column=0,columnspan=1,sticky='e',padx=10)
        b.grid(row=1,column=1,columnspan=1,sticky='w')
        c.grid(row=2,column=0,columnspan=2,sticky='n',pady=10)


        button1 = ttk.Button(self, text="MedPage1",command=lambda: controller.show_frame(MedPage1))
        button1.grid(row=3,column=0,columnspan = 1,pady=10,sticky='e')
        button2 = ttk.Button(self, text="MedPage2",command=lambda: controller.show_frame(MedPage2))
        button2.grid(row=3,column=1,columnspan = 1,pady=10,sticky='w')
        button3 = ttk.Button(self, text="MedPage3",command=lambda: controller.show_frame(MedPage3))
        button3.grid(row=3,column=2,columnspan =1,pady=10,sticky='w')
        button3.grid_columnconfigure(3, weight=1)
        button3.grid_columnconfigure(2, weight=5)

class MedPage3(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        tk.Frame.grid_rowconfigure(self,2, weight=0)
        tk.Frame.grid_rowconfigure(self,3, weight=3)
        tk.Frame.grid_columnconfigure(self,0, weight=1)
        tk.Frame.grid_columnconfigure(self,1, weight=3)
        tk.Frame.grid_columnconfigure(self,2, weight=3)


        label = tk.Label(self, text='Products 3', font = LARGE_FONT)
        label.grid(row=0,column=0,columnspan=2,pady=10,padx=10,sticky='n')

        Product = ['PMC0p','PMC12p','PMC17p','PMC17p_ALC']
        Product2 = ['PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC']
        Product3 = ['PMC20p']

        a = FloatInputBoxes(Product,4,self)
        b = FloatInputBoxes(Product2,4,self)
        c = FloatInputBoxes(Product3,1,self)
        a.grid(row=1,column=0,columnspan=1,sticky='e',padx=10)
        b.grid(row=1,column=1,columnspan=1,sticky='w')
        c.grid(row=2,column=0,columnspan=2,sticky='n',pady=10)



        button1 = ttk.Button(self, text="MedPage1",command=lambda: controller.show_frame(MedPage1))
        button1.grid(row=3,column=0,columnspan = 1,pady=10,sticky='e')
        button2 = ttk.Button(self, text="MedPage2",command=lambda: controller.show_frame(MedPage2))
        button2.grid(row=3,column=1,columnspan = 1,pady=10,sticky='w')
        button3 = ttk.Button(self, text="MedPage3",command=lambda: controller.show_frame(MedPage3))
        button3.grid(row=3,column=2,columnspan = 1,pady=10,sticky='w')


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text='Laboratories', font = LARGE_FONT)
        label.pack()


        LabName =['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
        'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2',
        'LabContactFax']
        a = StrInputBoxes(LabName,8,self)
        a.pack()


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
        a = StrInputBoxes(ProviderComp,8,self)
        a.pack()

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack()



app = MainApp()
app.geometry("500x350")
app.resizable(width=True, height=True)
app.mainloop()













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
