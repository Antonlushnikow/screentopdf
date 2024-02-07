from PIL import Image, ImageGrab
from pyautogui import press
import time
import configparser

config = configparser.ConfigParser()

config.read('settings.ini')
settings = config['main']
BOOK_LENGTH = int(settings['book_length'])
X1 = int(settings['left_top_x'])
Y1 = int(settings['left_top_y'])
X2 = int(settings['right_bottom_x'])
Y2 = int(settings['right_bottom_y'])
PAUSE_START = int(settings['pause_start'])
PAUSE_BETWEEN = int(settings['pause_between'])
DOC_NAME = settings['doc_name']
ACTION = settings['action']

time.sleep(PAUSE_START)

box = (X1, Y1, X2, Y2)
im_list = []

doc = Image.new('RGB', (1, 1))

for i in range(0, BOOK_LENGTH):
    press(ACTION)
    time.sleep(PAUSE_BETWEEN)
    im = ImageGrab.grab(bbox=box).convert('RGB')
    im_list.append(im)

doc.save(f"{DOC_NAME}.pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list)
