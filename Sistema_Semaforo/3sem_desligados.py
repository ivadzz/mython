import time as t
import os

def lt():
    os.system('cls')

from colorama import Fore, Back, Style, init

# Inicializa o colorama para garantir a compatibilidade com Windows
init()

sem1=['O ','O ','O ']
sem2=['O ','O ','O ']
sem3=['O ','O ','O ']
ped1 = 'O '
ped2 = 'O'
ped3 = 'O'


lt()
while True:
    print(Fore.WHITE+sem1[0]+Fore.WHITE+sem2[0]+sem3[0])
    print(Fore.YELLOW+sem1[1]+Fore.YELLOW+sem2[1]+sem3[1])
    print(Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+sem3[2])
    t.sleep(1)
    lt()
    print(Fore.WHITE+sem1[0]+Fore.WHITE+sem2[0]+sem3[0])
    print(Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+sem3[1])
    print(Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+sem3[2])
    t.sleep(.6)
    lt()
    