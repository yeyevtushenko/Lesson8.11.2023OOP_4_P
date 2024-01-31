from prettytable import PrettyTable

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        print("Атака героя!")
        self.display_stats()
        self.health -= self.damage
        print("Герой після атаки:")
        self.display_stats()

    def display_stats(self):
        table = PrettyTable()
        table.field_names = ["Характеристика", "Значення"]
        table.add_row(["Ім'я", self.name])
        table.add_row(["Здоров'я", self.health])
        table.add_row(["Пошкодження", self.damage])
        print(table)

    @classmethod
    def create_hero(cls):
        name = input("Введіть ім'я героя: ")
        health = int(input("Введіть кількість здоров'я героя: "))
        damage = int(input("Введіть кількість пошкодження героя: "))
        return cls(name, health, damage)


player = Character.create_hero()
player.attack()
