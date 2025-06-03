import json
import sqlite3
import tkinter as tk
from tkinter import messagebox


class Etel:
    """.write_ID( ) -> metódus a json fileba írja az ételek ID-jét \n
    .write_into_note( ) -> metódus a json fileba írja az ételeket\n
    .get_ID_by_name( ) -> metódus visszaadja az ételek ID-jét név alapján"""
    # az "adat" változóba kiszedem az össze json recordot
    with open('kaja.json', "r") as x:
        adat:list = json.load(x)

    counter = adat["Settings"]["F_ID_counter"]

    def __init__(self, name, cal_per_100, fat, carb, protein, Id = None):
        self.name:str = name
        self.Id = Id if Id is not None else Etel.counter
        self.carb:int = carb
        self.protein:int = protein
        self.fat:int = fat
        self.cal_per_100:float = cal_per_100

    #
    def write_ID(self):
        connection = sqlite3.connect("database.db", timeout=10)
        cursor = connection.cursor()
        #print(self.name)
        cursor.execute("SELECT obj_id,Name FROM Kaja_obj WHERE Name = ?",(self.name,),)
        result = cursor.fetchone()

        if result is not None:
            # If the meal already exists
            self.Id = result[0]  # Get the existing ID
            #print(self.Id)
        else:
            Etel.adat["Settings"]["F_ID_counter"] += 1
            Etel.counter += 1
            with open("kaja.json", "w") as file:
                json.dump(Etel.adat, file, indent=4)
        # Commit will be done at the end of the method
        connection.commit()
        connection.close()

    def insert_into_db(self):
        # Check if the meal already exists in the database
        connection = sqlite3.connect("database.db", timeout=20)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Kaja_obj WHERE Name = ?", (self.name,),)
        result = cursor.fetchone()

        if result is None:
            # If the meal does not exist, insert it
            cursor.execute("INSERT OR REPLACE INTO Kaja_obj (obj_id, Name, cal_per_100, fat, carb, protein) VALUES (?, ?, ?, ?, ?, ?)", (self.Id, self.name, self.cal_per_100, self.fat, self.carb, self.protein,),)
        else:
            # Create a pop-up window
            def popup():
                root = tk.Tk()
                root.withdraw()  # Hide the root window
                result = messagebox.askyesno("Duplicate Entry", "This already exists! Would you like to change?")
                root.destroy()  # Destroy the root window
                return result

            # Show the pop-up and handle the user's response
            if popup():
                # If the user clicks "Yes", update the existing record
                cursor.execute(
                    "UPDATE Kaja_obj SET cal_per_100 = ?, fat = ?, carb = ?, protein = ? WHERE Name = ?",(self.cal_per_100, self.fat, self.carb, self.protein, self.name,),)
            else:
                # If the user clicks "No", do nothing
                pass
        
        connection.commit()
        connection.close()

    def delete_from_db(self):
        # Connect to the database
        connection = sqlite3.connect("database.db", timeout=10)
        cursor = connection.cursor()

        # Check if the meal exists in the database
        cursor.execute("SELECT * FROM Kaja_obj WHERE Name = ?", (self.name,))
        result = cursor.fetchone()

        if result is not None:
            # If the meal exists, delete it
            cursor.execute("DELETE FROM Kaja_obj WHERE Name = ?", (self.name,))
            print(f"Record '{self.name}' deleted successfully.")
        else:
            print(f"Record '{self.name}' does not exist in the database.")

        # Commit changes and close the connection
        connection.commit()
        connection.close()

    def get_ID_by_name(self):
        for meal in Etel.adat["Meals"]:
            if meal["Name"] == self.name:
                return meal["ID"]
        
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"ID: {self.Id}, Név: {self.name}, Szénhidrát: {self.carb}, Fehérje: {self.protein}, Zsír: {self.fat}, Kalória: {self.cal_per_100}"


#connection = sqlite3.connect("database.db", timeout=10)
#cursor = connection.cursor()
#
#cursor.execute("SELECT obj_id, Name, cal_per_100, fat, carb, protein FROM Kaja_obj")
#rows = cursor.fetchall()
#for row in rows:
#    obj = Etel(row[1], row[2], row[3], row[4], row[5], row[0])
#connection.commit()
#connection.close()

#print(Etel.All_foods[1].__dict__)
#s = Etel("kupi",45,75,23,500)
#s.write_ID()
#s.write_into_note()
#print(s)