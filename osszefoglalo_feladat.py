from tkinter import *

foablak = Tk()
icon = PhotoImage(file = 'icon.png')
foablak.iconphoto(True, icon)
cimke1 = Label(foablak, text='Első mező', fg = 'Black')
cimke1.grid(column = 1, row = 1)
cimke2 = Label(foablak, text='Második mező', fg = 'Black')
cimke2.grid(column = 1, row = 2)
cimke3 = Label(foablak, text='Harmadik mező', fg = 'Black')
cimke3.grid(column = 1, row = 3)
mezo1 = Entry(foablak)
mezo1.grid(column=2, row=1)
mezo2 = Entry(foablak)
mezo2.grid(column=2, row=2)
mezo3 = Entry(foablak)
mezo3.grid(column=2, row=3)
can1 = Canvas(foablak, width = 200, height = 200, bg = 'white')
photo = PhotoImage(file = 'villanykörte.png')
item = can1.create_image(100, 100, image = photo)
can1.grid(column=3, row=1, rowspan=3)
foablak.mainloop()