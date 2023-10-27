import pyautogui
from pynput.mouse import Listener

class Photo:
  def __init__(self):
    self.count = 0

  def take_photo(self, x, y):
    my_screen = pyautogui.screenshot(region=(x - 10, y -10, 20, 20))
    path = 'icons_test/icon_{}.png'.format(self.count)
    self.count = self.count + 1
    my_screen.save(path)
  
  # Mouse left click: take a picture of the mouse position (20x20 pixels)
  # Mouse right click: stop this program
  def click(self, x, y, button, pressed):
    if button.name == 'right':
      return False
    if pressed:
      self.take_photo(x, y)

photo = Photo()

with Listener(on_click=photo.click) as listener:
  listener.join()
