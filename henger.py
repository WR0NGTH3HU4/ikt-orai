from tkinter import *
import math
def terfogat():
    r = int(mezo1.get())
    m = int(mezo2.get())
    terfogat = round (math.pi * r * r * m, 2)
    mezo3.delete(0, END)
    mezo3.insert(0, str(terfogat)+' cm3')

    vassuruseg = round (7.874 * terfogat, 2)
    mezo4.delete (0, END)
    mezo4.insert (0, str(vassuruseg)+' g' )

    fasuruseg = round (0.65 * terfogat, 2)
    mezo5.delete (0, END)
    mezo5.insert (0, str(fasuruseg)+' g')

foablak = Tk()
foablak.title('Henger')
foablak.geometry("280x150")

icon = PhotoImage(file = 'icon.png')
foablak.iconphoto(True, icon)

cimke1 = Label(foablak, text='Sugár (cm):', fg = 'Black')
cimke1.grid(column = 1, row = 1)

cimke2 = Label(foablak, text='Magasság (cm):', fg = 'Black')
cimke2.grid(column = 1, row = 2)

mezo1 = Entry(foablak)
mezo1.grid(column=2, row=1)

mezo2 = Entry(foablak)
mezo2.grid(column=2, row=2)

gomb4 = Button(foablak, text='Kiszámít', command = terfogat)
gomb4.grid(column=3, row = 3)

cimke3 = Label(foablak, text='Térfogat:', fg = 'Black')
cimke3.grid(column = 1 , row = 4)

mezo3 = Entry(foablak)
mezo3.grid(column = 2, row= 4)

cimke4 = Label(foablak, text='Vashenger:', fg = 'Black')
cimke4.grid(column = 1, row = 5)

mezo4 = Entry(foablak)
mezo4.grid(column = 2, row = 5)

cimke4 = Label(foablak, text='Fahenger:', fg = 'Black')
cimke4.grid(column = 1, row = 6)

mezo5 = Entry(foablak, )
mezo5.grid(column = 2, row = 6)

foablak.mainloop()