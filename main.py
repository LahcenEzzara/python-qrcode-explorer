import segno

qrcode = segno.make('Hello, world!', micro=False)

qrcode.save('qrcode.svg', border=1, scale=10, light=None)

qrcode.save('qrcode.png', border=1, scale=10)