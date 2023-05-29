from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
import mysql.connector

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(300, 200, 400, 200)

        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 30)
        self.username_input = QLineEdit(self)
        self.username_input.move(150, 30)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 70)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.move(150, 70)

        self.login_button = QPushButton("Login", self)
        self.login_button.move(150, 120)
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        try:
            db = mysql.connector.connect(
                host="localhost:3306",
                user="your_username",
                password="your_password",
                database="users"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM accounts WHERE username = %s AND password = %s", (username, password))
            account = cursor.fetchone()

            if account:
                QMessageBox.information(self, "Success", "Login successful!")
            else:
                QMessageBox.warning(self, "Error", "Invalid username or password.")

            db.close()

        except mysql.connector.Error as error:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {error}")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
