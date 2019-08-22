
class Weapon:

    _attack_damage = 10
    _name = "none"
    _origin = "none"

    def __init__(self, attack_damage: int, name: str, origin: str):
        self._attack_damage = attack_damage
        self._name = name
        self._origin = origin

    def attack(self) -> int:
        return self._attack_damage

    def change_name(self, new_name):
        self._name = new_name

    def change_origin(self, new_origin):
        self._origin = new_origin

    def obtain_description(self) -> str:
        return "WPN NAME: " + self._name + " ORGN: " + self._origin + " DMG: " + str(self._attack_damage)


LongSword = Weapon(50, "Longsword", "England")
Katana = Weapon(50, "Katana", "Japan")
print(LongSword.obtain_description())



