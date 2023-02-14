
import keyboard 
# import selenium
# from selenium import webdriver
import pyautogui
import random






while True:  
    try: 
        if (keyboard.is_pressed('4') 
        or keyboard.is_pressed('r') 
        or keyboard.is_pressed('e')
        or keyboard.is_pressed('1')
        or keyboard.is_pressed('2')
        or keyboard.is_pressed('3')
         ):  


            # driver = webdriver.Chrome()
            # driver.maximize_window()
            # driver.get('https://www.ravbug.com/bsod/bsod10/')
            # keyboard.press_and_release('f11')
            x = random.randint(1, 3400)
            y = random.randint(1, 1400)
            from time import sleep
            
            mylist = [0,0,0,0,1,2,3.5,2.3,1.2,4]
            n = random.choice(mylist)
            print("yooo: ", end = "")
            print(n)
            sleep(n)

            pyautogui.moveTo(x, y, duration=.2)

            
        
    except:
        break