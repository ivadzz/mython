import pyautogui as pa
import time as t

t.sleep(2)
# Obtém as coordenadas atuais do mouse
posX, posY = pa.position()
# Exibe as coordenadas na tela
print(f'Coordenadas do mouse: X={posX}, Y={posY}')