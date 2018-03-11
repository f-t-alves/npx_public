import tkinter as tk
from tkinter import ttk
from src.GUI import InputClasses as InpCla
from src.GUI import StartPage as StP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)



class LabPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        LabPageFrame = ttk.Frame(self,width= 940, height=123)
        LabPageFrame.grid(row=0,padx=220)

        label = ttk.Label(LabPageFrame, text='Laboratories', font = LARGE_FONT)
        label.grid(row=0)


        note = ttk.Notebook(LabPageFrame,width= 340, height=123)
        note.grid(row=1,sticky='nesw')
        f1 = ttk.Frame(note)   # first page, which would get widgets gridded into it
        f1.grid()
        f2 = ttk.Frame(note)   # second page
        f2.grid()
        note.add(f1, text='Infos')
        note.add(f2, text='Contato')


        LabName1 = ['LabID','LabName','LabCNPJ','LabOfficeAddress']
        LabName2 = ['LabContactEmail1','LabContactEmail2', 'LabContactPhone1',
         'LabContactPhone2','LabContactFax']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3
        infos = InpCla.InputBoxes(LabName1,3,4,f1)
        infos.grid(pady=15)
        contatos = InpCla.InputBoxes(LabName2,3,5,f2)
        contatos.grid(pady=5)




        button1 = ttk.Button(LabPageFrame, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button1.grid(row=2,sticky='w')

        SubmitButton = ttk.Button(LabPageFrame,text='Submit',command=lambda:InpCla.submLab(infos.entries,contatos.entries),
         width = 30)
        SubmitButton.grid(row=2,column=0,sticky='e')
