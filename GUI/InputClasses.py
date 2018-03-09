
import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)




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


LabVarInput = []

def submLab(entries):
    global LabVarInput
    Content = []
    entries = entries

    for entry in entries:
        Content.append(entry.get())
    LabVarInput.append(Content)
    print(Content)

ProvVarInput = []

def submProv(entries):
    global ProvVarInput
    Content = []
    entries = entries

    for entry in entries:
        Content.append(entry.get())
    ProvVarInput.append(Content)
    print(Content)


class MedSubmit:

    def __init__(self):

    def submMed1(self,entries1,entries2,entries3):

        self.Content1 = []
        entries = entries1 + entries2 + entries3

        for entry in entries:
            Content1.append(entry.get())
        
        print(Content)

    def submMed2(self,entries):

        Content = []
        entries = entries

        for entry in entries:
            Content.append(entry.get())
        VarInput.append(Content)
        print(Content)

    def submMed3(self,entries):

        Content = []
        entries = entries

        for entry in entries:
            Content.append(entry.get())
        VarInput.append(Content)
        print(Content)


# class submit(StrInputBoxes,IntInputBoxes,FloatInputBoxes):
#
#     def __init__(self,InputNames,EntryNumbers,parent):
#
#         def subm(self,a):
#             self.a = a
#             self.Content =[]
#
#             for self.entry in self.entries:
#                 self.Content.append(self.entry.get())
#
#             print(self.Content)
#
#             # for i in range(self.ctrl):
#             #     self.entr = tk.Entry(self,bg='azure')
#             #     #self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
#             #     self.entr.delete(0, 'end')
#
#             return(self.Content)
#
#         # self.SubmitButton = ttk.Button(self,text='Submit',command=self.subm,
#         #  width = 30)
#         # self.SubmitButton.grid(row=5,column=1, columnspan = 3,pady=10,padx=10)
