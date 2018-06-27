import random
import time

from actors import Wizard, MediumAnimal, SmallAnimal, Dragon, Predator


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
        SmallAnimal('Bat', random.randint(1, 10)),
        SmallAnimal('Rabbit', random.randint(1, 10)),
        MediumAnimal('Boar', random.randint(5, 15)),
        MediumAnimal('Deer', random.randint(5, 15)),
        Predator('Tiger', random.randint(5, 30)),
        Predator('Panther', random.randint(5, 30)),
        Dragon('Dragon', random.randint(10, 60), random.randint(1, 30), random.choice([True, False])),
        Wizard('Evil Wizard', random.randint(20, 60), random.randint(10, 80))
    ]

    print('')
    print('Welcome to Wizard Battles! Please enter player info below ')
    print('')
    
    name = input("What is your name? ")
    hero_name = name.capitalize()
    input_level = int(input("What is your experience like? "))
    input_hp = int(input("How tough are ya? "))
    i_m_lvl = input_level -20
    i_max_lvl = input_level + 30
    i_m_hp = input_hp - 20
    i_max_hp = input_hp + 30

    hero_level = random.randint(i_m_lvl, i_max_lvl)
    hero_hp = random.randint(i_m_hp, i_max_hp)
    print('')
    # print('input hp: ', input_hp)
    print('actual hp', hero_hp)
    # print('input xp: ', input_level)
    print('actual xp: ', hero_level)

    hero = Wizard(str(hero_name), int(hero_level), int(hero_hp))
    print('The adventure down a dark and misty path begins for {}, a level {} wizard......'.format(
        hero_name, hero_level))
    print('')

    while True:

        active_creature = random.choice(creatures)
        print('A level {} {} has appeared from a dark and foggy forest...'.format(active_creature.level, active_creature.name))
        print('')

        cmd = input('Do you [a]ttack, [r]un away, [l]ook  around, [s]tats? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                # print('The wizard runs and hides, taking time to recover....')
                # print(hero_hp)
                hero_hp = hero_hp - 10

                if hero_hp <= 0:
                    print('================')
                    print('    YOU DIED    ')
                    print('================')
                    break
                else:
                    pass
                print('You have {} remaining hitpoints'.format(hero_hp))
                print('The wizard, {}, takes damage, and runs to hide and recover...'.format(hero_name))
                time.sleep(3)
                print('The wizard return revitalized!')
                print('')
        elif cmd == 'r':
            print('The wizard, {}, has become unsure of his power and flees!'.format(
                hero.name
            ))
            hero_hp = hero_hp + random.randint(1, 10)
            print('The Wizard has fled, restoring some hp...')
            print('{} hitpoints remaining'.format(hero_hp))
            print('')
            print('')
        elif cmd == 'l':
            print('The wizard, {}, takes in the surroundings and sees: '.format(
                hero.name
            ))
            print('')
            for c in creatures:
                print(' * A level {} {} '.format(c.level, c.name))
        elif cmd == 's':
            print('')
            print('Currently {}, a level {} wizard, has {} hitpoints'.format(hero_name, hero_level, hero_hp))
            print('')
        else:
            print('Exiting game...')
            break

        if not creatures:
            print('================================================================================================')
            print('                                     Game over!                                                  ')
            print('================================================================================================')
            print('     You, {}, have defeated all the creatures! Congratulations player, well done!'.format(hero.name))
            print('================================================================================================')
            break


if __name__ == '__main__':
    main()

