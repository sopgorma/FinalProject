"""
Sophia Gorman
Final Project - Genshin Pity
11/30/23

"""
#This program will determine how many pulls you need to get the wanted "banner" character.
#Based on the popular game "Genshin Impact". This program is based on purchasing primogems instead of farming them.

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter as tk
from main_frame import MainFrame
from pity_chance import 

window = tk.Tk()

frame = MainFrame()
frame.grid(row=0, column=0)

frame = None

def start_pity():
    global frame
    pity_chance = Pity()
    pity_chance.grid(row=0, column= 0, sticky= "NSEW")
    calculate = tk.Button(pity_chance, text="Calculate Total", command=calculate_pity)
    calculate.grid(row=1, column=1)

def calculate_pity():
    frame.grid_forget()
    frame.grid(row=0, column= 0, sticky= "NSEW")

begin = tk.Button(frame, text="Will you get the banner character?", command=start_pity)
begin.grid(row=0, column=0)

window.mainloop()