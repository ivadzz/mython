from colorama import Fore, Back, Style, init
import random as r
init()
for i in range(0,10**10):
    hack = Fore.GREEN + Back.BLACK + "{}".format(r.randint(0,1))
    print(hack,end="")