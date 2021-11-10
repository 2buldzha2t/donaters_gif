from selenium import webdriver
from time import sleep
from os import listdir, mkdir, chdir, remove
from os.path import isdir, isfile
from shutil import rmtree
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from binascii import hexlify
from imageio import mimsave as gif_save, imread as screen_read

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
url = "https://widgets.donatty.com/stats/?ref=d1a1acc8-e047-4a49-adf1-e1e3aed64d5e&token=6UoXLFXaM6zHfmw0v1vLO1sVwe5cmd"
driver.get(url)
driver.set_window_size(800, 800)
sleep(5)
if isdir('screens'):
    rmtree('screens')
if isfile('output.gif'):
    remove('output.gif')
mkdir('screens')
chdir('screens')
for i in tqdm(range(300)):
    screen_id = hexlify(int.to_bytes(i, length=2, byteorder='big')).decode()
    driver.save_screenshot(f'screen-{screen_id}.png')
    sleep(1/30)
driver.close()

images = []

for filename in tqdm(sorted(listdir())):
    images.append(screen_read(filename))
chdir('..')
gif_save('output.gif', images, fps=10)
