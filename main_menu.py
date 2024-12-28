import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import json
from CTkListbox import *
from datetime import datetime
from tkcalendar import *
import matplotlib.pyplot as plt
import numpy as np

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
print(nemtom)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")    

class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)

        self.title("TheFitnessApp")
        self.geometry("1000x400")
        

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
            self.nameLabel = ctk.CTkLabel(master=self.tab3, text="Name: ")
            self.nameLabel.grid(row=0, column=0, padx=20, pady=10)
            self.calorieLabel = ctk.CTkLabel(master=self.tab3, text="Calories/100: ")
            self.calorieLabel.grid(row=1, column=0, padx=20, pady=10)
            self.fatLabel = ctk.CTkLabel(master=self.tab3, text="Fat: ")
            self.fatLabel.grid(row=2, column=0, padx=20, pady=10)
            self.carboLabel = ctk.CTkLabel(master=self.tab3, text="Carbohydrate: ")
            self.carboLabel.grid(row=3, column=0, padx=20, pady=10)
            self.ProteinLabel = ctk.CTkLabel(master=self.tab3, text="Protein: ")
            self.ProteinLabel.grid(row=4, column=0, padx=20, pady=10)
            self.whenLabel = ctk.CTkLabel(master=self.tab3, text="When: ")
            self.whenLabel.grid(row=0, column=2, padx=20, pady=10)

            #Labels for tab " Calculate "
            self.whatLabel = ctk.CTkLabel(master=self.entryFrame, text="Meal: ")
            self.whatLabel.grid(row=0, column=0,padx=20, pady=10 )
            self.portionLabel = ctk.CTkLabel(master=self.entryFrame, text="Portion: ")
            self.portionLabel.grid(row=1, column=0,padx=20, pady=10 )
            self.allCaloriesLabel = ctk.CTkLabel(master=self.entryFrame, text="All calories: ")
            self.allCaloriesLabel.grid(column=0,row=4,padx=20, pady=10 )
            self.allCaloriesCalculated = ctk.CTkLabel(master=self.entryFrame, text="")
            self.allCaloriesCalculated.grid(column=1,row=4,padx=20, pady=10 )

            #Labels for tab " Calendar "
            self.datumLabel = ctk.CTkLabel(master=self.tab1, text="ASSSD")
            self.datumLabel.grid(row=2, column=0, padx=20, pady=10)

            #Listbox for tab " Calculate "
            self.listBox = CTkListbox(master=self.tab2,width=500)
            self.listBox.grid(column=2, row=0)

            #Listbox for tab " Calendar "
            #self.calendarlistBox = CTkListbox(master=self.tab1,width=500)
            #self.calendarlistBox.grid(column=0, row=1, padx=20, pady=0)
            ttk.style = ttk.Style()
            ttk.style.configure("Treeview", font=("helvetica",10),fieldbackground="#212121", background="#212121", foreground="white")
            ttk.style.configure("Treeview.Heading", font=("helvetica",10, "bold"),background="#4a4a4a", foreground="white",fieldbackground="#212121")
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
            self.calculateTreeView.grid(column=1, row=0, padx=10, pady=0)
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

            #Variables for tab " Add new meal " checkboxes
            self.checkboxBreakfast = ctk.StringVar()
            self.checkboxLunch = ctk.StringVar()
            self.checkboxDinner = ctk.StringVar()
            
            #Entries for tab " Add new meal "
            self.nameEntry = ctk.CTkEntry(master=self.tab3, textvariable="")
            self.nameEntry.grid(row=0, column=1, padx=20, pady=10)
            self.calorieEntry = ctk.CTkEntry(master=self.tab3)
            self.calorieEntry.grid(row=1, column=1, padx=20, pady=10)
            self.fatEntry = ctk.CTkEntry(master=self.tab3)
            self.fatEntry.grid(row=2, column=1, padx=20, pady=10)
            self.carboEntry = ctk.CTkEntry(master=self.tab3)
            self.carboEntry.grid(row=3, column=1, padx=20, pady=10)
            self.ProteinEntry = ctk.CTkEntry(master=self.tab3)
            self.ProteinEntry.grid(row=4, column=1, padx=20, pady=10)
            self.whenEntryBreakfast = ctk.CTkCheckBox(master=self.tab3, text="Breakfast", variable=self.checkboxBreakfast, onvalue="Breakfast")
            self.whenEntryBreakfast.grid(row=1, column=2, padx=20, pady=10)
            self.whenEntryLunch = ctk.CTkCheckBox(master=self.tab3, text="Lunch", variable=self.checkboxLunch, onvalue="Lunch")
            self.whenEntryLunch.grid(row=2, column=2, padx=20, pady=10)
            self.whenEntryDinner = ctk.CTkCheckBox(master=self.tab3, text="Dinner", variable=self.checkboxDinner, onvalue="Dinner")
            self.whenEntryDinner.grid(row=3, column=2, padx=20, pady=10)

            #Entries for tab " Calculate "
            self.combobox = ctk.CTkOptionMenu(master=self.entryFrame, values=kaja, button_color="green")
            self.combobox.grid(row=0, column=1, padx=20, pady=10)
            self.combobox.set("")
            self.portionEntry = ctk.CTkEntry(master=self.entryFrame)
            self.portionEntry.grid(row=1, column=1, padx=20, pady=10)

            #Entries for tab " Add new meal "
            self.comboboxMeal = ctk.CTkComboBox(master=self.tab3, values=kaja, command=Entry_k_visszaírása)
            self.comboboxMeal.grid(row=6, column=0, padx=20, pady=10)
            self.comboboxMeal.set("")

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

        def create_circle_meter(percentage, amount):
            # Validate the input
            if not 0 <= percentage <= 100:
                raise ValueError("Percentage must be between 0 and 100")

            # Create a figure and a single subplot
            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

            # Define the size of the wedge for the given percentage
            size = 0.3
            vals = np.array([percentage, 100 - percentage])

            # Create a pie chart with the given percentage
            wedges, texts = ax.pie(vals, wedgeprops=dict(width=size, edgecolor='w'), startangle=90)

            # Set the aspect ratio to be equal
            ax.set(aspect="equal")

            # Add a circle at the center
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig.gca().add_artist(centre_circle)

            # Annotate the percentage in the center of the circle
            plt.text(0, 0, f"{percentage:.0f}%", ha='center', va='center', fontsize=24, color='black')

            # Add the amount below the circle
            plt.text(0, -1.3, f"Amount: {amount}", ha='center', va='center', fontsize=14, color='black')

            # Display the plot
            plt.show()

        def Entry_k_visszaírása(choice):
            self.nameEntry.delete(0,"end")
            self.calorieEntry.delete(0,"end")
            self.fatEntry.delete(0,"end")
            self.carboEntry.delete(0,"end")
            self.ProteinEntry.delete(0,"end")
            for i in adat["Meals"]:
                 if i["Name"] == choice:
                    self.nameEntry.insert(0,i["Name"])
                    self.calorieEntry.insert(0,i["Calories/100"])
                    self.fatEntry.insert(0,i["Fat"])
                    self.carboEntry.insert(0,i["Carbohydrate"])
                    self.ProteinEntry.insert(0,i["Protein"])
                    self.whenEntryBreakfast #késöbb meg kell csinálni!!!!
                    self.whenEntryLunch
                    self.whenEntryDinner
            self.comboboxMeal.set("")

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

            # insert and refresh listbox
            self.listBox.insert(0,f"Név\t\tMennyiség\tkalória\tzsír\tszénhidrát\tprotein")
            #self.calendarlistBox.insert(0,f"Név\t\tMennyiség\tkalória\tzsír\tszénhidrát\tprotein")

            for i in adat["Calories"]:
                if i["datum"] == datum:
                    tápöl = (i["Neve"], i["Portion/each"], i["Calories_multiplication"], i["Fat_multiplication"], i["Carbohydrate_multiplication"], i["Protein_multiplication"])
                    eatWhat = i["Neve"]
                    eatMuch = i["Portion/each"]
                    eatSoMuch = i["Calories_multiplication"]
                    eatFat = i["Fat_multiplication"]
                    eatCarb = i["Carbohydrate_multiplication"]
                    eatProt = i["Protein_multiplication"]
                    #for táp in tápöl:
                    self.calendarTreeView.insert("",index="end", values=tápöl)
                    self.calculateTreeView.insert("",index="end", values=tápöl)
                    #if len(eatWhat) >8:
                    #    self.calendarTreeView.insert('end',f"{eatWhat}\t{eatMuch}\t\t{eatSoMuch}\t{eatFat}\t{eatCarb}\t\t{eatProt}")
                    #else:
                    #     self.calendarTreeView.insert('end',f"{eatWhat}\t\t{eatMuch}\t\t{eatSoMuch}\t{eatFat}\t{eatCarb}\t\t{eatProt}")
                    # modify all kcal
                    self.inClassSum += i["Calories_multiplication"]
            self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")
        refresh()

            #a név és caloria json-hoz adása
        def hozza_adás_calories():
            Neve = self.combobox.get()
            Portion_per_each = self.portionEntry.get()
            Portion_per_each =int(Portion_per_each)

            # Calories_multiplication kiszámolása
            x = 0
            for i in kaja:
                #y = adat["Meals"][x]["Calories/100"]
                if i == Neve:
                    cal = adat["Meals"][x]["Calories/100"]
                    fat = adat["Meals"][x]["Fat"]
                    carb = adat["Meals"][x]["Carbohydrate"]
                    prot = adat["Meals"][x]["Protein"]
                    cal_mul = (int(cal) * Portion_per_each) / 100
                    fat_mul = (float(fat) * Portion_per_each) / 100
                    carb_mul = (float(carb) * Portion_per_each) / 100
                    prot_mul = (float(prot) * Portion_per_each) / 100
                    x = 0
                    break
                else:
                     x += 1

            tápöl = (Neve, Portion_per_each, cal_mul, fat_mul, carb_mul, prot_mul)
            self.calculateTreeView.insert("",index="end", values=tápöl)        
            if len(Neve) >8:
                self.listBox.insert('end',f"{Neve}\t{Portion_per_each}\t\t{cal}\t{fat}\t{carb}\t{prot}")
            else:
                self.listBox.insert('end',f"{Neve}\t\t{Portion_per_each}\t\t{cal}\t{fat}\t{carb}\t\t{prot}")

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
            if s_item:
                self.calculateTreeView.delete(s_item)

            selected_item = self.listBox.curselection()
            if selected_item != None:
                selected_name = self.listBox.get(selected_item)
                selected_name = list(filter(None,selected_name.split("\t")))
                for i in adat["Calories"]:
                    if datum == i["datum"]:
                        if selected_item != 0:
                            x= adat["Calories"][n+selected_item-1]["Calories_multiplication"]
                            self.inClassSum -= float(x)
                            self.inClassSum = float("{:.1f}".format(self.inClassSum))
                            self.allCaloriesCalculated.configure(text=f"{self.inClassSum}   Kcal")
                            self.listBox.delete(selected_item)
                            break
                    else:
                        n+=1
            
            if selected_item != 0:
                del adat["Calories"][n+selected_item-1]
                with open("kaja.json", "w") as f:
                    json.dump(adat, f, indent=4)


        def hozza_adás_Meals():
            Nev = self.nameEntry.get()
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
                self.combobox.configure(values=kaja)

        def listabol_torles_Meals():
            n = 0
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
                self.ProteinEntry.delete(0,"end")

        def buttons():
        # Buttons
            self.addToListButton = ctk.CTkButton(master=self.entryFrame, text="Add to the list", command=hozza_adás_calories)
            self.addToListButton.grid(row=3, column=1, padx=20, pady=20)    
            self.removeFromListButton = ctk.CTkButton(master=self.entryFrame, text="Remove selected meal", command=listabol_torles_Calculat)
            self.removeFromListButton.grid(row=3, column=0, padx=20, pady=20)             
    
            self.mealAddToDatabase = ctk.CTkButton(master=self.tab3, text="Add to the database", command=hozza_adás_Meals)
            self.mealAddToDatabase.grid(row=6, padx=20, pady=10, column=1)
            self.delFromDatabase = ctk.CTkButton(master=self.tab3, text="Delete", command=listabol_torles_Meals,fg_color="#D12727",font=(None,14),hover_color="#811A1A")
            self.delFromDatabase.grid(row=6, padx=20, pady=10, column=2)

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


App()
