import secrets
import qrcode
import secrets

class QR:
    def __init__(self, text: "str") -> None:
        self.text = text
        self.filename = secrets.token_hex(10)+".png"
        self.qr = qrcode.QRCode(version=12, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=2, border=8)
        self.qr.add_data(text)
        self.qr.make()
        self.image = self.qr.make_image(fill_color="#d9dddc", back_color="#311432")

    def save(self, filename=''):
        if not filename:
            self.image.save(self.filename)
        else:
            self.image.save(filename)