from tkinter import *
import tkinter.messagebox

MainWindow = Tk()
MainWindow.geometry("415x210")
MainWindow.title('NPX')
MainWindow.config(bg='sky blue')

TopMenu = Menu(MainWindow)

MainWindow.config(menu=TopMenu)

subMenu = Menu(TopMenu)
TopMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='BlaBla', command=quit)
subMenu.add_separator()
subMenu.add_command(label='LoL')
text2 = Label(text='PLACEHOLDER', bg = 'blue')
text2.grid(rowspan=500)

class InputBoxes:

    def __init__(self,InputNames):

        self.InputNames = InputNames
        self.EntryNumbers = len(InputNames)
        self.entries = []
        self.create_entry_widgets(self.EntryNumbers,self.InputNames,
        self.entries)

    def create_entry_widgets(self,EntryNumbers,InputNames,entries):

        self.ctrl = int(EntryNumbers)
        self.List = InputNames

        for i in range(self.ctrl):

            self.text = Label(text = self.List[i],bg='sky blue')

            self.text.grid(row=2+i, column = 1, sticky = N)

        for i in range(self.ctrl):
            self.entr = Entry(bg='azure')
            self.entr.grid(row=2+i, column = 2, sticky = N)
            self.entries.append(self.entr)

        self.SubmitButton = Button(text='Submit',command = self.submit,
         width = 30)
        self.SubmitButton.grid(row=12,column=1, columnspan = 3)


    def submit(self):
        self.Content =[]
        for self.entry in self.entries:
            self.Content.append(self.entry.get())

        return(self.Content)

List=['LabName','LabCNPJ','LabOfficeAddress','LabContactEmail1',
'LabContactEmail2', 'LabContactPhone1', 'LabContactPhone2', 'LabContactFax']

me = InputBoxes(List)



MainWindow.mainloop()
print('', me.Content)
