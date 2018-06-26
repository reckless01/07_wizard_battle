import random
import time

from actors import Wizard, SmallAnimal, Dragon, Predator


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
        SmallAnimal('Toad', random.randint(1,10)),
        Predator('Tiger', random.randint(5, 20)),
        SmallAnimal('Bat', random.randint(1, 10)),
        Dragon('Dragon', random.randint(10, 60), random.randint(1, 30), random.choice([True, False])),
        Wizard('Evil Wizard', random.randint(20, 60), random.randint(10, 80))
    ]

    # print(creatures)
    print('')
    print('Welcome to Wizard Battles! Please enter player info below: ')
    print('')
    hero_name = input("What is your name? ")
    hero_level = input("What is your experience like? ")
    input_hp = input("How tough are ya? ")
    print('input hp: ' ,input_hp)

    hero_hp = random.randint(1, int(input_hp))
    print('actual hp' , hero_hp)

    hero = Wizard(str(hero_name), int(hero_level), int(hero_hp))

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
            print('')
        elif cmd == 'l':
            print('The wizard, {}, takes in the surroundings and sees: '.format(
                hero.name
            ))
            print('')
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