import keyboard as k
import pyautogui as pa
import os
import time as t

pa.press('win')
t.sleep(.1)
pa.typewrite('bloco')
t.sleep(.1)
pa.press('enter')
t.sleep(.4)
k.block_key('f4')
t.sleep(.1)
k.block_key('win')
t.sleep(.1) 
k.block_key('ctrl')
t.sleep(.1)

pa.typewrite('kkkkkkkkkkk valeu, flw ')
pa.press('enter')

t.sleep(1)
pa.typewrite('DESLIGANDO EM...')
pa.press('enter')

t.sleep(1)
pa.typewrite('3')
pa.press('enter')

t.sleep(1)
pa.typewrite('2')
pa.press('enter')

t.sleep(1)
pa.typewrite('1')
pa.press('enter')

t.sleep(1)

pa.hotkey('win','d')
t.sleep(.1)
pa.click(1,1,button='left', clicks=1, interval=0.0, duration=0.0)
t.sleep(.1)
pa.hotkey('alt','f4')
t.sleep(.1)
pa.press('enter')

