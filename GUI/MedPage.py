
import tkinter as tk
from tkinter import ttk
import InputClasses as InpCla
# import MainApp as MaP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)



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

        a = InpCla.StrInputBoxes(Product,4,self)
        b = InpCla.IntInputBoxes(Product2,7,self)
        c = InpCla.IntInputBoxes(Product3,4,self)

        a.grid(row=1,column=1,sticky='w')
        b.grid(row=1,column=2,rowspan=2,sticky='w')
        c.grid(row=2,column=1,sticky='w')
        c.grid_rowconfigure(1, weight=4)
        c.grid_rowconfigure(2, weight=1)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(MaP.StartPage))
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

        a = InpCla.FloatInputBoxes(Product,4,self)
        b = InpCla.FloatInputBoxes(Product2,4,self)
        c = InpCla.FloatInputBoxes(Product3,1,self)
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

        a = InpCla.FloatInputBoxes(Product,4,self)
        b = InpCla.FloatInputBoxes(Product2,4,self)
        c = InpCla.FloatInputBoxes(Product3,1,self)
        a.grid(row=1,column=0,columnspan=1,sticky='e',padx=10)
        b.grid(row=1,column=1,columnspan=1,sticky='w')
        c.grid(row=2,column=0,columnspan=2,sticky='n',pady=10)



        button1 = ttk.Button(self, text="MedPage1",command=lambda: controller.show_frame(MedPage1))
        button1.grid(row=3,column=0,columnspan = 1,pady=10,sticky='e')
        button2 = ttk.Button(self, text="MedPage2",command=lambda: controller.show_frame(MedPage2))
        button2.grid(row=3,column=1,columnspan = 1,pady=10,sticky='w')
        button3 = ttk.Button(self, text="MedPage3",command=lambda: controller.show_frame(MedPage3))
        button3.grid(row=3,column=2,columnspan = 1,pady=10,sticky='w')
