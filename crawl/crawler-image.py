import requests
import os

def saveImage(postUrl):
    # 儲存路徑
    path = r""
    if(os.path.exists(path) == False):
        os.makedirs(path)
    getImage = requests.get(postUrl)
    image = getImage.content
    imageSave = open(path + "\img.png", "wb")
    imageSave.write(image)
    imageSave.close()

# 要抓的圖片路徑
postUrl = ""
saveImage(postUrl)