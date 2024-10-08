import random

class Robot:
    def __init__(self):
        self.name = input("Enter robots name: ")
        self.health = int(input(f"Enter health points for {self.name}: "))
        self.attack_power = int(input(f"Enter attack power for {self.name}: "))

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, other_robot):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {other_robot.get_name()} for {damage} damage!")
        other_robot.take_damage(damage)

    def is_alive(self):
        return self.health > 0