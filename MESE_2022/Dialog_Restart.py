
## by karton4ik

from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Dialog_Restart(object):
    
    def setupUi(self, Dialog_Restart):
        self.Bool = False
        Dialog_Restart.setObjectName("Dialog_Restart")
        Dialog_Restart.resize(350, 130)
        Dialog_Restart.setMinimumSize(QtCore.QSize(350, 130))
        Dialog_Restart.setMaximumSize(QtCore.QSize(350, 130))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/reload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_Restart.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Restart)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 90, 311, 32))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.No|QtWidgets.QDialogButtonBox.StandardButton.Yes)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_Restart)
        self.label.setGeometry(QtCore.QRect(50, 40, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_Restart)
        self.buttonBox.accepted.connect(Dialog_Restart.accept)
        self.buttonBox.accepted.connect(self.yes_was_clicked)
        self.buttonBox.rejected.connect(Dialog_Restart.reject)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog_Restart)

    def retranslateUi(self, Dialog_Restart):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Restart.setWindowTitle(_translate("Dialog_Restart", "Restart the game?"))
        self.label.setText(_translate("Dialog_Restart", "Do you want to restart the game?"))
    
    def yes_was_clicked(self):
        # clear all files to avoid bugs
        # чистим все файлы во избежание багов
        open("result.txt", "w").close()
        open("data.json", "w").close()
        open("ClosePeriod_log.txt", "w").close()
        open("logs.txt", "w").close()
        # "settings.txt" and "Dialog_Setup.txt" files don't need to be cleaned
        # файлы "settings.txt" и "Dialog_Setup.txt" не нуждаются в очистке 
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Restart = QtWidgets.QDialog()
    ui = Ui_Dialog_Restart()
    ui.setupUi(Dialog_Restart)
    Dialog_Restart.show()
    sys.exit(app.exec())
