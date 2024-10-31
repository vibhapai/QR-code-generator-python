import qrcode as qr
img=qr.make("https://www.accenture.com/c")
img.save("accenture.png")