from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец без оружия."

# Класс Monster для демонстрации боя
class Monster:
    def __init__(self, name):
        self.name = name

def main():
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Боец выбирает меч
    sword = Sword()
    fighter.changeWeapon(sword)
    print(fighter.attack())
    print(f"{monster.name} побежден!\n")

    # Боец выбирает лук
    bow = Bow()
    fighter.changeWeapon(bow)
    print(fighter.attack())
    print(f"{monster.name} побежден!\n")

    # Добавление нового типа оружия
    class Axe(Weapon):
        def attack(self):
            return "Боец наносит удар топором."

    # Боец выбирает топор
    axe = Axe()
    fighter.changeWeapon(axe)
    print(fighter.attack())
    print(f"{monster.name} побежден!\n")

if __name__ == "__main__":
    main()