# I am using solution by BlackDilvish
# from the commit 09a6f633e8f0745084e2f348277e92c9116aa73a

import unittest
import task
import Events
import autonomicCar


class TestAutoCar(unittest.TestCase):

    def setUp(self):
        self.car = autonomicCar.AutonomicCar()

    def test_turn_left(self):
        self.car.turn('left')
        self.assertEqual(-15, self.car.wheel_angle)

    def test_turn_right(self):
        self.car.turn('right')
        self.assertEqual(15, self.car.wheel_angle)

    def test_turn_forward(self):
        self.car.turn('forward')
        self.assertEqual(0, self.car.wheel_angle)

    def test_print(self):
        self.car.speed = 31
        self.car.wheel_angle = 15
        str = self.car.print()
        self.assertEqual(str, "An autonimic car travels at a speed: 31 km/h with wheel angle: 15")

    def test_speed(self):
        self.car.speed = 171
        self.car.speed = 300
        self.assertEqual(300, self.car.speed)

    def test_act_nail(self):
        self.car.act_on_event(Events.NailOnTheRoad())
        self.assertEqual(7, self.car.hp)

    def test_act_rock(self):
        self.car.act_on_event(Events.RockUnderWheels())
        self.assertEqual(9, self.car.hp)

    def test_act_dead(self):
        self.car.act_on_event(Events.DeadEnd())
        self.assertEqual(8, self.car.hp)

    def test_act_nothing(self):
        self.car.act_on_event(Events.Nothing())
        self.assertEqual(10, self.car.hp)

    def test_indestructible(self):
        self.car.hp = 1000
        self.assertEqual(1000, self.car.hp)

    def test_event_nail(self):
        str = Events.NailOnTheRoad().description()
        self.assertEqual(str, "Your car was damaged because of the nail")

    def test_event_rock(self):
        str = Events.RockUnderWheels().description()
        self.assertEqual(str, "Rock under wheels damaged you!")

    def test_event_dead(self):
        str = Events.DeadEnd().description()
        self.assertEqual(str, "Car ended in dead end and you must to turn back")

    def test_event_nothing(self):
        str = Events.Nothing().description()
        self.assertEqual(str, "Nothing bad happened to your car this time, enjoy spectating this travel")

    def test_damage(self):
        str = self.car.after_damage_summary(9)
        self.assertEqual(str, "Now your car have 1 health points")


if __name__ == '__main__':
    unittest.main()
