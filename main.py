#!/usr/bin/python3
#
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("page-ui.ui",self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("Sina Meysami")
        self.setWindowIcon(QIcon("./Scr/mrprogrammer-logo.jpeg"))
        self.web_.clicked.connect(self.website)
        self.instagram_.clicked.connect(self.instagram)
        self.facebook_.clicked.connect(self.facebook)
        self.github_.clicked.connect(self.github)
        self.linkedin_.clicked.connect(self.linkedin)
        self.telegram_.clicked.connect(self.telegram)
        self.twitter_.clicked.connect(self.twitter)
        self.youtube_.clicked.connect(self.youtube)
        self.zlink_.clicked.connect(self.zlink)
        
        self.blacksoftware_.clicked.connect(self.blacksoftware)

        self.exit_btn.clicked.connect(self.close)

    def website(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/My-Web")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://mrprogrammer2938.github.io/mrprogrammer2938/"))
        win.setCentralWidget(browser)
        win.show()

    def instagram(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/Instagram")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://instagram.com/black_software_company"))
        win.setCentralWidget(browser)
        win.show()
    def github(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/Github")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://github.com/mrprogrammer2938"))
        win.setCentralWidget(browser)
        win.show()

    def telegram(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/Telegram")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://t.me/blacksoftware3"))
        win.setCentralWidget(browser)
        win.show()
    def twitter(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/Twitter")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://twitter.com/blacksoftware3"))
        win.setCentralWidget(browser)
        win.show()
    def youtube(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/YouTube")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://www.youtube.com/channel/UCJNgrVc2NvEuMkASBa5AzLg"))
        win.setCentralWidget(browser)
        win.show()
    def zlink(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/Zlink")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://zil.ink/blacksoftware"))
        win.setCentralWidget(browser)
        win.show()
    def linkedin(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/LinkedIn")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://www.linkedin.com/in/black-software-608425226/"))
        win.setCentralWidget(browser)
        win.show()
    def facebook(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/Facebook")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://www.facebook.com/profile.php?id=100076104841323"))
        win.setCentralWidget(browser)
        win.show()

    def blacksoftware(self):
        win = QMainWindow(self)
        win.setWindowTitle("Black-Webbrowser/Black-Software")
        win.setGeometry(500,100,800,700)
        win.setFixedSize(800,700)
        browser = QWebEngineView(self)
        browser.setUrl(QUrl("https://github.com/mrprogrammer2938"))
        win.setCentralWidget(browser)
        win.show()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sina Meysami")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()