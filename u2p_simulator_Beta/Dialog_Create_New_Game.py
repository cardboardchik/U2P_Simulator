


from PyQt6 import QtCore, QtGui, QtWidgets

import sqlite3 as sq
from datetime import datetime

import engine

class Ui_Dialog_create_new_game(object):
    def setupUi(self, Dialog_create_new_game):
        Dialog_create_new_game.setObjectName("Dialog_create_new_game")
        Dialog_create_new_game.resize(900, 620)
        Dialog_create_new_game.setMinimumSize(QtCore.QSize(900, 620))
        Dialog_create_new_game.setMaximumSize(QtCore.QSize(900, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\../Images/Add_Plus_Square.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_create_new_game.setWindowIcon(icon)
        Dialog_create_new_game.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_create_new_game = QtWidgets.QLabel(Dialog_create_new_game)
        self.label_create_new_game.setGeometry(QtCore.QRect(16, 10, 868, 40))
        self.label_create_new_game.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_create_new_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_create_new_game.setObjectName("label_create_new_game")
        self.frame_comands_name = QtWidgets.QFrame(Dialog_create_new_game)
        self.frame_comands_name.setGeometry(QtCore.QRect(16, 80, 300, 530))
        self.frame_comands_name.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-radius: 20px;")
        self.frame_comands_name.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comands_name.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comands_name.setObjectName("frame_comands_name")
        self.label_comands_name = QtWidgets.QLabel(self.frame_comands_name)
        self.label_comands_name.setGeometry(QtCore.QRect(0, 0, 300, 40))
        self.label_comands_name.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_comands_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_comands_name.setObjectName("label_comands_name")
        self.label_company_name_1 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_1.setGeometry(QtCore.QRect(12, 56, 30, 48))
        self.label_company_name_1.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_1.setObjectName("label_company_name_1")
        self.label_company_name_2 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_2.setGeometry(QtCore.QRect(12, 115, 30, 48))
        self.label_company_name_2.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_2.setObjectName("label_company_name_2")
        self.label_company_name_3 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_3.setGeometry(QtCore.QRect(12, 174, 30, 48))
        self.label_company_name_3.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_3.setObjectName("label_company_name_3")
        self.label_company_name_4 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_4.setGeometry(QtCore.QRect(12, 233, 30, 48))
        self.label_company_name_4.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_4.setObjectName("label_company_name_4")
        self.label_company_name_5 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_5.setGeometry(QtCore.QRect(12, 292, 30, 48))
        self.label_company_name_5.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_5.setObjectName("label_company_name_5")
        self.label_company_name_6 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_6.setGeometry(QtCore.QRect(12, 351, 30, 48))
        self.label_company_name_6.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_6.setObjectName("label_company_name_6")
        self.label_company_name_7 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_7.setGeometry(QtCore.QRect(12, 410, 30, 48))
        self.label_company_name_7.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_7.setObjectName("label_company_name_7")
        self.label_company_name_8 = QtWidgets.QLabel(self.frame_comands_name)
        self.label_company_name_8.setGeometry(QtCore.QRect(12, 469, 30, 48))
        self.label_company_name_8.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_company_name_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_8.setObjectName("label_company_name_8")
        self.lineEdit_company_name_1 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_1.setGeometry(QtCore.QRect(46, 56, 238, 48))
        self.lineEdit_company_name_1.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_1.setObjectName("lineEdit_company_name_1")
        self.lineEdit_company_name_2 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_2.setGeometry(QtCore.QRect(46, 115, 238, 48))
        self.lineEdit_company_name_2.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_2.setObjectName("lineEdit_company_name_2")
        self.lineEdit_company_name_3 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_3.setGeometry(QtCore.QRect(46, 174, 238, 48))
        self.lineEdit_company_name_3.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_3.setObjectName("lineEdit_company_name_3")
        self.lineEdit_company_name_4 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_4.setGeometry(QtCore.QRect(46, 233, 238, 48))
        self.lineEdit_company_name_4.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_4.setObjectName("lineEdit_company_name_4")
        self.lineEdit_company_name_5 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_5.setGeometry(QtCore.QRect(46, 292, 238, 48))
        self.lineEdit_company_name_5.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_5.setObjectName("lineEdit_company_name_5")
        self.lineEdit_company_name_6 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_6.setGeometry(QtCore.QRect(46, 351, 238, 48))
        self.lineEdit_company_name_6.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_6.setObjectName("lineEdit_company_name_6")
        self.lineEdit_company_name_7 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_7.setGeometry(QtCore.QRect(46, 410, 238, 48))
        self.lineEdit_company_name_7.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_7.setObjectName("lineEdit_company_name_7")
        self.lineEdit_company_name_8 = QtWidgets.QLineEdit(self.frame_comands_name)
        self.lineEdit_company_name_8.setGeometry(QtCore.QRect(46, 469, 238, 48))
        self.lineEdit_company_name_8.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_company_name_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_company_name_8.setObjectName("lineEdit_company_name_8")
        self.frame_game_name = QtWidgets.QFrame(Dialog_create_new_game)
        self.frame_game_name.setGeometry(QtCore.QRect(330, 80, 554, 114))
        self.frame_game_name.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-radius: 20px;")
        self.frame_game_name.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_game_name.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_game_name.setObjectName("frame_game_name")
        self.label_game_name = QtWidgets.QLabel(self.frame_game_name)
        self.label_game_name.setGeometry(QtCore.QRect(0, 0, 554, 40))
        self.label_game_name.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_game_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_game_name.setObjectName("label_game_name")
        self.lineEdit_game_name = QtWidgets.QLineEdit(self.frame_game_name)
        self.lineEdit_game_name.setGeometry(QtCore.QRect(16, 56, 522, 48))
        self.lineEdit_game_name.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_game_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_game_name.setObjectName("lineEdit_game_name")
        self.frame_game_level = QtWidgets.QFrame(Dialog_create_new_game)
        self.frame_game_level.setGeometry(QtCore.QRect(330, 204, 554, 114))
        self.frame_game_level.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-radius: 20px;")
        self.frame_game_level.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_game_level.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_game_level.setObjectName("frame_game_level")
        self.label_game_level = QtWidgets.QLabel(self.frame_game_level)
        self.label_game_level.setGeometry(QtCore.QRect(0, 0, 554, 40))
        self.label_game_level.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_game_level.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_game_level.setObjectName("label_game_level")
        self.comboBox_game_level = QtWidgets.QComboBox(self.frame_game_level)
        self.comboBox_game_level.setGeometry(QtCore.QRect(16, 49, 522, 55))
        self.comboBox_game_level.setStyleSheet("QComboBox#comboBox_game_level{\n"
"    border: 2px solid #000;\n"
"    border-radius: 8px;\n"
"    color: #000;\n"
"    font-family: Montserrat ExtraBold;\n"
"    font-size: 18px;\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    line-height: 24px; /* 85.714% */\n"
"    \n"
"}\n"
"QComboBox#comboBox_game_level::drop-down{\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QComboBox#comboBox_game_level::down-arrow{\n"
"    image: url(images/Chevron_Down_black.svg);\n"
"}")
        self.comboBox_game_level.setObjectName("comboBox_game_level")
        self.comboBox_game_level.addItem("")
        self.comboBox_game_level.addItem("")
        self.comboBox_game_level.addItem("")
        self.comboBox_game_level.addItem("")
        self.comboBox_game_level.addItem("")
        self.frame_game_script = QtWidgets.QFrame(Dialog_create_new_game)
        self.frame_game_script.setGeometry(QtCore.QRect(330, 328, 554, 179))
        self.frame_game_script.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-radius: 20px;")
        self.frame_game_script.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_game_script.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_game_script.setObjectName("frame_game_script")
        self.label_game_script = QtWidgets.QLabel(self.frame_game_script)
        self.label_game_script.setGeometry(QtCore.QRect(0, 0, 554, 40))
        self.label_game_script.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_game_script.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_game_script.setObjectName("label_game_script")
        self.comboBox_game_script = QtWidgets.QComboBox(self.frame_game_script)
        self.comboBox_game_script.setGeometry(QtCore.QRect(16, 49, 522, 55))
        self.comboBox_game_script.setStyleSheet("QComboBox#comboBox_game_script{\n"
"    border: 2px solid #000;\n"
"    border-radius: 8px;\n"
"    color: #000;\n"
"    font-family: Montserrat ExtraBold;\n"
"    font-size: 18px;\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    line-height: 24px; /* 85.714% */\n"
"    \n"
"}\n"
"QComboBox#comboBox_game_script::drop-down{\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QComboBox#comboBox_game_script::down-arrow{\n"
"    image: url(images/Chevron_Down_black.svg);\n"
"}")
        self.comboBox_game_script.setObjectName("comboBox_game_script")
        self.comboBox_game_script.addItem("")
        self.comboBox_game_script.addItem("")
        self.pushButton_create_new_script = QtWidgets.QPushButton(self.frame_game_script)
        self.pushButton_create_new_script.setGeometry(QtCore.QRect(16, 114, 522, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_create_new_script.setFont(font)
        self.pushButton_create_new_script.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton_create_new_script.setAutoFillBackground(False)
        self.pushButton_create_new_script.setStyleSheet("QPushButton{\n"
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
        self.pushButton_create_new_script.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_create_new_script.setCheckable(False)
        self.pushButton_create_new_script.setAutoDefault(False)
        self.pushButton_create_new_script.setFlat(False)
        self.pushButton_create_new_script.setObjectName("pushButton_create_new_script")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_create_new_game)
        self.pushButton_cancel.setGeometry(QtCore.QRect(613, 533, 271, 62))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_cancel.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(239, 0, 9, 1);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"letter-spacing: -1px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(47, 47, 47, 1);\n"
"color: #fff;\n"
"padding-top: -1px;\n"
"background-color:rgba(239, 0, 9, 1);\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_create = QtWidgets.QPushButton(Dialog_create_new_game)
        self.pushButton_create.setGeometry(QtCore.QRect(330, 533, 271, 62))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_create.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(57, 219, 0, 1);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -1px;\n"
"\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"letter-spacing: -1px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(47, 47, 47, 1);\n"
"color:#fff;\n"
"padding-top: -1px;\n"
"background-color:rgba(57, 219, 0, 1);\n"
"}\n"
"\n"
"")
        self.pushButton_create.setObjectName("pushButton_create")
        
        
        #connections
        self.pushButton_create.clicked.connect(self.create_new_game)
        self.pushButton_cancel.clicked.connect(Dialog_create_new_game.reject) #close
        
        self.lineEdit_game_name.textChanged.connect(self.lineEdit_game_name__txtChanged)
        
        self.lineEdit_company_name_1.textChanged.connect(self.lineEdit_company_name_1_txtChanged)
        self.lineEdit_company_name_2.textChanged.connect(self.lineEdit_company_name_2_txtChanged)
        self.lineEdit_company_name_3.textChanged.connect(self.lineEdit_company_name_3_txtChanged)
        self.lineEdit_company_name_4.textChanged.connect(self.lineEdit_company_name_4_txtChanged)
        self.lineEdit_company_name_5.textChanged.connect(self.lineEdit_company_name_5_txtChanged)
        self.lineEdit_company_name_6.textChanged.connect(self.lineEdit_company_name_6_txtChanged)
        self.lineEdit_company_name_7.textChanged.connect(self.lineEdit_company_name_7_txtChanged)
        self.lineEdit_company_name_8.textChanged.connect(self.lineEdit_company_name_8_txtChanged)


        #data
        self.game_name = ""
        self.script = [{'DemandChange': 0, 'RandDImpact': 0, 'PriceImpact': 0, 'MarketingImpact': 0, 'TaxRate': 25, 'InterestRate': 2.5, 'LoanLimit': 50000, 'MaxPrice': 99, 'MaxMarketing': 15000, 'MaxCapInv': 15000, 'MaxRandD': 15000, 'RandD': 30, 'Price': 40, 'Marketing': 30}]
        
        
        self.companies_names = {
                
        }
        
        self.retranslateUi(Dialog_create_new_game)
        QtCore.QMetaObject.connectSlotsByName(Dialog_create_new_game)

    def retranslateUi(self, Dialog_create_new_game):
        _translate = QtCore.QCoreApplication.translate
        Dialog_create_new_game.setWindowTitle(_translate("Dialog_create_new_game", "U2P Simulator - Create New Game"))
        self.label_create_new_game.setText(_translate("Dialog_create_new_game", "Создание новой игры"))
        self.label_comands_name.setText(_translate("Dialog_create_new_game", "Названия команд"))
        self.label_company_name_1.setText(_translate("Dialog_create_new_game", "1."))
        self.label_company_name_2.setText(_translate("Dialog_create_new_game", "2."))
        self.label_company_name_3.setText(_translate("Dialog_create_new_game", "3."))
        self.label_company_name_4.setText(_translate("Dialog_create_new_game", "4."))
        self.label_company_name_5.setText(_translate("Dialog_create_new_game", "5."))
        self.label_company_name_6.setText(_translate("Dialog_create_new_game", "6."))
        self.label_company_name_7.setText(_translate("Dialog_create_new_game", "7."))
        self.label_company_name_8.setText(_translate("Dialog_create_new_game", "8."))
        self.lineEdit_company_name_1.setPlaceholderText(_translate("Dialog_create_new_game", "Обязательное поле"))
        self.lineEdit_company_name_2.setPlaceholderText(_translate("Dialog_create_new_game", "Обязательное поле"))
        self.lineEdit_company_name_3.setPlaceholderText(_translate("Dialog_create_new_game", "Может быть пустым"))
        self.lineEdit_company_name_4.setPlaceholderText(_translate("Dialog_create_new_game", "Может быть пустым"))
        self.lineEdit_company_name_5.setPlaceholderText(_translate("Dialog_create_new_game", "Может быть пустым"))
        self.lineEdit_company_name_6.setPlaceholderText(_translate("Dialog_create_new_game", "Может быть пустым"))
        self.lineEdit_company_name_7.setPlaceholderText(_translate("Dialog_create_new_game", "Может быть пустым"))
        self.lineEdit_company_name_8.setPlaceholderText(_translate("Dialog_create_new_game", "Может быть пустым"))
        self.label_game_name.setText(_translate("Dialog_create_new_game", "Названиe игры"))
        self.lineEdit_game_name.setPlaceholderText(_translate("Dialog_create_new_game", "Игра 999"))
        self.label_game_level.setText(_translate("Dialog_create_new_game", "Уровень игры"))
        self.comboBox_game_level.setItemText(0, _translate("Dialog_create_new_game", "Цена, Производство, Маркетинг, Кап. Инв., R&D"))
        self.comboBox_game_level.setItemText(1, _translate("Dialog_create_new_game", "Цена, Производство, Маркетинг, Кап. Инв"))
        self.comboBox_game_level.setItemText(2, _translate("Dialog_create_new_game", "Цена, Производство, Маркетинг"))
        self.comboBox_game_level.setItemText(3, _translate("Dialog_create_new_game", "Цена, Производство"))
        self.comboBox_game_level.setItemText(4, _translate("Dialog_create_new_game", "Цена"))
        self.label_game_script.setText(_translate("Dialog_create_new_game", "Сценарий игры"))
        self.comboBox_game_script.setItemText(0, _translate("Dialog_create_new_game", "Стандартный"))
        self.comboBox_game_script.setItemText(1, _translate("Dialog_create_new_game", "Рандомный кризис"))
        self.pushButton_create_new_script.setText(_translate("Dialog_create_new_game", "Создать новый сценарий"))
        self.pushButton_cancel.setText(_translate("Dialog_create_new_game", "Отмена"))
        self.pushButton_create.setText(_translate("Dialog_create_new_game", "Создать"))


    def lineEdit_game_name__txtChanged(self, name):
        self.game_name = str(name)

    def lineEdit_company_name_1_txtChanged(self, name):
        self.companies_names["Company_1"] = str(name)

    def lineEdit_company_name_2_txtChanged(self, name):
        self.companies_names["Company_2"] = str(name)

    def lineEdit_company_name_3_txtChanged(self, name):
        self.companies_names["Company_3"] = str(name)

    def lineEdit_company_name_4_txtChanged(self, name):
        self.companies_names["Company_4"] = str(name)

    def lineEdit_company_name_5_txtChanged(self, name):
        self.companies_names["Company_5"] = str(name)

    def lineEdit_company_name_6_txtChanged(self, name):
        self.companies_names["Company_6"] = str(name)

    def lineEdit_company_name_7_txtChanged(self, name):
        self.companies_names["Company_7"] = str(name)

    def lineEdit_company_name_8_txtChanged(self, name):
        self.companies_names["Company_8"] = str(name)
    
    
        
    def create_new_game(self):
        current_time = str(datetime.now().strftime("%d-%m-%Y %H:%M"))
        
        print(self.companies_names, current_time)
        periods = [engine.exec(engine.init(len(self.companies_names)))]
        # connect to db
        with sq.connect("db.sqlite3") as con_db:
            cur_db = con_db.cursor()
            
            try:
                cur_db.execute(f"""INSERT INTO games VALUES("{self.game_name}", "{current_time}", "{periods}", "{self.companies_names}", "{self.script}")""")
            except sq.IntegrityError:
                print("игра с таким названием уже существует")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_create_new_game = QtWidgets.QDialog()
    ui = Ui_Dialog_create_new_game()
    ui.setupUi(Dialog_create_new_game)
    Dialog_create_new_game.show()
    sys.exit(app.exec())
