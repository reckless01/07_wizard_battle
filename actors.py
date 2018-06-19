import random
# TODO 'exploring specialized derived classes'


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('')
        print('The wizard {} attacks the level {} {}'.format(
            self.name, creature.level, creature.name
        ))
        print('')

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You roll a {}....'.format(my_roll))
        print('{} rolls a {}....'.format(creature, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard {} has defeated the level {} {}'.format(self.name, creature.level, creature.name))
            return True
        else:
            print('The wizard {} has been defeated!'.format(self.name))
            return False


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "A level {} {}".format(
            self.level, self.name
        )

    #def get_defensive_roll(selfs):