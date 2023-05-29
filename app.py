import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from flask import Flask, jsonify, request


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.Window2 = NewWindow()

        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("images/trashcashlogosymbolunstrace copy 1.png"))
        self.setStyleSheet("background-color : #FFFAF3")
        #self.setWindowFlag(Qt.FramelessWindowHint)

        layout = QHBoxLayout()
       # widget1 = QListWidget()
        title = QLabel(self)
        title.setText("TrashCash Kiosks")
        title.move(150,40)
        title.resize(500,100)
        title.setStyleSheet("QLabel { font-weight: 900; font-size: 50px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(title)

        greeting= QLabel(self)
        greeting.setText("Hello There")
        greeting.move(150,200)
        greeting.resize(500,100)
        greeting.setStyleSheet("QLabel { font-weight: 900; font-size: 50px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(greeting)

        email= QLineEdit(self)
        email.setText("Email")
        email.move(150,300)
        email.resize(500,70)
        email.setStyleSheet("QLineEdit {  line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px;  box-shadow:50x; padding-left: 24px; }" )
      #  layout.addWidget(username)

        password= QLineEdit(self)
        password.setText("Password")
        password.move(150,400)
        password.resize(500,70)
        password.setStyleSheet("QLineEdit { lineedit-password-character: 9679; line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; position: absolute; box-shadow:50x; padding-left: 24px;}" )
    
        #widget2 = QPlainTextEdit()

        log_btn = QPushButton("Login",self)
        log_btn.setStyleSheet("QPushButton { font-size: 40px; background-color: #0E7470; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" )
        log_btn.setGeometry(150, 500, 500, 70)
        log_btn.clicked.connect(self.add_window)
        layout2 = QHBoxLayout()
        add = QLabel(self)
        add.pixmap = QPixmap('images/trashcashlogosymbolunstrace copy 1.png')
        add.setPixmap(add.pixmap)
        add.resize(add.pixmap.width(),add.pixmap.height())
        add.move(800,200)   # Subjected to change for monitor size
        layout2.addWidget(add)
        self.setLayout(layout2)

    def user_account(self):
        User = [
            {
                "Email": input(" "),
                "Password": input(" ")
            }
        ]
    
    def add_window(self):
        self.Window2.showMaximized()
        self.close()

class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Welcome Screen 1")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.step_1()
        self.step1()
        self.step_2()
        self.step2()
        self.step_3()
        self.step3()
        self.start_btn()
        self.Window3 = NewWindow2()

    def help_btn(self):
        help = help_button = QPushButton(" ", self)
        help_button.setGeometry(20, 20, 55, 55)
        help.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_info.png);  border-radius: 30px;}")
        #help.clicked.connect(self.print)

    def welcome_to_plark(self):
        layout2 = QHBoxLayout()
        #widget1 = QListWidget()
        title2 = QLabel(self)
        title2.setText("Welcome to PLARK")
        title2.move(150,20)
        title2.resize(1000,60)
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setStyleSheet("QLabel { font-weight: 900; font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout2.addWidget(title2)
    
    def additional_info(self):
        layout3 = QHBoxLayout()
        #widget1 = QListWidget()
        title3 = QLabel(self)
        title3.setText("TrashCash Plastic Recovery Kiosk")
        title3.move(150,80)
        title3.resize(1000,60)
        title3.setAlignment(QtCore.Qt.AlignCenter)
        title3.setStyleSheet("QLabel { font-weight: 400; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout3.addWidget(title3)
        
    def logout_btn(self):
        logout = logout_button = QPushButton(" ", self)
        logout_button.setGeometry(1280, 20, 55, 55)
        logout.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_logout.png);  border-radius: 0px;}")
        logout.clicked.connect(self.__init__)

    def step_1(self):
        step_1_info = QLabel(self)
        step_1_info.setText("Put your recyclables""\n""\r\r\r\r\r\r\r\r\r""to PLARK""\n""\r\r\r\r\r\r\r\r\r")
        step_1_info.resize(300,80)
        step_1_info.move(150,565)
        step_1_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_1_extend = QLabel(self)
        step_1_extend.setText("Step 1")
        step_1_extend.move(220,620)
        step_1_extend.resize(150,25)
       # step_1_extend.setAlignment(QtCore.Qt.AlignLeft)
        step_1_extend.setStyleSheet("QLabel { font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
       

    def step1(self):
        step_1 = QLabel(self)
        step_1.pixmap = QPixmap('images/Waste management-rafiki 1.png')
        step_1.setPixmap(step_1.pixmap)
        step_1.resize(step_1.pixmap.width(),step_1.pixmap.height())
        step_1.move(50,160)   # Subjected to change for monitor size

    def step_2(self):
        step_2_info = QLabel(self)
        step_2_info.setText("Our AI will sort""\n""\r\r\r""your plastic""\n""\r\r\r\r\r\r\r\r\r")
        step_2_info.move(620,565)
        step_2_info.resize(300,80)
        step_2_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_extend = QLabel(self)
        step_2_extend.setText("Step 2")
        step_2_extend.move(670,620)
        step_2_extend.resize(150,25)
       # step_2_extend.setAlignment(QtCore.Qt.AlignCenter)
        step_2_extend.setStyleSheet("QLabel { font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def step2(self):
        step_2 = QLabel(self)
        step_2.pixmap = QPixmap('images/Waste management-amico 1.png')
        step_2.setPixmap(step_2.pixmap)
        step_2.resize(step_2.pixmap.width(),step_2.pixmap.height())
        step_2.move(500,160)   # Subjected to change for monitor size


    def step_3(self):
        step_3_info = QLabel(self)
        step_3_info.setText("Earn point and redeem""\n""\r\r\r\r\r\r\r\r\r\r\r\r\r""rewards")
        step_3_info.move(1020,550)
        step_3_info.resize(300,80)
        step_3_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_3_extend = QLabel(self)
        step_3_extend.setText("Step 3")
        step_3_extend.move(1113,620)
        step_3_extend.resize(150,25)
       # step_2_extend.setAlignment(QtCore.Qt.AlignCenter)
        step_3_extend.setStyleSheet("QLabel { font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def step3(self):
        step_1 = QLabel(self)
        step_1.pixmap = QPixmap('images/Subscriber-bro 1.png')
        step_1.setPixmap(step_1.pixmap)
        step_1.resize(step_1.pixmap.width(),step_1.pixmap.height())
        step_1.move(950,160)   # Subjected to change for monitor size
  

    def add_manually(self):
        self.add_manual = QMainWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)
       # self.add_manual.setGeometry(0, 0, 1920, 1080)
        self.add_manual = QLabel(self)
        self.add_manual.setText("Please input your mobile number")
        self.add_manual.setStyleSheet("QLabel {font-weight: 900; font-size: 60px; font-family: Roboto; font-style: normal; color: #0E7470; }" )
      #  self.add_manual.move(440,300)   
      #  self.add_manual.resize(1000,80)
        self.add_manual.setWindowIcon(QIcon("images/trashcash.jpg"))
        self.num_input()
        self.num_btn()
       # self.add_manual.showMaximized()

    def num_input(self):
        num = QLineEdit(self)
        num.setMaxLength(4)
        num.setAlignment(Qt.AlignCenter)
        num.setFont(QFont("Roboto",50))
        num.move(440,400)
        num.resize(1000,100)
        num.setInputMask('09999999999')
        num.setStyleSheet("QLineEdit { background-color: white; border-radius: 20px; }" )

		
    def num_btn(self):
        num_button = QPushButton("Next",self)
        num_button.setStyleSheet("QPushButton { font-size: 40px; background-color: #0E7470; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        num_button.setGeometry(440, 200, 1000, 100)

    def start_btn(self):
        start = start_button = QPushButton("Start", self)
        start_button.setGeometry(0, 670, 1500, 60)
        start.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        start.clicked.connect(self.add_window)

    def add_window(self):
        self.Window3.showMaximized()
        self.close()
       
class NewWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Welcome Screen 2")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn1()
        self.welcome_to_plark1()
        self.logout_btn1()
        self.additional_info1()
        self.deposit_btn1()
        self.next_btn1()
        self.Window4 = NewWindow3()
        self.loginWindow = Login()

    def help_btn1(self):
        help = help_button = QPushButton(" ", self)
        help_button.setGeometry(20, 20, 55, 55)
        help.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_info.png);  border-radius: 30px;}")
        #help.clicked.connect(self.print)

    def welcome_to_plark1(self):
        layout2 = QHBoxLayout()
        #widget1 = QListWidget()
        title2 = QLabel(self)
        title2.setText("Welcome to PLARK")
        title2.move(150,20)
        title2.resize(1000,60)
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setStyleSheet("QLabel { font-weight: 900; font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout2.addWidget(title2)
    
    def additional_info1(self):
        layout3 = QHBoxLayout()
        #widget1 = QListWidget()
        title3 = QLabel(self)
        title3.setText("TrashCash Plastic Recovery Kiosk")
        title3.move(150,80)
        title3.resize(1000,60)
        title3.setAlignment(QtCore.Qt.AlignCenter)
        title3.setStyleSheet("QLabel { font-weight: 400; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout3.addWidget(title3)
        
    def logout_btn1(self):
        logout = logout_button = QPushButton(" ", self)
        logout_button.setGeometry(1280, 20, 55, 55)
        logout.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-image : url(images/material-symbols_logout.png);  border-radius: 0px;}")
        logout.clicked.connect(Login)

    def deposit_btn1(self):
        deposit = deposit_button = QPushButton("Deposit", self)
        deposit_button.setIcon(QIcon('Images/plastic-containers-icon copy 1.png)'))
        #deposit2  = QPushButton(" ", self)
        deposit_button.setGeometry(500, 220, 390, 370)
       # deposit2.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { image : url(images/plastic-container-icon copy 1.png); color: white; background-color: #0E7470;}" )
        deposit.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { padding-top: 40px;  text-align: center; font-family: 'Roboto'; background-color: #0E7470; font-size: 40px;   border-radius: 30px; color: white;}" )
        #start.clicked.connect(self.)

    def next_btn1(self):
        next = next_button = QPushButton("Next", self)
        next_button.setGeometry(0, 670, 1500, 60)
        next.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        next.clicked.connect(self.add_window)
    
    def add_window(self):
        self.Window4.showMaximized()
        self.close()

class NewWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Welcome Screen 3")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.step_1()
        self.step1()
        self.done_btn()
        self.Window5 = NewWindow4()

    def help_btn(self):
        help = help_button = QPushButton(" ", self)
        help_button.setGeometry(20, 20, 55, 55)
        help.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_info.png);  border-radius: 30px;}")
        #help.clicked.connect(self.print)

    def welcome_to_plark(self):
        layout2 = QHBoxLayout()
        #widget1 = QListWidget()
        title2 = QLabel(self)
        title2.setText("Welcome to PLARK")
        title2.move(150,20)
        title2.resize(1000,60)
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setStyleSheet("QLabel { font-weight: 900; font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout2.addWidget(title2)
    
    def additional_info(self):
        layout3 = QHBoxLayout()
        #widget1 = QListWidget()
        title3 = QLabel(self)
        title3.setText("TrashCash Plastic Recovery Kiosk")
        title3.move(150,80)
        title3.resize(1000,60)
        title3.setAlignment(QtCore.Qt.AlignCenter)
        title3.setStyleSheet("QLabel { font-weight: 400; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout3.addWidget(title3)
        
    def logout_btn(self):
        logout = logout_button = QPushButton(" ", self)
        logout_button.setGeometry(1280, 20, 55, 55)
        logout.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_logout.png);  border-radius: 0px;}")
        #logout.clicked.connect(self.)

    def step_1(self):
        step_1_info = QLabel(self)
        step_1_info.setText("Please put your plastic waste to the hole.")
        step_1_info.move(500,565)
        step_1_info.resize(600,80)
        step_1_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
       
    def step1(self):
        step_1 = QLabel(self)
        step_1.pixmap = QPixmap('images/Waste management-rafiki 1.png')
        step_1.setPixmap(step_1.pixmap)
        step_1.resize(step_1.pixmap.width(),step_1.pixmap.height())
        step_1.move(500,160)   # Subjected to change for monitor size


    def done_btn(self):
        done = done_button = QPushButton("Done", self)
        done_button.setGeometry(0, 670, 1500, 60)
        done.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        done.clicked.connect(self.add_window)

    def add_window(self):
        self.Window5.showMaximized()
        self.close()

class NewWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Welcome Screen 4")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.step_2()
        self.step2()
        self.done_btn()
        self.Window6 = NewWindow5()

    def help_btn(self):
        help = help_button = QPushButton(" ", self)
        help_button.setGeometry(20, 20, 55, 55)
        help.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_info.png);  border-radius: 30px;}")
        #help.clicked.connect(self.print)

    def welcome_to_plark(self):
        layout2 = QHBoxLayout()
        #widget1 = QListWidget()
        title2 = QLabel(self)
        title2.setText("Welcome to PLARK")
        title2.move(150,20)
        title2.resize(1000,60)
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setStyleSheet("QLabel { font-weight: 900; font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout2.addWidget(title2)
    
    def additional_info(self):
        layout3 = QHBoxLayout()
        #widget1 = QListWidget()
        title3 = QLabel(self)
        title3.setText("TrashCash Plastic Recovery Kiosk")
        title3.move(150,80)
        title3.resize(1000,60)
        title3.setAlignment(QtCore.Qt.AlignCenter)
        title3.setStyleSheet("QLabel { font-weight: 400; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout3.addWidget(title3)
        
    def logout_btn(self):
        logout = logout_button = QPushButton(" ", self)
        logout_button.setGeometry(1280, 20, 55, 55)
        logout.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_logout.png);  border-radius: 0px;}")
        #logout.clicked.connect(self.)

    def step_2(self):
        step_2_info = QLabel(self)
        step_2_info.setText("Our AI is currently sorting your plastic waste.")
        step_2_info.move(465,565)
        step_2_info.resize(600,80)
        step_2_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info1 = QLabel(self)
        step_2_info1.setText("Please wait...")
        step_2_info1.move(620,620)
        step_2_info1.resize(600,20)
        step_2_info1.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def step2(self):
        step_2 = QLabel(self)
        step_2.pixmap = QPixmap('images/Waste management-amico 1.png')
        step_2.setPixmap(step_2.pixmap)
        step_2.resize(step_2.pixmap.width(),step_2.pixmap.height())
        step_2.move(500,160)   # Subjected to change for monitor size


    def done_btn(self):
        done = done_button = QPushButton("Done", self)
        done_button.setGeometry(0, 670, 1500, 60)
        done.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        done.clicked.connect(self.add_window)

    def add_window(self):
        self.Window6.showMaximized()
        self.close()

class NewWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Welcome Screen 5")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.review_transaction()
        self.next_btn()
     #   self.Window5 = NewWindow4()

    def help_btn(self):
        help = help_button = QPushButton(" ", self)
        help_button.setGeometry(20, 20, 55, 55)
        help.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_info.png);  border-radius: 30px;}")
        #help.clicked.connect(self.print)

    def welcome_to_plark(self):
        layout2 = QHBoxLayout()
        #widget1 = QListWidget()
        title2 = QLabel(self)
        title2.setText("Welcome to PLARK")
        title2.move(150,20)
        title2.resize(1000,60)
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setStyleSheet("QLabel { font-weight: 900; font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout2.addWidget(title2)
    
    def additional_info(self):
        layout3 = QHBoxLayout()
        #widget1 = QListWidget()
        title3 = QLabel(self)
        title3.setText("TrashCash Plastic Recovery Kiosk")
        title3.move(150,80)
        title3.resize(1000,60)
        title3.setAlignment(QtCore.Qt.AlignCenter)
        title3.setStyleSheet("QLabel { font-weight: 400; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout3.addWidget(title3)
        
    def logout_btn(self):
        logout = logout_button = QPushButton(" ", self)
        logout_button.setGeometry(1280, 20, 55, 55)
        logout.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(images/material-symbols_logout.png);  border-radius: 0px;}")
        #logout.clicked.connect(self.)

    def review_transaction(self):
        review_transact = QLabel(self)
        review_transact.setText("Please Review")
        review_transact.move(50,150)
        review_transact.resize(300,50)
        review_transact.setStyleSheet("QLabel { font-weight: 700; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info1 = QLabel(self)
        step_2_info1.setText("Category")
        step_2_info1.move(50,200)
        step_2_info1.resize(300,40)
        step_2_info1.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info2 = QLabel(self)
        step_2_info2.setText("Weight")
        step_2_info2.move(270,200)
        step_2_info2.resize(300,40)
        step_2_info2.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info3 = QLabel(self)
        step_2_info3.setText("Points")
        step_2_info3.move(270,200)
        step_2_info3.resize(300,40)
        step_2_info3.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def next_btn(self):
        next = next_button = QPushButton("Next", self)
        next_button.setGeometry(0, 670, 1500, 60)
        next.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
       # start.clicked.connect(self.add_window)

    #def add_window(self):
     #   self.Window4.showMaximized()
      #  self.close()

app = QApplication(sys.argv)

loginWindow = Login()
window2 = NewWindow()
window3 = NewWindow2()
window4 = NewWindow3()
window5 = NewWindow4()
window6 = NewWindow5()
loginWindow.showMaximized()

app.exec()
