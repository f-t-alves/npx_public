
import tkinter as tk
from tkinter import ttk
import LabPage as LabP
import MedPage as MedP
import ProviderPage as ProvP


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
        tk.Tk.iconbitmap(self, default='clinic.ico')

        master = tk.Frame(self)
        master.pack(expand=1)

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save Settings", command = lambda:popupmsg('Not Suppoerted Yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = quit)
        menubar.add_cascade(label='File', menu=filemenu)


        # button = ttk.Button(self, text="Med Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(PageOne))
        # button.pack(ipady=10,fill ='x')



        tk.Tk.config(self,menu=menubar)

        self.frames = {}

        for F in(StartPage,MedP.MedPage1,MedP.MedPage2,MedP.MedPage3,LabP.PageTwo,ProvP.PageThree):

            frame = F(master, self)

            self.frames[F] = frame

            frame.grid(row=5,column=5,columnspan=1,rowspan=1,sticky='NSEW')
            frame.grid_rowconfigure(0,weight=0)
            frame.grid_columnconfigure(0,weight=0)
            frame.grid_propagate(False)


        self.show_frame(StartPage)

    def show_frame(self, ctrl):

        frame = self.frames[ctrl]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        tk.Frame.pack(self,fill='both')
        label = tk.Label(self, text='Welcome to Input Window', font = LARGE_FONT)
        label.pack(pady=10,padx=10,fill='both')

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)

        button = ttk.Button(self, text="Med Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(MedP.MedPage1))
        button.pack(ipady=10,fill ='x')
        button2 = ttk.Button(self, text="Lab Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(LabP.PageTwo))
        button2.pack(ipady=10,fill ='x')
        button3 = ttk.Button(self, text="Provider Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(ProvP.PageThree))
        button3.pack(ipady=10,fill ='x')



app = MainApp()
app.geometry("500x350")
app.resizable(width=True, height=True)
app.mainloop()
