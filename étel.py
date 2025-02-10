import json


class Etel:
    """.write_ID( ) -> metódus a json fileba írja az ételek ID-jét \n
    .write_into_note( ) -> metódus a json fileba írja az ételeket\n
    .get_ID_by_name( ) -> metódus visszaadja az ételek ID-jét név alapján"""
    # az "adat" változóba kiszedem az össze json recordot
    with open('kaja.json', "r") as x:
        adat:list = json.load(x)

    counter = adat["Settings"]["F_ID_counter"]

    def __init__(self, name, carb, protein, fat, cal_per_100, Id = None):
        self.name:str = name
        self.Id = Id if Id is not None else Etel.counter
        self.carb:int = carb
        self.protein:int = protein
        self.fat:int = fat
        self.cal_per_100:float = cal_per_100

    #
    def write_ID(self):
        Etel.adat["Settings"]["F_ID_counter"] = Etel.counter +1
        with open("kaja.json", "w") as file:
            json.dump(Etel.adat, file, indent=4)
        Etel.counter += 1

    def write_into_note(self):
        if self.name not in [i["Name"] for i in Etel.adat["Meals"]]:
            # ha nincs benne a json fileban akkor hozzáadom
            with open("kaja.json", "r+") as file:
                Etel.adat["Meals"].append({"ID":self.Id,"Name": self.name,"cal_per_100": self.cal_per_100, "fat": self.fat,"carb": self.carb, "protein": self.protein})
                json.dump(Etel.adat, file, indent=4)
        else:
            # ha benne van akkor frissítem
            for meal in Etel.adat["Meals"]:
                if meal["Name"] == self.name:
                    meal["cal_per_100"] = self.cal_per_100
                    meal["fat"] = self.fat
                    meal["carb"] = self.carb
                    meal["protein"] = self.protein
                    break

            with open("kaja.json", "w") as file:
                json.dump(Etel.adat, file, indent=4)

    def get_ID_by_name(self):
        for meal in Etel.adat["Meals"]:
            if meal["Name"] == self.name:
                return meal["ID"]
        

    def __repr__(self):
        return f"ID: {self.Id}, Név: {self.name}, Szénhidrát: {self.carb}, Fehérje: {self.protein}, Zsír: {self.fat}, Kalória: {self.cal_per_100}"

#s = Etel("kupi",45,75,23,500)
#s.write_ID()
#s.write_into_note()
#print(s)