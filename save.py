from ahk import AHK
import time
import cv2
import cmpimg
#import capscr
import PIL.ImageGrab

loc = {
        "page1": (960,740),
        "page2": (1170,735),
        "fight": (1210,720),
        "challenge":(1060,635),
        "result": (1315,750)
}

act = {
        "go": (1210,530),
        "challenge":(1060,635),
        "fight": (1210,720)
}

ahk=AHK()
offset=0

def sfd_click(ahk,xx):
    x=xx[0]
    y=xx[1]
    ahk.click(x,y)
    time.sleep(0.1)
    ahk.click(x,y)

def saveIcon(im,xx,path):
    #im = PIL.ImageGrab.grab()
    x=xx[0]+offset
    y=xx[1]+offset
    crop=im.crop((x,y,x+32,y+32))
    crop.save(path)

def cmpCurrentAct(xx,refPic):
    x=xx[0]+offset
    y=xx[1]+offset
    im = PIL.ImageGrab.grab()
    crop=im.crop((x,y,x+32,y+32))
    crop.save("./res/chk.png")
    compare_image = cmpimg.CompareImage(refPic, './res/chk.png')
    image_difference = compare_image.compare_image()
    print (image_difference)
    return image_difference


print("SFD")
time.sleep(0.2)
win = ahk.win_get(title=b'BlueStacks')
win.to_top()
win.activate()
win.show()
#sfd_click(ahk,(offset+500,60))

im = PIL.ImageGrab.grab()
#saveIcon(im,loc["page1"],"./res/page1.png")
#saveIcon(im,loc["page2"],"./res/page2.png")
#saveIcon(im,loc["fight"],"./res/fight.png")
#saveIcon(im,loc["challenge"],"./res/challenge.png")
#saveIcon(im,loc["result"],"./res/result.png")
