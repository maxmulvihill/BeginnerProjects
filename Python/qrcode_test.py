import qrcode
import os
from sys import platform

data = "https://maxmulvihill.me"

img = qrcode.make(data)

cwd = os.getcwd()
if platform == "win32":
    imgname = "\qrcodetest.png"
else:
    imgname = "/qrcodetest.png"

img.save(cwd + imgname)
