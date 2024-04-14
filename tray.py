import os
import time
from pystray import Icon as icon, MenuItem as item, Menu as menu
from PIL import Image

def stop_script(icon, item):
    open('stop.txt', 'w').close()  # Signal the numlock.py script to stop
    time.sleep(0.5)
    os.remove('stop.txt')
    icon.stop()  # Stop the icon and exit

def create_image():
    # Load an image for the icon
    return Image.open('tray.png')

if __name__ == "__main__":
    # Set up the system tray icon with a menu to stop the script
    icon = icon('test_icon', create_image(), menu=menu(item('Stop', stop_script)))
    icon.run()
