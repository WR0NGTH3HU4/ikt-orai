from tkinter import *

foablak = Tk()
foablak.title('A téglatest adatai')
foablak.geometry("200x100")


def szamitas():
    a = float(amezo.get())
    b = float(bmezo.get())
    c = float(cmezo.get())
    terfogat = round (a*b*c, 2)
    mezo3.delete(0, END)
    mezo3.insert(0, str(terfogat)+' cm3')
    ablak2 = Toplevel(foablak)
    dmezo = Entry(ablak2,)
    ablak2.mainloop()

#elso mezo
a = Label(foablak, text='a:', fg = 'Black')
a.grid(column = 1, row = 1)
amezo = Entry(foablak)
amezo.grid(column=2, row=1)

#masodik mezo
b = Label(foablak, text='b:', fg = 'Black')
b.grid(column = 1, row = 2)
bmezo = Entry(foablak)
bmezo.grid(column=2, row=2)

#harmadik mezo
c = Label(foablak, text='c:', fg = 'Black')
c.grid(column = 1, row = 3)
cmezo = Entry(foablak)
cmezo.grid(column=2, row=3)

szoveg1 = Label(foablak, text = 'Kattints a gombra!')
gomb1 = Button(foablak, text = 'Névjegy', command = ujablak)

foablak.mainloop()