
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



# class submit(StrInputBoxes,IntInputBoxes,FloatInputBoxes):
#
#         self.SubmitButton = ttk.Button(self,text='Submit',command = self.submit,
#          width = 30)
#         self.SubmitButton.grid(row=self.ctrl+3,column=1, columnspan = 3,pady=10,padx=10)
#
#         self.Content =[]
#
#         for self.entry in self.entries:
#             self.Content.append(self.entry.get())
#
#         print(self.Content)
#
#         for i in range(self.ctrl):
#             self.entr = tk.Entry(self,bg='azure')
#             #self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
#             self.entr.delete(0, 'end')
#
#         (self.Content)
