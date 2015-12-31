#Import the Cloudinary library for uploading pictures
import cloudinary
import cloudinary.uploader
import cloudinary.api
#Import the pyperclip library for putting the URL into the clipboard
import pyperclip
#Import the glob library for directory sifting
import glob
#Import the time library for pausing
import time
#import the os library for deleting files after they have been uploaded online
import os
#Import the webbrowser library for opening the direct URL to the uploaded image.
import webbrowser
#Login to the Cloudinary API
cloudinary.config(cloud_name = "scarabcoder", api_key = "345834587964339", api_secret = "dIR0j-1c5LA1-tYLLqi3Zv_uhP8")
#Every 1 second, check for images in the directly and loop through each one.
while True:
    time.sleep(1)
    #glob.glob allows you to get a list of files as a string
    for file in glob.glob("*[.jpg, .png, .jpeg, .gif]"):
        #Upload the image; it returns the URL as well as other things, so we save that to the variable "uploaded"
        uploaded = cloudinary.uploader.upload(file)
        #Print the URL in case we need to get that later
        os.system("notify-send \"Image Uploader\" \"" + uploaded.get("original_filename") + " uploaded, URL in clipboard\"")
        print "Uploaded " + uploaded.get("original_filename") + ": " + uploaded.get("url")
        #Copies the URL to clipboard
        pyperclip.copy(uploaded.get("url"))
        #Deletes the image in the folder.
        #TODO possibly keep the image there, and instead make a list of already uploaded images
        #for it to skip for uploading. It might take longer to loop through though.
        os.remove(file)
