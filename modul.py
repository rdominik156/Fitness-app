import customtkinter as ctk
from CTkListbox import *

class Kereső:
    def __init__(self, root, list):
        # Keresőmező változó
        search_var = ctk.StringVar()
        # Trace changes to the search_var and call update_list on write events
        search_var.trace_add("write", lambda *args: update_list(None))

        # Keresőmező létrehozása
        self.entry = ctk.CTkEntry(root, textvariable=search_var, width=150)
        self.entry.pack(pady=10)

        # Listbox a találatok megjelenítésére
        self.listbox = CTkListbox(master=root, height=160, border_width=1, scroll_height=100)
        self.listbox.pack(pady=10, padx=10)

        # Kezdő lista feltöltése
        for item in list:
            self.listbox.insert("end", item)
        

        def update_list(event):
            #Frissíti a listát a beírt keresési feltétel alapján.
            search_term = search_var.get().lower()
            filtered_data = [item for item in list if search_term in item.lower()]

            # Töröljük az aktuális listát
            self.listbox.delete(0, "end")
            # Hozzáadjuk a szűrt elemeket
            for item in filtered_data:
                self.listbox.insert("end", item)
        
    def get_selected(self):
        """Visszaadja a kijelölt elemet"""
        return self.listbox.get(self.listbox.curselection())