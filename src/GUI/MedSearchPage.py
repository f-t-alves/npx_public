
import tkinter as tk
from tkinter import ttk
from src.GUI import InputClasses as InpCla
from src.GUI import StartPage as StP
# import MainApp as MP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)




class SearchMedPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        # style=ttk.Style()
        # a = style.element_names()
        # print(a)

        PageFrame = ttk.Frame(self,width=940,relief='solid')
        PageFrame.grid(column=1,padx=250,pady=10)
        PageFrame.grid_propagate(True)


        Product = ['EAN','ProdID']
        Product2 = ['ProdName']


        a = InpCla.InputBoxes(Product,2,2,PageFrame)
        a.grid(row=0)
        b = InpCla.InputBoxes(Product2,3,1,PageFrame)
        b.grid(row=1)

        # CÓDIGOS PARA CHECK BOX E Combobox

        # listtrib = ttk.Combobox(PageFrame)
        # listtrib['values'] = ['Positiva', 'Neutra', 'Negativa']
        # listtrib.grid(row=2,column=1,sticky='n',pady = 15)
        #
        #
        # checkbox_frame = ttk.Frame(PageFrame)
        # checkbox_frame.grid(row=1, column=3,sticky='e')
        #
        # self.RestHosp = tk.IntVar()
        # check1 = ttk.Checkbutton(checkbox_frame, text='RestHosp',variable = self.RestHosp, onvalue = 1, offvalue = 0 )
        # check1.grid(row=0,column=3,sticky='w')




        b1 = ttk.Button(PageFrame, text="Back to Home",command=lambda: controller.show_frame(StP.StartPage))
        b1.grid(row=2,columnspan=2,sticky = 'n',pady = 10,padx = 40)
