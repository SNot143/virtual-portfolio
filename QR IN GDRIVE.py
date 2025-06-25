import qrcode
from PIL import Image

google_drive_link = "https://drive.google.com/file/d/17U98rhB7SlnHx1H-wA3HBXjRu9gvyBnf/view?usp=sharing"
qr_code_path = "QR IN GDRIVE.png"

def generate_qr_code(link, path):
    qr = qrcode.QRCode(version=3, box_size=7, border=2)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)

generate_qr_code(google_drive_link, qr_code_path)
Image.open(qr_code_path).show()

print("✅ QR code generated:", qr_code_path)