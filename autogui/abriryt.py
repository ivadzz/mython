import keyboard as k
import pyautogui as pa
import time as t
pa.FAILSAFE = False

pa.press('win')
t.sleep(.1)
pa.typewrite('cmd')
t.sleep(.1)
pa.press('enter')
t.sleep(.4)
pa.typewrite('start https://encr.pw/youtube-Ru470zz3kawd2igbf5')
t.sleep(.1)
pa.press('enter')
t.sleep(1)
k.block_key('f4')
t.sleep(.1)
k.block_key('win')
t.sleep(.1) 
k.block_key('ctrl')
t.sleep(.1)
pa.moveTo(0,500,10)
t.sleep(3)