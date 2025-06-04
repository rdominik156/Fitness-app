import json
import sqlite3
import tkinter as tk
from tkinter import messagebox


class Etel:
    def __init__(self, name, cal_per_100, fat, carb, protein, Id=None):
        self.name:str = name
        self.Id:int = Id
        self.carb:int = carb
        self.protein:int = protein
        self.fat:int = fat
        self.cal_per_100:float = cal_per_100

    def insert_into_db(self, cursor):
        # Check if the meal already exists in the database
        cursor.execute("SELECT * FROM Kaja_obj WHERE Name = ?", (self.name,),)
        result = cursor.fetchone()

        if result is None:
            # If the meal does not exist, insert it
            cursor.execute("INSERT INTO Kaja_obj (Name, cal_per_100, fat, carb, protein) VALUES (?, ?, ?, ?, ?)", (self.name, self.cal_per_100, self.fat, self.carb, self.protein,),)
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

    def delete_from_db(self, index):
        # Connect to the database
        connection = sqlite3.connect("database.db", timeout=10)
        cursor = connection.cursor()

        # Check if the meal exists in the database
        cursor.execute("SELECT Name FROM Kaja_obj WHERE obj_id = ?", (index,))
        result = cursor.fetchone()

        if result is not None:
            # If the meal exists, delete it
            cursor.execute("DELETE FROM Kaja_obj WHERE obj_id = ?", (index,))
            print(f"Record '{self.name}' deleted successfully.")
        else:
            print(f"Record '{self.name}' does not exist in the database.")

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        
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
#s.write_into_note()
#print(s)