# Take a series of time-lapse images using picamera2 and save them to a directory
# with a timestamped filename.
# This script is intended to be run on a Raspberry Pi with a camera module.
# It requires the picamera2 library.

# initially draws from https://randomnerdtutorials.com/raspberry-pi-picamera2-python/#take-photo-picamera2

from picamera2 import Picamera2
import time
import os

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

output_dir_prefix = "../img/time_lapse_"
output_dir = output_dir_prefix + time.strftime("%Y%m%d-%H%M%S")
# make directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Set the time between photos in seconds
time_between_photos = 1
# Set the number of photos to take
number_of_photos = 100

# Make a loop to take a series of photos
picam2.start()
for i in range(number_of_photos):
    picam2.capture_file(output_dir + "/photo" + str(i).zfill(4) + ".jpg")
    # write the image number and time to nearest ms to a csv file
    with open(output_dir + "/photo_times.csv", "a") as f:
        f.write(str(i) + "," + time.strftime("%Y%m%d-%H%M%S") + "," + str(time.time()) + "\n")
    time.sleep(time_between_photos)



