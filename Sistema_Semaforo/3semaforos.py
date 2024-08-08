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
    print('  '+Fore.WHITE+sem1[0]+Fore.RED+sem2[0]+sem3[0])
    print(Fore.RED+ped1+Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+sem3[1]+Fore.GREEN+ped3)
    print('  '+Fore.GREEN+sem1[2]+Fore.WHITE+sem2[2]+sem3[2])
    print(Fore.GREEN+'    O')
    t.sleep(15)
    lt()
    print('  '+Fore.WHITE+sem1[0]+Fore.RED+sem2[0]+sem3[0])
    print(Fore.RED+ped1+Fore.YELLOW+sem1[1]+Fore.WHITE+sem2[1]+sem3[1]+Fore.RED+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+sem3[2])
    print(Fore.GREEN+'    O')
    t.sleep(4)
    lt()
    print('  '+Fore.RED+sem1[0]+Fore.RED+sem2[0]+sem3[0])
    print(Fore.RED+ped1+Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+sem3[1]+Fore.RED+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+sem3[2])
    print(Fore.GREEN+'    O')
    t.sleep(2)
    lt()

    print('  '+Fore.RED+sem1[0]+Fore.RED+sem2[0]+Fore.WHITE+sem3[0])
    print(Fore.GREEN+ped1+Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+sem3[1]+Fore.RED+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+Fore.GREEN+sem3[2])
    print(Fore.GREEN+'    O')
    t.sleep(15)
    lt()
    print('  '+Fore.RED+sem1[0]+Fore.RED+sem2[0]+Fore.WHITE+sem3[0])
    print(Fore.GREEN+ped1+Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+Fore.YELLOW+sem3[1]+Fore.RED+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+Fore.WHITE+sem3[2])
    print(Fore.RED+'    O')
    t.sleep(4)
    lt()
    print('  '+Fore.RED+sem1[0]+Fore.RED+sem2[0]+Fore.RED+sem3[0])
    print(Fore.GREEN+ped1+Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+sem3[1]+Fore.RED+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+Fore.WHITE+sem3[2])
    print(Fore.RED+'    O')
    t.sleep(2)
    lt()

    print('  '+Fore.RED+sem1[0]+Fore.WHITE+sem2[0]+Fore.RED+sem3[0])
    print(Fore.GREEN+ped1+Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+sem3[1]+Fore.GREEN+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.GREEN+sem2[2]+Fore.WHITE+sem3[2])
    print(Fore.RED+'    O')
    t.sleep(30)
    lt()
    print('  '+Fore.RED+sem1[0]+Fore.WHITE+sem2[0]+Fore.RED+sem3[0])
    print(Fore.RED+ped1+Fore.WHITE+sem1[1]+Fore.YELLOW+sem2[1]+Fore.WHITE+sem3[1]+Fore.GREEN+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+Fore.WHITE+sem3[2])
    print(Fore.RED+'    O')
    t.sleep(4)
    lt()
    print('  '+Fore.RED+sem1[0]+Fore.RED+sem2[0]+Fore.RED+sem3[0])
    print(Fore.RED+ped1+Fore.WHITE+sem1[1]+Fore.WHITE+sem2[1]+sem3[1]+Fore.GREEN+ped3)
    print('  '+Fore.WHITE+sem1[2]+Fore.WHITE+sem2[2]+Fore.WHITE+sem3[2])
    print(Fore.RED+'    O')
    t.sleep(2)
    lt()