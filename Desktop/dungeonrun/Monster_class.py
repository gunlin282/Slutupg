class Spider:
    def __init__(self, name):
        self.name = name
        self.monsterType = "Jättespindel"
        self.initiative = 7
        self.resistance = 1
        self.attack = 2
        self.agility = 3
        self.rarety = 20


class Skeleton:
    def __init__(self, name):
        self.name = name
        self.monsterType = "Skelett"
        self.initiative = 4
        self.resistance = 2
        self.attack = 3
        self.agility = 3
        self.rarety = 15


class Orc:
    def __init__(self, name):
        self.name = name
        self.monsterType = "Orc"
        self.initiative = 6
        self.resistance = 3
        self.attack = 4
        self.agility = 4
        self.rarety = 10


class Troll:
    def __init__(self, name):
        self.name = name
        self.monsterType = "Troll"
        self.initiative = 2
        self.resistance = 4
        self.attack = 7
        self.agility = 2
        self.rarety = 5
