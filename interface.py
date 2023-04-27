import tkinter as tk
from logic_side import *

class ui:
    def __init__(self,master):
        master.resizable(False,False)
        
        self.input_ = tk.Entry(borderwidth=5,relief="groove")
        
       

        self.input_.place(x= 50,y=50)
        self.background = master.configure(bg = "#A2DDEF")

        self.size_ = master.geometry("250x250")
        self.button_ =tk.Button(master,text ="compress",borderwidth=5,relief="groove")
        
        self.button_.place(x=50,y=85)
        
        self.button_open= tk.Button(master,text="make",borderwidth=5,relief="groove",command=lambda:make_zipfile(self.input_.get()))
        self.button_open.place(x=120,y=85)
        


        


root = tk.Tk()


f = ui(root)

root.mainloop()
        


        
    
        


