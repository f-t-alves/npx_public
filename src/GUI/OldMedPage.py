
import tkinter as tk
from tkinter import ttk
from src.GUI import InputClasses as InpCla
from src.GUI import StartPage as StP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)



class MedPage1(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=300,height=300)

        tk.Frame.grid_rowconfigure(self,1, weight=0)
        tk.Frame.grid_rowconfigure(self,2, weight=0)
        tk.Frame.grid_columnconfigure(self,1, weight=2)
        tk.Frame.grid_columnconfigure(self,2, weight=3)
        tk.Frame.grid_columnconfigure(self,3, weight=5)
        #tk.Frame.grid_propagate(False)


        label = tk.Label(self, text='Products 1', font = LARGE_FONT)
        label.grid(column=1, columnspan = 3,pady=10,padx=10,sticky='n')

        Product = ['ProdName','PrinAtivo','Description','TeraClassID','ProdType']
        Product2 = ['RestHosp','CAP','CONFAZ87','AnalRecur','ListaTribID',
        'Comerc2016','Tarja']
        Product3 = ['EAN','LabID','CodGGREM','Registro']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        a = InpCla.InputBoxes(Product,3,4,self)
        b = InpCla.InputBoxes(Product2,2,7,self)
        c = InpCla.InputBoxes(Product3,2,4,self)

        a.grid(row=1,column=1,sticky='w')
        b.grid(row=1,column=2,rowspan=2,sticky='w')
        c.grid(row=1,column=3,sticky='w')
        c.grid_rowconfigure(1, weight=4)
        c.grid_rowconfigure(2, weight=1)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button1.grid(row=4,column=2,columnspan = 1,sticky = 'nwse')
        button2 = ttk.Button(self, text="MedPage1",command=lambda: controller.show_frame(MedPage1))
        button2.grid(row=3,column=2,columnspan = 1,pady=1,sticky='w')
        button3 = ttk.Button(self, text="MedPage2",command=lambda: controller.show_frame(MedPage2))
        button3.grid(row=3,column=2,columnspan = 1,pady=1)
        button4 = ttk.Button(self, text="MedPage3",command=lambda: controller.show_frame(MedPage3))
        button4.grid(row=3,column=2,columnspan = 1,pady=1,sticky='e')

class MedPage2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=300,height=300)

        tk.Frame.grid_rowconfigure(self,2, weight=0)
        tk.Frame.grid_rowconfigure(self,1, weight=0)
        tk.Frame.grid_columnconfigure(self,0, weight=0)
        tk.Frame.grid_columnconfigure(self,1, weight=0)
        tk.Frame.grid_columnconfigure(self,2, weight=0)
        #tk.Frame.grid_propagate(False)


        label = tk.Label(self, text='Products 2', font = LARGE_FONT)
        label.grid(row=0,column=0,columnspan=2,pady=1,padx=1,sticky='n')


        Product = ['PF0p','PF12p','PF17p','PF17p_ALC']
        Product2 = ['PF17p5','PF17p5_ALC','PF18p','PF18p_ALC']
        Product3 = ['PF20p']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        a = InpCla.InputBoxes(Product,1,4,self)
        b = InpCla.InputBoxes(Product2,1,4,self)
        c = InpCla.InputBoxes(Product3,1,1,self)
        a.grid(row=1,column=0,columnspan=1,sticky='e',padx=0)
        b.grid(row=1,column=1,columnspan=1,sticky='w')
        c.grid(row=2,column=0,columnspan=1,sticky='e',pady=1)

        print(a.entries)

        button1 = ttk.Button(self, text="MedPage1",command=lambda: controller.show_frame(MedPage1))
        button1.grid(row=3,column=0,columnspan = 1,pady=1,sticky='w')
        button2 = ttk.Button(self, text="MedPage2",command=lambda: controller.show_frame(MedPage2))
        button2.grid(row=3,column=0,columnspan = 1,pady=1)
        button3 = ttk.Button(self, text="MedPage3",command=lambda: controller.show_frame(MedPage3))
        button3.grid(row=3,column=0,columnspan =1,pady=1,sticky='e')
        button4 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button4.grid(row=4,column=0,columnspan = 1,sticky = 'nwse')

class MedPage3(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=700,height=700)

        tk.Frame.grid_rowconfigure(self,2, weight=0)
        tk.Frame.grid_rowconfigure(self,3, weight=0)
        tk.Frame.grid_columnconfigure(self,0, weight=0)
        tk.Frame.grid_columnconfigure(self,1, weight=0)
        tk.Frame.grid_columnconfigure(self,2, weight=0)



        label = tk.Label(self, text='Products 3', font = LARGE_FONT)
        label.grid(row=0,column=0,columnspan=2,pady=1,padx=1,sticky='n')

        Product = ['PMC0p','PMC12p','PMC17p','PMC17p_ALC']
        Product2 = ['PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC']
        Product3 = ['PMC20p']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        a = InpCla.InputBoxes(Product,1,4,self)
        b = InpCla.InputBoxes(Product2,1,4,self)
        c = InpCla.InputBoxes(Product3,1,1,self)
        a.grid(row=1,column=0,columnspan=1,sticky='e')
        b.grid(row=1,column=1,columnspan=1,sticky='w')
        c.grid(row=2,column=0,columnspan=1,sticky='e',pady=0)
        a.grid_propagate(True)
        b.grid_propagate(True)
        c.grid_propagate(True)



        button1 = ttk.Button(self, text="MedPage1",command=lambda: controller.show_frame(MedPage1))
        button1.grid(row=3,column=0,columnspan = 1,pady=1,sticky='w')
        button2 = ttk.Button(self, text="MedPage2",command=lambda: controller.show_frame(MedPage2))
        button2.grid(row=3,column=0,columnspan = 1,pady=1)
        button3 = ttk.Button(self, text="MedPage3",command=lambda: controller.show_frame(MedPage3))
        button3.grid(row=3,column=0,columnspan = 1,pady=1,sticky='e')
        button4 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button4.grid(row=4,column=0,columnspan = 1,sticky = 'nwse')
        # SubmitButton = ttk.Button(self,text='Submit',command=lambda:
        # InpCla.submMedToT(MedPage1.a.entries,MedPage1.b.entries,
        # MedPage1.c.entries,MedPage2.a.entries,MedPage2.b.entries,MedPage2.c.entries,
        # a.entries,b.entries,c.entries,),width = 30)
        # SubmitButton.grid(row=5,column=0)
