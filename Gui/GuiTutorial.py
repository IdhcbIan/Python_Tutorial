
"""
import tkinter as tk

root = tk.Tk()


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42") 
canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(root, relwidht=0.8, relheight=0.8)


root.mainloop()


"""
#       // Basic window  //         

"""

from tkinter import *
class window:
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Helo World!', background='green')
        self.botao.pack()
        self.botao2 = Button(self.fr1, text='Welcome', background='green')
        self.botao2.pack()

root=Tk()
window(root)
root.mainloop()

"""

#////////////////////////////////////////////////////////////////


"""
from tkinter import *

class Janela:
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao1 = Button(self.fr1,text='Oi!')
        self.botao1['background']='green'
        self.botao1['font']=('Times','14','italic','bold')
        self.botao1['height']=20
        self.botao1.pack()
        self.botao2 = Button(self.fr1,bg='blue', font=('Times','16'))
        self.botao2['text']='Tchau!'
        self.botao2['fg']='black'
        self.botao2['width']=30
        self.botao2.pack()
  


raiz=Tk()
Janela(raiz)

raiz.resizable(False, False)

raiz.mainloop()

"""




#//////////////////////////////////////////////////////////////