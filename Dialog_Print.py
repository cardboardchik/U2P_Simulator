
## by karton4ik

from PyQt6 import QtCore, QtGui, QtWidgets, QtPrintSupport
from ast import literal_eval
import win32print
import win32api
import subprocess
import time
from PyPDF2 import PdfMerger



class Ui_Dialog_Print(object):
    def setupUi(self, Dialog_Print):
        
        Dialog_Print.setObjectName("Dialog_Print")
        Dialog_Print.resize(380, 300)
        Dialog_Print.setMinimumSize(QtCore.QSize(380, 300))
        Dialog_Print.setMaximumSize(QtCore.QSize(380, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/setting.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_Print.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Print)
        self.buttonBox.setGeometry(QtCore.QRect(107, 270, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox_1 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_1.setGeometry(QtCore.QRect(70, 50, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setChecked(True)
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 80, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_3.setGeometry(QtCore.QRect(70, 110, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_4.setGeometry(QtCore.QRect(70, 140, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_5.setGeometry(QtCore.QRect(220, 50, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_6.setGeometry(QtCore.QRect(220, 80, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_7.setGeometry(QtCore.QRect(220, 110, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_8.setGeometry(QtCore.QRect(220, 140, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setObjectName("checkBox_8")
        self.label = QtWidgets.QLabel(Dialog_Print)
        self.label.setGeometry(QtCore.QRect(60, 10, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog_Print)
        self.line.setGeometry(QtCore.QRect(0, 160, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.checkBox_Industry = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_Industry.setEnabled(False)
        self.checkBox_Industry.setGeometry(QtCore.QRect(80, 180, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_Industry.setFont(font)
        self.checkBox_Industry.setObjectName("checkBox_Industry")
        self.checkBox_Summary = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_Summary.setEnabled(False)
        self.checkBox_Summary.setGeometry(QtCore.QRect(80, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_Summary.setFont(font)
        self.checkBox_Summary.setObjectName("checkBox_Summary")
        self.checkBox_SR = QtWidgets.QCheckBox(Dialog_Print)
        self.checkBox_SR.setGeometry(QtCore.QRect(210, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.checkBox_SR.setFont(font)
        self.checkBox_SR.setChecked(True)
        self.checkBox_SR.setTristate(False)
        self.checkBox_SR.setObjectName("checkBox_SR")
        self.lineEdit_Industry = QtWidgets.QLineEdit(Dialog_Print)
        self.lineEdit_Industry.setEnabled(False)
        self.lineEdit_Industry.setGeometry(QtCore.QRect(160, 180, 25, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.lineEdit_Industry.setFont(font)
        self.lineEdit_Industry.setMaxLength(3)
        self.lineEdit_Industry.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Industry.setObjectName("lineEdit_Industry")
        
        self.label_ATTENTION = QtWidgets.QLabel(Dialog_Print)
        self.label_ATTENTION.setGeometry(QtCore.QRect(35, 230, 340, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.label_ATTENTION.setFont(font)
        self.label_ATTENTION.setObjectName("label_1")
        self.label_ATTENTION.setText("ATTENTION! The default printer is used for printing.")
        self.label_ATTENTION.setOpenExternalLinks(True)
        self.label_ATTENTION.setStyleSheet("color: red;")
        
        self.label_download = QtWidgets.QLabel(Dialog_Print)
        self.label_download.setGeometry(QtCore.QRect(115, 242.5, 340, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.label_download.setFont(font)
        self.label_download.setObjectName("label_1")
        self.label_download.setText("Get acrobat you can <a href='https://get.adobe.com/reader/'>here</a>.")
        self.label_download.setOpenExternalLinks(True)
        
        self.label_prompt = QtWidgets.QLabel(Dialog_Print)
        self.label_prompt.setGeometry(QtCore.QRect(20, 255, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.label_prompt.setFont(font)
        self.label_prompt.setObjectName("label_1")
        self.label_prompt.setText("To print, you need to take a few simple steps. <a href='https://helpx.adobe.com/acrobat/kb/not-default-pdf-owner-windows10.html'>Instruction</a>.")
        self.label_prompt.setOpenExternalLinks(True)

        self.setup = literal_eval(open("Dialog_Setup.txt").readline())
        setup_len = len(self.setup)

        self.checkBox_status = {
            f"Company_{i}": True for i in range(1, setup_len + 1)
        }

        self.setup_array = []
        n = 1
        while n <= 8:
            if n <= setup_len:
                self.setup_array.append(self.setup[f"Company_{n}"])
            else:
                self.setup_array.append(f"Company {n}")

            n += 1

        if setup_len == 7:
            self.checkBox_8.setEnabled(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_status["Company_8"] = False
        elif setup_len == 6:
            self.checkBox_8.setEnabled(False)
            self.checkBox_7.setEnabled(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_status["Company_8"] = False
            self.checkBox_status["Company_7"] = False
        elif setup_len == 5:
            self.checkBox_8.setEnabled(False)
            self.checkBox_7.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_status["Company_8"] = False
            self.checkBox_status["Company_7"] = False
            self.checkBox_status["Company_6"] = False
        elif setup_len == 4:
            self.checkBox_8.setEnabled(False)
            self.checkBox_7.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_status["Company_8"] = False
            self.checkBox_status["Company_7"] = False
            self.checkBox_status["Company_6"] = False
            self.checkBox_status["Company_5"] = False
        elif setup_len == 3:
            self.checkBox_8.setEnabled(False)
            self.checkBox_7.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_status["Company_8"] = False
            self.checkBox_status["Company_7"] = False
            self.checkBox_status["Company_6"] = False
            self.checkBox_status["Company_5"] = False
            self.checkBox_status["Company_4"] = False
        elif setup_len == 2:
            self.checkBox_8.setEnabled(False)
            self.checkBox_7.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_status["Company_8"] = False
            self.checkBox_status["Company_7"] = False
            self.checkBox_status["Company_6"] = False
            self.checkBox_status["Company_5"] = False
            self.checkBox_status["Company_4"] = False
            self.checkBox_status["Company_3"] = False
        else:
            pass

        self.retranslateUi(Dialog_Print)
        self.buttonBox.accepted.connect(Dialog_Print.accept)
        self.buttonBox.accepted.connect(self.print)
        self.buttonBox.rejected.connect(Dialog_Print.reject)

        self.checkBox_1.clicked.connect(self.checkBox_1_Clicked)
        self.checkBox_2.clicked.connect(self.checkBox_2_Clicked)
        self.checkBox_3.clicked.connect(self.checkBox_3_Clicked)
        self.checkBox_4.clicked.connect(self.checkBox_4_Clicked)
        self.checkBox_5.clicked.connect(self.checkBox_5_Clicked)
        self.checkBox_6.clicked.connect(self.checkBox_6_Clicked)
        self.checkBox_7.clicked.connect(self.checkBox_7_Clicked)
        self.checkBox_8.clicked.connect(self.checkBox_8_Clicked)

        QtCore.QMetaObject.connectSlotsByName(Dialog_Print)


    def retranslateUi(self, Dialog_Print):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Print.setWindowTitle(_translate("Dialog_Print", "Print"))
        self.checkBox_1.setText(_translate(
            "Dialog_Print", self.setup_array[0]))
        self.checkBox_2.setText(_translate(
            "Dialog_Print", self.setup_array[1]))
        self.checkBox_3.setText(_translate(
            "Dialog_Print", self.setup_array[2]))
        self.checkBox_4.setText(_translate(
            "Dialog_Print", self.setup_array[3]))
        self.checkBox_5.setText(_translate(
            "Dialog_Print", self.setup_array[4]))
        self.checkBox_6.setText(_translate(
            "Dialog_Print", self.setup_array[5]))
        self.checkBox_7.setText(_translate(
            "Dialog_Print", self.setup_array[6]))
        self.checkBox_8.setText(_translate(
            "Dialog_Print", self.setup_array[7]))
        self.label.setText(_translate(
            "Dialog_Print", "Сhoose the ones you want to print"))
        self.checkBox_Industry.setText(_translate("Dialog_Print", "Industry"))
        self.checkBox_Summary.setText(_translate("Dialog_Print", "Summary"))
        self.checkBox_SR.setText(_translate("Dialog_Print", "Short Reports"))
        self.lineEdit_Industry.setText(_translate("Dialog_Print", "E"))

    def checkBox_1_Clicked(self, status):
        self.checkBox_status["Company_1"] = status

    def checkBox_2_Clicked(self, status):
        self.checkBox_status["Company_2"] = status

    def checkBox_3_Clicked(self, status):
        self.checkBox_status["Company_3"] = status

    def checkBox_4_Clicked(self, status):
        self.checkBox_status["Company_4"] = status

    def checkBox_5_Clicked(self, status):
        self.checkBox_status["Company_5"] = status

    def checkBox_6_Clicked(self, status):
        self.checkBox_status["Company_6"] = status

    def checkBox_7_Clicked(self, status):
        self.checkBox_status["Company_7"] = status

    def checkBox_8_Clicked(self, status):
        self.checkBox_status["Company_8"] = status
        
        

    def print(self):
    
        result = literal_eval(open("result.txt", "r").readline())
        companies = literal_eval(open("Dialog_Setup.txt", "r").readline())
        
        # for merger
        pdf_array = []
        
        # for merger
        for i, g in self.checkBox_status.items():
            if g == True:
   
                pdf_array.append(f'./reports/{int(i[-1])}.pdf')
        
        
        # merger PDF files
        merger = PdfMerger()

        for pdf in pdf_array:
            merger.append(pdf)

        merger.write("report_for_print.pdf")
        merger.close()
        
        
        # print report
        currentprinter = win32print.GetDefaultPrinter()

        win32api.ShellExecute(0, "print", "report_for_print.pdf", None,  ".",  0)
        win32print.SetDefaultPrinter(currentprinter)
        
        time.sleep(5)
        
        subprocess.call("TASKKILL /F /IM Acrobat.exe", shell=True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Print = QtWidgets.QDialog()
    ui = Ui_Dialog_Print()
    ui.setupUi(Dialog_Print)
    Dialog_Print.show()
    sys.exit(app.exec())
