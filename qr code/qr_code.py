import qrcode
import qrcode.constants

text = input("URL: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=2
)

qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")
