import tkinter
from tkinter import *
box=Tk()
box.geometry("810x500")
box.title("ABOUT ME")
box.configure(bg="powder blue")
atext=Label(text="MAYANK SAINI",bg="powder blue",font=("calibari",15,"bold"))
atext.pack()
aboutme=Label(text="I Mayank Saini , AM a student at IIT Madras studying BS in Data Science .\n And i am also given JEE in 2024 as well as 2025 and get \n90 percentile in 2024 and 96.24 percentile in 2025 .\nI also get 91.40% in RBSC board in 2024 and get 20th rank in my school.\n Now I am about to take admission in an reputated NIT .\nTill now in josaa i have alloted NIT jalandhar textile engineering branch" , font=("comicsansms",16)
              ,background="powder blue",)
aboutme.pack()
box.mainloop()

