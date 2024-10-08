from Robots import Robot
from Game import Game

if __name__ == "__main__":
    
    game = Game()

    num_of_robots = int(input("How many robots you want to create: "))
    for _ in range(num_of_robots):
        robot = Robot()  
        game.add_robot(robot)

    game.start_game()