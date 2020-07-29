import pyautogui as pg
import time

def clickOnScreen(xCordinate,yCordinate):
  while True:
      try:
          pg.click(x=xCordinate,y=yCordinate)
          time.sleep(5)
      except KeyBoardInterrupt:
          exit()
          
clickOnScreen(1123,543)          
        
  
  

  
