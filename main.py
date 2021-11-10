from selenium import webdriver
from time import sleep
from os import listdir, mkdir, chdir, remove
from os.path import isdir, isfile
from shutil import rmtree
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from binascii import hexlify
from imageio import mimsave as gif_save, imread as screen_read


if not isfile('donatty.secret'):
    print('Donatty token not found.')
    exit(1)

with open('donatty.secret') as file:
    donatty = file.read()

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(donatty)
driver.set_window_size(800, 210)
sleep(5)
if isdir('screens'):
    rmtree('screens')
if isfile('output.gif'):
    remove('output.gif')
mkdir('screens')
chdir('screens')
for i in tqdm(range(400)):
    screen_id = hexlify(int.to_bytes(i, length=2, byteorder='big')).decode()
    driver.save_screenshot(f'screen-{screen_id}.png')
    sleep(1/30)
driver.close()

images = []

for filename in tqdm(sorted(listdir())):
    images.append(screen_read(filename))
chdir('..')
gif_save('output.gif', images, fps=10)
