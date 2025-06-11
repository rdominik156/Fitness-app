import customtkinter as ctk
from CTkListbox import *
import tkinter as tk
import sqlite3
from étel import Etel


class Kereső():
    def __init__(self, root):
        self.objs = []  # Lista az objektumok tárolására
        # Keresőmező változó
        search_var = ctk.StringVar()
        # Trace changes to the search_var and call update_list on write events
        search_var.trace_add("write", lambda *args: self.update_list_sql(search_var))

        # Keresőmező létrehozása
        self.entry = ctk.CTkEntry(root, textvariable=search_var, width=150)
        self.entry.pack(pady=10)

        # Listbox a találatok megjelenítésére
        self.listbox = tk.Listbox(master=root, height=12, borderwidth=0, highlightthickness=0, bg="#212121", fg="#DCE4EE", font=("Roboto", 10))
        self.listbox.pack(pady=10, padx=10)

        # SQL adatbázisból adatok betöltése
        conn = sqlite3.connect('database.db')  # Csatlakozás az adatbázishoz
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Kaja_obj LIMIT 100")  # Feltételezve, hogy van egy 'items' tábla 'Name' oszloppal
        rows = cursor.fetchall()
        for row in rows:
            rec = Etel(row[1], row[2], row[3], row[4], row[5], row[0])
            self.listbox.insert("end", rec)
            self.objs.append(rec)
        conn.close()

    def update_list_sql(self, search_var):
        self.objs.clear()

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
            self.objs.append(rec)
        conn.close()
    
    def remove(self, index:int):
        # Törli a kijelölt elemet
        self.listbox.delete(index)
    
    def insert(self, item:str):
        # Beszúr egy elemet a lista végére
        self.listbox.insert("end", item)
        
    def get_selected(self):
        """Visszaadja a kijelölt elem obj_id-ját"""
        try:
            index = self.listbox.curselection()
            print(index)
            if index:
                sel_obj = self.objs[index[0]]
                sel_obj_id = sel_obj.__getattribute__('Id')
                return sel_obj_id
        except tk.TclError:
            return None  # Nincs kijelölés
        #return sel_obj_id
    
    def get_selected_name(self):
        """Visszaadja a kijelölt elem nevét"""
        try:
            index:int = self.listbox.curselection()
            if index:
                sel_obj = self.objs[index[0]]
                sel_obj_name = sel_obj.__getattribute__('name')
                return sel_obj_name
        except tk.TclError:
            return None
        #return sel_obj_name