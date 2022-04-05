from tkinter import *

ablak1 = Tk()

def ujablak():
    ablak2 = Toplevel(ablak1)
    uzenet2 = Message(ablak2, text = 'Készítette: Kulimák Máté\nBaja\n2022.04.05', width = 300)
    gomb2 = Button(ablak2, text = 'Kilép', command = ablak2.destroy)
    uzenet2.pack()
    gomb2.pack()
    ablak2.mainloop()

szoveg1 = Label(ablak1, text = 'Kattints a gombra!')
gomb1 = Button(ablak1, text = 'Névjegy', command = ujablak)

szoveg1.pack()
gomb1.pack()

ablak1.mainloop()