from tkinter import *
ablak1 = Tk()

gyoker = 'H:\\IKT\\'
ablak1.geometry('450x450')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file = 'circle.png')
ablak1.iconphoto(True, icon)
''' másik verzió!!!
icon = PhotoImage(file = gyoker+ H:\\IKT\\python\\circle.png)
ablak1.iconphoto(True, icon)
'''
ablak1.config(background = 'black')
elsokep = PhotoImage(file ='madar.png')
cimke = Label(ablak1,
                text = ' Üdvözlet!',
                fg = 'green',
                bg = '#c3cee0',
                font = ('Arial', 45, 'bold',),
                bd = 10,
                relief = RAISED,
                padx = 25,
                pady = 30,
                image = elsokep,
                compound = 'center').pack()

ablak1.mainloop()