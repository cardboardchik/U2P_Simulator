# Form implementation generated from reading ui file 'Dialog_EnterDecisions.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 410)
        
        Dialog.setMinimumSize(QtCore.QSize(600, 410))
        Dialog.setMaximumSize(QtCore.QSize(600, 410))
        
        self.f = open("logs.txt", "r").readline()
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 370, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label_Decision = QtWidgets.QLabel(Dialog)
        self.label_Decision.setGeometry(QtCore.QRect(20, 11, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.label_Decision.setFont(font)
        self.label_Decision.setObjectName("label_Decision")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 38, 379, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(190, 0, 16, 349))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(280, 0, 16, 349))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_UnitPrice = QtWidgets.QLabel(Dialog)
        self.label_UnitPrice.setGeometry(QtCore.QRect(20, 65, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_UnitPrice.setFont(font)
        self.label_UnitPrice.setObjectName("label_UnitPrice")
        self.label_Production = QtWidgets.QLabel(Dialog)
        self.label_Production.setGeometry(QtCore.QRect(20, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_Production.setFont(font)
        self.label_Production.setObjectName("label_Production")
        self.label_Marketing = QtWidgets.QLabel(Dialog)
        self.label_Marketing.setGeometry(QtCore.QRect(20, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_Marketing.setFont(font)
        self.label_Marketing.setObjectName("label_Marketing")
        self.label_Capacity__ = QtWidgets.QLabel(Dialog)
        self.label_Capacity__.setGeometry(QtCore.QRect(20, 125, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_Capacity__.setFont(font)
        self.label_Capacity__.setObjectName("label_Capacity__")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 100, 379, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 160, 379, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(0, 220, 379, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(0, 280, 379, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_RandD = QtWidgets.QLabel(Dialog)
        self.label_RandD.setGeometry(QtCore.QRect(20, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_RandD.setFont(font)
        self.label_RandD.setObjectName("label_RandD")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(0, 340, 380, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_Period_Past = QtWidgets.QLabel(Dialog)
        self.label_Period_Past.setGeometry(QtCore.QRect(202, 11, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.label_Period_Past.setFont(font)
        self.label_Period_Past.setObjectName("label_Period_Past")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(370, 0, 16, 348))
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_Period_Present = QtWidgets.QLabel(Dialog)
        self.label_Period_Present.setGeometry(QtCore.QRect(292, 11, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.label_Period_Present.setFont(font)
        self.label_Period_Present.setObjectName("label_Period_Present")
        self.label_Deprec__ = QtWidgets.QLabel(Dialog)
        self.label_Deprec__.setGeometry(QtCore.QRect(20, 245, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_Deprec__.setFont(font)
        self.label_Deprec__.setObjectName("label_Deprec__")
        self.label_CapInv = QtWidgets.QLabel(Dialog)
        self.label_CapInv.setGeometry(QtCore.QRect(20, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_CapInv.setFont(font)
        self.label_CapInv.setObjectName("label_CapInv")
        self.label_UnitPrice_unit_Past = QtWidgets.QLabel(Dialog)
        self.label_UnitPrice_unit_Past.setGeometry(QtCore.QRect(202, 65, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_UnitPrice_unit_Past.setFont(font)
        self.label_UnitPrice_unit_Past.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_UnitPrice_unit_Past.setObjectName("label_UnitPrice_unit_Past")
        self.label_Production_unit_Past = QtWidgets.QLabel(Dialog)
        self.label_Production_unit_Past.setGeometry(QtCore.QRect(202, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_Production_unit_Past.setFont(font)
        self.label_Production_unit_Past.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Production_unit_Past.setObjectName("label_Production_unit_Past")
        self.label_Marketing_unit_Past = QtWidgets.QLabel(Dialog)
        self.label_Marketing_unit_Past.setGeometry(QtCore.QRect(202, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_Marketing_unit_Past.setFont(font)
        self.label_Marketing_unit_Past.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Marketing_unit_Past.setObjectName("label_Marketing_unit_Past")
        self.label_CapInv_unit_Past = QtWidgets.QLabel(Dialog)
        self.label_CapInv_unit_Past.setGeometry(QtCore.QRect(202, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_CapInv_unit_Past.setFont(font)
        self.label_CapInv_unit_Past.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_CapInv_unit_Past.setObjectName("label_CapInv_unit_Past")
        self.label_RandD_unit_Past = QtWidgets.QLabel(Dialog)
        self.label_RandD_unit_Past.setGeometry(QtCore.QRect(202, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label_RandD_unit_Past.setFont(font)
        self.label_RandD_unit_Past.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_RandD_unit_Past.setObjectName("label_RandD_unit_Past")
        self.lineEdit_UnitPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_UnitPrice.setGeometry(QtCore.QRect(292, 63, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.lineEdit_UnitPrice.setFont(font)
        self.lineEdit_UnitPrice.setMaxLength(6)
        self.lineEdit_UnitPrice.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_UnitPrice.setObjectName("lineEdit_UnitPrice")
        self.lineEdit_Production = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Production.setGeometry(QtCore.QRect(292, 123, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.lineEdit_Production.setFont(font)
        self.lineEdit_Production.setMaxLength(6)
        self.lineEdit_Production.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Production.setObjectName("lineEdit_Production")
        self.lineEdit_Marketing = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Marketing.setGeometry(QtCore.QRect(292, 183, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.lineEdit_Marketing.setFont(font)
        self.lineEdit_Marketing.setMaxLength(6)
        self.lineEdit_Marketing.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Marketing.setObjectName("lineEdit_Marketing")
        self.lineEdit_CapInv = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_CapInv.setGeometry(QtCore.QRect(292, 243, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.lineEdit_CapInv.setFont(font)
        self.lineEdit_CapInv.setMaxLength(6)
        self.lineEdit_CapInv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_CapInv.setObjectName("lineEdit_CapInv")
        self.lineEdit_RandD = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_RandD.setGeometry(QtCore.QRect(292, 303, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.lineEdit_RandD.setFont(font)
        self.lineEdit_RandD.setMaxLength(6)
        self.lineEdit_RandD.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_RandD.setObjectName("lineEdit_RandD")
        self.label_AvailbleCash = QtWidgets.QLabel(Dialog)
        self.label_AvailbleCash.setGeometry(QtCore.QRect(390, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_AvailbleCash.setFont(font)
        self.label_AvailbleCash.setObjectName("label_AvailbleCash")
        self.label_AvailbleCash_int = QtWidgets.QLabel(Dialog)
        self.label_AvailbleCash_int.setGeometry(QtCore.QRect(520, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_AvailbleCash_int.setFont(font)
        self.label_AvailbleCash_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_AvailbleCash_int.setObjectName("label_AvailbleCash_int")
        self.label_CreditLine = QtWidgets.QLabel(Dialog)
        self.label_CreditLine.setGeometry(QtCore.QRect(390, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_CreditLine.setFont(font)
        self.label_CreditLine.setObjectName("label_CreditLine")
        self.label_CreditLine_int = QtWidgets.QLabel(Dialog)
        self.label_CreditLine_int.setGeometry(QtCore.QRect(520, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_CreditLine_int.setFont(font)
        self.label_CreditLine_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_CreditLine_int.setObjectName("label_CreditLine_int")
        self.label_FundsAvailable = QtWidgets.QLabel(Dialog)
        self.label_FundsAvailable.setGeometry(QtCore.QRect(390, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_FundsAvailable.setFont(font)
        self.label_FundsAvailable.setObjectName("label_FundsAvailable")
        self.label_FundsAvailable_int = QtWidgets.QLabel(Dialog)
        self.label_FundsAvailable_int.setGeometry(QtCore.QRect(520, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_FundsAvailable_int.setFont(font)
        self.label_FundsAvailable_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_FundsAvailable_int.setObjectName("label_FundsAvailable_int")
        self.label_ProductionCost = QtWidgets.QLabel(Dialog)
        self.label_ProductionCost.setGeometry(QtCore.QRect(390, 130, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_ProductionCost.setFont(font)
        self.label_ProductionCost.setObjectName("label_ProductionCost")
        self.label_ProductionCost_int = QtWidgets.QLabel(Dialog)
        self.label_ProductionCost_int.setGeometry(QtCore.QRect(520, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_ProductionCost_int.setFont(font)
        self.label_ProductionCost_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ProductionCost_int.setObjectName("label_ProductionCost_int")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(380, 100, 221, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(370, 0, 21, 348))
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_CostUnit__ = QtWidgets.QLabel(Dialog)
        self.label_CostUnit__.setGeometry(QtCore.QRect(390, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.label_CostUnit__.setFont(font)
        self.label_CostUnit__.setObjectName("label_CostUnit__")
        self.label_MarketingCost = QtWidgets.QLabel(Dialog)
        self.label_MarketingCost.setGeometry(QtCore.QRect(390, 170, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_MarketingCost.setFont(font)
        self.label_MarketingCost.setObjectName("label_MarketingCost")
        self.label_MarketingCost_int = QtWidgets.QLabel(Dialog)
        self.label_MarketingCost_int.setGeometry(QtCore.QRect(520, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_MarketingCost_int.setFont(font)
        self.label_MarketingCost_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_MarketingCost_int.setObjectName("label_MarketingCost_int")
        self.label_NetInv = QtWidgets.QLabel(Dialog)
        self.label_NetInv.setGeometry(QtCore.QRect(390, 190, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_NetInv.setFont(font)
        self.label_NetInv.setObjectName("label_NetInv")
        self.label_NetInv_int = QtWidgets.QLabel(Dialog)
        self.label_NetInv_int.setGeometry(QtCore.QRect(520, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_NetInv_int.setFont(font)
        self.label_NetInv_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_NetInv_int.setObjectName("label_NetInv_int")
        self.label_RandDCost = QtWidgets.QLabel(Dialog)
        self.label_RandDCost.setGeometry(QtCore.QRect(390, 210, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_RandDCost.setFont(font)
        self.label_RandDCost.setObjectName("label_RandDCost")
        self.label_RandDCost_int = QtWidgets.QLabel(Dialog)
        self.label_RandDCost_int.setGeometry(QtCore.QRect(520, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_RandDCost_int.setFont(font)
        self.label_RandDCost_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_RandDCost_int.setObjectName("label_RandDCost_int")
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(380, 230, 221, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_FundsReamaining = QtWidgets.QLabel(Dialog)
        self.label_FundsReamaining.setGeometry(QtCore.QRect(390, 240, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_FundsReamaining.setFont(font)
        self.label_FundsReamaining.setObjectName("label_FundsReamaining")
        self.label_FundsReamaining_int = QtWidgets.QLabel(Dialog)
        self.label_FundsReamaining_int.setGeometry(QtCore.QRect(520, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_FundsReamaining_int.setFont(font)
        self.label_FundsReamaining_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_FundsReamaining_int.setObjectName("label_FundsReamaining_int")
        self.label_ReamainingCash = QtWidgets.QLabel(Dialog)
        self.label_ReamainingCash.setGeometry(QtCore.QRect(390, 260, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_ReamainingCash.setFont(font)
        self.label_ReamainingCash.setObjectName("label_ReamainingCash")
        self.label_ReamainingCash_int = QtWidgets.QLabel(Dialog)
        self.label_ReamainingCash_int.setGeometry(QtCore.QRect(520, 260, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_ReamainingCash_int.setFont(font)
        self.label_ReamainingCash_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ReamainingCash_int.setObjectName("label_ReamainingCash_int")
        self.label_ReamainingCredit = QtWidgets.QLabel(Dialog)
        self.label_ReamainingCredit.setGeometry(QtCore.QRect(390, 280, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_ReamainingCredit.setFont(font)
        self.label_ReamainingCredit.setObjectName("label_ReamainingCredit")
        self.label_ReamainingCredit_int = QtWidgets.QLabel(Dialog)
        self.label_ReamainingCredit_int.setGeometry(QtCore.QRect(520, 280, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_ReamainingCredit_int.setFont(font)
        self.label_ReamainingCredit_int.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ReamainingCredit_int.setObjectName("label_ReamainingCredit_int")

        self.retranslateUi(Dialog)
        
        
        self.lineEdit_UnitPrice.textChanged.connect(self.change_UnitPrice)
        self.lineEdit_Production.textChanged.connect(self.change_Production)
        self.lineEdit_Marketing.textChanged.connect(self.change_Marketing)
        self.lineEdit_CapInv.textChanged.connect(self.change_CI)
        self.lineEdit_RandD.textChanged.connect(self.change_RandD)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.save)# type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.cacel)# type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.data = {
            "company": self.f[0:-1],
            "UnitPrice": 30,
            "Production": 393,
            "Marketing": 1050,
            "CI": 1050,
            "RandD": 393
            }
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enter Decisions for " + self.f[0:-1]))
        self.label_Decision.setText(_translate("Dialog", "Decision"))
        self.label_UnitPrice.setText(_translate("Dialog", "Unit Price"))
        self.label_Production.setText(_translate("Dialog", "Production"))
        self.label_Marketing.setText(_translate("Dialog", "Marketing"))
        self.label_Capacity__.setText(_translate("Dialog", "(Capacity = 525)"))
        self.label_RandD.setText(_translate("Dialog", "R and D"))
        self.label_Period_Past.setText(_translate("Dialog", "Period 0"))
        self.label_Period_Present.setText(_translate("Dialog", "Period 0+"))
        self.label_Deprec__.setText(_translate("Dialog", "(Depreciaction = 1050$)"))
        self.label_CapInv.setText(_translate("Dialog", "Capital Investment"))
        self.label_UnitPrice_unit_Past.setText(_translate("Dialog", "30"))
        self.label_Production_unit_Past.setText(_translate("Dialog", "393"))
        self.label_Marketing_unit_Past.setText(_translate("Dialog", "1050"))
        self.label_CapInv_unit_Past.setText(_translate("Dialog", "1050"))
        self.label_RandD_unit_Past.setText(_translate("Dialog", "393"))
        self.lineEdit_UnitPrice.setText(_translate("Dialog", "30"))
        self.lineEdit_Production.setText(_translate("Dialog", "393"))
        self.lineEdit_Marketing.setText(_translate("Dialog", "1050"))
        self.lineEdit_CapInv.setText(_translate("Dialog", "1050"))
        self.lineEdit_RandD.setText(_translate("Dialog", "393"))
        self.label_AvailbleCash.setText(_translate("Dialog", "Available Cash"))
        self.label_AvailbleCash_int.setText(_translate("Dialog", "0"))
        self.label_CreditLine.setText(_translate("Dialog", "Credit Line"))
        self.label_CreditLine_int.setText(_translate("Dialog", "0"))
        self.label_FundsAvailable.setText(_translate("Dialog", "Funds Availalble"))
        self.label_FundsAvailable_int.setText(_translate("Dialog", "0"))
        self.label_ProductionCost.setText(_translate("Dialog", "Production Cost"))
        self.label_ProductionCost_int.setText(_translate("Dialog", "0"))
        self.label_CostUnit__.setText(_translate("Dialog", "(Cost/Unit = 18.36$)"))
        self.label_MarketingCost.setText(_translate("Dialog", "Marketing Cost"))
        self.label_MarketingCost_int.setText(_translate("Dialog", "0"))
        self.label_NetInv.setText(_translate("Dialog", "Net Investment"))
        self.label_NetInv_int.setText(_translate("Dialog", "0"))
        self.label_RandDCost.setText(_translate("Dialog", "R and D Cost"))
        self.label_RandDCost_int.setText(_translate("Dialog", "0"))
        self.label_FundsReamaining.setText(_translate("Dialog", "Funds Reamaining"))
        self.label_FundsReamaining_int.setText(_translate("Dialog", "0"))
        self.label_ReamainingCash.setText(_translate("Dialog", "Remaining Cash"))
        self.label_ReamainingCash_int.setText(_translate("Dialog", "0"))
        self.label_ReamainingCredit.setText(_translate("Dialog", "Reamaining Credit"))
        self.label_ReamainingCredit_int.setText(_translate("Dialog", "0"))

    def change_UnitPrice(self, i):
        self.data["UnitPrice"] = i
        
    def change_Production(self, i):
        self.data["Production"] = i
           
    def change_Marketing(self, i):
        self.data["Marketing"] = i
        
    def change_CI(self, i):
        self.data["CI"] = i
        
    def change_RandD(self, i):
        self.data["RandD"] = i       

        
    def save(self):
        open("logs.txt", "a").write("T")
        
        
        
        with open("data.json",'r+') as file:
          # First we load existing data into a dict.
            file_data = json.load(file)
        # Join new_data with file_data inside emp_details
            file_data["input_data"].append(self.data)
        # Sets file's current position at offset.
            file.seek(0)
        # convert back to json.
            json.dump(file_data, file, indent = 4)
        
    def cacel(self):
        open("logs.txt", "a").write("F")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    sys.exit(app.exec())
    