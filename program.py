import random
import time

from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('=======================')
    print('   Wizard Battles!')
    print('=======================')
    print('')


def game_loop():

    creatures = [
        Creature('Toad', 3),
        Creature('Tiger', 9),
        Creature('Bat', 4),
        Creature('Dragon', 15),
        Creature('Evil Wizard', 20)
    ]

    # print(creatures)
    print('')

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A level {} {} has appeared from a dark and foggy forest...'.format(active_creature.level, active_creature.name))
        print('')

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook  around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides, taking time to recover....')
                time.sleep(5)
                print('The wizard return revitalized!')
                print('')
        elif cmd == 'r':
            print('The wizard, {}, has become unsure of his power and flees!'.format(
                hero.name
            ))
            print('')
        elif cmd == 'l':
            print('The wizard, {}, takes in the surroundings and sees: '.format(
                hero.name
            ))
            for c in creatures:
                print(' * A level {} {} '.format(c.level, c.name))
        else:
            print('Exiting game...')
            break

        if not creatures:
            print('')
            print('You, {}, have defeated all the creatures! Congratulations player, well done!'.format(hero.name))
            print('')
            break


if __name__ == '__main__':
    main()