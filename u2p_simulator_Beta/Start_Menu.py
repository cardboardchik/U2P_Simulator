## by karton4ik

#python -m PyQt6.uic.pyuic -x [FILENAME].ui -o [FILENAME].py

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\../Images/icon_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_login = QtWidgets.QWidget(self.centralwidget)
        self.widget_login.setEnabled(True)
        self.widget_login.setGeometry(QtCore.QRect(0, 0, 750, 500))
        self.widget_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_login.setObjectName("widget_login")
        self.label_login_logo = QtWidgets.QLabel(self.widget_login)
        self.label_login_logo.setGeometry(QtCore.QRect(272, 41, 205, 114))
        self.label_login_logo.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_login_logo.setText("")
        self.label_login_logo.setPixmap(QtGui.QPixmap("UI\\../Images/u2p_sim_full_logo.svg"))
        self.label_login_logo.setScaledContents(True)
        self.label_login_logo.setWordWrap(True)
        self.label_login_logo.setObjectName("label_login_logo")
        self.label_login_in_your_account = QtWidgets.QLabel(self.widget_login)
        self.label_login_in_your_account.setGeometry(QtCore.QRect(195, 169, 360, 40))
        self.label_login_in_your_account.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 30px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_login_in_your_account.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_login_in_your_account.setObjectName("label_login_in_your_account")
        self.lineEdit_login_login = QtWidgets.QLineEdit(self.widget_login)
        self.lineEdit_login_login.setGeometry(QtCore.QRect(265, 248, 220, 48))
        self.lineEdit_login_login.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_login_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_login_login.setObjectName("lineEdit_login_login")
        self.lineEdit_login_password = QtWidgets.QLineEdit(self.widget_login)
        self.lineEdit_login_password.setGeometry(QtCore.QRect(265, 322, 220, 48))
        self.lineEdit_login_password.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_login_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_login_password.setObjectName("lineEdit_login_password")
        self.label_login_login = QtWidgets.QLabel(self.widget_login)
        self.label_login_login.setGeometry(QtCore.QRect(265, 226, 220, 20))
        self.label_login_login.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 18px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_login_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_login_login.setObjectName("label_login_login")
        self.label_login_password = QtWidgets.QLabel(self.widget_login)
        self.label_login_password.setGeometry(QtCore.QRect(265, 300, 220, 20))
        self.label_login_password.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 18px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_login_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_login_password.setObjectName("label_login_password")
        self.pushButton_login_exit = QtWidgets.QPushButton(self.widget_login)
        self.pushButton_login_exit.setGeometry(QtCore.QRect(389, 396, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_login_exit.setFont(font)
        self.pushButton_login_exit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_login_exit.setStyleSheet("QPushButton{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(239, 0, 9, 1);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 120% */\n"
"letter-spacing: -1px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(47, 47, 47, 1);\n"
"color: #fff;\n"
"padding-top: -1px;\n"
"background-color:rgba(239, 0, 9, 1);\n"
"}")
        self.pushButton_login_exit.setObjectName("pushButton_login_exit")
        self.pushButton_login_login = QtWidgets.QPushButton(self.widget_login)
        self.pushButton_login_login.setGeometry(QtCore.QRect(165, 396, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_login_login.setFont(font)
        self.pushButton_login_login.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_login_login.setStyleSheet("QPushButton{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(57, 219, 0, 1);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 120% */\n"
"letter-spacing: -1px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(47, 47, 47, 1);\n"
"color:#fff;\n"
"padding-top: -1px;\n"
"background-color:rgba(57, 219, 0, 1);\n"
"}\n"
"\n"
"")
        self.pushButton_login_login.setObjectName("pushButton_login_login")
        self.label_login_sub = QtWidgets.QLabel(self.widget_login)
        self.label_login_sub.setGeometry(QtCore.QRect(150, 465, 450, 20))
        self.label_login_sub.setAutoFillBackground(False)
        self.label_login_sub.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_login_sub.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_login_sub.setObjectName("label_login_sub")
        self.label_login_background = QtWidgets.QLabel(self.widget_login)
        self.label_login_background.setGeometry(QtCore.QRect(0, 0, 750, 500))
        self.label_login_background.setText("")
        self.label_login_background.setPixmap(QtGui.QPixmap("UI\\../Images/background_logn_and_startmenu.png"))
        self.label_login_background.setObjectName("label_login_background")
        self.label_login_background.raise_()
        self.label_login_logo.raise_()
        self.label_login_in_your_account.raise_()
        self.lineEdit_login_login.raise_()
        self.lineEdit_login_password.raise_()
        self.label_login_login.raise_()
        self.label_login_password.raise_()
        self.pushButton_login_exit.raise_()
        self.pushButton_login_login.raise_()
        self.label_login_sub.raise_()
        self.widget_main = QtWidgets.QWidget(self.centralwidget)
        self.widget_main.setEnabled(True)
        self.widget_main.setGeometry(QtCore.QRect(0, 0, 750, 500))
        self.widget_main.setAutoFillBackground(False)
        self.widget_main.setStyleSheet("background-color: #fff;")
        self.widget_main.setObjectName("widget_main")
        self.label__main_background = QtWidgets.QLabel(self.widget_main)
        self.label__main_background.setGeometry(QtCore.QRect(0, 0, 750, 500))
        self.label__main_background.setText("")
        self.label__main_background.setPixmap(QtGui.QPixmap("UI\\../Images/background_logn_and_startmenu.png"))
        self.label__main_background.setObjectName("label__main_background")
        self.label_main_logo = QtWidgets.QLabel(self.widget_main)
        self.label_main_logo.setGeometry(QtCore.QRect(224, 81, 301, 168))
        self.label_main_logo.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_main_logo.setText("")
        self.label_main_logo.setPixmap(QtGui.QPixmap("UI\\../Images/u2p_sim_full_logo.svg"))
        self.label_main_logo.setScaledContents(True)
        self.label_main_logo.setWordWrap(True)
        self.label_main_logo.setObjectName("label_main_logo")
        self.pushButton_main_exit = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_main_exit.setGeometry(QtCore.QRect(384, 375, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_main_exit.setFont(font)
        self.pushButton_main_exit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_main_exit.setStyleSheet("QPushButton{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(239, 0, 9, 1);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 120% */\n"
"letter-spacing: -1px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(47, 47, 47, 1);\n"
"color: #fff;\n"
"padding-top: -1px;\n"
"background-color:rgba(239, 0, 9, 1);\n"
"}")
        self.pushButton_main_exit.setObjectName("pushButton_main_exit")
        self.pushButton_main_new_game = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_main_new_game.setGeometry(QtCore.QRect(169, 300, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_main_new_game.setFont(font)
        self.pushButton_main_new_game.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton_main_new_game.setAutoFillBackground(False)
        self.pushButton_main_new_game.setStyleSheet("QPushButton{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid #000;\n"
"color:#fff;\n"
"padding-top: -1px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #F7931E, stop:1 #EF0009);\n"
"}\n"
"\n"
"")
        self.pushButton_main_new_game.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_main_new_game.setCheckable(False)
        self.pushButton_main_new_game.setAutoDefault(False)
        self.pushButton_main_new_game.setFlat(False)
        self.pushButton_main_new_game.setObjectName("pushButton_main_new_game")
        self.pushButton_main_settings = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_main_settings.setGeometry(QtCore.QRect(169, 375, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_main_settings.setFont(font)
        self.pushButton_main_settings.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton_main_settings.setAutoFillBackground(False)
        self.pushButton_main_settings.setStyleSheet("QPushButton{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"display: flex;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 8px;\n"
"flex-shrink: 0;\n"
"padding-top: -1px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid #000;\n"
"color:#fff;\n"
"padding-top: -1px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #EF0009, stop:1 #F7931E);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI\\../Images/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_main_settings.setIcon(icon1)
        self.pushButton_main_settings.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_main_settings.setCheckable(False)
        self.pushButton_main_settings.setAutoDefault(False)
        self.pushButton_main_settings.setDefault(False)
        self.pushButton_main_settings.setFlat(False)
        self.pushButton_main_settings.setObjectName("pushButton_main_settings")
        self.pushButton_main_download_game = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_main_download_game.setGeometry(QtCore.QRect(384, 300, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_main_download_game.setFont(font)
        self.pushButton_main_download_game.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton_main_download_game.setAutoFillBackground(False)
        self.pushButton_main_download_game.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid #000;\n"
"color:#fff;\n"
"padding-top: -1px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #F7931E, stop:1 #EF0009);\n"
"}")
        self.pushButton_main_download_game.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_main_download_game.setCheckable(False)
        self.pushButton_main_download_game.setAutoDefault(False)
        self.pushButton_main_download_game.setFlat(False)
        self.pushButton_main_download_game.setObjectName("pushButton_main_download_game")
        self.widget_settings = QtWidgets.QWidget(self.centralwidget)
        self.widget_settings.setEnabled(True)
        self.widget_settings.setGeometry(QtCore.QRect(0, 0, 750, 500))
        self.widget_settings.setAutoFillBackground(False)
        self.widget_settings.setStyleSheet("background-color: #DCDCDC;")
        self.widget_settings.setObjectName("widget_settings")
        self.frame_settings_menu = QtWidgets.QFrame(self.widget_settings)
        self.frame_settings_menu.setGeometry(QtCore.QRect(0, 0, 330, 500))
        self.frame_settings_menu.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.frame_settings_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings_menu.setObjectName("frame_settings_menu")
        self.frame_settings_menu_home = QtWidgets.QFrame(self.frame_settings_menu)
        self.frame_settings_menu_home.setGeometry(QtCore.QRect(0, 0, 330, 60))
        self.frame_settings_menu_home.setStyleSheet("QFrame#frame_settings_menu_home{\n"
"border-bottom: 1px solid #FFF;\n"
"}")
        self.frame_settings_menu_home.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings_menu_home.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings_menu_home.setObjectName("frame_settings_menu_home")
        self.label_settings_menu_home = QtWidgets.QLabel(self.frame_settings_menu_home)
        self.label_settings_menu_home.setGeometry(QtCore.QRect(77, 18, 235, 26))
        self.label_settings_menu_home.setStyleSheet("color: #FFF;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */")
        self.label_settings_menu_home.setObjectName("label_settings_menu_home")
        self.label_settings_menu_home_icon = QtWidgets.QLabel(self.frame_settings_menu_home)
        self.label_settings_menu_home_icon.setGeometry(QtCore.QRect(16, 8, 45, 45))
        self.label_settings_menu_home_icon.setAutoFillBackground(False)
        self.label_settings_menu_home_icon.setText("")
        self.label_settings_menu_home_icon.setPixmap(QtGui.QPixmap("UI\\../Images/House_01.svg"))
        self.label_settings_menu_home_icon.setObjectName("label_settings_menu_home_icon")
        
        self.pushButton_settings_menu_home = QtWidgets.QPushButton(self.frame_settings_menu_home)
        self.pushButton_settings_menu_home.setGeometry(QtCore.QRect(0, 0, 330, 60))
        self.pushButton_settings_menu_home.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pushButton_settings_menu_home.setText("")
        self.pushButton_settings_menu_home.setCheckable(False)
        self.pushButton_settings_menu_home.setChecked(False)
        self.pushButton_settings_menu_home.setObjectName("pushButton_settings_menu_home")
        
        
        self.frame_settings_menu_profile = QtWidgets.QFrame(self.frame_settings_menu)
        self.frame_settings_menu_profile.setGeometry(QtCore.QRect(0, 160, 330, 60))
        self.frame_settings_menu_profile.setStyleSheet("QFrame#frame_settings_menu_profile{\n"
"border-top: 1px solid #FFF;\n"
"border-bottom: 1px solid #FFF;\n"
"background: #404040;\n"
"}")
        self.frame_settings_menu_profile.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings_menu_profile.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings_menu_profile.setObjectName("frame_settings_menu_profile")
        self.label_settings_menu_profile = QtWidgets.QLabel(self.frame_settings_menu_profile)
        self.label_settings_menu_profile.setGeometry(QtCore.QRect(77, 10, 235, 35))
        self.label_settings_menu_profile.setAutoFillBackground(False)
        self.label_settings_menu_profile.setStyleSheet("color: #FFF;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_menu_profile.setObjectName("label_settings_menu_profile")
        self.label_settings_menu_profile_icon = QtWidgets.QLabel(self.frame_settings_menu_profile)
        self.label_settings_menu_profile_icon.setGeometry(QtCore.QRect(16, 8, 45, 45))
        self.label_settings_menu_profile_icon.setAutoFillBackground(False)
        self.label_settings_menu_profile_icon.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_settings_menu_profile_icon.setText("")
        self.label_settings_menu_profile_icon.setPixmap(QtGui.QPixmap("UI\\../Images/person-circle.svg"))
        self.label_settings_menu_profile_icon.setObjectName("label_settings_menu_profile_icon")
        
        self.pushButton_settings_menu_profile = QtWidgets.QPushButton(self.frame_settings_menu_profile)
        self.pushButton_settings_menu_profile.setGeometry(QtCore.QRect(0, 0, 330, 60))
        self.pushButton_settings_menu_profile.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pushButton_settings_menu_profile.setText("")
        self.pushButton_settings_menu_profile.setCheckable(False)
        self.pushButton_settings_menu_profile.setChecked(False)
        self.pushButton_settings_menu_profile.setObjectName("pushButton_settings_menu_profile")
              
        self.frame_settings_menu_interface = QtWidgets.QFrame(self.frame_settings_menu)
        self.frame_settings_menu_interface.setGeometry(QtCore.QRect(0, 220, 330, 60))
        self.frame_settings_menu_interface.setStyleSheet("QFrame#frame_settings_menu_interface{\n"
"border-bottom: 1px solid #FFF;\n"
"}")
        self.frame_settings_menu_interface.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings_menu_interface.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings_menu_interface.setObjectName("frame_settings_menu_interface")
        self.label_settings_menu_interface = QtWidgets.QLabel(self.frame_settings_menu_interface)
        self.label_settings_menu_interface.setGeometry(QtCore.QRect(77, 10, 235, 35))
        self.label_settings_menu_interface.setStyleSheet("color: #FFF;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_menu_interface.setObjectName("label_settings_menu_interface")
        self.label_settings_menu_interface_icon = QtWidgets.QLabel(self.frame_settings_menu_interface)
        self.label_settings_menu_interface_icon.setGeometry(QtCore.QRect(16, 8, 45, 45))
        self.label_settings_menu_interface_icon.setAutoFillBackground(False)
        self.label_settings_menu_interface_icon.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_settings_menu_interface_icon.setText("")
        self.label_settings_menu_interface_icon.setPixmap(QtGui.QPixmap("UI\\../Images/Slider_03.svg"))
        self.label_settings_menu_interface_icon.setObjectName("label_settings_menu_interface_icon")
        
        self.pushButton_settings_menu_interface = QtWidgets.QPushButton(self.frame_settings_menu_interface)
        self.pushButton_settings_menu_interface.setGeometry(QtCore.QRect(0, 0, 330, 60))
        self.pushButton_settings_menu_interface.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pushButton_settings_menu_interface.setText("")
        self.pushButton_settings_menu_interface.setCheckable(False)
        self.pushButton_settings_menu_interface.setChecked(False)
        self.pushButton_settings_menu_interface.setObjectName("pushButton_settings_menu_interface")
        
        self.frame_settings_menu_other = QtWidgets.QFrame(self.frame_settings_menu)
        self.frame_settings_menu_other.setGeometry(QtCore.QRect(0, 280, 330, 60))
        self.frame_settings_menu_other.setStyleSheet("QFrame#frame_settings_menu_other{\n"
"border-bottom: 1px solid #FFF;\n"
"}")
        self.frame_settings_menu_other.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings_menu_other.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings_menu_other.setObjectName("frame_settings_menu_other")
        self.label_settings_menu_other = QtWidgets.QLabel(self.frame_settings_menu_other)
        self.label_settings_menu_other.setGeometry(QtCore.QRect(77, 7, 235, 40))
        self.label_settings_menu_other.setStyleSheet("color: #FFF;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_menu_other.setObjectName("label_settings_menu_other")
        self.label_settings_menu_other_icon = QtWidgets.QLabel(self.frame_settings_menu_other)
        self.label_settings_menu_other_icon.setGeometry(QtCore.QRect(16, 8, 45, 45))
        self.label_settings_menu_other_icon.setAutoFillBackground(False)
        self.label_settings_menu_other_icon.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_settings_menu_other_icon.setText("")
        self.label_settings_menu_other_icon.setPixmap(QtGui.QPixmap("UI\\../Images/More_Horizontal.svg"))
        self.label_settings_menu_other_icon.setObjectName("label_settings_menu_other_icon")
        
        self.pushButton_settings_menu_other = QtWidgets.QPushButton(self.frame_settings_menu_other)
        self.pushButton_settings_menu_other.setGeometry(QtCore.QRect(0, 0, 330, 60))
        self.pushButton_settings_menu_other.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pushButton_settings_menu_other.setText("")
        self.pushButton_settings_menu_other.setCheckable(False)
        self.pushButton_settings_menu_other.setChecked(False)
        self.pushButton_settings_menu_other.setObjectName("pushButton_settings_menu_other")
        
        self.frame_settings_menu_about = QtWidgets.QFrame(self.frame_settings_menu)
        self.frame_settings_menu_about.setGeometry(QtCore.QRect(0, 440, 330, 60))
        self.frame_settings_menu_about.setStyleSheet("QFrame#frame_settings_menu_about{\n"
"border-top: 1px solid #FFF;\n"
"}")
        self.frame_settings_menu_about.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings_menu_about.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings_menu_about.setObjectName("frame_settings_menu_about")
        self.label_settings_menu_about = QtWidgets.QLabel(self.frame_settings_menu_about)
        self.label_settings_menu_about.setGeometry(QtCore.QRect(77, 12, 235, 35))
        self.label_settings_menu_about.setStyleSheet("color: #FFF;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_menu_about.setObjectName("label_settings_menu_about")
        self.label__settings_menu_about_icon = QtWidgets.QLabel(self.frame_settings_menu_about)
        self.label__settings_menu_about_icon.setGeometry(QtCore.QRect(16, 8, 45, 45))
        self.label__settings_menu_about_icon.setAutoFillBackground(False)
        self.label__settings_menu_about_icon.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label__settings_menu_about_icon.setText("")
        self.label__settings_menu_about_icon.setPixmap(QtGui.QPixmap("UI\\../Images/Info.svg"))
        self.label__settings_menu_about_icon.setObjectName("label__settings_menu_about_icon")
        
        self.pushButton_settings_menu_about = QtWidgets.QPushButton(self.frame_settings_menu_about)
        self.pushButton_settings_menu_about.setGeometry(QtCore.QRect(0, 0, 330, 60))
        self.pushButton_settings_menu_about.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pushButton_settings_menu_about.setText("")
        self.pushButton_settings_menu_about.setCheckable(False)
        self.pushButton_settings_menu_about.setChecked(False)
        self.pushButton_settings_menu_about.setObjectName("pushButton_settings_menu_about")
        
        self.widget_settings_profile = QtWidgets.QWidget(self.widget_settings)
        self.widget_settings_profile.setGeometry(QtCore.QRect(330, 0, 420, 500))
        self.widget_settings_profile.setObjectName("widget_settings_profile")
        self.label_settings_profile_ = QtWidgets.QLabel(self.widget_settings_profile)
        self.label_settings_profile_.setGeometry(QtCore.QRect(16, 0, 388, 60))
        self.label_settings_profile_.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_profile_.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_profile_.setObjectName("label_settings_profile_")
        self.label_settings_profile_edit_icon = QtWidgets.QLabel(self.widget_settings_profile)
        self.label_settings_profile_edit_icon.setGeometry(QtCore.QRect(359, 7, 45, 45))
        self.label_settings_profile_edit_icon.setAutoFillBackground(False)
        self.label_settings_profile_edit_icon.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_settings_profile_edit_icon.setText("")
        self.label_settings_profile_edit_icon.setPixmap(QtGui.QPixmap("UI\\../Images/Edit_Pencil_01.svg"))
        self.label_settings_profile_edit_icon.setObjectName("label_settings_profile_edit_icon")
        self.label_settings_profile_logo = QtWidgets.QLabel(self.widget_settings_profile)
        self.label_settings_profile_logo.setGeometry(QtCore.QRect(135, 60, 150, 150))
        self.label_settings_profile_logo.setText("")
        self.label_settings_profile_logo.setPixmap(QtGui.QPixmap("UI\\../Images/schoollogo.png"))
        self.label_settings_profile_logo.setScaledContents(True)
        self.label_settings_profile_logo.setObjectName("label_settings_profile_logo")
        self.label_settings_profile_name = QtWidgets.QLabel(self.widget_settings_profile)
        self.label_settings_profile_name.setGeometry(QtCore.QRect(16, 210, 388, 80))
        self.label_settings_profile_name.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"text-align: center;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_profile_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_profile_name.setObjectName("label_settings_profile_name")
        self.label_settings_profile_username = QtWidgets.QLabel(self.widget_settings_profile)
        self.label_settings_profile_username.setGeometry(QtCore.QRect(16, 285, 388, 31))
        self.label_settings_profile_username.setStyleSheet("color: rgba(0, 0, 0, 0.65);\n"
"font-family: Montserrat ExtraBold;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"text-align: center;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_profile_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_profile_username.setObjectName("label_settings_profile_username")
        self.label_settings_profile_email = QtWidgets.QLabel(self.widget_settings_profile)
        self.label_settings_profile_email.setGeometry(QtCore.QRect(16, 315, 388, 31))
        self.label_settings_profile_email.setStyleSheet("color: rgba(0, 0, 0, 0.65);\n"
"font-family: Montserrat ExtraBold;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"text-align: center;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_profile_email.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_profile_email.setObjectName("label_settings_profile_email")
        self.label_settings_profile_sub_end = QtWidgets.QLabel(self.widget_settings_profile)
        self.label_settings_profile_sub_end.setGeometry(QtCore.QRect(16, 350, 388, 61))
        self.label_settings_profile_sub_end.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-feature-settings: \'clig\' off, \'liga\' off;\n"
"text-align: center;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_profile_sub_end.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_profile_sub_end.setObjectName("label_settings_profile_sub_end")
        self.pushButton_settings_profile_logout = QtWidgets.QPushButton(self.widget_settings_profile)
        self.pushButton_settings_profile_logout.setGeometry(QtCore.QRect(87, 435, 245, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_settings_profile_logout.setFont(font)
        self.pushButton_settings_profile_logout.setAutoFillBackground(False)
        self.pushButton_settings_profile_logout.setStyleSheet("QPushButton{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(239, 0, 9, 1);\n"
"color:#000;\n"
"padding-top: -1px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"border-radius: 5px;\n"
"border: 3px solid #000;\n"
"color: #fff;\n"
"padding-top: -1px;\n"
"background-color: rgba(239, 0, 9, 1);\n"
"}")
        self.pushButton_settings_profile_logout.setCheckable(False)
        self.pushButton_settings_profile_logout.setAutoDefault(False)
        self.pushButton_settings_profile_logout.setFlat(False)
        self.pushButton_settings_profile_logout.setObjectName("pushButton_settings_profile_logout")
        self.widget_settings_interface = QtWidgets.QWidget(self.widget_settings)
        self.widget_settings_interface.setGeometry(QtCore.QRect(330, 0, 420, 500))
        self.widget_settings_interface.setObjectName("widget_settings_interface")
        self.label_settings_interface = QtWidgets.QLabel(self.widget_settings_interface)
        self.label_settings_interface.setGeometry(QtCore.QRect(16, 0, 388, 60))
        self.label_settings_interface.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_interface.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_interface.setObjectName("label_settings_interface")
        self.label_settings_interface_language = QtWidgets.QLabel(self.widget_settings_interface)
        self.label_settings_interface_language.setGeometry(QtCore.QRect(16, 107, 150, 60))
        self.label_settings_interface_language.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_interface_language.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_settings_interface_language.setObjectName("label_settings_interface_language")
        self.label_settings_interface_theme = QtWidgets.QLabel(self.widget_settings_interface)
        self.label_settings_interface_theme.setGeometry(QtCore.QRect(16, 174, 150, 60))
        self.label_settings_interface_theme.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_interface_theme.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_settings_interface_theme.setObjectName("label_settings_interface_theme")
        self.comboBox_settings_interface_language = QtWidgets.QComboBox(self.widget_settings_interface)
        self.comboBox_settings_interface_language.setGeometry(QtCore.QRect(189, 110, 215, 55))
        self.comboBox_settings_interface_language.setStyleSheet("QComboBox#comboBox_settings_interface_language{\n"
"    border: 0px;\n"
"    background-color: rgb(116, 116, 116);\n"
"    border-radius: 8px;\n"
"    color: #fff;\n"
"    font-family: Montserrat ExtraBold;\n"
"    font-size: 28px;\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    line-height: 24px; /* 85.714% */\n"
"    \n"
"\n"
"}\n"
"QComboBox#comboBox_settings_interface_language::drop-down{\n"
"border: 0px;\n"
"border-radius: 5px;\n"
"background-color: rgb(116, 116, 116);\n"
"}\n"
"\n"
"QComboBox#comboBox_settings_interface_language::down-arrow{\n"
"    image: url();\n"
"}")
        self.comboBox_settings_interface_language.setObjectName("comboBox_settings_interface_language")
        self.comboBox_settings_interface_language.addItem("")
        self.comboBox_settings_interface_language.addItem("")
        self.comboBox_settings_interface_theme = QtWidgets.QComboBox(self.widget_settings_interface)
        self.comboBox_settings_interface_theme.setGeometry(QtCore.QRect(189, 177, 215, 55))
        self.comboBox_settings_interface_theme.setStyleSheet("QComboBox#comboBox_settings_interface_theme{\n"
"    border: 0px;\n"
"    background-color: rgb(116, 116, 116);\n"
"    border-radius: 8px;\n"
"    color: #fff;\n"
"    font-family: Montserrat ExtraBold;\n"
"    font-size: 28px;\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    line-height: 24px; /* 85.714% */\n"
"    \n"
"\n"
"}\n"
"QComboBox#comboBox_settings_interface_theme::drop-down{\n"
"border: 0px;\n"
"border-radius: 5px;\n"
"background-color: rgb(116, 116, 116);\n"
"}\n"
"\n"
"QComboBox#comboBox_settings_interface_theme::down-arrow{\n"
"    image: url();\n"
"}")
        self.comboBox_settings_interface_theme.setObjectName("comboBox_settings_interface_theme")
        self.comboBox_settings_interface_theme.addItem("")
        self.comboBox_settings_interface_theme.addItem("")
        self.widget_settings_other = QtWidgets.QWidget(self.widget_settings)
        self.widget_settings_other.setGeometry(QtCore.QRect(330, 0, 420, 500))
        self.widget_settings_other.setObjectName("widget_settings_other")
        self.label_settings_other = QtWidgets.QLabel(self.widget_settings_other)
        self.label_settings_other.setGeometry(QtCore.QRect(16, 0, 388, 60))
        self.label_settings_other.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_other.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_other.setObjectName("label_settings_other")
        self.widget_settings_about = QtWidgets.QWidget(self.widget_settings)
        self.widget_settings_about.setGeometry(QtCore.QRect(330, 0, 420, 500))
        self.widget_settings_about.setObjectName("widget_settings_about")
        self.label_settings_about = QtWidgets.QLabel(self.widget_settings_about)
        self.label_settings_about.setGeometry(QtCore.QRect(16, 0, 388, 60))
        self.label_settings_about.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_about.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_about.setObjectName("label_settings_about")
        self.labelt_settings_about_logo_u2p_sim_full = QtWidgets.QLabel(self.widget_settings_about)
        self.labelt_settings_about_logo_u2p_sim_full.setGeometry(QtCore.QRect(110, 73, 210, 117))
        self.labelt_settings_about_logo_u2p_sim_full.setText("")
        self.labelt_settings_about_logo_u2p_sim_full.setPixmap(QtGui.QPixmap("UI\\../Images/u2p_sim_full_logo.svg"))
        self.labelt_settings_about_logo_u2p_sim_full.setScaledContents(True)
        self.labelt_settings_about_logo_u2p_sim_full.setObjectName("labelt_settings_about_logo_u2p_sim_full")
        self.label_settings_about_logo_u2p = QtWidgets.QLabel(self.widget_settings_about)
        self.label_settings_about_logo_u2p.setGeometry(QtCore.QRect(117, 271, 185, 117))
        self.label_settings_about_logo_u2p.setText("")
        self.label_settings_about_logo_u2p.setPixmap(QtGui.QPixmap("UI\\../Images/u2p_full_logo.svg"))
        self.label_settings_about_logo_u2p.setScaledContents(True)
        self.label_settings_about_logo_u2p.setObjectName("label_settings_about_logo_u2p")
        self.label_settings_about_dev_inf = QtWidgets.QLabel(self.widget_settings_about)
        self.label_settings_about_dev_inf.setGeometry(QtCore.QRect(20, 190, 388, 75))
        self.label_settings_about_dev_inf.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_about_dev_inf.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_about_dev_inf.setObjectName("label_settings_about_dev_inf")
        self.label_settings_about_contact_text = QtWidgets.QLabel(self.widget_settings_about)
        self.label_settings_about_contact_text.setGeometry(QtCore.QRect(16, 400, 200, 41))
        self.label_settings_about_contact_text.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_about_contact_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_settings_about_contact_text.setObjectName("label_settings_about_contact_text")
        self.label_settings_about_version_text = QtWidgets.QLabel(self.widget_settings_about)
        self.label_settings_about_version_text.setGeometry(QtCore.QRect(16, 450, 141, 41))
        self.label_settings_about_version_text.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_about_version_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_settings_about_version_text.setObjectName("label_settings_about_version_text")
        self.label_settings_about_conctact = QtWidgets.QLabel(self.widget_settings_about)
        self.label_settings_about_conctact.setGeometry(QtCore.QRect(220, 400, 181, 41))
        self.label_settings_about_conctact.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_about_conctact.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_settings_about_conctact.setObjectName("label_settings_about_conctact")
        self.label_settings_about_version = QtWidgets.QLabel(self.widget_settings_about)
        self.label_settings_about_version.setGeometry(QtCore.QRect(160, 450, 241, 41))
        self.label_settings_about_version.setStyleSheet("color: #000;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 75% */\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_settings_about_version.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_settings_about_version.setObjectName("label_settings_about_version")
        self.frame_settings_menu.raise_()
        self.widget_settings_interface.raise_()
        self.widget_settings_other.raise_()
        self.widget_settings_about.raise_()
        self.widget_settings_profile.raise_()
        self.widget_main.raise_()
        self.widget_settings.raise_()
        self.widget_login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        #connections login
        self.pushButton_login_login.clicked.connect(self.login)
        
        #connections main
        self.pushButton_main_settings.clicked.connect(self.pushButton_main_settings_was_clicked)
        
        #connections settings
        self.pushButton_settings_menu_home.clicked.connect(self.pushButton_settings_menu_home_was_clicked)
        self.pushButton_settings_menu_profile.clicked.connect(self.pushButton_settings_menu_profile_was_clicked)
        self.pushButton_settings_menu_interface.clicked.connect(self.pushButton_settings_menu_interface_was_clicked)
        
        
        

        
        #def settings
        self.widget_login.show() #show
        self.widget_main.hide()
        self.widget_settings.hide()
        self.widget_settings_profile.show() #show
        self.widget_settings_about.hide()
        self.widget_settings_interface.hide()
        self.widget_settings_other.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "U2P Simulator - ###"))
        self.label_login_in_your_account.setText(_translate("MainWindow", "Войдите в аккаунт"))
        self.lineEdit_login_login.setPlaceholderText(_translate("MainWindow", "Login"))
        self.lineEdit_login_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_login_login.setText(_translate("MainWindow", "Логин"))
        self.label_login_password.setText(_translate("MainWindow", "Пароль"))
        self.pushButton_login_exit.setText(_translate("MainWindow", "Выход"))
        self.pushButton_login_login.setText(_translate("MainWindow", "Войти"))
        self.label_login_sub.setText(_translate("MainWindow", "Приобрести подписку вы можете на сайте u2p.kz"))
        self.pushButton_main_exit.setText(_translate("MainWindow", "Выход"))
        self.pushButton_main_new_game.setText(_translate("MainWindow", "Новая игра"))
        self.pushButton_main_settings.setText(_translate("MainWindow", " Настройки"))
        self.pushButton_main_download_game.setText(_translate("MainWindow", "Загрузка игры"))
        self.label_settings_menu_home.setText(_translate("MainWindow", "Главная"))
        self.label_settings_menu_profile.setText(_translate("MainWindow", "Профиль"))
        self.label_settings_menu_interface.setText(_translate("MainWindow", "Интерфейс"))
        self.label_settings_menu_other.setText(_translate("MainWindow", "Другие"))
        self.label_settings_menu_about.setText(_translate("MainWindow", "О программе"))
        self.label_settings_profile_.setText(_translate("MainWindow", "Профиль"))
        self.label_settings_profile_name.setText(_translate("MainWindow", "<html><head/><body><p>Школа<br>                                                                                                                            Предпринимателей</p></body></html>"))
        self.label_settings_profile_username.setText(_translate("MainWindow", "schoolshp"))
        self.label_settings_profile_email.setText(_translate("MainWindow", "schoolshp@gmail.com"))
        self.label_settings_profile_sub_end.setText(_translate("MainWindow", "Дата окончания подписки:\n"
"31.12.2999"))
        self.pushButton_settings_profile_logout.setText(_translate("MainWindow", "Выйти из аккаунта"))
        self.label_settings_interface.setText(_translate("MainWindow", "Интерфейс"))
        self.label_settings_interface_language.setText(_translate("MainWindow", "Язык"))
        self.label_settings_interface_theme.setText(_translate("MainWindow", "Тема"))
        self.comboBox_settings_interface_language.setItemText(0, _translate("MainWindow", "Русский"))
        self.comboBox_settings_interface_language.setItemText(1, _translate("MainWindow", "English"))
        self.comboBox_settings_interface_theme.setItemText(0, _translate("MainWindow", "Cветлая"))
        self.comboBox_settings_interface_theme.setItemText(1, _translate("MainWindow", "Тёмная"))
        self.label_settings_other.setText(_translate("MainWindow", "Другие настройки"))
        self.label_settings_about.setText(_translate("MainWindow", "О программе"))
        self.label_settings_about_dev_inf.setText(_translate("MainWindow", "Разработана karton4ik\n"
"при поддержке"))
        self.label_settings_about_contact_text.setText(_translate("MainWindow", "Контакты"))
        self.label_settings_about_version_text.setText(_translate("MainWindow", "Версия"))
        self.label_settings_about_conctact.setText(_translate("MainWindow", "u2p.kz"))
        self.label_settings_about_version.setText(_translate("MainWindow", "1.1 closed beta"))


        
        
    def login(self):
        self.widget_login.hide()
        self.widget_main.show()
    
    def pushButton_main_settings_was_clicked(self):
        self.widget_main.hide()
        self.widget_settings.show()    
        
    def pushButton_settings_menu_home_was_clicked(self):
        self.widget_settings.hide()
        self.widget_main.show()
        
    def pushButton_settings_menu_profile_was_clicked(self):
        self.widget_settings_about.hide()
        self.widget_settings_interface.hide()
        self.widget_settings_other.hide()
        self.widget_settings_profile.show()
        
        self.frame_settings_menu_profile.setStyleSheet("QFrame#frame_settings_menu_profile{\n"
                "border-top: 1px solid #FFF;\n"
                "border-bottom: 1px solid #FFF;\n"
                "background: #404040;\n"
                "}")
        self.frame_settings_menu_interface.setStyleSheet("QFrame#frame_settings_menu_interface{\n"
                "border-top: 1px solid #FFF;\n"
                "border-bottom: 1px solid #FFF;\n"
                "background: #404040;\n"
                "}")
        self.frame_settings_menu_other.setStyleSheet("QFrame#frame_settings_menu_other{\n"
                "border-top: 1px solid #FFF;\n"
                "border-bottom: 1px solid #FFF;\n"
                "background: #404040;\n"
                "}")
        self.frame_settings_menu_about.setStyleSheet("QFrame#frame_settings_menu_about{\n"
                "border-top: 1px solid #FFF;\n"
                "border-bottom: 1px solid #FFF;\n"
                "background: #404040;\n"
                "}")
        
 
    def pushButton_settings_menu_interface_was_clicked(self):
        self.widget_settings.hide()
        self.widget_main.show()
        
    def pushButton_settings_menu_home_was_clicked(self):
        self.widget_settings.hide()
        self.widget_main.show()
        
    def pushButton_settings_menu_home_was_clicked(self):
        self.widget_settings.hide()
        self.widget_main.show()       
          

        


    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

