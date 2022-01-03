import pyscreenshot
import telebot

image = pyscreenshot.grab(bbox=(479, 57, 879, 561)) #set to quiz box parameters
image.save("liveTeamPosition.png") #save it in a folder
image = open('liveTeamPosition.png', 'rb')
