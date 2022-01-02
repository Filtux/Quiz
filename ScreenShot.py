import pyscreenshot
  
# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image = pyscreenshot.grab(bbox=(100, 100, 300, 300)) #set to quiz box parameters
  
# To view the screenshot
image.show()
  
# To save the screenshot
image.save("C:\PythonScripts\Quiz\liveTeamPosition.png")

