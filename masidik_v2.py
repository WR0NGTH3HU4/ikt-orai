from tkinter import *

foablak = Tk()
foablak.title('A téglatest adatai')
foablak.geometry("200x100")

def ujablak():
    ablak2 = Toplevel(ablak1)
    ablak2.title('Eredmények')
    ablak2.minsize(width = 300, height = 100)
    ablak2.mainloop()

    sz1 = Label(ablak2, text = 'Felszín:')
    sz2 = Label(ablak2, text = 'Térfogat:')
    m1 = Entry(ablak2)
    m2 = Entry(ablak2)

    sz1.grid(row = 1)
    sz2.grid(row = 2)
    m1.grid(row = 1, column = 2, sticky = W)
    m2.grid(row = 2, column = 2, sticky = W)

    a = eval(amezo.get())
    

foablak.mainloop()