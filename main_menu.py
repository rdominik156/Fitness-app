import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import json
from CTkListbox import *
from datetime import datetime
from tkcalendar import *
import matplotlib.pyplot as plt
import numpy as np
from felhasználo import Felhasznalo
from étel import Etel
from modul import *
import sqlite3


tabla_adat = ["Domi"]
#cursor.execute("INSERT INTO 'Kaja' ('Name') VALUES (?)", tabla_adat)
#connection.commit()

days_name_dic = {"Monday" : 0,
                 "Tuesday" : 1,
                 "Wednesday" : 2,
                 "Thursday" : 3,
                 "Friday" : 4,
                 "Saturday" : 5,
                 "Sunday" : 6}

datum = datetime.today().strftime("%d/%m/%Y")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):

    # adat = json-ból az össze adat!
    with open('kaja.json', "r", newline="") as hami:
        adat = json.load(hami)

    def __init__(self, user,**kwargs):
        super().__init__( **kwargs)
        self.title("TheFitnessApp")
        self.geometry("1000x500")        
        self.user = user
        
        self.k1_index = None
        self.k2_index = None

        # declare Tabview
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack( padx=20, pady=20)

        self.add_tabs()

    # tabs
    def add_tabs(self):
        self.tab3 = self.tab_view.add(" Add new meal ")
        self.tab2 = self.tab_view.add(" Calculate ")
        self.tab1 = self.tab_view.add(" Calendar ")

    

        def All_GUI(self):
            style = ttk.Style()
            style.theme_create("DarkTheme", parent="alt", settings={
                "TNotebook":        {"configure": {"tabmargins": [2, 5, 2, 0], "background": "#212121"}},
                "TNotebook.Tab":    {"configure": {"padding": [5, 1], "background": "#1e1e1e", "foreground": "#d9d9d9"},
                "map":              {"background": [("selected", "#323232")],
                "foreground":       [("selected", "#ffffff")]}},
                "TFrame":           {"configure": {"background": "#212121"}}
            })
            style.theme_use("DarkTheme")

            #Frame for " Calendar " tab
            self.calendarFrame = ctk.CTkFrame(master=self.tab1, border_width=2)
            self.calendarFrame.grid(row=0, column=0, padx=20, pady=10, sticky="w")

            #self.asdfghj = ctk.CTkLabel(master=self.tab1, border_width=2)
            #self.asdfghj.grid(row=0, column=1, padx=20, pady=10, sticky="w")

            #self.tab_calendar = ttk.Notebook(master=self.tab1)
            #self.tab_calendar.grid(row=0, column=0, pady=0)
            #self.nap = ttk.Frame(self.tab_calendar)
            #self.het = ttk.Frame(self.tab_calendar)
            #self.honap = ttk.Frame(self.tab_calendar)
            #self.tab_calendar.add(self.nap, text="Nap")
            #self.tab_calendar.add(self.het, text="Hét")
            #self.tab_calendar.add(self.honap, text="Hónap")

            #Frame for " calculate " tab
            self.entryFrame = ctk.CTkFrame(master=self.tab2, border_width=2)
            self.entryFrame.grid(row=0, column=0, padx=20, pady=10)

            #Labels for tab " Add new meal "
            self.Meals_Entry_Frame = ctk.CTkFrame(master=self.tab3, border_width=2, height=100, width=250)
            self.Meals_Entry_Frame.grid(row=0, column=0, padx=10, pady=10)

            self.nameLabel = ctk.CTkLabel(master=self.Meals_Entry_Frame, text="Name: ")
            self.nameLabel.grid(row=0, column=0, padx=20, pady=10)
            self.calorieLabel = ctk.CTkLabel(master=self.Meals_Entry_Frame, text="Calories/100: ")
            self.calorieLabel.grid(row=1, column=0, padx=20, pady=10)
            self.fatLabel = ctk.CTkLabel(master=self.Meals_Entry_Frame, text="Fat: ")
            self.fatLabel.grid(row=2, column=0, padx=20, pady=10)
            self.carboLabel = ctk.CTkLabel(master=self.Meals_Entry_Frame, text="Carbohydrate: ")
            self.carboLabel.grid(row=3, column=0, padx=20, pady=10)
            self.ProteinLabel = ctk.CTkLabel(master=self.Meals_Entry_Frame, text="Protein: ")
            self.ProteinLabel.grid(row=4, column=0, padx=20, pady=10)
            def kereső(root, list): #ha hibás a class késöbb elővenni
                # Lista az elemekhez
                def update_list(event):
                    #Frissíti a listát a beírt keresési feltétel alapján.
                    search_term = search_var.get().lower()
                    filtered_data = [item for item in list if search_term in item.lower()]

                    # Töröljük az aktuális listát
                    listbox.delete(0, "end")

                    # Hozzáadjuk a szűrt elemeket
                    for item in filtered_data:
                        listbox.insert("end", item)

                # Keresőmező változó
                search_var = ctk.StringVar()
                # Trace changes to the search_var and call update_list on write events
                search_var.trace_add("write", lambda *args: update_list(None))

                # Keresőmező létrehozása
                entry = ctk.CTkEntry(root, textvariable=search_var, width=150)
                entry.pack(pady=10)

                # Listbox a találatok megjelenítésére
                listbox = CTkListbox(master=root, height=160, border_width=1, scroll_height=100)
                listbox.pack(pady=10, padx=10, fill="both", expand=False)
                listbox.bind("<Double-Button-1>", lambda event: Entry_k_visszaírása(listbox.get(listbox.curselection())))
                listbox.bind("<Return>", lambda event: Entry_k_visszaírása(listbox.get(listbox.curselection())))
                listbox.bind("<Double-Button-1>", lambda event: self.whatLabel2.configure(text=listbox.get(listbox.curselection())))

                # Kezdő lista feltöltése
                for item in list:
                    listbox.insert("end", item)
            
            # Kereső 1 +Frame
            self.kereső_meals = ctk.CTkFrame(master=self.tab3, border_width=2, height=500, width=250)
            self.kereső_meals.grid(row=0, column=1, padx=20, pady=10)
            self.k1 = Kereső(self.kereső_meals)
            self.k1.listbox.bind("<<ListboxSelect>>", lambda event: (Entry_k_visszaírása(event), on_k1_select(event)))
            #self.k1.listbox.bind("<<ListboxSelect>>", on_k1_select)

            self.kereső_calories = ctk.CTkFrame(master=self.tab2, border_width=2, height=500, width=250)
            self.kereső_calories.grid(row=0, column=1, padx=20, pady=10)
            self.k2 = Kereső(self.kereső_calories)
            self.k2.listbox.bind("<<ListboxSelect>>", lambda event: (self.whatLabel2.configure(text=self.k2.get_selected_name()),on_k2_select(event)))


            #Labels for tab " Calculate "
            self.whatLabel = ctk.CTkLabel(master=self.entryFrame, text="Meal: ")
            self.whatLabel.grid(row=0, column=0,padx=20, pady=10 )
            self.whatLabel2 = ctk.CTkLabel(master=self.entryFrame, text="")
            self.whatLabel2.grid(row=0, column=1,padx=20, pady=10 )
            self.portionLabel = ctk.CTkLabel(master=self.entryFrame, text="Portion: ")
            self.portionLabel.grid(row=1, column=0,padx=20, pady=10 )
            self.allCaloriesLabel = ctk.CTkLabel(master=self.entryFrame, text="All calories: ")
            self.allCaloriesLabel.grid(column=0,row=4,padx=20, pady=10 )
            self.allCaloriesCalculated = ctk.CTkLabel(master=self.entryFrame, text="")
            self.allCaloriesCalculated.grid(column=1,row=4,padx=20, pady=10 )

            #Labels for tab " Calendar "
            self.datumLabel = ctk.CTkLabel(master=self.tab1, text="")
            self.datumLabel.grid(row=2, column=0, padx=20, pady=10, sticky="w")

            #Listbox for tab " Calendar "
            ttk.style = ttk.Style()
            ttk.style.configure("Treeview", font=("helvetica",10),fieldbackground="#212121", background="#212121", foreground="white")
            ttk.style.configure("Treeview.Heading", font=("helvetica",10, "bold"),background="#4a4a4a", foreground="white",fieldbackground="#212121")
            style.map('Treeview', background=[('selected', '#BFBFBF')])
            self.calendarTreeView = ttk.Treeview(master=self.tab1, height=5, columns=("név","mennyiség", "kalória", "zsír", "szénhidrát", "fehérje"),)
            self.calendarTreeView.grid(column=0, row=1, padx=10, pady=0)
            self.calendarTreeView.column("#0",width=15 ,stretch =False)
            self.calendarTreeView.heading("név", text="Név", anchor="w")
            self.calendarTreeView.column("név",width=150 ,stretch =True)
            self.calendarTreeView.heading("mennyiség", text="Mennyiség", anchor="w")
            self.calendarTreeView.column("mennyiség",width=80 ,stretch =True)
            self.calendarTreeView.heading("kalória", text="Kalória", anchor="w")
            self.calendarTreeView.column("kalória",width=80 ,stretch =True)
            self.calendarTreeView.heading("zsír", text="Zsír", anchor="w")
            self.calendarTreeView.column("zsír",width=80 ,stretch =True)
            self.calendarTreeView.heading("szénhidrát", text="Szénhidrát", anchor="w")
            self.calendarTreeView.column("szénhidrát",width=80 ,stretch =True)
            self.calendarTreeView.heading("fehérje", text="Fehérje", anchor="w")
            self.calendarTreeView.column("fehérje",width=80 ,stretch =True)

            self.calculateTreeView = ttk.Treeview(master=self.tab2, height=5, columns=("név","mennyiség", "kalória", "zsír", "szénhidrát", "fehérje"),)
            self.calculateTreeView.grid(column=0, row=1, padx=10, pady=0, columnspan=2)
            self.calculateTreeView.column("#0",width=15 ,stretch =False)
            self.calculateTreeView.heading("név", text="Név", anchor="w")
            self.calculateTreeView.column("név",width=150 ,stretch =True)
            self.calculateTreeView.heading("mennyiség", text="Mennyiség", anchor="w")
            self.calculateTreeView.column("mennyiség",width=80 ,stretch =True)
            self.calculateTreeView.heading("kalória", text="Kalória", anchor="w")
            self.calculateTreeView.column("kalória",width=80 ,stretch =True)
            self.calculateTreeView.heading("zsír", text="Zsír", anchor="w")
            self.calculateTreeView.column("zsír",width=80 ,stretch =True)
            self.calculateTreeView.heading("szénhidrát", text="Szénhidrát", anchor="w")
            self.calculateTreeView.column("szénhidrát",width=80 ,stretch =True)
            self.calculateTreeView.heading("fehérje", text="Fehérje", anchor="w")
            self.calculateTreeView.column("fehérje",width=80 ,stretch =True)

            # Calendar
            self.calend = Calendar(master=self.tab1, selectmode="day",
                                   year=int(datum[6:10]), month=int(datum[3:5]), day=int(datum[0:2]),
                                   date_pattern='dd/mm/yyyy',
                                   selectbackground="#4d4d4d",
                                   showweeknumbers=False,
                                   showothermonthdays=False)
            self.calend.grid(row=1, column=1, padx=20, pady=10)
            
            #Entries for tab " Add new meal "
            self.nameEntry = ctk.CTkEntry(master=self.Meals_Entry_Frame, textvariable="")
            self.nameEntry.grid(row=0, column=1, padx=20, pady=10)
            self.calorieEntry = ctk.CTkEntry(master=self.Meals_Entry_Frame)
            self.calorieEntry.grid(row=1, column=1, padx=20, pady=10)
            self.fatEntry = ctk.CTkEntry(master=self.Meals_Entry_Frame)
            self.fatEntry.grid(row=2, column=1, padx=20, pady=10)
            self.carboEntry = ctk.CTkEntry(master=self.Meals_Entry_Frame)
            self.carboEntry.grid(row=3, column=1, padx=20, pady=10)
            self.ProteinEntry = ctk.CTkEntry(master=self.Meals_Entry_Frame)
            self.ProteinEntry.grid(row=4, column=1, padx=20, pady=10)

            #Entries for tab " Calculate "
            self.portionEntry = ctk.CTkEntry(master=self.entryFrame)
            self.portionEntry.grid(row=1, column=1, padx=20, pady=10)

        def on_k1_select(event):
            selection = self.k1.listbox.curselection()
            print(selection)
            if selection:
                self.k1_index = selection[0]

        def on_k2_select(event):
            selection = self.k2.listbox.curselection()
            if selection:
                self.k2_index = selection[0]

        def Entry_k_visszaírása(event):
            # Get the Etel object from k1 using the index
            etel_obj_id = self.k1.get_selected()
            if etel_obj_id:
                self.k1_index = etel_obj_id
                # Fetch meal details from the database
                connection = sqlite3.connect("database.db")
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT Name, cal_per_100, fat, carb, protein FROM Kaja_obj WHERE obj_id = ?", (self.k1_index,))
                result = cursor.fetchone()

                if result:
                    name, cal_per_100, fat, carb, protein = result

                    self.nameEntry.delete(0, "end")
                    self.calorieEntry.delete(0, "end")
                    self.fatEntry.delete(0, "end")
                    self.carboEntry.delete(0, "end")
                    self.ProteinEntry.delete(0, "end")

                    self.nameEntry.insert(0, name)
                    self.calorieEntry.insert(0, cal_per_100)
                    self.fatEntry.insert(0, fat)
                    self.carboEntry.insert(0, carb)
                    self.ProteinEntry.insert(0, protein)
                connection.close()


        All_GUI(self)

        def get_datum(event):
            all_kcal_sum = 0
            all_eatMuch_sum = 0
            all_eatFat_sum = 0
            all_eatCarb_sum = 0
            all_eatProt_sum = 0

            # Clear previous items
            for item in self.calendarTreeView.get_children():
                self.calendarTreeView.delete(item)

            curent_data = self.calend.get_date()
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT name, portion, cal_mul, fat_mul, carb_mul, prot_mul FROM kaja_stored WHERE user_id = ? AND datum = ?",
                (self.user.user_id(), curent_data))
            rows = cursor.fetchall()

            # fill the calendarTreeView with data
            for row in rows:
                self.calendarTreeView.insert("", index="end", values=row)
                all_eatMuch_sum += row[1] if row[1] else 0
                all_kcal_sum += row[2] if row[2] else 0
                all_eatFat_sum += row[3] if row[3] else 0
                all_eatCarb_sum += row[4] if row[4] else 0
                all_eatProt_sum += row[5] if row[5] else 0
            connection.close()
            self.datumLabel.configure(text=f"\tÖsszes:{all_eatMuch_sum:25.1f}{all_kcal_sum:23.1f}{all_eatFat_sum:20.1f}{all_eatCarb_sum:20.1f}{all_eatProt_sum:20.1f}")

        self.calend.bind("<<CalendarSelected>>", get_datum)

        def color_calendar_dates(calendar):
            # Highlight calendar dates where the current user has entries in kaja_stored
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT datum FROM kaja_stored WHERE user_id = ?", (self.user.user_id(),))
            dates = cursor.fetchall()
            for (day,) in dates:
                try:
                    date_obj = datetime.strptime(day, '%d/%m/%Y').date()
                    calendar.calevent_create(date_obj, 'highlight', 'highlight')
                except Exception:
                    pass
            connection.close()
    
        color_calendar_dates(self.calend)

        def refresh():
            össz = [0, 0, 0, 0, 0]
            self.inClassSum = 0
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM kaja_stored WHERE datum = ?", (datum,))
            rows = cursor.fetchall()        

            for row in rows:
                for i in range(5):
                    össz[i] += row[i+3]
                self.calendarTreeView.insert("",index="end", values=row[2:8])
                self.calculateTreeView.insert("",index="end", values=row[2:8])
                self.inClassSum += row[4]
            connection.close()
            self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")
            self.datumLabel.configure(text=f"\tÖsszes:{össz[0]:25.1f}{össz[1]:23.1f}{össz[2]:20.1f}{össz[3]:20.1f}{össz[4]:20.1f}")

        refresh()

            # db kaja_stored rögzítése
        def hozza_adás_calories():
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            if self.k2_index:
                Portion_per_each = int(self.portionEntry.get())
                self.k2_index = self.k2.objs[self.k2_index].Id

                cursor.execute("SELECT * FROM Kaja_obj WHERE obj_id = ?", (self.k2_index,))
                obj_args = cursor.fetchone()
                cursor = connection.execute("SELECT user_id FROM Felhasználó WHERE Name = ?", (self.user.felhasználó_név,))
                user = cursor.fetchone()

                object = Etel(*obj_args[1:6], obj_args[0])

                for key, val in object.__dict__.items():
                    if not isinstance(val, str) and key != "Id":
                        object.__setattr__(key, (val * Portion_per_each) / 100)

                cursor.execute("INSERT INTO kaja_stored (user_id, obj_id, name, portion, cal_mul, fat_mul, carb_mul, prot_mul, datum) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (user[0], self.k2_index, object.name, Portion_per_each, object.cal_per_100, object.fat, object.carb, object.protein, datum))
                connection.commit()
                connection.close()

                self.calculateTreeView.insert("", index="end", values=(object.name, Portion_per_each, object.cal_per_100, object.fat, object.carb, object.protein))
                if self.calend.get_date() == datetime.today().strftime("%d/%m/%Y"):
                    self.calendarTreeView.insert("", index="end", values=(object.name, Portion_per_each, object.cal_per_100, object.fat, object.carb, object.protein))
                self.inClassSum += object.cal_per_100
                self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")

        def listabol_torles_Calculat():
            connentin = sqlite3.connect("database.db")
            cursor = connentin.cursor()
            sel_item = self.calculateTreeView.selection()
            if sel_item:
                item_ch = (self.calculateTreeView.get_children(), self.calendarTreeView.get_children())
                idx = self.calculateTreeView.index(sel_item[0])
                item = self.calculateTreeView.item(sel_item)
                self.inClassSum -= float(item["values"][2])
                self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")

                self.calculateTreeView.delete(item_ch[0][idx])
                # if the selected date is today, delete from calendarTreeView as well
                if self.calend.get_date() == datetime.today().strftime("%d/%m/%Y"):
                    self.calendarTreeView.delete(item_ch[1][idx])
 
                cursor.execute(
                    "DELETE FROM kaja_stored WHERE ROWID = (SELECT ROWID FROM kaja_stored WHERE user_id = ? AND name = ? AND portion = ? AND datum = ? LIMIT 1)",
                    (self.user.user_id(), item["values"][0], item["values"][1], datum)
                )
                connentin.commit()
            connentin.close()

        def hozza_adás_Meals():
            # Étel objektum létrehozása --> db fileba írás
            uj_etel = Etel(self.nameEntry.get(),  self.calorieEntry.get(), self.fatEntry.get(),self.carboEntry.get(), self.ProteinEntry.get())
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT obj_id FROM Kaja_obj WHERE Name = ?", (uj_etel.name,))
            
            if cursor.fetchone() is None:
                uj_etel.insert_into_db(cursor)
                connection.commit()
                cursor.execute("SELECT obj_id FROM Kaja_obj ORDER BY obj_id DESC LIMIT 1")
                last_record = cursor.fetchone()
                uj_etel.Id = last_record[0]
                self.k1.insert(uj_etel)
                self.k2.insert(uj_etel)
                self.k1.objs.append(uj_etel)
                self.k2.objs.append(uj_etel)
            else:
                uj_etel.insert_into_db(cursor)
                connection.commit()
            connection.close()

        def listabol_torles_Meals():
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            if self.nameEntry.get() != "":
                meal_to_delete = Etel(self.nameEntry.get(),  self.calorieEntry.get(), self.fatEntry.get(),self.carboEntry.get(), self.ProteinEntry.get())
                cursor.execute("SELECT obj_id FROM Kaja_obj WHERE Name = ? AND cal_per_100 = ? AND fat = ? AND carb = ? AND protein = ?", 
                               (meal_to_delete.name, meal_to_delete.cal_per_100, meal_to_delete.fat, meal_to_delete.carb, meal_to_delete.protein))
                meal_to_delete_index = cursor.fetchone()
                meal_to_delete.Id = meal_to_delete_index[0]

                if self.k1_index:
                    self.k1.remove(self.k1_index)
                    self.k2.remove(self.k1_index)
                    self.k1.objs.pop(self.k1_index)
                    self.k2.objs.pop(self.k1_index)
                    meal_to_delete.delete_from_db(meal_to_delete_index[0])
    
                    self.nameEntry.delete(0,"end")
                    self.calorieEntry.delete(0,"end")
                    self.fatEntry.delete(0,"end")
                    self.carboEntry.delete(0,"end")
                    self.ProteinEntry.delete(0,"end")
            connection.commit()
            connection.close()

        def buttons():
        # Buttons
            self.addToListButton = ctk.CTkButton(master=self.entryFrame, text="Add to the list", command=hozza_adás_calories)
            self.addToListButton.grid(row=3, column=1, padx=20, pady=20)    
            self.removeFromListButton = ctk.CTkButton(master=self.entryFrame, text="Remove selected meal", command=listabol_torles_Calculat)
            self.removeFromListButton.grid(row=3, column=0, padx=20, pady=20)             
    
            self.mealAddToDatabase = ctk.CTkButton(master=self.tab3, text="Add to the database", command=hozza_adás_Meals)
            self.mealAddToDatabase.grid(row=1, padx=20, pady=10, column=0)
            self.delFromDatabase = ctk.CTkButton(master=self.tab3, text="Delete", command=listabol_torles_Meals,fg_color="#D12727",font=(None,14),hover_color="#811A1A")
            self.delFromDatabase.grid(row=1, padx=20, pady=10, column=1)

            button_nap = ctk.CTkButton(master=self.calendarFrame, text="nap", width=50, height=25,fg_color="#212121")
            button_nap.grid(row=0, column=0, pady=0)
            button_het = ctk.CTkButton(master=self.calendarFrame, text="hét", width=50, height=25,fg_color="#212121")
            button_het.grid(row=0, column=1, pady=0)
            button_honap = ctk.CTkButton(master=self.calendarFrame, text="hónap", width=50, height=25,fg_color="#212121")
            button_honap.grid(row=0, column=2, pady=0)
    
            #self.get_datum_button = ctk.CTkButton(master=self.nap, text="kilistázás", command="""get_datum""")
            #self.get_datum_button.grid(row=1, padx=20, pady=10, column=1)
        buttons()

        self.mainloop()

#---------------------------------------------------------------LOGIN----------------------------------------------------------------------------------------------------------------------------

def validate_credentials():
    """Validate the user ID and password."""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    global userid_entry, password_entry
    userid = userid_entry.get()
    password = password_entry.get()

    cursor.execute("SELECT * FROM 'Felhasználó' WHERE Name = ? AND Password = ?", (userid, password))
    result = cursor.fetchone()
    if result:
        login_window.destroy()
        user = Felhasznalo(userid, password)
        user.betöltés()
        App(user = user)
    else:
        tk.messagebox.showerror("Login Failed", "Invalid User ID or Password")
    connection.close()

def register_user():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    global userid_entry, password_entry, confirm_password_entry
    username = userid_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()


    if password == confirm_password and username != "" and password != "":
        cursor.execute("INSERT INTO 'Felhasználó' ('Name', 'Password') VALUES (?, ?)", (username, password))
        connection.commit()

        tk.messagebox.showinfo("Registration Successful", "User registered successfully")
    else:
        tk.messagebox.showerror("Registration Failed", "Passwords do not match")
    connection.close()

# Create the login window
login_window = ctk.CTk()
login_window.title("Login")
login_window.geometry("300x200")

def login_UI():
    login_window.geometry("300x200")
    wigets = login_window.winfo_children()
    for widget in wigets:
        widget.destroy()

    global userid_entry, password_entry
    # User ID label and entry
    userid_label = tk.Label(login_window, text="Felhasználónév:", font=("Arial", 12))
    userid_label.pack(pady=5)

    userid_entry = tk.Entry(login_window, font=("Arial", 12))
    userid_entry.pack(pady=5)

    # Password label and entry
    password_label = tk.Label(login_window, text="Jelszó:", font=("Arial", 12))
    password_label.pack(pady=5)

    password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    # Frame to hold the buttons
    button_frame = tk.Frame(login_window, bg=login_window.cget('bg'), highlightthickness=0, bd=0)
    button_frame.pack(pady=20)

    # Login button
    login_button = tk.Button(button_frame, text="Login", font=("Arial", 12), command=validate_credentials)
    login_button.pack(side="left", padx=10)
    login_window.bind('<Return>', lambda event: validate_credentials())

    # Register button
    register_button = tk.Button(button_frame, text="Register", font=("Arial", 12), command=register_UI)
    register_button.pack(side="left", padx=10)

def register_UI():
    login_window.geometry("300x280")
    global userid_entry, password_entry, confirm_password_entry
    wigets = login_window.winfo_children()
    for widget in wigets:
        widget.destroy()

    # User ID label and entry
    userid_label = tk.Label(login_window, text="Felhasználónév:", font=("Arial", 12))
    userid_label.pack(pady=5)

    userid_entry = tk.Entry(login_window, font=("Arial", 12))
    userid_entry.pack(pady=5)

    # Password label and entry
    password_label = tk.Label(login_window, text="Jelszó:", font=("Arial", 12))
    password_label.pack(pady=5)

    password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    # Password label and entry
    confirm_password_label = tk.Label(login_window, text="Jelszó megerősítése:", font=("Arial", 12))
    confirm_password_label.pack(pady=5)

    confirm_password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
    confirm_password_entry.pack(pady=5)

    # Frame to hold the buttons
    button_frame = tk.Frame(login_window, bg=login_window.cget('bg'), highlightthickness=0, bd=0)
    button_frame.pack(pady=20)

    # Login button
    back_button = tk.Button(button_frame, text="Back", font=("Arial", 12), command=login_UI)
    back_button.pack(side="left", padx=10)

    # Register button
    sign_in_button = tk.Button(button_frame, text="Sign in", font=("Arial", 12), command=register_user)
    sign_in_button.pack(side="left", padx=10)
    login_window.bind('<Return>', lambda event: register_user())


login_UI()

# Run the login window
login_window.mainloop()


#to do
# a naptárnál ha hozzáadok egy új értéket a naphot nem változik meg azonnal a szín

# 0id-s felhasználó aki hozzá fér az összes adathoz