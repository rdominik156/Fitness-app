import os
import json

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
        #print(étel)
        self.ételek.append(étel)
        with open(self.felhasználó_név + ".txt", 'a', encoding='utf-8') as fajl:
            fajl.write("; ".join(map(str, étel))+ "\n")

    def betöltés(self):
        """
        Betölti a felhasználó ételeit a fájlból és hozzáadja azokat az ételek listához.
        A fájl neve a felhasználó nevéből származik és .txt kiterjesztésű.
        """
        with open(self.felhasználó_név + '.txt', 'r', encoding='utf-8') as tartalom:
            for i in tartalom.readlines():
                self.ételek.append(i.strip().split(";"))

    def __repr__(self):
        return f"felhasználó: {self.felhasználó_név}"
    
#s = Felhasznalo("Feri", "asd")
#s.hozzáadás_ételekhez(("kenyér",350,30))
#s.betöltés()
#print(s.ételek)