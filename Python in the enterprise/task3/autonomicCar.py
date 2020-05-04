import logging
from random import randint

class AutonomicCar:
    def __init__(self, speed = 50, wheel_angle = 0):
        logging.info("Deploying autonimic car...")
        self.speed = speed
        self.wheel_angle = wheel_angle
        self.hp = 10

    def print(self):
        logging.info(f"An autonimic car travels at a speed: {self.speed} km/h with wheel angle: {self.wheel_angle}")
        return str("An autonimic car travels at a speed: " + str(self.speed) + " km/h with wheel angle: " + str(self.wheel_angle))

    def after_damage_summary(self, damage):
        logging.info(f"Health points: {self.hp}-{damage} = {self.hp - damage}\n")
        logging.info(f"Now your car have {self.hp - damage} health points")
        return str("Now your car have " + str(self.hp - damage) + " health points")

    def turn(self, turn_value):
        logging.info("Car makes a decision...\n")
        #turn_value = turns[randint(0,2)]

        if turn_value == 'left':
            self.wheel_angle -= 15
        elif turn_value == 'right':
            self.wheel_angle += 15
        else:
            logging.info("Your car didnt turn, you go still forward!")
            return

        logging.info(f"Car turned {turn_value}, and now have wheel angle: {self.wheel_angle}")
        return

    def act_on_event(self, event):
        logging.info(event.description())

        self.after_damage_summary(event.damage())
        self.hp -= event.damage()
        self.speed -= event.damage()
        return