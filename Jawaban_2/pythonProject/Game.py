from Battle import Battle

class Game:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def display_robots(self):
        print("Choose robots for the battle:")
        for i, robot in enumerate(self.robots, 1):
            print(f"{i}. {robot.get_name()}")

    def select_robot(self):
        self.display_robots()
        first_robot_index = int(input("Select the first robot: ")) - 1
        second_robot_index = int(input("Select the second robot: ")) - 1
        return self.robots[first_robot_index], self.robots[second_robot_index]

    def start_game(self):
        robot1, robot2 = self.select_robot()
        battle = Battle(robot1, robot2)
        battle.fight()
