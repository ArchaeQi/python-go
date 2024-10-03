import time,random
import pyautogui,keyboard,pyscreeze

print("长按esc退出脚本")

while True:
    tiaozhan=pyscreeze.locateOnScreen(r".\image\tiaozhan.png", confidence=0.5)
    end=pyscreeze.locateOnScreen(r".\image\end.png", confidence=0.5)
    if end:
        x=end[0]+random.randint(0, end[2])
        y=end[1]+random.randint(0, end[3])
        pyautogui.moveTo(x, y)
        pyautogui.click()
    elif tiaozhan:
        x=tiaozhan[0]+random.randint(0, tiaozhan[2])
        y=tiaozhan[1]+random.randint(0, tiaozhan[3])
        pyautogui.moveTo(x, y)
        pyautogui.click()
    else:
        time.sleep(random.random())
        print("挑战中")
    if keyboard.is_pressed('esc'):
        print("退出成功")
        break