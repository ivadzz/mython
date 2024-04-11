import pyautogui as pa
import time as t


pa.press('win')
t.sleep(1)
pa.typewrite('cmd')
t.sleep(1)
pa.press('enter')
t.sleep(1)
pa.hotkey('win','right')
t.sleep(1)
pa.press('enter')
t.sleep(1)
pa.hotkey('alt','tab')
t.sleep(1)
pa.typewrite('start https://acesse.dev/OVGn7')
t.sleep(1)
pa.press('enter')
t.sleep(1)
pa.hotkey('win','left')
t.sleep(1)
pa.click(1048, 238, button='left', clicks=1, interval=0.0, duration=0.0)
t.sleep(1)
for a in range(1000):
    pa.moveTo(1,1)
    pa.press('space')

