from colorama import Fore, Back, Style, init
import random as r
init()
while True:
    hack = Fore.GREEN + Back.BLACK + "{}".format(r.randint(0,1))
    print(hack,end="")
    