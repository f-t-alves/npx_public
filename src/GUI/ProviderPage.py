
import tkinter as tk
from tkinter import ttk
from src.GUI import InputClasses as InpCla
from src.GUI import StartPage as StP


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)





class ProviderPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        PageFrame = ttk.Frame(self,width= 340, height=123)
        PageFrame.grid(row=0,padx=220)

        label = tk.Label(PageFrame, text='Provider Company', font = LARGE_FONT)
        label.grid(row=0)

        note = ttk.Notebook(PageFrame,width= 340, height=123)
        note.grid(row=1,sticky='nesw')
        f1 = ttk.Frame(note)   # first page, which would get widgets gridded into it
        f1.grid()
        f2 = ttk.Frame(note)   # second page
        f2.grid()
        note.add(f1, text='Infos')
        note.add(f2, text='Contato')


        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        ProviderComp = ['ProvCompID','ProvCompName','ProvCompCNPJ','ProvOfficeAddress']
        ProviderComp2 = ['ProvContactEmail1','ProvContactEmail2',
        'ProvContactPhone1','ProvContactPhone2','ProvContactFax']

        infos = InpCla.InputBoxes(ProviderComp,3,4,f1)
        infos.grid(pady=15)
        contatos = InpCla.InputBoxes(ProviderComp2,3,5,f2)
        contatos.grid(pady=5)

        button1 = ttk.Button(PageFrame, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button1.grid(row=2,sticky='w')


        SubmitButton = ttk.Button(PageFrame,text='Submit',command=lambda:InpCla.submProv(infos.entries,contatos.entries),
         width = 30)
        SubmitButton.grid(row=2,column=0,sticky='e')
