import os
import json
import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

class Felhasznalo:
    választható_ételek = []
    with open("kaja.json", 'r', encoding='utf-8') as json_fajl:
        data = json.load(json_fajl)
        for meal in data.get("Meals", []):
            választható_ételek.append(meal)
    
    def __init__(self, felhasználó_név, jelszó):
        self.felhasználó_név = felhasználó_név
        self.jelszó = jelszó
        self.ételek = []

    def hozzáadás_ételekhez(self, étel:list):
        cursor.execute("SELECT user_id FROM Felhasználó WHERE Name = ?", (self.felhasználó_név,))
        user_id = cursor.fetchone()[0]

        cursor.execute("INSERT INTO kaja_stored (user_id, name, portion, cal_mul, fat_mul, carb_mul, prot_mul, datum) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                   (user_id, étel[0], étel[1], étel[2], étel[3], étel[4], étel[5], étel[6]))
        connection.commit()

    def betöltés(self):
        """
        Betölti a felhasználó ételeit a fájlból és hozzáadja azokat az ételek listához.
        A fájl neve a felhasználó nevéből származik és .txt kiterjesztésű.
        """

        cursor.execute("SELECT kaja_stored.name ,portion,cal_mul,fat_mul,carb_mul,prot_mul,datum FROM kaja_stored JOIN Felhasználó on kaja_stored.user_id = Felhasználó.user_id WHERE Felhasználó.Name = ?", (self.felhasználó_név,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
            self.ételek.append(list(row))


    def __repr__(self):
        return f"felhasználó: {self.felhasználó_név}"
    
#s = Felhasznalo("Feri", "asd")
#s.hozzáadás_ételekhez(("kenyér",350,30))
#s.betöltés()
#print(s.ételek)