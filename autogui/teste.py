import keyboard as k
import pyautogui as pa
import time as t

pa.press('win')
t.sleep(.1)
pa.typewrite('cmd')
t.sleep(.1)
pa.press('enter')
t.sleep(.4)
pa.typewrite('start https://')
t.sleep(.3)
pa.typewrite('you')
t.sleep(.3)
pa.typewrite('tube')
t.sleep(.3)
pa.typewrite('.c')
t.sleep(.3)
pa.typewrite('om')
t.sleep(.3)
pa.typewrite('.br')
t.sleep(.3)
pa.press('enter')
t.sleep(1)
k.block_key('f4')
t.sleep(.1)
k.block_key('win')
t.sleep(.1) 
k.block_key('ctrl')
t.sleep(.1)
pa.moveTo(0,500,10)
