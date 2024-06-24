import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=6yEqkRyrpXo&t=1135s")
img.save("qr.png", "PNG")