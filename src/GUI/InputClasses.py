
import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)




class InputBoxes(tk.Frame):

    def __init__(self,InputNames,Type,EntryNumbers,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = EntryNumbers
        self.entries = []

        #'Float' = 1 ou 'Int' = 2 ou 'Str' = 3

        self.Type = Type

        self.create_entry_widgets(self.EntryNumbers,self.Type,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,Type,InputNames,entries):

        self.ctrl1 = int(EntryNumbers)
        self.List = InputNames
        self.TypeTest = Type

        if self.TypeTest == 1:

            for i in range(self.ctrl1):

                self.text = tk.Label(self,text = self.List[i],font=SMALL_FONT,width = 15)

                self.text.grid(row=i, column = 0, sticky = 'e',padx=10,pady=2)
                self.text.grid_columnconfigure(1,weight=1)

            for i in range(self.ctrl1):

                self.entr = tk.Entry(self,bg='azure',textvariable=tk.DoubleVar())
                self.entr.grid(row=i, column = 1,padx=10,pady=2,sticky='e')
                self.entries.append(self.entr)

        elif self.TypeTest == 2:

            for i in range(self.ctrl1):

                self.text = tk.Label(self,text = self.List[i],font=SMALL_FONT,width = 15)

                self.text.grid(row=i, column = 0, sticky = 'e',padx=10,pady=2)
                self.text.grid_columnconfigure(1,weight=1)

            for i in range(self.ctrl1):

                self.entr = tk.Entry(self,bg='azure',textvariable=tk.IntVar())
                self.entr.grid(row=i, column = 1,padx=10,pady=2,sticky='e')
                self.entries.append(self.entr)

        elif self.TypeTest == 3:

            for i in range(self.ctrl1):

                self.text = tk.Label(self,text = self.List[i],font=SMALL_FONT,width = 15)

                self.text.grid(row=i, column = 0, sticky = 'e',padx=10,pady=2)
                self.text.grid_columnconfigure(1,weight=1)

            for i in range(self.ctrl1):

                self.entr = tk.Entry(self,bg='azure',textvariable=tk.StringVar())
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





def submMedToT(entries1,entries2,entries3,entries4,entries5,entries6,entries7,entries8,entries9):

    Content1 = []
    entries = entries1 + entries2 + entries3 + entries4 + entries5 + entries6 + entries7 + entries8 + entries9

    for entry in entries:
        Content1.append(entry.get())

    print(Content1)






class MedSubmit:

    def __init__(self):

        def submMed1(self,entries1,entries2,entries3):

            self.Content1 = []
            entries = entries1 + entries2 + entries3

            for entry in entries:
                Content1.append(entry.get())

            print(Content1)

        def submMed2(self,entries):

            Content2 = []
            entries = entries

            for entry in entries:
                Content2.append(entry.get())

            print(Content2)

        def submMed3(self,entries):

            Content3 = []
            entries = entries

            for entry in entries:
                Content3.append(entry.get())

            print(Content3)


class submit(InputBoxes):

    def __init__(self,InputNames,EntryNumbers,entries,parent):


        self.entries = entries

        def input_box(self):




            self.Content =[]

            for self.entry in self.entries:
                self.Content.append(self.entry.get())

            print(self.Content)

            # for i in range(self.ctrl):
            #     self.entr = tk.Entry(self,bg='azure')
            #     #self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
            #     self.entr.delete(0, 'end')

            return(self.Content)

        # self.SubmitButton = ttk.Button(self,text='Submit',command=self.subm,
        #  width = 30)
        # self.SubmitButton.grid(row=5,column=1, columnspan = 3,pady=10,padx=10)
