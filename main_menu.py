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

days_name_dic = {"Monday" : 0,
                 "Tuesday" : 1,
                 "Wednesday" : 2,
                 "Thursday" : 3,
                 "Friday" : 4,
                 "Saturday" : 5,
                 "Sunday" : 6}

datum = datetime.today().strftime("%d/%m/%Y")

# adat = json-ból az össze adat!
with open('kaja.json', "r", newline="") as hami:
                adat = json.load(hami)

# Meals-ből csak a nevek!
kaja= []
for nemtom in adat["Meals"]:
      kaja.append(nemtom["Name"])
print(kaja)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")    

class App(ctk.CTk):
    def __init__(self, user,**kwargs):
        super().__init__( **kwargs)
        self.title("TheFitnessApp")
        self.geometry("1000x400")        
        self.user = user
        #print(self.user)
        #print(self.user.ételek)
        self.isTab = 1

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
            self.k1 = Kereső(self.kereső_meals, kaja)
            self.k1.listbox.bind("<Double-Button-1>", lambda event: Entry_k_visszaírása(self.k1.get_selected()))
            
            # Kereső 2 +Frame
            self.kereső_calories = ctk.CTkFrame(master=self.tab2, border_width=2, height=500, width=250)
            self.kereső_calories.grid(row=0, column=1, padx=20, pady=10)
            self.k2 = Kereső(self.kereső_calories, kaja)
            self.k2.listbox.bind("<Double-Button-1>", lambda event: self.whatLabel2.configure(text=self.k2.get_selected()))


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
            self.datumLabel = ctk.CTkLabel(master=self.tab1, text="ASSSD")
            self.datumLabel.grid(row=2, column=0, padx=20, pady=10)

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

            print(Felhasznalo.választható_ételek[2]["Name"]) # itt kisérletezés folyik, törlendő

        def Táblázat(self, adat):
            pass
            x = 0
            y = 0

            # code for creating table
            for i in adat["Calories"]:
                x += 1
                for j in i.values():
                    y += 1

                    self.e = entry = ctk.CTkEntry(self.tab2, placeholder_text='CTkEntry', width=140, height=28)
                    entry.place(x=10, y=10)

                    self.e.grid(row=x, column=y)
                    self.e.insert("end", j)
                y = 0

        def Entry_k_visszaírása(choice):
            print(choice)
            self.nameEntry.delete(0,"end")
            self.calorieEntry.delete(0,"end")
            self.fatEntry.delete(0,"end")
            self.carboEntry.delete(0,"end")
            self.ProteinEntry.delete(0,"end")
            for i in adat["Meals"]:
                if i["Name"] == choice and choice != "":
                    self.nameEntry.insert(0,i["Name"])
                    self.calorieEntry.insert(0,i["cal_per_100"])
                    self.fatEntry.insert(0,i["fat"])
                    self.carboEntry.insert(0,i["carb"])
                    self.ProteinEntry.insert(0,i["protein"])
                    break

        All_GUI(self)

        def get_datum(event):
            selected_date = self.calend.selection_get()
            day_of_week = selected_date.strftime('%A')
            print(f"Selected date: {selected_date.strftime('%d/%m/%Y')}, Day of the week: {day_of_week}")
            all_kcal_sum = 0
            all_eatMuch_sum = 0
            all_eatFat_sum = 0
            all_eatCarb_sum = 0
            all_eatProt_sum = 0

            #elemek kitörlése
            for item in self.calendarTreeView.get_children():
                self.calendarTreeView.delete(item)

            curent_data = self.calend.get_date()
            for i in adat["Calories"]:
                if i["datum"] == curent_data:

                    tápöl = (i["Neve"], i["Portion/each"], i["Calories_multiplication"], i["Fat_multiplication"], i["Carbohydrate_multiplication"], i["Protein_multiplication"])
                    self.calendarTreeView.insert("",index="end", values=tápöl)

                    all_kcal_sum += i["Calories_multiplication"]
                    all_eatMuch_sum += i["Portion/each"]
                    all_eatFat_sum += i["Fat_multiplication"]
                    all_eatCarb_sum += i["Carbohydrate_multiplication"]
                    all_eatProt_sum += i["Protein_multiplication"]
            self.datumLabel.configure(text=f"Összes:\t\t{all_eatMuch_sum}\t\t{all_kcal_sum}\t{all_eatFat_sum}\t{all_eatCarb_sum}\t\t{all_eatProt_sum}         ")        
        self.calend.bind("<<CalendarSelected>>", get_datum)

        def color_calendar_dates(calendar):

            for datumok in adat["Calories"]:
                day = datumok["datum"]
                date_obj = datetime.strptime(day, '%d/%m/%Y').date()
                calendar.calevent_create(date_obj, 'highlight', 'highlight')
    
        color_calendar_dates(self.calend)

        def refresh():
        # variable of display all kcal
            self.inClassSum = 0

            for i in adat["Calories"]:
                if i["datum"] == datum:
                    tápöl = (i["Neve"], i["Portion/each"], i["Calories_multiplication"], i["Fat_multiplication"], i["Carbohydrate_multiplication"], i["Protein_multiplication"])
                    #for táp in tápöl:
                    self.calendarTreeView.insert("",index="end", values=tápöl)
                    self.calculateTreeView.insert("",index="end", values=tápöl)
                    # modify all kcal
                    self.inClassSum += i["Calories_multiplication"]
            self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")
        refresh()

            #a név és caloria json-hoz adása
        def hozza_adás_calories():
            Neve = self.k2.get_selected()
            Portion_per_each = int(self.portionEntry.get())
            x = kaja.index(Neve)

            # Calories_multiplication kiszámolása
            cal_mul = (int(adat["Meals"][x]["cal_per_100"]) * Portion_per_each) / 100
            fat_mul = (float(adat["Meals"][x]["fat"]) * Portion_per_each) / 100
            carb_mul = (float(adat["Meals"][x]["carb"]) * Portion_per_each) / 100
            prot_mul = (float(adat["Meals"][x]["protein"]) * Portion_per_each) / 100

            lista = [Neve, Portion_per_each, cal_mul, fat_mul, carb_mul, prot_mul]
            self.calculateTreeView.insert("",index="end", values=lista)
            self.user.hozzáadás_ételekhez(lista + [datum])

            # Calories dictionary
            caloria_adatok = {
              "Neve": Neve,
              "Portion/each": Portion_per_each,
              "Calories_multiplication": cal_mul,
              "Fat_multiplication": fat_mul,
              "Carbohydrate_multiplication": carb_mul,
              "Protein_multiplication": prot_mul,
              "datum": datum
             }
            
            # add to json
            with open("kaja.json", "r+") as loader:
                adat["Calories"].append(caloria_adatok)
                json.dump(adat, loader, indent=4)
            # modify all kcal
            self.inClassSum += cal_mul
            self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")


        def listabol_torles_Calculat():
            n = 0
            s_item = self.calculateTreeView.selection()
            selected_item = int(s_item[0][1:4],16)
            if s_item:
                item = self.calculateTreeView.item(s_item)
                self.inClassSum -= float(item["values"][2])
                self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")
                self.calculateTreeView.delete(s_item)
                for i in adat["Calories"]:
                    if datum == i["datum"]:
                        break
                    else:
                        n+=1
            
            if selected_item != 0:
                del adat["Calories"][n+selected_item-1]
                with open("kaja.json", "w") as f:
                    json.dump(adat, f, indent=4)    


        def hozza_adás_Meals():
            uj_etel = Etel( self.nameEntry.get(), self.carboEntry.get(), self.ProteinEntry.get(), self.fatEntry.get(), self.calorieEntry.get())
            uj_etel.write_ID()
            uj_etel.write_into_note()

            kaja.append(uj_etel.name)

            """ Nev = self.nameEntry.get()
            Kaloria = self.calorieEntry.get()
            zsir = self.fatEntry.get()
            szenhidrat = self.carboEntry.get()
            feherje = self.ProteinEntry.get()              
            etkezes = [self.checkboxBreakfast.get(), self.checkboxLunch.get(), self.checkboxDinner.get()]

            # megnézem hogy van e üres érték -> ha van "0" értéket ad
            x = [Nev, Kaloria, zsir, szenhidrat, feherje]
            for i in x:
                if i != "":
                    continue
                else:
                    x[x.index(i)] = "0"

            # adat tömb
            adatok = {
                "Name": x[0],
                "Calories/100": x[1], 
                "Fat": x[2],
                "Carbohydrate": x[3],
                "Protein": x[4],
                "When": etkezes
            }

            # megnézem hogy van e már ez az étel json-ban -->
            van_már_ilyen = 0
            számláló = 0
            for j in kaja:
                if Nev == j:
                    van_már_ilyen = 1
                    break
                else:
                    számláló += 1

            # ha VAN ez fut le -> rámenti az újat a régire
            if van_már_ilyen == 1:
                with open("kaja.json", "w") as f:
                    adat["Meals"].pop(számláló)
                    adat["Meals"].insert(számláló,adatok)
                    json.dump(adat, f, indent=4)
                self.comboboxMeal.configure(values=kaja)
                self.combobox.configure(values=kaja)

            # ha NINCS ez fut le
            else:
                with open("kaja.json", "r+") as loader:
                    adat["Meals"].append(adatok)
                    json.dump(adat, loader, indent=4)
                kaja.append(adatok["Name"])
                self.comboboxMeal.configure(values=kaja)
                self.combobox.configure(values=kaja) """

        def listabol_torles_Meals():
            meal_to_delete = Etel( self.nameEntry.get(), self.carboEntry.get(), self.ProteinEntry.get(), self.fatEntry.get(), self.calorieEntry.get())
            print(meal_to_delete)
            print(meal_to_delete.Id)
            for i in Felhasznalo.választható_ételek:
                print(i)
                print(i["ID"])
                print(id(i))
                if i["ID"] == meal_to_delete.Id and i["Name"] == meal_to_delete.name and i["cal_per_100"] == meal_to_delete.cal_per_100 and i["fat"] == meal_to_delete.fat and i["carb"] == meal_to_delete.carb and i["protein"] == meal_to_delete.protein:
                    Felhasznalo.választható_ételek.remove(i) # itt kisérletezés folyik
                    break
            adat["Meals"] = Felhasznalo.választható_ételek  
            with open("kaja.json", "w") as f:
                json.dump(adat, f, indent=4)
            #for meal in adat["Meals"]:
            #    if meal["Name"] == meal_to_delete.name:
            #        adat["Meals"].remove(meal)
            #        break
            #    with open("kaja.json", "w") as f:
            #        json.dump(adat, f, indent=4)
                kaja.remove(meal_to_delete.name)
                #self.comboboxMeal.configure(values=kaja)
                #self.combobox.configure(values=kaja)
                self.nameEntry.delete(0,"end")
                self.calorieEntry.delete(0,"end")
                self.fatEntry.delete(0,"end")
                self.carboEntry.delete(0,"end")
                self.ProteinEntry.delete(0,"end")
            #else:
            #    tk.messagebox.showerror("Delete Failed", "Nincs ilyen étel")
            """  n = 0
            selected_item = self.nameEntry.get()
            if selected_item != "":
                for i in adat["Meals"]:
                    if i["Name"] == self.nameEntry.get():
                        break
                    
                    else:
                        n+=1
            
                del adat["Meals"][n]
                with open("kaja.json", "w") as f:
                    json.dump(adat, f, indent=4)
                kaja.pop(n)
                self.comboboxMeal.configure(values=kaja)
                self.nameEntry.delete(0,"end")
                self.calorieEntry.delete(0,"end")
                self.fatEntry.delete(0,"end")
                self.carboEntry.delete(0,"end")
                self.ProteinEntry.delete(0,"end") """

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
    global userid_entry, password_entry
    userid = userid_entry.get()
    password = password_entry.get()

    for user in adat["users"]:
        if userid == user["Name"] and password == user["password"]:
            login_window.destroy()
            user = Felhasznalo(userid, password)
            user.betöltés()
            App(user = user)
            break
    else:
        tk.messagebox.showerror("Login Failed", "Invalid User ID or Password")

def register_user():
    global userid_entry, password_entry, confirm_password_entry
    username = userid_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()


    if password == confirm_password and username != "" and password != "":
        with open("kaja.json", "r+", encoding='utf-8') as loader:
            adat["users"].append({"ID": adat["Settings"]["U_ID_counter"],"Name": username, "password": password})
            adat["Settings"]["U_ID_counter"] += 1
            json.dump(adat, loader, indent=4, ensure_ascii=False)
        with open(username + '.txt', 'w', encoding='utf-8'):
            pass
        tk.messagebox.showinfo("Registration Successful", "User registered successfully")
    else:
        tk.messagebox.showerror("Registration Failed", "Passwords do not match")

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