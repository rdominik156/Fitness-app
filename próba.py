from tkinter import *
import json
import json
import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk


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

""" import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="test"
)
mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE test") """





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
    try:
        lista = ["asd", "qwe", "zxc"].index("qwef")
        print(lista)
    except ValueError:
        print("Value not found in the list")

def event_handler():
    import tkinter as tk
    from tkinter import ttk
    from tkinter import ttk
    # Lista az elemekhez
    data = ["alma", "banán", "cseresznye", "datolya", "eper", "füge", "gránátalma"]

    def update_list(event):
        """Frissíti a listát a beírt keresési feltétel alapján."""
        search_term = search_var.get().lower()
        filtered_data = [item for item in data if search_term in item.lower()]

        # Töröljük az aktuális listát
        listbox.delete(0, tk.END)

        # Hozzáadjuk a szűrt elemeket
        for item in filtered_data:
            listbox.insert(tk.END, item)

        # Alap ablak létrehozása
    root = tk.Tk()
    root.title("Egyszerű Kereső")

    # Keresőmező változó
    search_var = tk.StringVar()
    # Trace changes to the search_var and call update_list on write events
    search_var.trace_add("write", lambda *args: update_list(None))

    # Keresőmező létrehozása
    entry = ttk.Entry(root, textvariable=search_var, width=30)
    entry.pack(pady=10)

    # Listbox a találatok megjelenítésére
    listbox = tk.Listbox(root, width=30, height=10)
    listbox.pack()

    # Kezdő lista feltöltése
    for item in data:
        listbox.insert(tk.END, item)

    # Ablak indítása
    root.mainloop()

__name__ == "__main__"
# program()
#event_handler()
import tkinter as tk
from tkinter import messagebox

# Sample class for listbox elements
class Item:
    def __init__(self, name, value, hidden_id):
        self.name = name
        self.value = value
        self.hidden_id = hidden_id  # Hidden attribute
    
    def __str__(self):
        return f"{self.name} ({self.value})"

# Function to handle item selection
def on_select(event):
    widget = event.widget
    selection_index = widget.curselection()
    if selection_index:
        index = selection_index[0]
        selected_item = displayed_items[index]  # Use displayed_items instead of items
        messagebox.showinfo("Item Selected", f"You selected: {selected_item.name}\nValue: {selected_item.value}")

# Function to search/filter data
def filter_list(search_text):
    global displayed_items
    listbox.delete(0, tk.END)  # Clear current listbox
    displayed_items = [item for item in items if search_text.lower() in item.name.lower()]  # Filter items
    for item in displayed_items:
        listbox.insert(tk.END, str(item))  # Update listbox with filtered results

# Create the main application window
root = tk.Tk()
root.title("Clickable Listbox with Filtering")

# Sample data
items = [
    Item("Apple", 100, "A001"),
    Item("Banana", 200, "A002"),
    Item("Cherry", 300, "A003"),
    Item("Date", 400, "A004")
]

displayed_items = items.copy()  # Initially, all items are displayed

# Create Entry for filtering
search_entry = tk.Entry(root)
search_entry.pack(pady=5)
search_entry.bind("<KeyRelease>", lambda event: filter_list(search_entry.get()))  # Live search

# Create Listbox
listbox = tk.Listbox(root, height=10)
listbox.pack(pady=20, padx=20)

# Insert items into the Listbox initially
for item in displayed_items:
    listbox.insert(tk.END, str(item))

# Bind selection event
listbox.bind("<<ListboxSelect>>", on_select)

# Run the application
root.mainloop()
