class Event:
    def description(self):
        pass

    def damage(self):
        pass


class NailOnTheRoad(Event):
    def description(self):
        return "Your car was damaged because of the nail"

    def damage(self):
        return 3


class RockUnderWheels(Event):
    def description(self):
        return "Rock under wheels damaged you!"

    def damage(self):
        return 1


class DeadEnd(Event):
    def description(self):
        return "Car ended in dead end and you must to turn back"

    def damage(self):
        return 2


class Nothing(Event):
    def description(self):
        return "Nothing bad happened to your car this time, enjoy spectating this travel"

    def damage(self):
        return 0