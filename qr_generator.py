import qrcode
import json
import os
from PIL import Image

with open("products.json") as f:
    products = json.load(f)

base_url = "http://192.168.0.105:5000/product/"
os.makedirs("qrcodes", exist_ok=True)

logo = Image.open("static/logo.png")  # your logo path
logo = logo.resize((60, 60))

for pid, data in products.items():
    url = base_url + pid

    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make()

    img = qr.make_image(fill="black", back_color="white").convert("RGB")

    # Add logo in center
    pos = ((img.size[0] - logo.size[0]) // 2,
           (img.size[1] - logo.size[1]) // 2)

    img.paste(logo, pos)

    img.save(f"qrcodes/{pid}.png")

    print(f"QR created for {pid}")

print("QR with logo generated!")