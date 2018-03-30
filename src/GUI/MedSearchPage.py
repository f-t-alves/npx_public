
import tkinter as tk
from tkinter import ttk
from src.GUI import InputClasses as InpCla
from src.GUI import StartPage as StP
# import MainApp as MP

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 7)

def SearchBox():
    searchbox = tk.Tk()
    searchbox.grid()
    searchbox.resizable(width=False, height=False)
    searchbox.wm_title('NPX')
    #searchbox.geometry('100x100')

    frame = tk.Frame(searchbox)
    frame.grid()

    label1 = tk.Label(frame,text='Product')
    label1.grid(row = 0,column=0,sticky='w')

    list_column=['Descrição','Estoque','Desconto','PMC','Whatevah '] #This will come from SQL
    data=[('das1','das2','das3','das4','das5 '),('das1','das2','das3','das4','das5 '),('das1','das2','das3','das4','das5 '),('das1','das2','das3','das4','das5 '),] #fetch this from SQL boyyz

    tree = ttk.Treeview(frame)
    tree.grid(row=2,pady=10,padx=10,columnspan =3)
    tree['columns'] = list_column

    for column in list_column:
        tree.column(column, width=130)
        tree.heading(column, text=column.capitalize())

    for i in data:
        tree.insert("", 0, text="", values=i)

    tree['show'] = 'headings' # Some com a coluna de icone e faz aparecer os nomezinhos


    entr = ttk.Entry(frame,width=100)
    entr.grid(row=0,column=1,padx=10,pady=10,ipadx=0,columnspan=2,sticky='w')


    CheckVar = tk.IntVar()
    check1 = ttk.Checkbutton(frame, text='Todas as filiais',variable = CheckVar, onvalue = 1, offvalue = 0)
    check1.grid(row=1,column=1,sticky='w')
    check1.instate(['selected'])

    frame2 = tk.Frame(searchbox)
    frame2.grid(row = 4,padx=10)
    frame3 = tk.Frame(searchbox)
    frame3.grid(row = 5,padx=10,sticky='w')

    label2 = ttk.Label(frame3,text='Price w/ Discount')
    label2.grid(row = 0,column=0,sticky='w')

    entr2 = ttk.Entry(frame3,width=6)
    entr2.grid(row = 0,column=1,padx=10,pady=10,sticky='w')
    DiscPrice = 'Disc'
    entr2.insert(0,DiscPrice)
    entr2.configure(state='readonly')

    label3 = ttk.Label(frame3,text='Price w/ Max Discount')
    label3.grid(row = 0,column=2,sticky='w',padx=15)

    entr3 = ttk.Entry(frame3,width=6)
    entr3.grid(row = 0,column=3,padx=10,pady=10,sticky='e')
    MaxDiscPrice = 'MDisc'
    entr3.insert(0,MaxDiscPrice)
    entr3.configure(state='readonly')

    label4 = ttk.Label(frame3,text='Product Cost')
    label4.grid(row = 0,column=4,sticky='e',padx=15)

    entr4 = ttk.Entry(frame3,width=6)
    entr4.grid(row = 0,column=5,padx=10,pady=10,sticky='w')
    Cost = 'Cost'
    entr4.insert(0,Cost)
    entr4.configure(state='readonly')

    label5 = ttk.Label(frame2,text='Product Description')
    label5.grid(row = 0,column=0,padx=0,sticky='we')

    entr5 = ttk.Entry(frame2,width=110)
    entr5.grid(row = 1,column=0,padx=0,pady=10,columnspan=5,sticky='we')
    Description = 'Product Description'
    entr5.insert(0,Description)
    entr5.configure(state='readonly')


    EAN_SQL=['78451'] # EAN vindo do SQL
    EAN_Label = 'EAN: ' + EAN_SQL[0]

    label6 = ttk.Label(frame2,text=EAN_Label)
    label6.grid(row = 0,column=1,sticky='we')

    ProdID_SQL=['1111'] # ProdID vindo do SQL
    ProdID_Label = 'ProdID: ' + ProdID_SQL[0]

    label7 = ttk.Label(frame2,text=ProdID_Label)
    label7.grid(row = 0,column=2,sticky='we')

    InfoFrame = ttk.LabelFrame(searchbox,text='Item Information',labelanchor='nw',padding=10)
    InfoFrame.grid(row = 3,padx=10,sticky='w')

    label8 = ttk.Label(InfoFrame,text='',width=105)
    label8.grid(row = 0,column=2,sticky='we')





    searchbox.mainloop()




class SearchMedPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,width=940)

        # style=ttk.Style()
        # a = style.element_names()
        # print(a)

        PageFrame = ttk.Frame(self,width=940,relief='solid')
        PageFrame.grid(column=1,padx=250,pady=10)
        PageFrame.grid_propagate(True)


        # Product = ['EAN','ProdID']
        # Product2 = ['ProdName']
        #
        #
        # a = InpCla.InputBoxes(Product,2,2,PageFrame)
        # a.grid(row=0)
        # b = InpCla.InputBoxes(Product2,3,1,PageFrame)
        # b.grid(row=1)

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
        b2 = ttk.Button(PageFrame, text="Search",command=SearchBox)
        b2.grid(row=3,columnspan=2,sticky = 'n',pady = 10,padx = 40)
