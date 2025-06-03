import customtkinter as ctk
from CTkListbox import *
import tkinter as tk
import sqlite3
from étel import Etel


class Kereső():
    def __init__(self, root):
        # Keresőmező változó
        search_var = ctk.StringVar()
        # Trace changes to the search_var and call update_list on write events
        search_var.trace_add("write", lambda *args: update_list_sql(None))

        # Keresőmező létrehozása
        self.entry = ctk.CTkEntry(root, textvariable=search_var, width=150)
        self.entry.pack(pady=10)

        # Listbox a találatok megjelenítésére
        self.listbox = tk.Listbox(master=root, height=12, borderwidth=0, highlightthickness=0, bg="#212121", fg="#DCE4EE", font=("Roboto", 10))
        self.listbox.pack(pady=10, padx=10)

        # SQL adatbázisból adatok betöltése
        conn = sqlite3.connect('database.db')  # Csatlakozás az adatbázishoz
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Kaja_obj")  # Feltételezve, hogy van egy 'items' tábla 'Name' oszloppal
        rows = cursor.fetchall()
        for row in rows:
            rec = Etel(row[1], row[2], row[3], row[4], row[5], row[0])
            self.listbox.insert("end", rec)  # Az SQL eredmény első oszlopát beszúrjuk
        conn.close()
        

        def update_list(event):
            # Frissíti a listát a beírt keresési feltétel alapján (eredeti, listás verzió)
            search_term = search_var.get().lower()
            filtered_data = [item for item in list if search_term in item["Name"].lower()]

            # Töröljük az aktuális listát
            self.listbox.delete(0, "end")
            # Hozzáadjuk a szűrt elemeket
            for item in filtered_data:
                self.listbox.insert("end", item["Name"])

        def update_list_sql(event):
            # Frissíti a listát a beírt keresési feltétel alapján (SQL verzió)
            search_term = search_var.get().lower()
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Kaja_obj WHERE LOWER(name) LIKE ?", ('%' + search_term + '%',))
            rows = cursor.fetchall()
            self.listbox.delete(0, "end")
            for row in rows:
                rec = Etel(row[1], row[2], row[3], row[4], row[5], row[0])
                self.listbox.insert("end", rec)
            conn.close()
    
    def remove(self, index:int):
        # Törli a kijelölt elemet
        self.listbox.delete(index[0])
    
    def insert(self, item:str):
        # Beszúr egy elemet a lista végére
        self.listbox.insert("end", item)
        
    def get_selected(self):
        """Visszaadja a kijelölt elem obj_id-ját"""
        try:
            index = self.listbox.curselection()
            print(index)
            if not index:
                return None
            selected_obj = self.listbox.get(index)
            print(getattr(selected_obj, 'obj_id', None))
            print(selected_obj)
            if hasattr(selected_obj, 'obj_id'):
                selected = selected_obj.name
                obj_id = selected_obj.obj_id
                print(obj_id + " " + selected)
            else:
                selected = selected_obj
                obj_id = None
        except tk.TclError:
            return None  # Nincs kijelölés

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT obj_id FROM Kaja_obj WHERE name = ?", (str(selected),))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None