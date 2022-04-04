from tkinter import *
import math

#szamitas
s = ''
def terfogat():
    if not s:
        ennyiliteresmezo.delete(0, END)
        ennyiliteresmezo.insert(0, str()+'a számításhoz adat kell ')

    r = float(sugarmezo.get())
    m = float(magassagmezo.get())
    b = float(hanylitermezo.get())
    
    if r>0 and m>0 and b>0:
        terfogat = round (math.pi * r * r * m /1000 ,2)
        ennyiliteresmezo.delete(0, END)
        ennyiliteresmezo.insert(0, str(terfogat)+' l')
        szazalek= round(b*(100/terfogat), 2)

        if b<= terfogat and b>0 and terfogat>0 :
            mennyihelymezo.delete(0, END)
            mennyihelymezo.insert(0, str(terfogat)+' l')
            belefermezo.delete(0, END)
            belefermezo.insert(0,str() +'igen')
            hanyszazalekmezo.delete(0, END)
            hanyszazalekmezo.insert(0, str(szazalek)+' %')
            ennyiliteresmezo.delete(0, END)
            ennyiliteresmezo.insert(0, str(terfogat - b)+' l')
        
         else:
            belefermezo.delete(0, END)
            belefermezo.insert(0,str() +'nem fér bele')
    else :
        ennyiliteresmezo.delete(0, END)
        ennyiliteresmezo.insert(0, str()+' nem lehet ')


foablak = Tk()
foablak.title('Hordó')
foablak.geometry("400x200")

#elso mezo
hanyliter = Label(foablak, text='Hány liter:', fg = 'Black')
hanyliter.grid(column = 1, row = 1)
hanylitermezo = Entry(foablak)
hanylitermezo.grid(column=2, row=1)

#masodik mezo
sugar = Label(foablak, text='Henger alapjának a sugara:', fg = 'Black')
sugar.grid(column = 1, row = 2)
sugarmezo = Entry(foablak)
sugarmezo.grid(column=2, row=2)

#harmadik mezo
magassag = Label(foablak, text='Henger magassága:', fg = 'Black')
magassag.grid(column = 1, row = 3)
magassagmezo = Entry(foablak)
magassagmezo.grid(column=2, row=3)

#kiszámít gomb
kiszamit = Button(foablak, text='Kiszámít', command = terfogat)
kiszamit.grid(column=2, row = 4, ipadx = 36)

#negyedik mezo
belefer = Label(foablak, text='Belefér?', fg = 'Black')
belefer.grid(column = 1 , row = 5)
belefermezo = Entry(foablak)
belefermezo.grid(column = 2, row= 5)

#ötödik mezo
mennyihely = Label(foablak, text='Mennyi hely marad?', fg = 'Black')
mennyihely.grid(column = 1, row = 6)
mennyihelymezo = Entry(foablak)
mennyihelymezo.grid(column = 2, row = 6)

#hatodik mezo
hanyszazalek = Label(foablak, text='Hány százalékát teszi ki?', fg = 'Black')
hanyszazalek.grid(column = 1, row = 7)
hanyszazalekmezo = Entry(foablak, )
hanyszazalekmezo.grid(column = 2, row = 7)

#hetedik mezo
ennyiliteres = Label(foablak, text='Ennyi literes a hordó:', fg = 'Black')
ennyiliteres.grid(column = 1, row = 8)
ennyiliteresmezo = Entry(foablak, )
ennyiliteresmezo.grid(column = 2, row = 8)

foablak.mainloop()
