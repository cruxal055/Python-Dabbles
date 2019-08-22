class Weapon:

    maxed_out = False

    def __init__(self):
        print("hello")

    def level_max(self):
        maxed_out = True


Sword = Weapon()
Saber = Weapon()
# print(Weapon.maxed_out)
# print(Sword.maxed_out)
# Sword.maxed_out = True
# print("afterword")
# print(Weapon.maxed_out)
# print(Sword.maxed_out)

Weapon.maxed_out = True
print(Weapon.maxed_out)
print(Saber.maxed_out)
Saber.maxed_out = False
print(Saber.maxed_out)
print(Weapon.maxed_out)