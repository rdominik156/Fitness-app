import tkinter as tk
from tkinter import *
import json


with open('kaja.json', "r", newline="") as hami:
                adat = json.load(hami)

""" from tkcalendar import Calendar
from datetime import date

def main():
    root = tk.Tk()
    root.title("tkcalendar example")

    # Create the calendar widget
    cal = Calendar(root, selectmode='day', year=2024, month=5, day=21)
    cal.pack(pady=20)

    # Define a style for the specific days
    cal.tag_config('highlight', background='lightblue', foreground='black')

    # Specify the days to highlight using datetime.date instances
    specific_days = [date(2024, 5, 20), date(2024, 5, 25), date(2024, 5, 30)]

    for day in specific_days:
        cal.calevent_create(day, 'highlight', 'highlight')

    # Set the background color for the tags
    #cal._configure('highlight', background='lightblue')

    root.mainloop()

if __name__ == "__main__":
    main() """
# táblázat
class Table:
     
    def __init__(self,root):
        x = 0
        y = 0
         
        # code for creating table
        for i in adat["Calories"]:
            x += 1
            for j in i.values():
                y += 1
             
                self.e = Entry(root)
             
                self.e.grid(row=x, column=y)
                self.e.insert(END, j)
            y = 0
 
# create root window
root = Tk()
t = Table(root)
root.mainloop() 