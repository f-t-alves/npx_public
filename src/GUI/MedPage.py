
import tkinter as tk
from tkinter import ttk
from src.GUI import InputClasses as InpCla
from src.GUI import StartPage as StP
# import MainApp as MP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)




class MedPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=300,height=300)
        tk.Frame.grid(self,row=0,column=0)

        n = ttk.Notebook(self)
        n.grid()
        f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
        f1.grid()
        f2 = ttk.Frame(n)   # second page
        f2.grid()
        f3 = ttk.Frame(n)   # second page
        f3.grid()
        n.add(f1, text='One')
        n.add(f2, text='Two')
        n.add(f3, text='Three')
        label1 =tk.Label(f1,text=' ')
        label1.grid(row=0,column=2,sticky = 'nwse')
        label2 =tk.Label(f2,text=' ')
        label2.grid(row=0,column=2,sticky = 'nwse')
        label3 =tk.Label(f3,text=' ')
        label3.grid(row=0,column=2,sticky = 'nwse')

        Product = ['PMC0p','PMC12p','PMC17p','PMC17p_ALC']
        Product2 = ['PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC']
        Product3 = ['PMC20p']


        a = InpCla.InputBoxes(Product,1,4,f1)
        b = InpCla.InputBoxes(Product2,1,4,f1)
        c = InpCla.InputBoxes(Product3,1,1,f1)
        a.grid(row=1,column=0,columnspan=1,sticky='e')
        b.grid(row=1,column=1,columnspan=1,sticky='w')
        c.grid(row=2,column=0,columnspan=1,sticky='e')


        Product4 = ['PF0p','PF12p','PF17p','PF17p_ALC']
        Product5 = ['PF17p5','PF17p5_ALC','PF18p','PF18p_ALC']
        Product6 = ['PF20p']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        d = InpCla.InputBoxes(Product4,1,4,f2)
        e = InpCla.InputBoxes(Product5,1,4,f2)
        f = InpCla.InputBoxes(Product6,1,1,f2)
        d.grid(row=1,column=0,columnspan=1,sticky='e',padx=0)
        e.grid(row=1,column=1,columnspan=1,sticky='w',padx=0)
        f.grid(row=2,column=0,columnspan=1,sticky='e',padx=0)

        Product7 = ['ProdName','PrinAtivo','Description','TeraClassID','ProdType']
        Product8 = ['RestHosp','CAP','CONFAZ87','AnalRecur','ListaTribID',
        'Comerc2016','Tarja']
        Product9 = ['EAN','LabID','CodGGREM','Registro']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        g = InpCla.InputBoxes(Product7,3,4,f3)
        h = InpCla.InputBoxes(Product8,2,7,f3)
        i = InpCla.InputBoxes(Product9,2,4,f3)

        g.grid(row=1,column=1,sticky='w')
        h.grid(row=1,column=2,rowspan=2,sticky='w')
        i.grid(row=2,column=1,sticky='w')
        c.grid_rowconfigure(1, weight=4)



        b1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        b1.grid(row=2,column=0,sticky = 'nw')
        b2 = ttk.Button(self, text = 'Submit',command =lambda: InpCla.submMedToT(a.entries,b.entries,c.entries,d.entries,e.entries,f.entries,g.entries,h.entries,i.entries),width = 30)
        b2.grid(row=2,column=0,sticky = 'ne')
        # b3 = ttk.Button(self, text = '3',command =lambda: raise_1(self,Frame3))
        # b3.grid(row=2,column=0,sticky = 'nw')
