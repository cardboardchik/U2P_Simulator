
## by karton4ik

from tkinter.tix import Tree
from PyQt6 import QtCore, QtGui, QtWidgets
import ast
from Dialog_Setup_error import Ui_Dialog_Setup_error

class Ui_Dialog_Setup(object):
    def setupUi(self, Dialog_Setup):
        self.file = ast.literal_eval(open("Dialog_Setup.txt", "r").readline())
        Dialog_Setup.setObjectName("Dialog_Setup")
        Dialog_Setup.resize(310, 390)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_Setup.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Setup)
        self.buttonBox.setGeometry(QtCore.QRect(-110, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_8.setGeometry(QtCore.QRect(310, 50, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_1.setGeometry(QtCore.QRect(130, 90, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setMaxLength(8)
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setCursorPosition(3)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_Company5 = QtWidgets.QLabel(Dialog_Setup)
        self.label_Company5.setGeometry(QtCore.QRect(55, 210, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_Company5.setFont(font)
        self.label_Company5.setObjectName("label_Company5")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_6.setGeometry(QtCore.QRect(180, 40, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium Medium")
        font.setPointSize(9)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_label_Company2 = QtWidgets.QLabel(Dialog_Setup)
        self.label_label_Company2.setGeometry(QtCore.QRect(55, 120, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_label_Company2.setFont(font)
        self.label_label_Company2.setObjectName("label_label_Company2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMaxLength(8)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_Company6 = QtWidgets.QLabel(Dialog_Setup)
        self.label_Company6.setGeometry(QtCore.QRect(55, 240, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_Company6.setFont(font)
        self.label_Company6.setObjectName("label_Company6")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_4.setGeometry(QtCore.QRect(100, 40, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_8.setGeometry(QtCore.QRect(260, 40, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.setChecked(True)
        
        
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 210, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setMaxLength(8)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_Company3 = QtWidgets.QLabel(Dialog_Setup)
        self.label_Company3.setGeometry(QtCore.QRect(55, 150, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_Company3.setFont(font)
        self.label_Company3.setObjectName("label_Company3")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 40, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 270, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setMaxLength(8)
        self.lineEdit_7.setFrame(True)
        self.lineEdit_7.setCursorPosition(3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_NumberofCompetitors = QtWidgets.QLabel(Dialog_Setup)
        self.label_NumberofCompetitors.setGeometry(QtCore.QRect(80, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_NumberofCompetitors.setFont(font)
        self.label_NumberofCompetitors.setObjectName("label_NumberofCompetitors")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_7.setGeometry(QtCore.QRect(220, 40, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 300, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setMaxLength(8)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_Company4 = QtWidgets.QLabel(Dialog_Setup)
        self.label_Company4.setGeometry(QtCore.QRect(55, 180, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_Company4.setFont(font)
        self.label_Company4.setObjectName("label_Company4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 180, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setMaxLength(8)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setCursorPosition(3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 150, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setMaxLength(8)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 40, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog_Setup)
        self.radioButton_5.setGeometry(QtCore.QRect(140, 40, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog_Setup)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 240, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setMaxLength(8)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_Company7 = QtWidgets.QLabel(Dialog_Setup)
        self.label_Company7.setGeometry(QtCore.QRect(55, 270, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_Company7.setFont(font)
        self.label_Company7.setObjectName("label_Company7")
        self.label_Company1 = QtWidgets.QLabel(Dialog_Setup)
        self.label_Company1.setGeometry(QtCore.QRect(55, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_Company1.setFont(font)
        self.label_Company1.setObjectName("label_Company1")
        self.label_Company8 = QtWidgets.QLabel(Dialog_Setup)
        self.label_Company8.setGeometry(QtCore.QRect(55, 300, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_Company8.setFont(font)
        self.label_Company8.setObjectName("label_Company8")
        self.line = QtWidgets.QFrame(Dialog_Setup)
        self.line.setGeometry(QtCore.QRect(-10, 60, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog_Setup)
        self.buttonBox.accepted.connect(Dialog_Setup.accept) # type: ignore
        self.buttonBox.accepted.connect(self.save_was_clicked)
        self.buttonBox.rejected.connect(Dialog_Setup.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_Setup)
        
        self.radioButton_8.clicked.connect(self.radioButton_8_selected)
        self.radioButton_7.clicked.connect(self.radioButton_7_selected)
        self.radioButton_6.clicked.connect(self.radioButton_6_selected)
        self.radioButton_5.clicked.connect(self.radioButton_5_selected)
        self.radioButton_4.clicked.connect(self.radioButton_4_selected)
        self.radioButton_3.clicked.connect(self.radioButton_3_selected)
        self.radioButton_2.clicked.connect(self.radioButton_2_selected)
        
        self.lineEdit_1.textChanged.connect(self.lineEdit_1_textChanged)
        self.lineEdit_2.textChanged.connect(self.lineEdit_2_textChanged)
        self.lineEdit_3.textChanged.connect(self.lineEdit_3_textChanged)
        self.lineEdit_4.textChanged.connect(self.lineEdit_4_textChanged)
        self.lineEdit_5.textChanged.connect(self.lineEdit_5_textChanged)
        self.lineEdit_6.textChanged.connect(self.lineEdit_6_textChanged)
        self.lineEdit_7.textChanged.connect(self.lineEdit_7_textChanged)
        self.lineEdit_8.textChanged.connect(self.lineEdit_8_textChanged)

        if self.file == "" or {}:
            pass
        else:
            self.all = 0
            for non in self.file:
                self.all += 1
            if self.all == 8:
                self.lineEdit_1.setText(self.file["Company_1"])
                self.lineEdit_2.setText(self.file["Company_2"])
                self.lineEdit_3.setText(self.file["Company_3"])
                self.lineEdit_4.setText(self.file["Company_4"])
                self.lineEdit_5.setText(self.file["Company_5"])
                self.lineEdit_6.setText(self.file["Company_6"])
                self.lineEdit_7.setText(self.file["Company_7"])
                self.lineEdit_8.setText(self.file["Company_8"])
            elif self.all == 7:
                self.lineEdit_8.setEnabled(False)
                self.label_Company8.setEnabled(False)
                self.radioButton_7.setChecked(True)
                
                self.lineEdit_1.setText(self.file["Company_1"])
                self.lineEdit_2.setText(self.file["Company_2"])
                self.lineEdit_3.setText(self.file["Company_3"])
                self.lineEdit_4.setText(self.file["Company_4"])
                self.lineEdit_5.setText(self.file["Company_5"])
                self.lineEdit_6.setText(self.file["Company_6"])
                self.lineEdit_7.setText(self.file["Company_7"])
            elif self.all == 6:
                self.lineEdit_8.setEnabled(False)
                self.label_Company8.setEnabled(False)
                self.lineEdit_7.setEnabled(False)
                self.label_Company7.setEnabled(False)
                self.radioButton_6.setChecked(True)
                
                self.lineEdit_1.setText(self.file["Company_1"])
                self.lineEdit_2.setText(self.file["Company_2"])
                self.lineEdit_3.setText(self.file["Company_3"])
                self.lineEdit_4.setText(self.file["Company_4"])
                self.lineEdit_5.setText(self.file["Company_5"])
                self.lineEdit_6.setText(self.file["Company_6"])
                
            elif self.all == 5:
                self.lineEdit_8.setEnabled(False)
                self.label_Company8.setEnabled(False)
                self.lineEdit_7.setEnabled(False)
                self.label_Company7.setEnabled(False)
                self.lineEdit_6.setEnabled(False)
                self.label_Company6.setEnabled(False)
                self.radioButton_5.setChecked(True)
                
                self.lineEdit_1.setText(self.file["Company_1"])
                self.lineEdit_2.setText(self.file["Company_2"])
                self.lineEdit_3.setText(self.file["Company_3"])
                self.lineEdit_4.setText(self.file["Company_4"])
                self.lineEdit_5.setText(self.file["Company_5"])
            elif self.all == 4:
                self.lineEdit_8.setEnabled(False)
                self.label_Company8.setEnabled(False)
                self.lineEdit_7.setEnabled(False)
                self.label_Company7.setEnabled(False)
                self.lineEdit_6.setEnabled(False)
                self.label_Company6.setEnabled(False)
                self.lineEdit_5.setEnabled(False)
                self.label_Company5.setEnabled(False)
                self.radioButton_4.setChecked(True)
                
                self.lineEdit_1.setText(self.file["Company_1"])
                self.lineEdit_2.setText(self.file["Company_2"])
                self.lineEdit_3.setText(self.file["Company_3"])
                self.lineEdit_4.setText(self.file["Company_4"])
            elif self.all == 3:
                self.lineEdit_8.setEnabled(False)
                self.label_Company8.setEnabled(False)
                self.lineEdit_7.setEnabled(False)
                self.label_Company7.setEnabled(False)
                self.lineEdit_6.setEnabled(False)
                self.label_Company6.setEnabled(False)
                self.lineEdit_5.setEnabled(False)
                self.label_Company5.setEnabled(False)
                self.lineEdit_4.setEnabled(False)
                self.label_Company4.setEnabled(False)
                self.radioButton_3.setChecked(True)
                
                self.lineEdit_1.setText(self.file["Company_1"])
                self.lineEdit_2.setText(self.file["Company_2"])
                self.lineEdit_3.setText(self.file["Company_3"])
            elif self.all == 2:
                self.lineEdit_8.setEnabled(False)
                self.label_Company8.setEnabled(False)
                self.lineEdit_7.setEnabled(False)
                self.label_Company7.setEnabled(False)
                self.lineEdit_6.setEnabled(False)
                self.label_Company6.setEnabled(False)
                self.lineEdit_5.setEnabled(False)
                self.label_Company5.setEnabled(False)
                self.lineEdit_4.setEnabled(False)
                self.label_Company4.setEnabled(False)
                self.lineEdit_3.setEnabled(False)
                self.label_Company3.setEnabled(False)
                self.radioButton_2.setChecked(True)
                
                self.lineEdit_1.setText(self.file["Company_1"])
                self.lineEdit_2.setText(self.file["Company_2"])

            
        #self.data = {
        #    "Company_1": 111,
        #    "Company_2": 222,
        #    "Company_3": 333,
        #    "Company_4": 444,
        #    "Company_5": 555,
        #    "Company_6": 666,
        #    "Company_7": 777,
        #    "Company_8": 888
        #}
        
    def retranslateUi(self, Dialog_Setup):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Setup.setWindowTitle(_translate("Dialog_Setup", "Setup"))
        self.radioButton_8.setText(_translate("Dialog_Setup", "8"))
        self.lineEdit_1.setText(_translate("Dialog_Setup", "111"))
        self.lineEdit_1.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.label_Company5.setText(_translate("Dialog_Setup", "Company 5"))
        self.radioButton_6.setText(_translate("Dialog_Setup", "6"))
        self.label_label_Company2.setText(_translate("Dialog_Setup", "Company 2"))
        self.lineEdit_2.setText(_translate("Dialog_Setup", "222"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.label_Company6.setText(_translate("Dialog_Setup", "Company 6"))
        self.radioButton_4.setText(_translate("Dialog_Setup", "4"))
        self.radioButton_8.setText(_translate("Dialog_Setup", "8"))
        self.lineEdit_5.setText(_translate("Dialog_Setup", "555"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.label_Company3.setText(_translate("Dialog_Setup", "Company 3"))
        self.radioButton_3.setText(_translate("Dialog_Setup", "3"))
        self.lineEdit_7.setText(_translate("Dialog_Setup", "777"))
        self.lineEdit_7.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.label_NumberofCompetitors.setText(_translate("Dialog_Setup", "Number of Competitors"))
        self.radioButton_7.setText(_translate("Dialog_Setup", "7"))
        self.lineEdit_8.setText(_translate("Dialog_Setup", "888"))
        self.lineEdit_8.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.label_Company4.setText(_translate("Dialog_Setup", "Company 4"))
        self.lineEdit_4.setText(_translate("Dialog_Setup", "444"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.lineEdit_3.setText(_translate("Dialog_Setup", "333"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.radioButton_2.setText(_translate("Dialog_Setup", "2"))
        self.radioButton_5.setText(_translate("Dialog_Setup", "5"))
        self.lineEdit_6.setText(_translate("Dialog_Setup", "666"))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog_Setup", "Company Name"))
        self.label_Company7.setText(_translate("Dialog_Setup", "Company 7"))
        self.label_Company1.setText(_translate("Dialog_Setup", "Company 1"))
        self.label_Company8.setText(_translate("Dialog_Setup", "Company 8"))
    
    #stupid but it works :)
    def reset_lineEdit_text(self):
        self.lineEdit_1.setText("111")
        self.lineEdit_2.setText("222")
        self.lineEdit_3.setText("333")
        self.lineEdit_4.setText("444")
        self.lineEdit_5.setText("555")
        self.lineEdit_6.setText("666")
        self.lineEdit_7.setText("777")
        self.lineEdit_8.setText("888")
        
    def radioButton_8_selected(self):
        self.lineEdit_8.setEnabled(True)
        self.label_Company8.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.label_Company7.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.label_Company6.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.label_Company5.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.label_Company4.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.label_Company3.setEnabled(True)
        
        self.reset_lineEdit_text()
        
        self.file.clear()
        for i in range(1, 8 + 1):
            self.file[f"Company_{i}"] = str(i)*3
            
        self.all = 8
        

    def radioButton_7_selected(self):
        self.lineEdit_8.setEnabled(False)
        self.label_Company8.setEnabled(False)
        self.lineEdit_7.setEnabled(True)
        self.label_Company7.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.label_Company6.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.label_Company5.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.label_Company4.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.label_Company3.setEnabled(True)
        
        self.reset_lineEdit_text()
        
        self.file.clear()
        for i in range(1, 7 + 1):
            self.file[f"Company_{i}"] = str(i)*3
            
        self.all = 7
        
    def radioButton_6_selected(self):
        self.lineEdit_8.setEnabled(False)
        self.label_Company8.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.label_Company7.setEnabled(False)
        self.lineEdit_6.setEnabled(True)
        self.label_Company6.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.label_Company5.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.label_Company4.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.label_Company3.setEnabled(True)
        
        self.reset_lineEdit_text()
        
        self.file.clear()
        for i in range(1, 6 + 1):
            self.file[f"Company_{i}"] = str(i)*3
            
        self.all = 6
        
    def radioButton_5_selected(self):
        self.lineEdit_8.setEnabled(False)
        self.label_Company8.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.label_Company7.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.label_Company6.setEnabled(False)
        self.lineEdit_5.setEnabled(True)
        self.label_Company5.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.label_Company4.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.label_Company3.setEnabled(True)
        
        self.reset_lineEdit_text()
        
        self.file.clear()
        for i in range(1, 5 + 1):
            self.file[f"Company_{i}"] = str(i)*3
            
        self.all = 5
        
    def radioButton_4_selected(self):
        self.lineEdit_8.setEnabled(False)
        self.label_Company8.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.label_Company7.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.label_Company6.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.label_Company5.setEnabled(False)
        self.lineEdit_4.setEnabled(True)
        self.label_Company4.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.label_Company3.setEnabled(True)
        
        self.reset_lineEdit_text()
        
        self.file.clear()
        for i in range(1, 4 + 1):
            self.file[f"Company_{i}"] = str(i)*3
            
        self.all = 4
    
    def radioButton_3_selected(self):
        self.lineEdit_8.setEnabled(False)
        self.label_Company8.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.label_Company7.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.label_Company6.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.label_Company5.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.label_Company4.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        self.label_Company3.setEnabled(True)
        
        self.reset_lineEdit_text()
        
        self.file.clear()
        for i in range(1, 3 + 1):
            self.file[f"Company_{i}"] = str(i)*3
            
        self.all = 3
        
    def radioButton_2_selected(self):
        self.lineEdit_8.setEnabled(False)
        self.label_Company8.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.label_Company7.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.label_Company6.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.label_Company5.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.label_Company4.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.label_Company3.setEnabled(False)
        
        self.reset_lineEdit_text()
        
        self.file.clear()
        for i in range(1, 2 + 1):
            self.file[f"Company_{i}"] = str(i)*3
            
        self.all = 2
        
    def lineEdit_1_textChanged(self, i):
        self.file["Company_1"] = i
    
    def lineEdit_2_textChanged(self, i):
        self.file["Company_2"] = i
    
    def lineEdit_3_textChanged(self, i):
        self.file["Company_3"] = i
    
    def lineEdit_4_textChanged(self, i):
        self.file["Company_4"] = i
    
    def lineEdit_5_textChanged(self, i):
        self.file["Company_5"] = i
    
    def lineEdit_6_textChanged(self, i):
        self.file["Company_6"] = i
    
    def lineEdit_7_textChanged(self, i):
        self.file["Company_7"] = i
    
    def lineEdit_8_textChanged(self, i):
        self.file["Company_8"] = i
    
    
    def save_was_clicked(self):
        result = 0
        for i in range(1, self.all + 1):
            for g in range(1, self.all + 1):
                if i == g or i - 1 == g:
                    pass
                else:
                    try:
                        if self.file[f"Company_{i}"] == self.file[f"Company_{g}"]:
                            result = 1
                    except KeyError:
                        pass
                        
        if result == 1:
            self.Dialog_Setup_error = QtWidgets.QDialog()
            self.Dialog_Setup_error_ui = Ui_Dialog_Setup_error()
            self.Dialog_Setup_error_ui.setupUi(self.Dialog_Setup_error)
            self.Dialog_Setup_error.exec()
        else:            
            f = open("Dialog_Setup.txt", "w")
            f.write(str(self.file))
            f.close()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Setup = QtWidgets.QDialog()
    ui = Ui_Dialog_Setup()
    ui.setupUi(Dialog_Setup)
    Dialog_Setup.show()
    sys.exit(app.exec())
