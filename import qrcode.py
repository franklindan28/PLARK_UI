import qrcode
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Generate the QR code with a border
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=10)
        qr.add_data('https://www.example.com')  # Your data for the QR code
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save('qrcode.png')  # Save the QR code as an image

        # Create a QLabel to display the QR code
        self.qr_label = QLabel(self)
        pixmap = QPixmap('qrcode.png')
        self.qr_label.setPixmap(pixmap)
        self.qr_label.setScaledContents(True)
        self.setCentralWidget(self.qr_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
