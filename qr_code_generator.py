import qrcode
import image

qr = qrcode.QRCode(
    version=15,  # level of complicated image
    box_size=10,  # size of displaying qr code
    border=5
)
data = "https://github.com/abi-lilone"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="red")
img.save("abi98.png")
