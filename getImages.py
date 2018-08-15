from selenium import webdriver
import time
from PIL import Image
import random
import string
import os

def getImages(searchitem):
	l = []
	
	reader = open(searchitem + '.csv', 'rb').read().splitlines()
	for row in reader:
		l.append(row)
		
	if not os.path.exists(searchitem):
		os.mkdir(searchitem)
	
	#dOwnloadlIst = l[2:10]
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	driver = webdriver.Chrome(chrome_options=options)
	#print(*dOwnloadlIst)
	
	for i in range(len(l)):
		driver.get(l[i+1].decode('utf-8'))
		time.sleep(5)
		element = driver.find_element_by_tag_name('img')
		location = element.location_once_scrolled_into_view
		size = element.size
		iMgnAme = searchitem + '\\' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.png'
		driver.save_screenshot(iMgnAme) 
		print('Saving ' + iMgnAme + ': \n')
		
		image = Image.open(iMgnAme)
		left = location['x']
		top = location['y']
		right = location['x'] + size['width']
		bottom = location['y'] + size['height']
		image = image.crop((left, top, right, bottom))  # defines crop point
        image.convert("RGB");
		image.save(searchitem + '\\'+''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg' , 'JPEG' )  # saves new cropped image
		os.remove(iMgnAme)
            
	driver.close()