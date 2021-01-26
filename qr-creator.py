import qrcode
from PIL import Image

# Create qr-code and configure size
qr = qrcode.QRCode()
# qr = qrcode.QRCode(box_size=50, border=2) # Can be used if size needs to be adjusted
qr.add_data("*Insert any text you desire*")

# Configure output and color schemes
img = qr.make_image(fill_color="black", back_color="white")
img.save("Filename.png")
# img.show()

# Additional settings for custom image inside qr code

# Path for additional image
path = "C:\Path\To\Logo.png"

# Add layer to insert custom image
layer = Image.open("Filename.png")
layer = layer.convert("RGBA")

# Open additional image
logo = Image.open(path)
box = (135, 135, 235, 235)

# Resize image to fit in qr code
layer.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))

# Insert image in qr code
img.paste(region, box)

# Show result
img.show()
