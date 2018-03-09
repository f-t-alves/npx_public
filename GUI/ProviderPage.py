
import tkinter as tk
from tkinter import ttk
import InputClasses as InpCla
import StartPage as StP


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)





class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=300,height=300)
        label = tk.Label(self, text='Provider Company', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        ProviderComp = ['ProvCompName','ProvCompCNPJ','ProvOfficeAddress',
        'ProvContactEmail1','ProvContactEmail2','ProvContactPhone1','ProvContactPhone2',
        'ProvContactFax']
        a = InpCla.StrInputBoxes(ProviderComp,8,self)
        a.pack()

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button1.pack()
