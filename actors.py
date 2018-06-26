import random
# TODO add new creature classes
# TODO add randomness to creature level **DONE**
# TODO story board
# TODO Add player input to start
# TODO store player stats/hp/info
# TODO add unique player attributes


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "A level {} {}".format(
            self.level, self.name
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scale_thickness = scale_thickness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scale_thickness / 10

        return base_roll * fire_modifier * scale_modifier


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Predator(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll * 1.5

# test


class Wizard(Creature):
    def __init__(self, name, level, hp):
        super().__init__(name, level)
        self.hp = hp
        # TODO more features for player wizard and evil wizard
        # self.beard_color = beard_color

    def attack(self, creature):
        print('')
        print('The wizard {} attacks the level {} {}'.format(
            self.name, creature.level, creature.name
        ))
        print('')

        my_roll = random.randint(1, 12) * self.level
        creature_roll = creature.get_defensive_roll()

        print('You roll a {}....'.format(my_roll))
        print('{} rolls a {}....'.format(creature, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard {} has TRIUMPHED over the level {} {}'.format(self.name, creature.level, creature.name))
            print('')
            return True
        else:
            print('The wizard {} has been DEFEATED!'.format(self.name))
            print('')
            return False


