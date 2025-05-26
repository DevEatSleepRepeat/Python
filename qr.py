# basic_qrcode.py
from PIL import Image
import segno

qrcode = segno.make_qr("S")
qrcode.save(
    "scaled_qrcode.png",
    scale=10,
)
img = Image.open('qr.png')
img.show()