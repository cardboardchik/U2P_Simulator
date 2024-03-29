
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Change_Level_of_Play(object):
    def setupUi(self, Dialog_Change_Level_of_Play):
        Dialog_Change_Level_of_Play.setObjectName("Dialog_Change_Level_of_Play")
        Dialog_Change_Level_of_Play.resize(500, 240)
        Dialog_Change_Level_of_Play.setMinimumSize(QtCore.QSize(500, 240))
        Dialog_Change_Level_of_Play.setMaximumSize(QtCore.QSize(500, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_Change_Level_of_Play.setWindowIcon(icon)
        Dialog_Change_Level_of_Play.setAutoFillBackground(False)
        Dialog_Change_Level_of_Play.setSizeGripEnabled(False)
        Dialog_Change_Level_of_Play.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Change_Level_of_Play)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.radioButton_Price = QtWidgets.QRadioButton(Dialog_Change_Level_of_Play)

        self.radioButton_Price.setEnabled(False) #temporarily unavailable

        self.radioButton_Price.setGeometry(QtCore.QRect(30, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_Price.setFont(font)
        self.radioButton_Price.setCheckable(True)
        self.radioButton_Price.setObjectName("radioButton_Price")
        self.radioButton_Price_Production = QtWidgets.QRadioButton(Dialog_Change_Level_of_Play)

        self.radioButton_Price_Production.setEnabled(False) #temporarily unavailable

        self.radioButton_Price_Production.setGeometry(QtCore.QRect(30, 60, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_Price_Production.setFont(font)
        self.radioButton_Price_Production.setCheckable(True)
        self.radioButton_Price_Production.setObjectName("radioButton_Price_Production")
        self.radioButton_Price_Production_Marketing = QtWidgets.QRadioButton(Dialog_Change_Level_of_Play)

        self.radioButton_Price_Production_Marketing.setEnabled(False) #temporarily unavailable

        self.radioButton_Price_Production_Marketing.setGeometry(QtCore.QRect(30, 90, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_Price_Production_Marketing.setFont(font)
        self.radioButton_Price_Production_Marketing.setCheckable(True)
        self.radioButton_Price_Production_Marketing.setObjectName("radioButton_Price_Production_Marketing")
        self.radioButton_Price_Production_Marketing_CI = QtWidgets.QRadioButton(Dialog_Change_Level_of_Play)

        self.radioButton_Price_Production_Marketing_CI.setEnabled(False) #temporarily unavailable

        self.radioButton_Price_Production_Marketing_CI.setGeometry(QtCore.QRect(30, 120, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_Price_Production_Marketing_CI.setFont(font)
        self.radioButton_Price_Production_Marketing_CI.setCheckable(True)
        self.radioButton_Price_Production_Marketing_CI.setChecked(False)
        self.radioButton_Price_Production_Marketing_CI.setAutoRepeat(False)
        self.radioButton_Price_Production_Marketing_CI.setAutoExclusive(True)
        self.radioButton_Price_Production_Marketing_CI.setObjectName("radioButton_Price_Production_Marketing_CI")
        self.radioButton_Price_Production_Marketing_CI_RD = QtWidgets.QRadioButton(Dialog_Change_Level_of_Play)
        self.radioButton_Price_Production_Marketing_CI_RD.setGeometry(QtCore.QRect(30, 150, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_Price_Production_Marketing_CI_RD.setFont(font)
        self.radioButton_Price_Production_Marketing_CI_RD.setChecked(True)
        self.radioButton_Price_Production_Marketing_CI_RD.setAutoRepeat(False)
        self.radioButton_Price_Production_Marketing_CI_RD.setObjectName("radioButton_Price_Production_Marketing_CI_RD")


        self.retranslateUi(Dialog_Change_Level_of_Play)
        self.buttonBox.accepted.connect(Dialog_Change_Level_of_Play.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_Change_Level_of_Play.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_Change_Level_of_Play)

    def retranslateUi(self, Dialog_Change_Level_of_Play):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Change_Level_of_Play.setWindowTitle(_translate("Dialog_Change_Level_of_Play", "Change Level of Play"))
        self.radioButton_Price.setText(_translate("Dialog_Change_Level_of_Play", "Price"))
        self.radioButton_Price_Production.setText(_translate("Dialog_Change_Level_of_Play", "Price, Production"))
        self.radioButton_Price_Production_Marketing.setText(_translate("Dialog_Change_Level_of_Play", "Price, Production, Marketing"))
        self.radioButton_Price_Production_Marketing_CI.setText(_translate("Dialog_Change_Level_of_Play", "Price, Production, Marketing, Capital Investment"))
        self.radioButton_Price_Production_Marketing_CI_RD.setText(_translate("Dialog_Change_Level_of_Play", "Price, Production, Marketing, Capital Investment, R and  D"))
       
    def yes_was_clicked(self):
        pass

    def first(self):
        pass

    def second(self):
        pass

    def third(self):
        pass

    def forth(self):
        pass

    def fifth(self):
        pass





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Change_Level_of_Play = QtWidgets.QDialog()
    ui = Ui_Dialog_Change_Level_of_Play()
    ui.setupUi(Dialog_Change_Level_of_Play)
    Dialog_Change_Level_of_Play.show()
    sys.exit(app.exec())
