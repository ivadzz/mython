import keyboard as k
import pyautogui as pa
import time as t
pa.FAILSAFE = False

t.sleep(5)
k.block_key('f4')
t.sleep(.1)
k.block_key('win')
t.sleep(.1) 
k.block_key('ctrl')
t.sleep(.1)
k.block_key('alt')
t.sleep(.1)
k.block_key('tab')
t.sleep(.1)
pa.moveTo(0,700,500)



