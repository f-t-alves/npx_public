
import tkinter as tk
from tkinter import ttk
import LabPage as LabP
import MedPage as MedP
import ProviderPage as ProvP


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)


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
