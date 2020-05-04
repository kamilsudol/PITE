from random import randint
import time
import logging
import sys
from autonomicCar import AutonomicCar
import Events


class Enviroment:
    def __init__(self):
        self.events = [Events.NailOnTheRoad(), Events.RockUnderWheels(), Events.DeadEnd(), Events.Nothing()]

    def random_event(self):
        return self.events[randint(0,3)]


def set_logger():
    a_logger = logging.getLogger()
    a_logger.setLevel(logging.NOTSET)
    output_file_handler = logging.FileHandler("output.log")
    a_logger.addHandler(output_file_handler)


if __name__ == '__main__':

    car = AutonomicCar()
    env = Enviroment()
    set_logger()

    turns = ['left', 'right', 'forward']
    logging.info("Our car starts its travel here\n")

    while True:

        car.print()
        time.sleep(0.5)

        car.turn(turns)
        time.sleep(1)

        car.act_on_event(env.random_event())
        time.sleep(0.2)

        if(car.hp <= 0):
            logging.error("Your car is badly damaged and cannot continue its travel...\n")
            break

        logging.info("Do you want your car to exit this travel? ['yes'/'no']: ")
        inp = input().lower()

        if inp == 'yes':
            break
        elif inp == 'no':
            logging.info("Let's go on!\n")
        else:
            logging.warning("Undefined input, so let's go on!\n")
        time.sleep(1)

    logging.info("Thank you for testing our autonimic car!\n")