# import tkinter as tk
# from tkinter import *
# import json
# import customtkinter as ctk
# import matplotlib.pyplot as plt
# import numpy as np



# with open('kaja.json', "r", newline="") as hami:
#                 adat = json.load(hami)

# """ from tkcalendar import Calendar
# from datetime import date

# def main():
#     root = tk.Tk()
#     root.title("tkcalendar example")

#     # Create the calendar widget
#     cal = Calendar(root, selectmode='day', year=2024, month=5, day=21)
#     cal.pack(pady=20)

#     # Define a style for the specific days
#     cal.tag_config('highlight', background='lightblue', foreground='black')

#     # Specify the days to highlight using datetime.date instances
#     specific_days = [date(2024, 5, 20), date(2024, 5, 25), date(2024, 5, 30)]

#     for day in specific_days:
#         cal.calevent_create(day, 'highlight', 'highlight')

#     # Set the background color for the tags
#     #cal._configure('highlight', background='lightblue')

#     root.mainloop()

# if __name__ == "__main__":
#     main() """
# # táblázat
# class Table:
     
#     def __init__(self,root):
#         x = 0
#         y = 0
         
#         # code for creating table
#         for i in adat["Calories"]:
#             x += 1
#             for j in i.values():
#                 y += 1
             
#                 self.e = Entry(root)
             
#                 self.e.grid(row=x, column=y)
#                 self.e.insert(END, j)
#             y = 0
 
# # create root window
# root = Tk()
# t = Table(root)
# root.mainloop() 


# def create_circle_meter(percentage, amount):
#     # Validate the input
#     if not 0 <= percentage <= 100:
#         raise ValueError("Percentage must be between 0 and 100")

#     # Create a figure and a single subplot
#     fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

#     # Define the size of the wedge for the given percentage
#     size = 0.3
#     vals = np.array([percentage, 100 - percentage])

#     # Create a pie chart with the given percentage
#     wedges, texts = ax.pie(vals, wedgeprops=dict(width=size, edgecolor='w'), startangle=90)

#     # Set the aspect ratio to be equal
#     ax.set(aspect="equal")

#     # Add a circle at the center
#     centre_circle = plt.Circle((0, 0), 0.70, fc='white')
#     fig.gca().add_artist(centre_circle)

#     # Annotate the percentage in the center of the circle
#     plt.text(0, 0, f"{percentage:.0f}%", ha='center', va='center', fontsize=24, color='black')

#     # Add the amount below the circle
#     plt.text(0, -1.3, f"Amount: {amount}", ha='center', va='center', fontsize=14, color='black')

#     # Display the plot
#     plt.show()

# # Example usage
# percentage = 75
# amount = 150
# create_circle_meter(percentage, amount)

import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class CircleMeterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Circle Meter")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        # Input for percentage
        self.percentage_label = ctk.CTkLabel(self, text="Percentage:")
        self.percentage_label.pack(pady=5)
        
        self.percentage_var = ctk.StringVar()
        self.percentage_entry = ctk.CTkEntry(self, textvariable=self.percentage_var)
        self.percentage_entry.pack(pady=5)

        # Input for amount
        self.amount_label = ctk.CTkLabel(self, text="Amount:")
        self.amount_label.pack(pady=5)
        
        self.amount_var = ctk.StringVar()
        self.amount_entry = ctk.CTkEntry(self, textvariable=self.amount_var)
        self.amount_entry.pack(pady=5)

        # Button to create the circle meter
        self.create_button = ctk.CTkButton(self, text="Create Circle Meter", command=self.create_circle_meter)
        self.create_button.pack(pady=20)

        # Placeholder for the canvas
        self.canvas = None

    def create_circle_meter(self):
        percentage = float(self.percentage_var.get())
        amount = float(self.amount_var.get())

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

        size = 0.3
        vals = np.array([percentage, 100 - percentage])
        wedges, texts = ax.pie(vals, wedgeprops=dict(width=size, edgecolor='w'), startangle=90)

        ax.set(aspect="equal")
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig.gca().add_artist(centre_circle)

        plt.text(0, 0, f"{percentage:.0f}%", ha='center', va='center', fontsize=24, color='black')
        plt.text(0, -1.3, f"Amount: {amount}", ha='center', va='center', fontsize=14, color='black')

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=20)

def program():
    lista = ["asd", "qwe", "zxc"].index("qwef")
    print(lista)

if __name__ == "__main__":
    #app = CircleMeterApp()
    #app.mainloop()
    program()