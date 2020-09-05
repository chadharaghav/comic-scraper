# SCIPT FOR LOADING THE SETTINGS FROM 'CONFIG.INI' FILE

import os
import configparser

from make_config import *


# MAKES 'CONFIG.INI' FILE ONLY IT IF DOES NOT ALREADY EXIST
appdata_path = os.getenv('APPDATA')
config_path = os.path.join(appdata_path, 'Comic Viewer\config.ini')
if not os.path.isfile(config_path):
	makeConfig()


# FOR FETCHING DIFFERENT USER SETTING FROM THE 'CONFIG.INI' FILE!
config_location = config_path
print(config_location)


def get_theme():
	config = configparser.ConfigParser()
	file = config_location
	config.read(file)
	theme = config['DEFAULT']['THEME']
	return theme


def get_mainFolderPath():
	config = configparser.ConfigParser()
	file = config_location
	config.read(file)
	required_path = config['DEFAULT']['MAINFOLDER_PATH']
	return required_path

def get_comicsPath():
	config = configparser.ConfigParser()
	file = config_location
	config.read(file)
	required_path = config['DEFAULT']['COMICS_PATH']
	return required_path

def get_favouritesPath():
	config = configparser.ConfigParser()
	file = config_location
	config.read(file)
	required_path = config['DEFAULT']['FAVOURITES_PATH']
	return required_path


THEME = get_theme()
MAINFOLDER_PATH = get_mainFolderPath()
COMICS_PATH = get_comicsPath()
FAVOURITES_PATH = get_favouritesPath()


# print(THEME)
# print(MAINFOLDER_PATH)
# print(COMICS_PATH)
# print(FAVOURITES_PATH)

