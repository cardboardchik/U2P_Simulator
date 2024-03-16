
## by karton4ik

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Setup_error(object):
    def setupUi(self, Dialog_Setup_error):
        Dialog_Setup_error.setObjectName("Dialog_Setup_error")
        Dialog_Setup_error.resize(350, 150)
        Dialog_Setup_error.setMinimumSize(QtCore.QSize(350, 150))
        Dialog_Setup_error.setMaximumSize(QtCore.QSize(350, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/setup_error.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_Setup_error.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Setup_error)
        self.buttonBox.setGeometry(QtCore.QRect(-58, 115, 311, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_Setup_error)
        self.label.setGeometry(QtCore.QRect(110, 40, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_Setup_error)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_photo = QtWidgets.QLabel(Dialog_Setup_error)
        self.label_photo.setGeometry(QtCore.QRect(0, 10, 111, 111))
        self.label_photo.setText("")
        self.label_photo.setPixmap(QtGui.QPixmap("Images/setup_error.png"))
        self.label_photo.setScaledContents(True)
        self.label_photo.setObjectName("label_photo")

        self.retranslateUi(Dialog_Setup_error)
        
        self.buttonBox.accepted.connect(Dialog_Setup_error.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_Setup_error.reject)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog_Setup_error)

    def retranslateUi(self, Dialog_Setup_error):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Setup_error.setWindowTitle(_translate("Dialog_Setup_error", "The usernames are the same"))
        self.label.setText(_translate("Dialog_Setup_error", "The usernames are the same."))
        self.label_2.setText(_translate("Dialog_Setup_error", "Please pick a different name."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Setup_error = QtWidgets.QDialog()
    ui = Ui_Dialog_Setup_error()
    ui.setupUi(Dialog_Setup_error)
    Dialog_Setup_error.show()
    sys.exit(app.exec())
