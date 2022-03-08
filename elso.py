from tkinter import *
import math
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Különbség: '+str(c))
def szorzat():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Szorzat: '+str(c))
def negyzet():
    a = int(mezo1.get())
    c = a*a
    mezo3.delete(0, END)
    mezo3.insert(0, 'Négyzet: '+str(c))
def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a/b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Hányados: '+str(c))
def gyok():
    a = int(mezo1.get())
    c = math.sqrt(a)
    mezo3.delete(0, END)
    mezo3.insert(0, 'Gyök: '+str(c))
foablak = Tk()
cimke = Label(foablak, text='Üdvözlet!',fg='Black')
cimke.grid()
mezo1 = Entry(foablak)
mezo1.grid(column=0, row=1)
mezo2 = Entry(foablak)
mezo2.grid(column=0, row=2)
mezo3 = Entry(foablak)
mezo3.grid(column=2, row = 1)
gomb4 = Button(foablak, text='Összead', command=osszeg)
gomb4.grid(column=1, row = 1)
gomb5 = Button(foablak, text='Kivonas', command=kivonas)
gomb5.grid(column=1, row = 2)
gomb6 = Button(foablak, text='Szorzat', command=szorzat)
gomb6.grid(column=1, row = 3)
gomb7 = Button(foablak, text='Osztas', command=osztas)
gomb7.grid(column=1, row = 4)
gomb8 = Button(foablak, text='Négyzet', command=negyzet)
gomb8.grid(column=1, row = 5)
gomb9 = Button(foablak, text='Gyök', command=gyok)
gomb9.grid(column=1, row = 6)
gomb10 = Button(foablak, text='Kilépés', command=foablak.destroy)
gomb10.grid(column=1, row =7 )

can1 = Canvas(foablak, width = 460, height = 460, bg = 'white')
photo = PhotoImage(file = 'ikt.gif')
item = can1.create_image(80, 80, image = photo)
can1.grid()

'''gomb1 = Button(foablak, text='OK')
gomb1.pack()
gomb2 = Button(foablak, text='Mégse')
gomb2.pack()
gomb3 = Button(foablak, text='Kilépés', command=foablak.destroy)
gomb3.pack()'''

foablak.mainloop()