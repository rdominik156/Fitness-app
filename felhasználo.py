class Felhasznalo:
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
        tartalom = open(self.felhasználó_név + '.txt', 'r', encoding='utf-8')
        for i in tartalom:
            self.ételek.append(i.strip().split(";"))

    def __repr__(self):
        return f"felhasználó: {self.felhasználó_név}"
    
#s = Felhasznalo("Feri", "asd")
#s.hozzáadás_ételekhez(("kenyér",350,30))
#s.betöltés()
#print(s.ételek)