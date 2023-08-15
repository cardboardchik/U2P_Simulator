## by karton4ik

# version 1.1 Closed Beta

#python -m PyQt6.uic.pyuic -x [FILENAME].ui -o [FILENAME].py


from ast import literal_eval
from PyQt6 import QtCore, QtGui, QtWidgets

from Dialog_Enter_decisions_select_company import Ui_Dialog_Enter_decisions_select_company




class Ui_u2p(object):
        
    def setupUi(self, u2p, game_data_db):
        self.game_data_db = game_data_db
        
        u2p.setObjectName("u2p")
        #u2p.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        u2p.resize(810, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(u2p.sizePolicy().hasHeightForWidth())
        u2p.setSizePolicy(sizePolicy)
        
        u2p.setMinimumSize(QtCore.QSize(810, 540))
        u2p.setMaximumSize(QtCore.QSize(810, 540))
        u2p.setBaseSize(QtCore.QSize(810, 540))
        
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        u2p.setFont(font)
        u2p.setTabletTracking(False)
        u2p.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        u2p.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off) #logo
        u2p.setWindowIcon(icon)
        
        u2p.setAcceptDrops(False)
        u2p.setToolTip("")
        u2p.setToolTipDuration(-1)
        u2p.setAutoFillBackground(False)
        #u2p.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        #u2p.setAnimated(True)
        #u2p.setDocumentMode(False)
        #u2p.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        #u2p.setDockNestingEnabled(False)
        #u2p.setUnifiedTitleAndToolBarOnMac(False)
        
        self.centralwidget = QtWidgets.QWidget(parent=u2p)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.centralwidget.setObjectName("centralwidget")
        
        self.header = QtWidgets.QFrame(parent=self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 810, 80))
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet("background: rgb(47, 47, 47)")
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        
        self.logo = QtWidgets.QLabel(parent=self.header)
        self.logo.setGeometry(QtCore.QRect(341, 5, 127, 71))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/logo.svg"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        
        self.account_logo = QtWidgets.QLabel(parent=self.header)
        self.account_logo.setEnabled(True)
        self.account_logo.setGeometry(QtCore.QRect(570, 0, 41, 80))
        self.account_logo.setAutoFillBackground(False)
        self.account_logo.setStyleSheet("color: rgb(255, 255, 255);\n""")
        self.account_logo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.account_logo.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.account_logo.setLineWidth(0)
        self.account_logo.setText("")
        self.account_logo.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.account_logo.setPixmap(QtGui.QPixmap("images/person-circle.svg"))
        self.account_logo.setScaledContents(False)
        self.account_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.account_logo.setWordWrap(False)
        self.account_logo.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.account_logo.setObjectName("account_logo")
        
        self.label_account_name = QtWidgets.QLabel(parent=self.header)
        self.label_account_name.setGeometry(QtCore.QRect(623, 0, 171, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_account_name.setFont(font)
        self.label_account_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_account_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_account_name.setObjectName("label_account_name")
        
        self.comboBox_language = QtWidgets.QComboBox(parent=self.header)
        self.comboBox_language.setGeometry(QtCore.QRect(16, 0, 91, 80))
        self.comboBox_language.setStyleSheet("#comboBox_language{\n"
                                        "    border: 0px;\n"  
                                        "}\n"

                                        "#comboBox_language::drop-down{\n"
                                        "border: 0px;\n"
                                        "border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "#comboBox_language::down-arrow{\n"
                                        "    image: url(images/Chevron_Down.svg);\n"
                                        "}")
        self.comboBox_language.setEditable(False)
        self.comboBox_language.setCurrentText("")
        self.comboBox_language.setIconSize(QtCore.QSize(61, 41))
        self.comboBox_language.setFrame(True)
        self.comboBox_language.setObjectName("comboBox_language")
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Flag_of_Russia.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.comboBox_language.addItem(icon, "")
        self.comboBox_language.setItemText(0, "")
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Flag_of_the_United_Kingdom_(3-5).svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.comboBox_language.addItem(icon1, "")
        self.comboBox_language.setItemText(1, "")
        
        self.label_help = QtWidgets.QLabel(parent=self.header)
        self.label_help.setGeometry(QtCore.QRect(148, 0, 40, 80))
        self.label_help.setText("")
        self.label_help.setPixmap(QtGui.QPixmap("images/Circle_Help.svg"))
        self.label_help.setScaledContents(False)
        self.label_help.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_help.setObjectName("label_help")
        
        self.frame_game_N = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_game_N.setGeometry(QtCore.QRect(0, 80, 810, 40))
        self.frame_game_N.setAutoFillBackground(False)
        self.frame_game_N.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_game_N.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_game_N.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_game_N.setLineWidth(1)
        self.frame_game_N.setObjectName("frame_game_N")
        self.label = QtWidgets.QLabel(parent=self.frame_game_N)
        self.label.setGeometry(QtCore.QRect(16, 0, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.pushButton_savegame = QtWidgets.QPushButton(parent=self.frame_game_N)
        self.pushButton_savegame.setGeometry(QtCore.QRect(537, 2, 125, 35))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        
        self.pushButton_savegame.setFont(font)
        self.pushButton_savegame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_savegame.setStyleSheet("\n"
                                "\n"
                                "\n"
                                "QPushButton{\n"
                                "\n"
                                "border-radius: 5px;\n"
                                "border: 3px solid rgba(57, 219, 0, 1);\n"
                                "color: rgb(255, 255, 255);\n"
                                "padding-top: -1px;\n"
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
        self.pushButton_savegame.setObjectName("pushButton_savegame")
        self.pushButton_closegame = QtWidgets.QPushButton(parent=self.frame_game_N)
        self.pushButton_closegame.setGeometry(QtCore.QRect(672, 2, 125, 35))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.pushButton_closegame.setFont(font)
        self.pushButton_closegame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_closegame.setStyleSheet("\n"
                                "\n"
                                "QPushButton{\n"
                                "\n"
                                "border-radius: 5px;\n"
                                "border: 3px solid rgba(239, 0, 9, 1);\n"
                                "color: rgb(255, 255, 255);\n"
                                "padding-top: -1px;\n"
                                "\n"
                                "}\n"
                                "\n"
                                "QPushButton::hover{\n"
                                "\n"
                                "border-radius: 5px;\n"
                                "border: 3px solid rgba(47, 47, 47, 1);\n"
                                "color: #000;\n"
                                "padding-top: -1px;\n"
                                "background-color:rgba(239, 0, 9, 1);\n"
                                "}")
        self.pushButton_closegame.setObjectName("pushButton_closegame")
        
        self.line = QtWidgets.QFrame(parent=self.frame_game_N)
        self.line.setGeometry(QtCore.QRect(10, 40, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 120, 810, 1))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.frame_compan_list = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_compan_list.setGeometry(QtCore.QRect(520, 121, 290, 419))
        self.frame_compan_list.setStyleSheet("")
        self.frame_compan_list.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_compan_list.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_compan_list.setObjectName("frame_compan_list")
        self.label_company_list = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_list.setGeometry(QtCore.QRect(0, 0, 290, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_list.setFont(font)
        self.label_company_list.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_list.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_list.setObjectName("label_company_list")
        self.label_company_list_name = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_list_name.setGeometry(QtCore.QRect(60, 54, 153, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_list_name.setFont(font)
        self.label_company_list_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_list_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_list_name.setObjectName("label_company_list_name")
        
        self.label_company_list_upi = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_list_upi.setGeometry(QtCore.QRect(221, 54, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_list_upi.setFont(font)
        self.label_company_list_upi.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_list_upi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_list_upi.setObjectName("label_company_list_upi")
        
        self.line_3 = QtWidgets.QFrame(parent=self.frame_compan_list)
        self.line_3.setGeometry(QtCore.QRect(19, 82, 250, 1))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        
        self.line_4 = QtWidgets.QFrame(parent=self.frame_compan_list)
        self.line_4.setGeometry(QtCore.QRect(213, 60, 1, 340))
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        
        self.label_company_place_1 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_1.setGeometry(QtCore.QRect(29, 87, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_1.setFont(font)
        self.label_company_place_1.setStyleSheet("color: rgb(255, 215, 0);")
        self.label_company_place_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_1.setObjectName("label_company_place_1")
        
        self.label_company_place_2 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_2.setGeometry(QtCore.QRect(29, 127, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_2.setFont(font)
        self.label_company_place_2.setStyleSheet("color: rgb(192, 192, 192);")
        self.label_company_place_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_2.setObjectName("label_company_place_2")
        
        self.label_company_place_3 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_3.setGeometry(QtCore.QRect(29, 167, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_3.setFont(font)
        self.label_company_place_3.setStyleSheet("color: rgb(205, 127, 50);")
        self.label_company_place_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_3.setObjectName("label_company_place_3")
        
        self.label_company_place_4 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_4.setGeometry(QtCore.QRect(29, 207, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_4.setFont(font)
        self.label_company_place_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_place_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_4.setObjectName("label_company_place_4")
        
        self.label_company_place_5 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_5.setGeometry(QtCore.QRect(29, 247, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_5.setFont(font)
        self.label_company_place_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_place_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_5.setObjectName("label_company_place_5")
        
        self.label_company_place_6 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_6.setGeometry(QtCore.QRect(29, 287, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_6.setFont(font)
        self.label_company_place_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_place_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_6.setObjectName("label_company_place_6")
        
        self.label_company_place_7 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_7.setGeometry(QtCore.QRect(29, 327, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_7.setFont(font)
        self.label_company_place_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_place_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_7.setObjectName("label_company_place_7")
        
        self.label_company_place_8 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_place_8.setGeometry(QtCore.QRect(29, 367, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_place_8.setFont(font)
        self.label_company_place_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_place_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_place_8.setObjectName("label_company_place_8")
        
        self.label_company_name_2 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_name_2.setGeometry(QtCore.QRect(60, 127, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_2.setFont(font)
        self.label_company_name_2.setStyleSheet("color: rgb(192, 192, 192);")
        self.label_company_name_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_2.setObjectName("label_company_name_2")
        self.label_company_name_3 = QtWidgets.QLabel(parent=self.frame_compan_list)
        
        self.label_company_name_3.setGeometry(QtCore.QRect(60, 167, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_3.setFont(font)
        self.label_company_name_3.setStyleSheet("color: rgb(205, 127, 50);")
        self.label_company_name_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_3.setObjectName("label_company_name_3")
        
        self.label_company_name_7 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_name_7.setGeometry(QtCore.QRect(60, 327, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_7.setFont(font)
        self.label_company_name_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_name_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_7.setObjectName("label_company_name_7")
        
        self.label_company_name_6 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_name_6.setGeometry(QtCore.QRect(60, 287, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_6.setFont(font)
        self.label_company_name_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_name_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_6.setObjectName("label_company_name_6")
        
        self.label_company_name_4 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_name_4.setGeometry(QtCore.QRect(60, 207, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_4.setFont(font)
        self.label_company_name_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_name_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_4.setObjectName("label_company_name_4")
        
        self.label_company_name_1 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_name_1.setGeometry(QtCore.QRect(60, 87, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_1.setFont(font)
        self.label_company_name_1.setStyleSheet("color: rgb(255, 215, 0);")
        self.label_company_name_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_1.setObjectName("label_company_name_1")
        
        self.label_company_name_5 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_name_5.setGeometry(QtCore.QRect(60, 247, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_5.setFont(font)
        self.label_company_name_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_name_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_5.setObjectName("label_company_name_5")
        
        self.label_company_name_8 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_name_8.setGeometry(QtCore.QRect(60, 367, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_name_8.setFont(font)
        self.label_company_name_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_name_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_name_8.setObjectName("label_company_name_8")
        
        self.label_company_upi_2 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_2.setGeometry(QtCore.QRect(221, 127, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_2.setFont(font)
        self.label_company_upi_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_2.setObjectName("label_company_upi_2")
        
        self.label_company_upi_1 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_1.setGeometry(QtCore.QRect(221, 87, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_1.setFont(font)
        self.label_company_upi_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_1.setObjectName("label_company_upi_1")
        
        self.label_company_upi_4 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_4.setGeometry(QtCore.QRect(221, 207, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_4.setFont(font)
        self.label_company_upi_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_4.setObjectName("label_company_upi_4")
        
        self.label_company_upi_3 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_3.setGeometry(QtCore.QRect(221, 167, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_3.setFont(font)
        self.label_company_upi_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_3.setObjectName("label_company_upi_3")
        
        self.label_company_upi_6 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_6.setGeometry(QtCore.QRect(221, 287, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_6.setFont(font)
        self.label_company_upi_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_6.setObjectName("label_company_upi_6")
        
        self.label_company_upi_5 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_5.setGeometry(QtCore.QRect(221, 247, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_5.setFont(font)
        self.label_company_upi_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_5.setObjectName("label_company_upi_5")
        
        self.label_company_upi_8 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_8.setGeometry(QtCore.QRect(221, 367, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_8.setFont(font)
        self.label_company_upi_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_8.setObjectName("label_company_upi_8")
        
        self.label_company_upi_7 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_upi_7.setGeometry(QtCore.QRect(221, 327, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_upi_7.setFont(font)
        self.label_company_upi_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_company_upi_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_upi_7.setObjectName("label_company_upi_7")
        
        self.label_company_arrow_1 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_1.setGeometry(QtCore.QRect(6, 96, 19, 17))
        self.label_company_arrow_1.setText("")
        self.label_company_arrow_1.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_1.setObjectName("label_company_arrow_1")
        
        self.label_company_arrow_num_1 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_1.setGeometry(QtCore.QRect(12, 97, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_1.setFont(font)
        self.label_company_arrow_num_1.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_1.setObjectName("label_company_arrow_num_1")
        
        self.label_company_arrow_2 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_2.setGeometry(QtCore.QRect(6, 136, 19, 17))
        self.label_company_arrow_2.setText("")
        self.label_company_arrow_2.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_2.setObjectName("label_company_arrow_2")
        
        self.label_company_arrow_num_2 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_2.setGeometry(QtCore.QRect(12, 137, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_2.setFont(font)
        self.label_company_arrow_num_2.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_2.setObjectName("label_company_arrow_num_2")
        
        self.label_company_arrow_3 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_3.setGeometry(QtCore.QRect(6, 176, 19, 17))
        self.label_company_arrow_3.setText("")
        self.label_company_arrow_3.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_3.setObjectName("label_company_arrow_3")
        
        self.label_company_arrow_num_3 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_3.setGeometry(QtCore.QRect(12, 177, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_3.setFont(font)
        self.label_company_arrow_num_3.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_3.setObjectName("label_company_arrow_num_3")
        
        self.label_company_arrow_4 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_4.setGeometry(QtCore.QRect(6, 216, 19, 17))
        self.label_company_arrow_4.setText("")
        self.label_company_arrow_4.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_4.setObjectName("label_company_arrow_4")
        
        self.label_company_arrow_num_4 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_4.setGeometry(QtCore.QRect(12, 217, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_4.setFont(font)
        self.label_company_arrow_num_4.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_4.setObjectName("label_company_arrow_num_4")
        
        self.label_company_arrow_5 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_5.setGeometry(QtCore.QRect(6, 256, 19, 17))
        self.label_company_arrow_5.setText("")
        self.label_company_arrow_5.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_5.setObjectName("label_company_arrow_5")
        
        self.label_company_arrow_num_5 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_5.setGeometry(QtCore.QRect(12, 257, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_5.setFont(font)
        self.label_company_arrow_num_5.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_5.setObjectName("label_company_arrow_num_5")
        
        self.label_company_arrow_6 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_6.setGeometry(QtCore.QRect(6, 296, 19, 17))
        self.label_company_arrow_6.setText("")
        self.label_company_arrow_6.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_6.setObjectName("label_company_arrow_6")
        
        self.label_company_arrow_num_6 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_6.setGeometry(QtCore.QRect(12, 297, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_6.setFont(font)
        self.label_company_arrow_num_6.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_6.setObjectName("label_company_arrow_num_6")
        
        self.label_company_arrow_7 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_7.setGeometry(QtCore.QRect(6, 336, 19, 17))
        self.label_company_arrow_7.setText("")
        self.label_company_arrow_7.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_7.setObjectName("label_company_arrow_7")
        
        self.label_company_arrow_num_7 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_7.setGeometry(QtCore.QRect(12, 337, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_7.setFont(font)
        self.label_company_arrow_num_7.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_7.setObjectName("label_company_arrow_num_7")
        
        self.label_company_arrow_8 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_8.setGeometry(QtCore.QRect(6, 376, 19, 17))
        self.label_company_arrow_8.setText("")
        self.label_company_arrow_8.setPixmap(QtGui.QPixmap("images/arrow_up.svg"))
        self.label_company_arrow_8.setObjectName("label_company_arrow_8")
        
        self.label_company_arrow_num_8 = QtWidgets.QLabel(parent=self.frame_compan_list)
        self.label_company_arrow_num_8.setGeometry(QtCore.QRect(12, 377, 9, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_arrow_num_8.setFont(font)
        self.label_company_arrow_num_8.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_company_arrow_num_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_arrow_num_8.setObjectName("label_company_arrow_num_8")
        
        self.label_current_period = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_current_period.setGeometry(QtCore.QRect(16, 119, 492, 35))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_current_period.setFont(font)
        self.label_current_period.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(255, 255, 255, 0);")
        self.label_current_period.setMidLineWidth(1)
        self.label_current_period.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_current_period.setObjectName("label_current_period")
        
        self.frame_decisions = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_decisions.setGeometry(QtCore.QRect(16, 160, 239, 245))
        self.frame_decisions.setStyleSheet(
                "border-radius: 20px;\n"
                "background: rgba(47, 47, 47, 1);")
        self.frame_decisions.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_decisions.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_decisions.setObjectName("frame_decisions")
        
        self.label_decisions = QtWidgets.QLabel(parent=self.frame_decisions)
        self.label_decisions.setGeometry(QtCore.QRect(0, 0, 239, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_decisions.setFont(font)
        self.label_decisions.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_decisions.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_decisions.setObjectName("label_decisions")
        
        self.pushButton_EnterallDecisions = QtWidgets.QPushButton(parent=self.frame_decisions)
        self.pushButton_EnterallDecisions.setGeometry(QtCore.QRect(21, 50, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_EnterallDecisions.setFont(font)
        self.pushButton_EnterallDecisions.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton_EnterallDecisions.setAutoFillBackground(False)
        self.pushButton_EnterallDecisions.setStyleSheet("\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid rgb(255, 255, 255);\n"
                "color: rgb(255, 255, 255);\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color:#F03D23;\n"
                "padding-top: -1px;\n"
                "background-color: rgb(255, 255, 255);\n"
                "}")
        self.pushButton_EnterallDecisions.setCheckable(False)
        self.pushButton_EnterallDecisions.setAutoDefault(False)
        self.pushButton_EnterallDecisions.setFlat(False)
        self.pushButton_EnterallDecisions.setObjectName("pushButton_EnterallDecisions")
        
        self.pushButton_ReviewDecisions = QtWidgets.QPushButton(parent=self.frame_decisions)
        self.pushButton_ReviewDecisions.setGeometry(QtCore.QRect(21, 115, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_ReviewDecisions.setFont(font)
        self.pushButton_ReviewDecisions.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_ReviewDecisions.setAutoFillBackground(False)
        self.pushButton_ReviewDecisions.setStyleSheet("\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid rgb(255, 255, 255);\n"
                "color: rgb(255, 255, 255);\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color:#F03D23;\n"
                "padding-top: -1px;\n"
                "background-color: rgb(255, 255, 255);\n"
                "}")
        self.pushButton_ReviewDecisions.setCheckable(False)
        self.pushButton_ReviewDecisions.setAutoDefault(False)
        self.pushButton_ReviewDecisions.setDefault(False)
        self.pushButton_ReviewDecisions.setFlat(False)
        self.pushButton_ReviewDecisions.setObjectName("pushButton_ReviewDecisions")
        
        self.pushButton_ClosePeriod = QtWidgets.QPushButton(parent=self.frame_decisions)
        self.pushButton_ClosePeriod.setGeometry(QtCore.QRect(21, 180, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ClosePeriod.setFont(font)
        self.pushButton_ClosePeriod.setAutoFillBackground(False)
        self.pushButton_ClosePeriod.setStyleSheet("\n"
                "\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color: #fff;\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #fff;\n"
                "color: #fff;\n"
                "padding-top: -1px;\n"
                "background-color: #F03D23;\n"
                "}")
        self.pushButton_ClosePeriod.setCheckable(False)
        self.pushButton_ClosePeriod.setAutoDefault(False)
        self.pushButton_ClosePeriod.setFlat(False)
        self.pushButton_ClosePeriod.setObjectName("pushButton_ClosePeriod")
        
        self.frame_results = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_results.setGeometry(QtCore.QRect(269, 160, 239, 245))
        self.frame_results.setStyleSheet(
                "border-radius: 20px;\n"
                "background: rgba(47, 47, 47, 1);")
        self.frame_results.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_results.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_results.setObjectName("frame_results")
        
        self.label_results = QtWidgets.QLabel(parent=self.frame_results)
        self.label_results.setGeometry(QtCore.QRect(0, 0, 239, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_results.setFont(font)
        self.label_results.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_results.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_results.setObjectName("label_results")
        
        self.pushButton_Print = QtWidgets.QPushButton(parent=self.frame_results)
        self.pushButton_Print.setGeometry(QtCore.QRect(21, 115, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_Print.setFont(font)
        self.pushButton_Print.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_Print.setAutoFillBackground(False)
        self.pushButton_Print.setStyleSheet("\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid rgb(255, 255, 255);\n"
                "color: rgb(255, 255, 255);\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color:#F03D23;\n"
                "padding-top: -1px;\n"
                "background-color: rgb(255, 255, 255);\n"
                "}")
        self.pushButton_Print.setCheckable(False)
        self.pushButton_Print.setAutoDefault(False)
        self.pushButton_Print.setDefault(False)
        self.pushButton_Print.setFlat(False)
        self.pushButton_Print.setObjectName("pushButton_Print")
        
        self.pushButton_Graph = QtWidgets.QPushButton(parent=self.frame_results)
        self.pushButton_Graph.setGeometry(QtCore.QRect(21, 180, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Graph.setFont(font)
        self.pushButton_Graph.setAutoFillBackground(False)
        self.pushButton_Graph.setStyleSheet("\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid rgb(255, 255, 255);\n"
                "color: rgb(255, 255, 255);\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color:#F03D23;\n"
                "padding-top: -1px;\n"
                "background-color: rgb(255, 255, 255);\n"
                "}")
        self.pushButton_Graph.setCheckable(False)
        self.pushButton_Graph.setAutoDefault(False)
        self.pushButton_Graph.setFlat(False)
        self.pushButton_Graph.setObjectName("pushButton_Graph")
        
        self.pushButton_View = QtWidgets.QPushButton(parent=self.frame_results)
        self.pushButton_View.setGeometry(QtCore.QRect(21, 50, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_View.setFont(font)
        self.pushButton_View.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton_View.setAutoFillBackground(False)
        self.pushButton_View.setStyleSheet("\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid rgb(255, 255, 255);\n"
                "color: rgb(255, 255, 255);\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color:#F03D23;\n"
                "padding-top: -1px;\n"
                "background-color: rgb(255, 255, 255);\n"
                "}")
        self.pushButton_View.setCheckable(False)
        self.pushButton_View.setAutoDefault(False)
        self.pushButton_View.setFlat(False)
        self.pushButton_View.setObjectName("pushButton_View")
        
        self.frame_period_options = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_period_options.setGeometry(QtCore.QRect(16, 415, 492, 115))
        self.frame_period_options.setStyleSheet(
                "border-radius: 20px;\n"
                "background: rgba(47, 47, 47, 1);")
        self.frame_period_options.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_period_options.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_period_options.setObjectName("frame_period_options")
        self.label_period_options = QtWidgets.QLabel(parent=self.frame_period_options)
        self.label_period_options.setGeometry(QtCore.QRect(0, 0, 492, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_period_options.setFont(font)
        self.label_period_options.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_period_options.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_period_options.setObjectName("label_period_options")
        
        self.pushButton_Parameters = QtWidgets.QPushButton(parent=self.frame_period_options)
        self.pushButton_Parameters.setGeometry(QtCore.QRect(271, 50, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Parameters.setFont(font)
        self.pushButton_Parameters.setAutoFillBackground(False)
        self.pushButton_Parameters.setStyleSheet("\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid rgb(255, 255, 255);\n"
                "color: rgb(255, 255, 255);\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color:#F03D23;\n"
                "padding-top: -1px;\n"
                "background-color: rgb(255, 255, 255);\n"
                "}")
        self.pushButton_Parameters.setCheckable(False)
        self.pushButton_Parameters.setAutoDefault(False)
        self.pushButton_Parameters.setFlat(False)
        self.pushButton_Parameters.setObjectName("pushButton_Parameters")
        
        self.pushButton_Restart = QtWidgets.QPushButton(parent=self.frame_period_options)
        self.pushButton_Restart.setGeometry(QtCore.QRect(21, 50, 196, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.pushButton_Restart.setFont(font)
        self.pushButton_Restart.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_Restart.setAutoFillBackground(False)
        self.pushButton_Restart.setStyleSheet("\n"
                "QPushButton{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid rgb(255, 255, 255);\n"
                "color: rgb(255, 255, 255);\n"
                "padding-top: -1px;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton::hover{\n"
                "\n"
                "border-radius: 5px;\n"
                "border: 3px solid #F03D23;\n"
                "color:#F03D23;\n"
                "padding-top: -1px;\n"
                "background-color: rgb(255, 255, 255);\n"
                "}")
        self.pushButton_Restart.setCheckable(False)
        self.pushButton_Restart.setAutoDefault(False)
        self.pushButton_Restart.setDefault(False)
        self.pushButton_Restart.setFlat(False)
        self.pushButton_Restart.setObjectName("pushButton_Restart")
        
        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(517, 120, 1, 420))
        self.line_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        
        #u2p.setCentralWidget(self.centralwidget)
        
        #self.menubar = QtWidgets.QMenuBar(parent=u2p)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        #self.menubar.setObjectName("menubar")
        #u2p.setMenuBar(self.menubar)
        
        #set game data
        self.label.setText(game_data_db[-1][0]) #game_name
        self.label_current_period.setText(f"Период {literal_eval(game_data_db[0][2])[-1]['now_tick']}")
        self.top_company_list()
        
        #connections
        self.pushButton_savegame.clicked.connect(self.save_game)
        self.pushButton_closegame.clicked.connect(self.close_game)
        self.pushButton_EnterallDecisions.clicked.connect(self.pushButton_EnterallDecisions_was_clicked)
        self.pushButton_ReviewDecisions.clicked.connect(self.pushButton_ReviewDecisions_was_clicked)
        self.pushButton_ClosePeriod.clicked.connect(self.pushButton_ClosePeriod_was_clicked)
        self.pushButton_View.clicked.connect(self.pushButton_View_was_clicked)
        self.pushButton_Print.clicked.connect(self.pushButton_Print_was_clicked)
        self.pushButton_Graph.clicked.connect(self.pushButton_Graph_was_clicked)
        self.pushButton_Restart.clicked.connect(self.pushButton_Restart_was_clicked)
        self.pushButton_Parameters.clicked.connect(self.pushButton_ClosePeriod_was_clicked)
        

        self.retranslateUi(u2p)
        QtCore.QMetaObject.connectSlotsByName(u2p)

    def retranslateUi(self, u2p):
        _translate = QtCore.QCoreApplication.translate
        u2p.setWindowTitle(_translate("u2p", "U2P Simulator"))
        self.label_account_name.setText(_translate("u2p", "Школа<br> Предпринимателей"))
        # self.label.setText(_translate("u2p", "Игра №99999"))
        self.pushButton_savegame.setText(_translate("u2p", "Сохранить игру"))
        self.pushButton_closegame.setText(_translate("u2p", "Закончить игру"))
        self.label_company_list.setText(_translate("u2p", "Список компаний"))
        self.label_company_list_name.setText(_translate("u2p", "НАЗАНИЕ"))
        self.label_company_list_upi.setText(_translate("u2p", "UPI"))
        self.label_company_place_1.setText(_translate("u2p", "1."))
        self.label_company_place_2.setText(_translate("u2p", "2."))
        self.label_company_place_3.setText(_translate("u2p", "3."))
        self.label_company_place_4.setText(_translate("u2p", "4."))
        self.label_company_place_5.setText(_translate("u2p", "5."))
        self.label_company_place_6.setText(_translate("u2p", "6."))
        self.label_company_place_7.setText(_translate("u2p", "7."))
        self.label_company_place_8.setText(_translate("u2p", "8."))
        # self.label_company_name_2.setText(_translate("u2p", "PQRLLC"))
        # self.label_company_name_3.setText(_translate("u2p", "GHIComp"))
        # self.label_company_name_7.setText(_translate("u2p", "XYZInc"))
        # self.label_company_name_6.setText(_translate("u2p", "JKLIndus"))
        # self.label_company_name_4.setText(_translate("u2p", "DEFLtd"))
        # self.label_company_name_1.setText(_translate("u2p", "QRSCo"))
        # self.label_company_name_5.setText(_translate("u2p", "ABCCorp"))
        # self.label_company_name_8.setText(_translate("u2p", "MNOGroup"))
        # self.label_company_upi_2.setText(_translate("u2p", "350"))
        # self.label_company_upi_1.setText(_translate("u2p", "380"))
        # self.label_company_upi_4.setText(_translate("u2p", "290"))
        # self.label_company_upi_3.setText(_translate("u2p", "300"))
        # self.label_company_upi_6.setText(_translate("u2p", "190"))
        # self.label_company_upi_5.setText(_translate("u2p", "230"))
        # self.label_company_upi_8.setText(_translate("u2p", "120"))
        # self.label_company_upi_7.setText(_translate("u2p", "160"))
        self.label_company_arrow_num_1.setText(_translate("u2p", "1"))
        self.label_company_arrow_num_2.setText(_translate("u2p", "1"))
        self.label_company_arrow_num_3.setText(_translate("u2p", "1"))
        self.label_company_arrow_num_4.setText(_translate("u2p", "1"))
        self.label_company_arrow_num_5.setText(_translate("u2p", "1"))
        self.label_company_arrow_num_6.setText(_translate("u2p", "1"))
        self.label_company_arrow_num_7.setText(_translate("u2p", "1"))
        self.label_company_arrow_num_8.setText(_translate("u2p", "1"))
        #self.label_current_period.setText(_translate("u2p", "Период №99"))
        self.label_decisions.setText(_translate("u2p", "Решения"))
        self.pushButton_EnterallDecisions.setText(_translate("u2p", "Ввод решений"))
        self.pushButton_ReviewDecisions.setText(_translate("u2p", "Правка решений"))
        self.pushButton_ClosePeriod.setText(_translate("u2p", "Закрыть период"))
        self.label_results.setText(_translate("u2p", "Результаты"))
        self.pushButton_Print.setText(_translate("u2p", "Печать"))
        self.pushButton_Graph.setText(_translate("u2p", "Графики"))
        self.pushButton_View.setText(_translate("u2p", "Смотреть"))
        self.label_period_options.setText(_translate("u2p", "Настройки периода"))
        self.pushButton_Parameters.setText(_translate("u2p", "Параметры"))
        self.pushButton_Restart.setText(_translate("u2p", "Перезапустить"))


    
    def save_game(self):
        pass

    def close_game(self):
        pass
  
    def pushButton_EnterallDecisions_was_clicked(self):
        self.EnterallDecisions = QtWidgets.QDialog()
        self.EnterallDecisions_ui = Ui_Dialog_Enter_decisions_select_company()
        self.EnterallDecisions_ui.setupUi(self.EnterallDecisions, self.game_data_db)
        self.EnterallDecisions.exec()

    def pushButton_ReviewDecisions_was_clicked(self):
        pass

    def pushButton_ClosePeriod_was_clicked(self):
        pass

    def pushButton_View_was_clicked(self):
        pass

    def pushButton_Print_was_clicked(self):
        pass

    def pushButton_Graph_was_clicked(self):
        pass

    def pushButton_Restart_was_clicked(self):
        pass

    def pushButton_ClosePeriod_was_clicked(self):
        pass    

    def top_company_list(self):
        company_upi_dict = {}
        companies_name = literal_eval(self.game_data_db[-1][3])
        data_periods = literal_eval(self.game_data_db[-1][2])
        n = 1
        for i in data_periods[-1]["data"]["upi"]:
            company_upi_dict[companies_name[f"Company_{n}"]] = i
            n += 1
        sorted_company_upi_dict = list(sorted(company_upi_dict.items(), key=lambda x:x[1], reverse=True))
        
        for i in range(8 - len(sorted_company_upi_dict)):
            sorted_company_upi_dict.append(("", ""))
                
        self.label_company_name_1.setText(str(sorted_company_upi_dict[0][0]))
        self.label_company_upi_1.setText(str(sorted_company_upi_dict[0][1]))
        self.label_company_name_2.setText(str(sorted_company_upi_dict[1][0]))
        self.label_company_upi_2.setText(str(sorted_company_upi_dict[1][1]))
        self.label_company_name_3.setText(str(sorted_company_upi_dict[2][0]))
        self.label_company_upi_3.setText(str(sorted_company_upi_dict[2][1]))
        self.label_company_name_4.setText(str(sorted_company_upi_dict[3][0]))
        self.label_company_upi_4.setText(str(sorted_company_upi_dict[3][1]))
        self.label_company_name_5.setText(str(sorted_company_upi_dict[4][0]))
        self.label_company_upi_5.setText(str(sorted_company_upi_dict[4][1]))
        self.label_company_name_6.setText(str(sorted_company_upi_dict[5][0]))
        self.label_company_upi_6.setText(str(sorted_company_upi_dict[5][1]))
        self.label_company_name_7.setText(str(sorted_company_upi_dict[6][0]))
        self.label_company_upi_7.setText(str(sorted_company_upi_dict[6][1]))
        self.label_company_name_8.setText(str(sorted_company_upi_dict[7][0]))
        self.label_company_upi_8.setText(str(sorted_company_upi_dict[7][1]))



        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    u2p = QtWidgets.QDialog()
    ui = Ui_u2p()
    ui.setupUi(u2p)
    u2p.show()
    
    sys.exit(app.exec())
