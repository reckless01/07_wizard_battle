

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('')
        print('The wizard {} attacks the level {} {}'.format(
            self.name, creature.level, creature.name
        ))

# helloK

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "A level {} {}".format(
            self.level, self.name
        )