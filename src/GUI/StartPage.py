
import tkinter as tk
from tkinter import ttk
from src.GUI import LabPage as LabP
from src.GUI import ProviderPage as ProvP
from src.GUI import MedPage2 as MedP
from src.GUI import MedSearchPage as MSP


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        PageFrame=ttk.Frame(self,width=940)
        PageFrame.grid(ipady=300)

        label = tk.Label(PageFrame, text='Welcome to NPX', font = LARGE_FONT)
        label.grid(row = 0,pady=10,padx=340,sticky = 'we')
        label2 = tk.Label(PageFrame, text='Menu', font = NORM_FONT)
        label2.grid(row = 1,pady=10,padx=23,sticky = 'w')

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)

        button = ttk.Button(PageFrame, text="Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(Input),width=10)
        button.grid(row = 2,ipady=3,sticky = 'nw')
        button2 = ttk.Button(PageFrame, text="Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(Search),width=10)
        button2.grid(row = 3,ipady=3,sticky = 'nw')
        button3 = ttk.Button(PageFrame, text="NFe Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=10)
        button3.grid(row = 4,ipady=3,sticky = 'nw')
        button4 = ttk.Button(PageFrame, text="PlaceHolder",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=10)
        button4.grid(row = 5,ipady=3,sticky = 'nw')
        button5 = ttk.Button(PageFrame, text="PlaceHolder",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=10)
        button5.grid(row = 6,ipady=3,sticky = 'nw')
        button6 = ttk.Button(PageFrame, text="PlaceHolder",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=10)
        button6.grid(row = 7,ipady=3,sticky = 'nw')
        # button4 = ttk.Button(self, text="Med Input 2.0",style='Front Page Button.TButton',command=lambda: controller.show_frame(MedP2.MedPage))
        # button4.pack(ipady=10,fill ='x')


class Input(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        PageFrame=ttk.Frame(self,width=940)
        PageFrame.grid(padx=300)

        label = tk.Label(PageFrame, text='Input Page', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)

        button = ttk.Button(PageFrame, text="Med Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(MedP.MedPage),width=30)
        button.grid(ipady=10)
        button2 = ttk.Button(PageFrame, text="Lab Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(LabP.LabPage),width=30)
        button2.grid(ipady=10)
        button3 = ttk.Button(PageFrame, text="Provider Input",style='Front Page Button.TButton',command=lambda: controller.show_frame(ProvP.ProviderPage),width=30)
        button3.grid(ipady=10)
        button4 = ttk.Button(PageFrame, text="Back Home",style='Front Page Button.TButton',command=lambda: controller.show_frame(StartPage))
        button4.grid(pady=10)


class Search(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        PageFrame=ttk.Frame(self,width=940)
        PageFrame.grid(padx=300)

        label = tk.Label(PageFrame, text='Search Page', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        s = ttk.Style()
        s.configure('Front Page Button.TButton', font = NORM_FONT)

        button = ttk.Button(PageFrame, text="Med Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(MSP.SearchMedPage),width=30)
        button.grid(ipady=10)
        button2 = ttk.Button(PageFrame, text="Lab Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=30)
        button2.grid(ipady=10)
        button3 = ttk.Button(PageFrame, text="Provider Search",style='Front Page Button.TButton',command=lambda: controller.show_frame(PlaceHolder),width=30)
        button3.grid(ipady=10)
        button4 = ttk.Button(PageFrame, text="Back Home",style='Front Page Button.TButton',command=lambda: controller.show_frame(StartPage))
        button4.grid(pady=10)


class PlaceHolder(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        PageFrame=ttk.Frame(self)
        PageFrame.grid(padx=300)

        label = tk.Label(PageFrame, text='PlaceHolder', font = LARGE_FONT)
        label.grid(pady=10,padx=10)

        button = ttk.Button(PageFrame, text="Back Home",style='Front Page Button.TButton',command=lambda: controller.show_frame(StartPage))
        button.grid(pady=10)
