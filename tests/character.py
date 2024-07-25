class Character:
    def __init__(self, health: float, attack: float, headarmor: float, chestarmor: float, legarmor: float, bootarmor: float):
        self.health = health
        self.attack = attack
        self.headarmor = headarmor
        self.chestarmor = chestarmor
        self.legarmor = legarmor
        self.bootarmor = bootarmor

    def damage(self, option, damage: float):
        if option == 1:
            self.health = self.health-damage
            return self.health
        elif option == 2:
            self.headarmor = self.headarmor-damage
            return self.headarmor
        elif option == 3:
            self.chestarmor = self.chestarmor-damage
            return self.chestarmor
        elif option == 4:
            self.legarmor = self.legarmor-damage
            return self.legarmor
        elif option == 5:
            self.bootarmor = self.bootarmor-damage
            return self.bootarmor