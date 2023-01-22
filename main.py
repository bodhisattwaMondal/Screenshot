# This app will take screenshot 
from PIL import ImageGrab
import time
import os

def takeScreenshot():
    time.sleep(5) # The code will stop here for 5 sec. In this 5 sec move to the desired window of which you want to take the screenshot.

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','sc.png') # Fetching the desktop dir.
    image = ImageGrab.grab()
    image.save(desktop,'png') # Image will be saved to the desktop dir.
    print("Screenshot Taken, Check your desktop !!")

# Driver Code :
def main():
    takeScreenshot();

if __name__ == '__main__':
    main()

"""
 Requirments : 
 1. pillow Module : pip install pillow
 2. time module (built-in module)
 3. os module (built-in module)
"""