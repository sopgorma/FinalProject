"""
Sophia Gorman
Final Progject - Genshin Pity
11/30/23

"""
#This program will determine how many pulls you need to get the wanted "banner" character.
#Based on the popular game "Genshin Impact". This program is based on purchasing primogems instead of farming them.

from breezypythongui import EasyFrame
from tkinter import PhotoImage

import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window)
entry1 = tk.Entry(master=frame, width=25)
wish = tk.Label(master=frame, text="")
f_value = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
entry1.grid(row=0, column=0, sticky="e")
wish.grid(row=0, column=0, sticky="w")
f_value.grid(row=0, column=1, sticky="e")

class IMGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="~GENSHIN PITY~", width=500, height=500)
        self.config(bg="lightpink4")
        frame = tk.Frame(master=window)
        entry1 = tk.Entry(master=frame, width=25)
        wish = tk.Label(master=frame, text="")
        f_value = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
        entry1.grid(row=0, column=0, sticky="e")
        wish.grid(row=0, column=0, sticky="w")
        f_value.grid(row=0, column=1, sticky="e")

        self.gen = ('GENLOSE')
        counter = 0

        for name in self.gen:
            img = PhotoImage(file=f'./genpics/GENLOSE.gif', width=400, height=250)
            lbl = self.addLabel(text="",row=0, column=counter)
            lbl.config(image=img)
            lbl.img = img
          
IMGUI().mainloop()
window.mainloop() 