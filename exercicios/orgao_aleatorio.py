import random as r
import os

def limpatela():
    os.system('cls')

orgaos = ['coração', 'pulmão', 'rim']

def sortear():
    sorteado = r.choice(orgaos)
    return sorteado

while True:

    premio = sortear()
    aleatorio = r.randint(0,1)
    num=int(input('Digite um numero entre 0 e 1: '))
    if aleatorio == num:
        print('Você ganhou um {}'.format(premio))
        input('Pressione enter...')
        limpatela()
        break
        
    else:
        print('tente dnv!')
