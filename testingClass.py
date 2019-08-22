class Person:

    def __init__(self):
        print("hello")
        self._age = 0
        self._occupation = "none"
        self._gender = "?"
        self._name = "none"

    def get_age(self) -> int:
        return self._age

    def get_gender(self) -> str:
        return self._gender

    def get_occupation(self) -> str:
        return self._occupation

    def get_name(self) -> str:
        return self._name

    def set_occupation(self, new_occ: str):
        self._occupation = new_occ

    def set_age(self, new_age: int):
        self._age = new_age

    def set_gender(self, new_gender: str):
        self._gender = new_gender

    def set_name(self, new_name: str):
        self._name = new_name

    def say_hello(self):
        print("hello, my name is " + self._name + " and I am " + str(self._age)
              + " my occupation is " + self._occupation)


class Car:

    def __init__(self):
        self._brand = "none"
        self._car_name = "none"
        self._type = "none"
        self._year = 0

    def __init__(self, brand, car_type, car_name, year):
        self._brand = brand
        self._type = car_type
        self._car_name = car_name
        self._year = year

    def to_string(self) -> str:
        return "YR: " + str(self._year) + " NME: " + self._car_name + " MKE: " + self._brand


camry = Car("Toyota", "sedan", "Camry", 2019)
Rav4 = Car("Toyota", "sedan", "RAV4", 2019)
corolla = Car("Toyota", "sedan", "Corolla", 2019)
print(Car.to_string(corolla))
print(corolla.to_string(camry))


#
# Toyota = []
# Toyota.append(corolla)
# Toyota.append(camry)
# Toyota.append(Rav4)
# for x in Toyota:
#     print(x.to_string())
#
#
#
#
# John = Person()
# print(John.get_age())
# John.set_age(10)
# John.set_gender("male")
# John.set_occupation("therapist")
# print(John.get_age())
# print(John.say_hello())



