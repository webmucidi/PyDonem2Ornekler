import tkinter as tk

meyveler=["elma","armut","çilek","üzüm","karpuz","kavun"]

pencere=tk.Tk()

pencere.title("List Box Aracı")

pencere.geometry("350x350")

list1=tk.Listbox()
list1.place(x=100,y=50)

for i in meyveler:
    list1.insert(tk.END,i)
    
pencere.mainloop()