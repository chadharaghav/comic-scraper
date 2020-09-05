# SCRIPT FOR MAKING 'CONFIG.INI' FILE 

import os
import configparser


def makeConfig():

	appdata_path = os.getenv('APPDATA')

	folder_path = os.path.join(appdata_path , 'Comic Viewer')

	if (not os.path.isdir(folder_path)):
			os.makedirs(folder_path)

	config_path = os.path.join(folder_path, 'config.ini')

	config = configparser.ConfigParser()

	file = config_path
	# print(file)
	config.read(file)

	PATH1 = folder_path
	# print(PATH1)
	PATH2 = PATH1 + '\Comics'
	# print(PATH2)
	PATH3 = PATH1 + '\Favourites'
	# print(PATH3)
	
	config.set('DEFAULT', 'THEME' , 'dark')
	config.set('DEFAULT', 'MAINFOLDER_PATH' , PATH1)
	config.set('DEFAULT', 'COMICS_PATH' , PATH2)
	config.set('DEFAULT', 'FAVOURITES_PATH' , PATH3)


	with open(file , "w") as f:
		config.write(f)