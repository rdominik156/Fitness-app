import json


class Etel:
    # az "adat" változóba kiszedem az össze json recordot
    with open('kaja.json', "r") as x:
        adat:list = json.load(x)

    counter = adat["Settings"][0]["ID_counter"]

    def __init__(self, name, carb, protein, fat, cal_per_100):
        self.ID = Etel.counter
        self.name:str = name
        self.carb:int = carb
        self.protein:int = protein
        self.fat:int = fat
        self.cal_per_100:float = cal_per_100

    #
    def write_ID(self):
        Etel.adat["Settings"][0]["ID_counter"] = Etel.counter +1
        with open("kaja.json", "w") as file:
            json.dump(Etel.adat, file, indent=4)

    def write_into_note():
        pass

    def __repr__(self):
        return f"ID: {self.ID}, Név: {self.name}"

#s = Etel("asdfg",45,75,23,500)
#s.write_ID()
#print(s)