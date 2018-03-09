
import tkinter as tk
from tkinter import ttk
import InputClasses as InpCla
import StartPage as StP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)



class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text='Laboratories', font = LARGE_FONT)
        label.pack()


        LabName =['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
        'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2',
        'LabContactFax']
        a = InpCla.StrInputBoxes(LabName,8,self)
        a.pack()




        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        button1.pack()

        SubmitButton = ttk.Button(self,text='Submit',command=lambda:InpCla.submLab(a.entries),
         width = 30)
        SubmitButton.pack()
