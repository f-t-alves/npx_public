import tkinter as tk
from tkinter import ttk
from src.GUI import InputClasses as InpCla
from src.GUI import StartPage as StP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)



class LabPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text='Laboratories', font = LARGE_FONT)
        label.pack()


        LabName =['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
        'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2',
        'LabContactFax']

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3
        a = InpCla.InputBoxes(LabName,3,8,self)
        a.pack()




        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button1.pack()

        SubmitButton = ttk.Button(self,text='Submit',command=lambda:InpCla.submLab(a.entries),
         width = 30)
        SubmitButton.pack()
