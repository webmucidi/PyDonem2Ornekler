import tkinter as tk
from tkinter import *
from datetime import datetime
from datetime import date

pencere=Tk()
pencere.title("List Box Aracı")
pencere.geometry("350x350")

uygulama = Frame(pencere)
uygulama.grid()

an=datetime.now()
bugun=date.today()
yil=bugun.year

L1 = Label(uygulama, text=yil,font="Times 30 italic")
L1.grid(padx=110, pady=10)

list_yillar=tk.Listbox()
list_yillar.grid(padx=110, pady=50)

for i in range(yil,2000,-1):
    list_yillar.insert(tk.END,i)

pencere.mainloop()