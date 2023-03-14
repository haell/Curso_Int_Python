import random
import time

def displayIntro():
    print('Você está em uma terra cheia de dragões. Na sua frente,')
    print('você vê duas cavernas. Em uma caverna, o dragão é amigável')
    print('e compartilhará seu tesouro com você. O outro dragão')
    print('é ganancioso e faminto, e vai comer você imediatamente.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Em qual caverna você quer entrar? (Digite 1 ou 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('Você se aproxima da caverna...')
    time.sleep(2)
    print('É escuro e assustador...')
    time.sleep(2)
    print('Um grande dragão salta na sua frente! Ele abre suas mandíbulas e...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Te entrega o tesouro!')
    else:
        print('Te engole num bocado!')

playAgain = 'sim'
while playAgain == 'sim' or playAgain == 's':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Você quer jogar de novo? (sim ou não)')
    playAgain = input()
    if playAgain.lower() == 'não' or playAgain.lower() == 'n':
        print('Obrigado por jogar!')
        break