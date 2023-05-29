import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,)
from PyQt5.QtGui import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("images/trashcashlogosymbolunstrace copy 1.png"))
        self.setStyleSheet("background-color : #FFFAF3")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        logo_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(logo_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("red")
 #       btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)

        logo = QImage("images/trashcashlogosymbolunstrace copy 1.png")
     #   btn.pressed.connect(self.activate_tab_2)
        logo_layout.addWidget(logo)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec()
