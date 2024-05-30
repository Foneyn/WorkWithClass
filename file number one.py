import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()

        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Компьютер победил!")

    def player_turn(self):
        print("\nХод игрока:")
        self.player.attack(self.computer)
        self.print_status()

    def computer_turn(self):
        print("\nХод компьютера:")
        self.computer.attack(self.player)
        self.print_status()

    def print_status(self):
        print(f"{self.player.name} здоровье: {self.player.health}")
        print(f"{self.computer.name} здоровье: {self.computer.health}")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()