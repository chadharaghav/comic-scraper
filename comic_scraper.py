# SCRIPT FOR DOWNLOADING THE COMICS

import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import os

from load_config import *


# CURRENTLY WORKING COMICS
# 1. XKCD
# 2. THREE WORD PHRASE    
# 3. DILBERT
# 4. SATURDAY MORNING BREAKFAST CEREAL
# 5. CALVIN AND HOBBES



# HEADERS
hdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


TODAY = '(' + str(datetime.date.today()) + ')'
SMBC = 'smbc' + TODAY + '.jpeg'
DILBERT = 'dilbert' + TODAY + '.jpeg'
CALVINHOBBES = "calvin and hobbes" + TODAY + ".jpeg"
THREEWORDPHRASE = "three word phrase" + TODAY + ".jpeg"
XKCD = 'xkcd' + TODAY + '.jpeg'


def fetch_xkcd():
	source = requests.get('https://xkcd.com/').text
	soup = BeautifulSoup(source, 'lxml')
	comic_div = soup.find('div' , {"id": "comic"})                                                                                               
	comic = comic_div.find('img')
	path = "https:" + comic['src']

	file_path = os.path.join(COMICS_PATH , XKCD)
	if not os.path.exists(COMICS_PATH):
		os.makedirs(COMICS_PATH)

	xkcd_file = open(file_path , 'wb')
	xkcd_file.write(urllib.request.urlopen(path).read())
	xkcd_file.close()



def fetch_smbc():
	source = requests.get('https://www.smbc-comics.com/').text
	soup = BeautifulSoup(source, 'lxml')
	comic_div = soup.find('div' , {'id' : 'cc-comicbody'})
	comic = comic_div.find('img')
	path = comic['src']

	file_path = os.path.join(COMICS_PATH , SMBC)
	if not os.path.exists(COMICS_PATH):
		os.makedirs(COMICS_PATH)

	smbc_file = open(file_path , 'wb')
	smbc_file.write(urllib.request.urlopen(path).read())
	smbc_file.close()



def fetch_dilbert():
	source = requests.get('https://dilbert.com/').text
	soup = BeautifulSoup(source, 'lxml')
	comic_div = soup.find('div', {'class' : 'img-comic-container'})
	comic = comic_div.find('img')
	path = "https:" + comic['src']

	file_path = os.path.join(COMICS_PATH , DILBERT)
	if not os.path.exists(COMICS_PATH):
		os.makedirs(COMICS_PATH)

	dilbert_file = open(file_path , "wb")
	dilbert_file.write(urllib.request.urlopen(path).read())
	dilbert_file.close()



def fetch_calvinHobbes():
	temp = str(datetime.date.today())
	flag = temp.split("-")
	year = flag[0]
	month = flag[1]
	day = flag[2]

	url = "https://www.gocomics.com/calvinandhobbes/" + year + "/" + month + "/" + day
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	comic_div = soup.find('div' , {'class' : 'comic__image js-comic-swipe-target'})
	comic = comic_div.a.img
	path = comic['src']

	file_path = os.path.join(COMICS_PATH , CALVINHOBBES)
	if not os.path.exists(COMICS_PATH):
		os.makedirs(COMICS_PATH)

	calvinHobbes_file = open(file_path , "wb")
	calvinHobbes_file.write(urllib.request.urlopen(path).read())
	calvinHobbes_file.close()


def fetch_threeWordPhrase():
	source = requests.get('http://threewordphrase.com/index.htm').text
	soup = BeautifulSoup(source, 'lxml')
	comic_div = soup.find_all('div', {'align' : 'center'})
	comic_div = comic_div[1]
	comic_table = comic_div.find_all('table')
	comic_table = comic_table[1]
	comic = comic_table.img
	path = "http://threewordphrase.com/" + comic['src']

	file_path = os.path.join(COMICS_PATH , THREEWORDPHRASE)
	if not os.path.exists(COMICS_PATH):
		os.makedirs(COMICS_PATH)

	threewordphrase_file = open(file_path, "wb")
	threewordphrase_file.write(urllib.request.urlopen(path).read())
	threewordphrase_file.close()