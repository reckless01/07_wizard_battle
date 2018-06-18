import random

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

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook  around? ')
        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('r')
        elif cmd == 'l':
            print('l')
        else:
            print('Exiting game...')
            break


if __name__ == '__main__':
    main()