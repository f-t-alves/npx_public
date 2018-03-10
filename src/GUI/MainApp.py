
import tkinter as tk
from tkinter import ttk
from src.GUI import LabPage as LabP
from src.GUI import MedPage2 as MedP
from src.GUI import ProviderPage as ProvP
from src.GUI import StartPage as StP
from src.GUI import InputClasses as InpCla

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)

def popupmsg(msg):
    popup =tk.Tk()



    popup.wm_title('NPX')
    label = ttk.Label(popup, text =msg, font=NORM_FONT,anchor='center')
    label.pack(side='top', fill='x', pady=10,anchor='center')
    B1 = ttk.Button(popup, text='Ok',command=popup.destroy)
    B1.pack()
    popup.geometry("200x80")
    popup.resizable(width=False, height=False)
    popup.mainloop()





class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self,'New Pharma eXperience')
        tk.Tk.iconbitmap(self, default='src/GUI/clinic.ico')

        master = tk.Frame(self)
        master.pack(expand=1)

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save Settings", command = lambda:popupmsg('Not Suppoerted Yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = quit)
        menubar.add_cascade(label='File', menu=filemenu)




        tk.Tk.config(self,menu=menubar)

        self.frames = {}

        for F in(StP.StartPage,LabP.LabPage,ProvP.ProviderPage,MedP.MedPage):

            frame = F(master, self)

            self.frames[F] = frame

            frame.grid(row=5,column=5,columnspan=1,rowspan=1,sticky='NSEW')
            frame.grid_rowconfigure(0,weight=0)
            frame.grid_columnconfigure(0,weight=0)
            frame.grid_propagate(True)


        self.show_frame(StP.StartPage)

    def show_frame(self, ctrl):


        frame = self.frames[ctrl]
        frame.tkraise()




#app = MainApp()
#app.geometry("940x270")
#app.resizable(width=True, height=True)
#app.mainloop()
