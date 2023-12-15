"""
Sophia Gorman
Final Project - Genshin Pity
11/30/23

"""
#This program will determine how many pulls you need to get the wanted "banner" character.
#Based on the popular game "Genshin Impact". This program is based on purchasing primogems instead of farming them.

#This is the main frame used to run the program. Have fun!

from breezypythongui import EasyFrame
import tkinter as tk
from picture_frame import IMGUI
from pity_chance import Pity

#Create a window and put the images from IMGUI into frame
window = tk.Tk()

frame = IMGUI()
frame.grid(row=0,column=0)

#This will begin the application, with an "End Session" button if wanting to quit
def start_pity():
    global frame
    frame = Pity(input)
    frame.grid(row=0, column= 0, sticky= "NSEW")
    end_s = tk.Button(frame, text="End Session", command=end_session)
    end_s.grid(row=4, column=0)

def end_session():
    frame.grid_forget()

begin = tk.Button(frame, text="Let's begin!", width=15, height=3,command=start_pity, bg="chartreuse2", fg="black", font = "bold")
begin.grid(row=1, column=0)


window.mainloop()
