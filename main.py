from PyQt5 import QtCore, QtGui, QtWidgets
from settings import Ui_SecondWindow
import pyautogui
import random
import time
import keyboard
import json

class Ui_MainWindow(object):

    def executeProgram(self):
        with open("settings.json", "r") as file:
            data = json.load(file)

            # Extract the variable values from the loaded data
        cursor_delay = data["cursor_delay"]
        keyboard_delay = data["keyboard_delay"]
        scroll_delay = data["scroll_delay"]
        switch_app_delay = data["switch_app_delay"]
        switch_tab_delay = data["switch_tab_delay"]
        enable_cursor = data["enable_cursor"]
        enable_keyboard = data["enable_keyboard"]
        enable_scroll = data["enable_scroll"]
        enable_switch_app = data["enable_switch_app"]
        enable_switch_tab = data["enable_switch_tab"]
        countdown_minutes = data["countdown_minutes"]

        def random_duration(min_duration, max_duration):
            return random.uniform(min_duration, max_duration)

        def move_cursor():
            screen_width, screen_height = pyautogui.size()
            current_x, current_y = pyautogui.position()
            new_x = random.randint(0, screen_width)
            new_y = random.randint(0, screen_height)

            while new_x == current_x and new_y == current_y:
                new_x = random.randint(0, screen_width)
                new_y = random.randint(0, screen_height)

            pyautogui.moveTo(new_x, new_y, duration=random_duration(400, 800) / 1000)

        def strike_keyboard():
            key = random.choice(['left', 'right', 'up', 'down'])
            pyautogui.press(key)
            time.sleep(random_duration(450, 598) / 1000)

        def scroll():
            direction = random.choice(['vertical', 'horizontal', 'bidirectional'])
            distance = random.randint(100, 300)

            if direction == 'vertical':
                pyautogui.scroll(distance)
            elif direction == 'horizontal':
                pyautogui.hscroll(distance)
            elif direction == 'bidirectional':
                pyautogui.scroll(distance)
                pyautogui.hscroll(distance)

            time.sleep(random_duration(400, 800) / 1000)

        def switch_app():
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(random_duration(400, 800) / 1000)
            pyautogui.keyUp('alt')

        def switch_tab():
            pyautogui.keyDown('ctrl')
            pyautogui.press('tab')
            time.sleep(random_duration(400, 800) / 1000)
            pyautogui.keyUp('ctrl')

        stop_key = 'esc'
        stop_flag = False

        def stop_script():
            global stop_flag
            stop_flag = True

        keyboard.on_press_key(stop_key, lambda _: stop_script())

        start_time = time.time()
        end_time = start_time + (countdown_minutes * 60)

        while not stop_flag and time.time() < end_time:
            if enable_cursor:
                move_cursor()
                time.sleep(cursor_delay)

            if enable_keyboard:
                strike_keyboard()
                time.sleep(keyboard_delay)

            if enable_scroll:
                scroll()
                time.sleep(scroll_delay)

            if enable_switch_app:
                switch_app()
                time.sleep(switch_app_delay)

            if enable_switch_tab:
                switch_tab()
                time.sleep(switch_tab_delay)
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 238)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(140, 30, 121, 51))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("wriggle-logo-png-transparent.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 171, 91))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("5261101.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(150, 150))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.executeProgram)  # Connect the button click to openWindow

        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(90, 130, 61, 51))
        self.settingsButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("free-settings-icon-960-thumb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon1)
        self.settingsButton.setIconSize(QtCore.QSize(50, 50))
        self.settingsButton.setFlat(True)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.clicked.connect(self.openWindow)  # Connect the button click to openWindow

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
