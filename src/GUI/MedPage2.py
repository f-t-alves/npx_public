
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
        tk.Frame.__init__(self,parent,width=300,height=500)

        # style=ttk.Style()
        # a = style.element_names()
        # print(a)

        PageFrame = ttk.Frame(self)
        PageFrame.grid(padx=35,pady=10)

        note = ttk.Notebook(PageFrame,width= 690, height=170)
        note.grid()
        f1 = ttk.Frame(note)   # first page, which would get widgets gridded into it
        f1.grid()
        f2 = ttk.Frame(note)   # second page
        f2.grid()
        f3 = ttk.Frame(note)   # second page
        f3.grid()
        note.add(f1, text='Infos')
        note.add(f2, text='PF')
        note.add(f3, text='PMC')
        label1 =tk.Label(f1,text=' ')
        label1.grid(row=0,column=2,sticky = 'nwse')
        label2 =tk.Label(f2,text=' ')
        label2.grid(row=0,column=2,sticky = 'nwse')
        label3 =tk.Label(f3,text=' ')
        label3.grid(row=0,column=2,sticky = 'nwse')
        lp = ttk.Button(f3)
        lp.grid()

        Product = ['PMC0p','PMC12p','PMC17p','PMC17p_ALC']
        Product2 = ['PMC17p5','PMC17p5_ALC','PMC18p','PMC18p_ALC']
        Product3 = ['PMC20p']


        a = InpCla.InputBoxes(Product,1,4,f3)
        b = InpCla.InputBoxes(Product2,1,4,f3)
        c = InpCla.InputBoxes(Product3,1,1,f3)
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
        d.grid(row=1,column=1,columnspan=1,sticky='e',padx=0)
        e.grid(row=1,column=2,columnspan=1,sticky='w',padx=0)
        f.grid(row=2,column=1,columnspan=1,sticky='ne',padx=0)

        listtrib = ttk.Combobox(f1)
        listtrib['values'] = ['Positiva', 'Neutra', 'Negativa']
        listtrib.grid(row=2,column=1,sticky='n',pady = 15)

        prodtype = ttk.Combobox(f1)
        prodtype['values'] = ['Biológico', 'Referência', 'Similar','Genérico']
        prodtype.grid(row=2,column=3,sticky='n',pady = 15)

        checkbox_frame = ttk.Frame(f1)
        checkbox_frame.grid(row=1, column=3,sticky='e')

        self.RestHosp = tk.IntVar()
        check1 = ttk.Checkbutton(checkbox_frame, text='RestHosp',variable = self.RestHosp, onvalue = 1, offvalue = 0 )
        check1.grid(row=0,column=3,sticky='w')
        self.CAP = tk.IntVar()
        check2 = ttk.Checkbutton(checkbox_frame, text='CAP',variable = self.CAP, onvalue = 1, offvalue = 0 )
        check2.grid(row=1,column=3,sticky='w')
        self.AnalRecur = tk.IntVar()
        check3 = ttk.Checkbutton(checkbox_frame, text='AnalRecur',variable = self.AnalRecur, onvalue = 1, offvalue = 0 )
        check3.grid(row=2,column=3,sticky='w')
        self.Comerc2016 = tk.IntVar()
        check4 = ttk.Checkbutton(checkbox_frame, text='Comerc2016',variable = self.Comerc2016, onvalue = 1, offvalue = 0 )
        check4.grid(row=3,column=3,sticky='w')
        f1.grid_rowconfigure(2,weight=1)
        f1.grid_columnconfigure(0, weight=0)

        Product7 = ['ProdName','PrinAtivo','Description','TeraClassID','ProdType']
        Product8 = ['CONFAZ87','Tarja']
        Product9 = ['EAN','LabID','CodGGREM','Registro']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        g = InpCla.InputBoxes(Product7,3,4,f1)
        h = InpCla.InputBoxes(Product8,2,2,f1)
        i = InpCla.InputBoxes(Product9,2,4,f1)

        g.grid(row=1,column=0,sticky='nw')
        h.grid(row=2,column=0,rowspan=2,sticky='nw')
        i.grid(row=1,column=1,sticky='nw')
        c.grid_rowconfigure(1, weight=4)



        b1 = ttk.Button(PageFrame, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        b1.grid(row=2,column=0,sticky = 'nw')
        b2 = ttk.Button(PageFrame, text = 'Submit',command =lambda: InpCla.submMedToT(a.entries,b.entries,c.entries,
        d.entries,e.entries,f.entries,g.entries,h.entries,i.entries,self.RestHosp,self.CAP,self.AnalRecur,self.Comerc2016,prodtype,listtrib),width = 30)
        b2.grid(row=2,column=0,sticky = 'ne')
        # b3 = ttk.Button(self, text = '3',command =lambda: raise_1(self,Frame3))
        # b3.grid(row=2,column=0,sticky = 'nw')


        # Popup para busca: LabID, PrinAtivo
