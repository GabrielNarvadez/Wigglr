import json

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 10, 141, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.clickTick = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.clickTick.setObjectName("clickTick")
        self.verticalLayout.addWidget(self.clickTick)
        self.scrollTick = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.scrollTick.setObjectName("scrollTick")
        self.verticalLayout.addWidget(self.scrollTick)
        self.windowsTick = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.windowsTick.setObjectName("windowsTick")
        self.verticalLayout.addWidget(self.windowsTick)
        self.tabsTick = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.tabsTick.setObjectName("tabsTick")
        self.verticalLayout.addWidget(self.tabsTick)
        self.strikeTick = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.strikeTick.setObjectName("strikeTick")
        self.verticalLayout.addWidget(self.strikeTick)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 151, 250))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.mouseEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.mouseEdit.setObjectName("mouseEdit")
        self.mouseEdit.setValidator(QtGui.QIntValidator())
        self.verticalLayout_2.addWidget(self.mouseEdit)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.mouseScroll = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.mouseScroll.setObjectName("mouseScroll")
        self.mouseScroll.setValidator(QtGui.QIntValidator())
        self.verticalLayout_2.addWidget(self.mouseScroll)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.windowsChange = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.windowsChange.setObjectName("windowsChange")
        self.windowsChange.setValidator(QtGui.QIntValidator())
        self.verticalLayout_2.addWidget(self.windowsChange)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.tabsChange = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.tabsChange.setObjectName("tabsChange")
        self.tabsChange.setValidator(QtGui.QIntValidator())
        self.verticalLayout_2.addWidget(self.tabsChange)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.keyboardStrike = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.keyboardStrike.setObjectName("keyboardStrike")
        self.keyboardStrike.setValidator(QtGui.QIntValidator())
        self.verticalLayout_2.addWidget(self.keyboardStrike)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(180, 170, 160, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.countdownTimer = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.countdownTimer.setObjectName("countdownTimer")
        self.countdownTimer.setValidator(QtGui.QIntValidator())
        self.verticalLayout_3.addWidget(self.countdownTimer)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 260, 158, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.saveButton.clicked.connect(self.saveButtonClicked)
        self.loadDefaultValues()  # Load default values on startup
        self.resetButton.clicked.connect(self.resetButtonClicked)
        self.saveButton.clicked.connect(self.saveButtonClicked)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadDefaultValues(self):
        # Load default values from the JSON file
        with open("settings.json", "r") as json_file:
            data = json.load(json_file)

        # Set the default values in the input fields
        self.mouseEdit.setText(str(data.get("cursor_delay", 0.5)))
        self.keyboardStrike.setText(str(data.get("keyboard_delay", 0.5)))
        self.mouseScroll.setText(str(data.get("scroll_delay", 0.5)))
        self.windowsChange.setText(str(data.get("switch_app_delay", 0.5)))
        self.tabsChange.setText(str(data.get("switch_tab_delay", 0.5)))
        self.clickTick.setChecked(data.get("enable_cursor", True))
        self.strikeTick.setChecked(data.get("enable_keyboard", True))
        self.scrollTick.setChecked(data.get("enable_scroll", True))
        self.windowsTick.setChecked(data.get("enable_switch_app", True))
        self.tabsTick.setChecked(data.get("enable_switch_tab", True))
        self.countdownTimer.setText(str(data.get("countdown_minutes", 5)))

    def resetButtonClicked(self):
        # Set the default values in the input fields
        self.mouseEdit.setText("0.5")
        self.keyboardStrike.setText("0.5")
        self.mouseScroll.setText("0.5")
        self.windowsChange.setText("0.5")
        self.tabsChange.setText("0.5")
        self.clickTick.setChecked(True)
        self.strikeTick.setChecked(True)
        self.scrollTick.setChecked(True)
        self.windowsTick.setChecked(True)
        self.tabsTick.setChecked(True)
        self.countdownTimer.setText("5")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "What to do?"))
        self.clickTick.setText(_translate("MainWindow", "Mouse Click (seconds)"))
        self.scrollTick.setText(_translate("MainWindow", "Mouse Scroll (seconds)"))
        self.windowsTick.setText(_translate("MainWindow", "Windows (seconds)"))
        self.tabsTick.setText(_translate("MainWindow", "Tabs (seconds)"))
        self.strikeTick.setText(_translate("MainWindow", "Keyboard Strike (seconds)"))
        self.label_5.setText(_translate("MainWindow", "Delay"))
        self.label_2.setText(_translate("MainWindow", "Mouse Click (seconds)"))
        self.label_7.setText(_translate("MainWindow", "Mouse Scroll (seconds)"))
        self.label_3.setText(_translate("MainWindow", "Windows (seconds)"))
        self.label_4.setText(_translate("MainWindow", "Tabs (seconds)"))
        self.label_6.setText(_translate("MainWindow", "Keyboard Strike (seconds)"))
        self.label_8.setText(_translate("MainWindow", "What to do?"))
        self.label_9.setText(_translate("MainWindow", "Countdown Timer (minutes)"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.saveButton.setText(_translate("MainWindow", "Save"))

    def saveButtonClicked(self):
        # Get the values from the input fields
        cursor_delay = float(self.mouseEdit.text())
        keyboard_delay = float(self.keyboardStrike.text())
        scroll_delay = float(self.mouseScroll.text())
        switch_app_delay = float(self.windowsChange.text())
        switch_tab_delay = float(self.tabsChange.text())
        enable_cursor = self.clickTick.isChecked()
        enable_keyboard = self.strikeTick.isChecked()
        enable_scroll = self.scrollTick.isChecked()
        enable_switch_app = self.windowsTick.isChecked()
        enable_switch_tab = self.tabsTick.isChecked()
        countdown_minutes = int(self.countdownTimer.text())

        # Create a dictionary to store the input values
        data = {
            "cursor_delay": cursor_delay,
            "keyboard_delay": keyboard_delay,
            "scroll_delay": scroll_delay,
            "switch_app_delay": switch_app_delay,
            "switch_tab_delay": switch_tab_delay,
            "enable_cursor": enable_cursor,
            "enable_keyboard": enable_keyboard,
            "enable_scroll": enable_scroll,
            "enable_switch_app": enable_switch_app,
            "enable_switch_tab": enable_switch_tab,
            "countdown_minutes": countdown_minutes
        }

        # Save the data to a JSON file
        with open("settings.json", "w") as json_file:
            json.dump(data, json_file)

        MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
