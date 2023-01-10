# force close

from PyQt6 import QtCore, QtGui, QtWidgets
from ast import literal_eval
from Dialog_ClosePeriod import Ui_Dialog_ClosePeriod


class Ui_Dialog_ClosePeriod_Error(object):
    def setupUi(self, Dialog_ClosePeriod_Error):
        Dialog_ClosePeriod_Error.setObjectName("Dialog_ClosePeriod_Error")
        Dialog_ClosePeriod_Error.resize(200, 300)
        Dialog_ClosePeriod_Error.setMinimumSize(QtCore.QSize(200, 300))
        Dialog_ClosePeriod_Error.setMaximumSize(QtCore.QSize(200, 300))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_ClosePeriod_Error.setWindowIcon(icon)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_ClosePeriod_Error)
        self.buttonBox.setGeometry(QtCore.QRect(19, 260, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label_txt_1 = QtWidgets.QLabel(Dialog_ClosePeriod_Error)
        self.label_txt_1.setGeometry(QtCore.QRect(5, 5, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_txt_1.setFont(font)
        self.label_txt_1.setObjectName("label_txt_1")
        self.label_txt_2 = QtWidgets.QLabel(Dialog_ClosePeriod_Error)
        self.label_txt_2.setGeometry(QtCore.QRect(5, 25, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_txt_2.setFont(font)
        self.label_txt_2.setObjectName("label_txt_2")
        self.listWidget = QtWidgets.QListWidget(Dialog_ClosePeriod_Error)
        self.listWidget.setGeometry(QtCore.QRect(9, 50, 181, 201))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setMovement(QtWidgets.QListView.Movement.Static)
        self.listWidget.setFlow(QtWidgets.QListView.Flow.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.LayoutMode.Batched)
        self.listWidget.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        
        self.file = literal_eval(open("Dialog_Setup.txt", "r").readline())
        
        for i in range(len(self.file)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)

        self.retranslateUi(Dialog_ClosePeriod_Error)
        
        self.buttonBox.accepted.connect(Dialog_ClosePeriod_Error.accept)
        self.buttonBox.accepted.connect(self.yes_was_clicked)
         
        self.buttonBox.rejected.connect(Dialog_ClosePeriod_Error.reject) 
        QtCore.QMetaObject.connectSlotsByName(Dialog_ClosePeriod_Error)
        
        file = open("ClosePeriod_log.txt", "r").readline()
        
        for i in file.split(" "):
                if i== "":
                    pass
                else:
                    self.listWidget.takeItem(int(i))
        

    def retranslateUi(self, Dialog_ClosePeriod_Error):
        period = literal_eval(open('result.txt', 'r').readline())
        _translate = QtCore.QCoreApplication.translate
        Dialog_ClosePeriod_Error.setWindowTitle(_translate("Dialog_ClosePeriod_Error", f"Close Period {period['now_tick']}"))
        self.label_txt_1.setText(_translate("Dialog_ClosePeriod_Error", "There are missing decisions."))
        self.label_txt_2.setText(_translate("Dialog_ClosePeriod_Error", " Do you really want to do it?"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        for i in range(1, len(self.file) + 1):
            try:
                item = self.listWidget.item(i-1)
                item.setText(_translate("Dialog_EnterallDecisions", self.file[f"Company_{i}"]))
                
            except KeyError:
                pass
            
        self.listWidget.setSortingEnabled(__sortingEnabled)

    
    def yes_was_clicked(self):
        
        
        self.Dialog_ClosePeriod = QtWidgets.QDialog()
        self.Dialog_ClosePeriod_ui = Ui_Dialog_ClosePeriod()
        self.Dialog_ClosePeriod_ui.setupUi(self.Dialog_ClosePeriod)
        self.Dialog_ClosePeriod.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ClosePeriod_Error = QtWidgets.QDialog()
    ui = Ui_Dialog_ClosePeriod_Error()
    ui.setupUi(Dialog_ClosePeriod_Error)
    Dialog_ClosePeriod_Error.show()
    sys.exit(app.exec())
