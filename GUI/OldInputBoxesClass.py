
class InputBoxes(tk.Frame):

    def __init__(self,InputNames,parent):
        tk.Frame.__init__(self,parent)
        self.InputNames = InputNames
        self.EntryNumbers = len(self.InputNames)
        self.entries = []

        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries,)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl):

            self.text = tk.Label(self,text = self.List[i],)

            self.text.grid(row=i, column = 1, sticky = 'E',pady=2)
            self.text.grid_columnconfigure(1,weight=1)

        for i in range(self.ctrl):

            self.entr = tk.Entry(self,bg='azure')
            self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
            self.entries.append(self.entr)


        self.SubmitButton = ttk.Button(self,text='Submit',command = self.submit,
         width = 30)
        self.SubmitButton.grid(row=self.ctrl+3,column=1, columnspan = 3,pady=10,padx=10)

    def submit(self):
        self.Content =[]

        for self.entry in self.entries:
            self.Content.append(self.entry.get())

        print(self.Content)

        for i in range(self.ctrl):
            self.entr = tk.Entry(self,bg='azure')
            #self.entr.grid(row=i, column = 2, sticky = 'W',pady=2)
            self.entr.delete(0, 'end')

        return(self.Content)
