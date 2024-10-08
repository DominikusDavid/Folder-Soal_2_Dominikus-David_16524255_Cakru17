class Battle:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def fight(self):
        print("Battle Start!")
        while self.robot1.is_alive() and self.robot2.is_alive():
            self.robot1.attack(self.robot2)
            if self.robot2.is_alive():
                self.robot2.attack(self.robot1)
            print()

        if self.robot1.is_alive():
            print(f"{self.robot2.get_name()} is defeated!")
            print(f"{self.robot1.get_name()} wins!")
        else:
            print(f"{self.robot1.get_name()} is defeated!")
            print(f"{self.robot2.get_name()} wins!")
