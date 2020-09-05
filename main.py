from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import datetime
import time
import webbrowser
import shutil
import sys
import configparser

from comic_scraper import *
from make_config import *
from load_config import *



# FOR CHECKING IF CONNECTED TO THE INTERNET
def working_internet():
	try:
		urllib.request.urlopen('http://google.com')
		return True
	except:
		return False

if not working_internet():
	temp = Tk()
	temp.withdraw()
	messagebox.showwarning("NO INTERNET!", "THIS APPLICATION REQUIRES A WORKING INTERNET CONNECTION!")
	sys.exit(0)



# FOR SETTING THE THEME !!
if THEME == "dark":
	BGCOLOR = "black"
	FGCOLOR = "white"

elif THEME == "light":
	BGCOLOR = "white"
	FGCOLOR = "black"

elif THEME == "red on black":
	BGCOLOR = "black"
	FGCOLOR = "red"

elif THEME == "blue on black":
	BGCOLOR = "black"
	FGCOLOR = "blue"



# FOR FETCHING COMICS FROM RESPECTIVE WEBSITES / SOURCES (FUNCTIONS DEFINED IN 'COMIC_SCRAPER.PY')
def fetch_all():

	fetch_xkcd()
	fetch_smbc()
	fetch_dilbert()
	fetch_calvinHobbes()
	fetch_threeWordPhrase()


def make_directory():	
	if (not os.path.isdir(FAVOURITES_PATH)):
		os.makedirs(FAVOURITES_PATH)
	if (not os.path.isdir(COMICS_PATH)):
		os.makedirs(COMICS_PATH)


fetch_all()       # UNCOMMENT THIS (IF COMMENTED) , BEFORE EXECUTING THE PROGRAM
make_directory()


TODAY = '(' + str(datetime.date.today()) + ')'   

# PATHS FOR COMICS
CALVINHOBBES =  COMICS_PATH + "/calvin and hobbes" + TODAY + ".jpeg"
DILBERT = COMICS_PATH + "/dilbert" + TODAY + ".jpeg"
SMBC = COMICS_PATH + "/smbc" + TODAY + ".jpeg"
XKCD = COMICS_PATH + "/xkcd" + TODAY + ".jpeg"
THREEWORDPHRASE = COMICS_PATH + "/three word phrase" + TODAY + ".jpeg"



root = Tk()
root.title("Comic Viewer 1.0")
root.iconbitmap('icon.ico')
root.configure(bg=BGCOLOR)


# FOR OPENING THE DOWNLOADED COMICS USING 'PILLOW'
OPEN_CALVINHOBBES = ImageTk.PhotoImage(Image.open(CALVINHOBBES))
OPEN_DILBERT = ImageTk.PhotoImage(Image.open(DILBERT))
OPEN_SMBC = ImageTk.PhotoImage(Image.open(SMBC).resize((450,600)))
OPEN_XKCD = ImageTk.PhotoImage(Image.open(XKCD))
OPEN_THREEWORDPHRASE = ImageTk.PhotoImage(Image.open(THREEWORDPHRASE))


# FOR CYCLING THROUGH THE COMICS IN THE VIEWER
COMIC_LIST = [OPEN_CALVINHOBBES, OPEN_DILBERT, OPEN_XKCD, OPEN_SMBC, OPEN_THREEWORDPHRASE]
COMICPATH_LIST = [CALVINHOBBES, DILBERT, XKCD, SMBC, THREEWORDPHRASE]
TITLE_LIST = ['Calvin And Hobbes', 'Dilbert' , 'XKCD' , 'Saturday Morning Breakfast Cereal' , 'Three Word Phrase']
LIST_FLAG = 0
MAX = 4


# THIS FUNCTION JUST ADDS THE CURRENT DISPLAYED COMIC TO THE 'FAVOURITES' FOLDER
def add_favourite():
	global COMIC_LIST
	global LIST_FLAG

	if (not os.path.isdir(FAVOURITES_PATH)):
		os.makedirs(FAVOURITES_PATH)

	shutil.copy(COMICPATH_LIST[LIST_FLAG], FAVOURITES_PATH)

	message = TITLE_LIST[LIST_FLAG].upper() + ' WAS ADDED TO FAVOURITES!'
	messagebox.showinfo('INFORMATION', message)




#*************************************************** TOOLBAR *************************************************** 

# OPENS THE OFFICIAL WEBSITES OF THE COMICS IN A BROWSER WINDOW
def web_calvinHobbes():
	webbrowser.open('https://www.calvinandhobbes.com/about-calvin-and-hobbes/', new=2)

def web_Dilbert():
	webbrowser.open('https://dilbert.com/' , new=2)

def web_XKCD():
	webbrowser.open('https://xkcd.com/' , new=2)

def web_SMBC():
	webbrowser.open('https://www.smbc-comics.com/' , new=2)

def web_TWP():
	webbrowser.open('http://threewordphrase.com/' , new=2)


# FOR UPDATING THE COMICS MANUALLY
def refreshComics():
	fetch_all()
	messagebox.showinfo("UPDATE COMPLETE!", "LATEST COMICS HAVE BEEN DOWNLOADED!")



# DELETES ALL THE DOWNLOADED COMICS FROM THE 'COMIC VIEWER / COMICS' FOLDER
def clear_comics():
	response = messagebox.askyesno("DELETE COMICS" , "DELETE ALL FETCHED COMICS?")

	if response == 1:
		for root, dirs, files in os.walk(COMICS_PATH):
		    for f in files:
		        os.unlink(os.path.join(root, f))
		    for d in dirs:
		        shutil.rmtree(os.path.join(root, d))


# DELETES ALL OF THE COMICS ADDED TO THE 'COMIC VIEWER / FAVOURITES' FOLDER
def clear_favourites():
	response = messagebox.askyesno("DELETE FAVOURITES" , "DELETE ALL FAVOURITE COMICS?")

	if response == 1:
		for root, dirs, files in os.walk(FAVOURITES_PATH):
		    for f in files:
		        os.unlink(os.path.join(root, f))
		    for d in dirs:
		        shutil.rmtree(os.path.join(root, d))


# OPENS README.TXT
def open_readme():
	pass


# FOR CHANGING THE THEME OF THE VIEWER
def set_theme(theme):
	config = configparser.ConfigParser()
	file = config_location
	config.read(file)
	config.set('DEFAULT', 'THEME', theme)
	with open(file , 'w') as f:
		config.write(f)
	messagebox.showinfo('RESTART REQUIRED' , 'RESTART APPLICATION FOR THE CHANGES TO TAKE PLACE!')


# FOR CHANGING THE DIRECTORY WHERE THE FILES ARE SAVED
def change_dir():
	new_dir = filedialog.askdirectory()
	mainfolder_path = new_dir + '/Comic Scraper'
	comics_path = mainfolder_path + '/Comics'
	favourites_path = mainfolder_path + '/Favourites'

	config = configparser.ConfigParser()
	file = config_location
	config.read(file)
	config.set('DEFAULT' , 'MAINFOLDER_PATH', mainfolder_path)
	config.set('DEFAULT' , 'COMICS_PATH', comics_path)
	config.set('DEFAULT' , 'FAVOURITES_PATH', favourites_path)
	with open(file, 'w') as f:
		config.write(f)


# ADDING THE TOOLBAR TO THE GUI
toolbar = Menu(root)
root.config(menu=toolbar)

file = Menu(toolbar, tearoff=0)
toolbar.add_cascade(label="File", menu=file)
file.add_command(label="open README.TXT...", command=open_readme)
file.add_command(label="Update Comics", command=refreshComics)
file.add_command(label="Add To Favourites", command=add_favourite)
file.add_separator()
file.add_command(label="CLEAR 'COMICS' FOLDER", command=clear_comics)
file.add_command(label="CLEAR 'FAVOURITES' FOLDER", command=clear_favourites)
file.add_command(label="CHANGE DIRECTORY...", command=change_dir)
file.add_separator()
file.add_command(label="EXIT", command=root.quit)

change_theme = Menu(toolbar, tearoff=0)
toolbar.add_cascade(label="Change Theme", menu=change_theme)
change_theme.add_command(label="dark", command=lambda: set_theme('dark'))   
change_theme.add_command(label="light", command=lambda: set_theme('light'))		
change_theme.add_command(label="red on black", command=lambda: set_theme('red on black'))
change_theme.add_command(label="blue on black", command=lambda: set_theme('blue on black'))


official_websites = Menu(toolbar, tearoff=0)
toolbar.add_cascade(label="Visit Official Website...", menu=official_websites)
official_websites.add_command(label="Calvin and Hobbes", command=web_calvinHobbes)
official_websites.add_command(label="Dilbert", command=web_Dilbert)
official_websites.add_command(label="XKCD", command=web_XKCD)
official_websites.add_command(label="Saturday Morning Breakfast Cereal", command=web_SMBC)
official_websites.add_command(label="Three Word Phrase", command=web_TWP)



# *************************************************** TITLE FRAME *************************************************** 
title_frame = LabelFrame(root, bg=BGCOLOR)
title_frame.grid(row=0, column=0, padx=10, pady=2.5)
title_frame.config(borderwidth=0)

title = TITLE_LIST[LIST_FLAG]
title_label = Label(title_frame, text=title , bg=BGCOLOR, fg=FGCOLOR)
title_label.config(font=('Comic Sans', 25))
title_label.grid(row=0, column=0)

# FOR UPDATING THE TITLE
def update_title():
	global LIST_FLAG
	global title_label
	title_label.grid_forget()
	title = TITLE_LIST[LIST_FLAG]
	title_label = Label(title_frame, text=title , bg=BGCOLOR, fg=FGCOLOR)
	title_label.config(font=('Comic Sans', 25))
	title_label.grid(row=0, column=0)




# *************************************************** COMIC FRAME *************************************************** 
comic_frame = LabelFrame(root, bg=BGCOLOR)
comic_frame.config(borderwidth=5)
comic_frame.grid(row=1, column=0, padx=10, pady=2.5)
comic_label = Label(comic_frame, image=OPEN_CALVINHOBBES)
comic_label.grid(row=0, column=0, padx=10, pady=10)




#***************************************************  BUTTON COMMANDS ***************************************************  

# DEFINING WHAT A BUTTON CLICK DOES

# DISPLAYS THE PREVIOUS COMIC
def prev_comic(event = None):
	global comic_label
	global comic_frame
	global LIST_FLAG

	if LIST_FLAG == 0:
		pass

	else:
		comic_label.grid_forget()
		comic_label = Label(comic_frame, image=COMIC_LIST[LIST_FLAG - 1])
		comic_label.grid(row=0, column=0, padx=10, pady=10)
		LIST_FLAG = LIST_FLAG - 1
		update_title()
		update_counter()


# DISPLAYS THE NEXT COMIC
def next_comic(event = None):
	global comic_label
	global comic_frame
	global LIST_FLAG

	if LIST_FLAG == MAX:
		pass

	else:
		comic_label.grid_forget()
		comic_label = Label(comic_frame, image=COMIC_LIST[LIST_FLAG + 1])
		comic_label.grid(row=0, column=0, padx=10, pady=10)
		LIST_FLAG = LIST_FLAG + 1
		update_title()
		update_counter()




# *************************************************** BUTTON FRAME *************************************************** 
button_frame = LabelFrame(root, background=BGCOLOR, foreground=FGCOLOR)
button_frame.config(borderwidth=0)
button_frame.grid(row=2, column=0, padx=10, pady=15)

filler_one = Label(button_frame, text="                   ", background=BGCOLOR, foreground=FGCOLOR)
filler_two = Label(button_frame, text="                   ", background=BGCOLOR, foreground=FGCOLOR)

prev_button = Button(button_frame, text="<<", command=prev_comic, background=BGCOLOR, foreground=FGCOLOR)
prev_button.config(width=5, font=5, borderwidth=0)
prev_button.grid(row=0, column=0)
filler_two.grid(row=0,column=1)
root.bind('<Left>', prev_comic)

favourite_button = Button(button_frame, text="ADD TO FAVOURITE! <3", command=add_favourite, background=BGCOLOR, foreground=FGCOLOR)
favourite_button.config(font=5, borderwidth=0)
favourite_button.grid(row=0, column=2)
filler_one.grid(row=0,column=3)

next_button = Button(button_frame, text=">>", command=next_comic, background=BGCOLOR, foreground=FGCOLOR)
next_button.config(width=5, font=5, borderwidth=0)
next_button.grid(row=0, column=4)
root.bind('<Right>', next_comic)


# *************************************************** COUNTER *************************************************** 
counter_frame = LabelFrame(root, background=BGCOLOR, foreground=FGCOLOR)
counter_frame.config(borderwidth=0)
counter_frame.grid(row=2, column=1, padx=10, pady=15)

status = str(LIST_FLAG + 1) + "/" + str(MAX + 1) 
counter_label = Label(counter_frame , text=status , background=BGCOLOR, foreground=FGCOLOR)
counter_label.config(font=10)
counter_label.grid(row=0, column=0)

def update_counter():
	global counter_label
	global LIST_FLAG
	global MAX
	counter_label.grid_forget()
	status = str(LIST_FLAG + 1) + "/" + str(MAX + 1) 
	counter_label = Label(counter_frame , text=status , background=BGCOLOR, foreground=FGCOLOR)
	counter_label.config(font=10)
	counter_label.grid(row=0, column=0)



root.mainloop()