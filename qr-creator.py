import qrcode
from PIL import Image

# Create qr-code and configure size
qr = qrcode.QRCode(box_size=50, border=2)
qr.add_data("*Beliebigen Inhalt einfügen*")

# Configure output and color schemes
img = qr.make_image(fill_color="black", back_color="white")
img.save("Filename.png")
img.show()
