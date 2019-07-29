import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import pandas as pd
import glob2
import os
import random


def convert2hdf(source_dir, desti_dir='./'):
    temp = []
    for path_name in glob2.iglob(source_dir+'**/*.txt', recursive=True):
        _, file_name = os.path.split(path_name)
        file_name = file_name.split(".")[0]
        file_name = ''.join([i for i in file_name if not i.isdigit()])
        file_name = file_name.replace("_","")
        data = open(path_name, "r").read()
        temp.append([file_name,data])
    df = pd.DataFrame(temp, columns=["file_name", "data"])
    print(df)
    hdf_name = desti_dir + "/data.h5"
    df.to_hdf(hdf_name, key="df")

def printer(file):
    os.system("lpr -o page-left=60 -o page-right=60 -o page-top=90 -o page-bottom=90 -P HP_LaserJet_1020_1 {}".format(file))

def do_some(channel):
	global root_path
	txtDir = root_path + "/data"
	hdf_name = root_path + '/data.h5'
	# convert2hdf(txtDir, desti_dir=root_path)
	df = pd.read_hdf(hdf_name, 'df')
	index = random.randint(0,len(df))
	text = df.ix[index,'file_name'] + "\n\n" + df.ix[index,'data']
	print(text)
	file_name = _name=root_path+"/output.txt"
	with open(file_name, "w") as text_file:
	    text_file.write(text)
	
	printer(file_name)

def shutdown(channel):
    os.system("sudo shutdown -h now")
   
def restart(channel):
    os.system("sudo shutdown -r now")

    
global root_path
root_path = "/home/pi/Desktop/Exhib"
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# printing button
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

# shutdown button
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# restart button
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(10, GPIO.RISING, callback = do_some, bouncetime = 2000)
GPIO.add_event_detect(16, GPIO.RISING, callback = shutdown, bouncetime = 2000)  
GPIO.add_event_detect(22, GPIO.RISING, callback = restart, bouncetime = 2000) 
# message = input("Press enter to quit\n\n") # Run until someone presses enter
# GPIO.cleanup() # Clean up
while True:
    pass
