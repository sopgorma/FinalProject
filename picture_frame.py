#This is where I import pictures into the first window of my GUI application

from breezypythongui import EasyFrame
from tkinter import PhotoImage

class IMGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="~Genshin Pity Calculator~")
        self.config(bg="darksalmon")
        self.genshin = ['GENSHIN','GENWIN']
        counter = 0

        for name in self.genshin:
            img = PhotoImage(file=f'./genpics/{name}.gif')
            lbl = self.addLabel(text="",row=0,column=counter)
            lbl.config(image=img)
            lbl.image = img
            counter +=1

frame = IMGUI()
frame.grid(row=0, column=0, sticky = "NSEW")
frame = None
