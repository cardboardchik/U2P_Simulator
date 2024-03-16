
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Enter_Decisions_for_company(object):
    def setupUi(self, Dialog_Enter_Decisions_for_company):
        Dialog_Enter_Decisions_for_company.setObjectName("Dialog_Enter_Decisions_for_company")
        Dialog_Enter_Decisions_for_company.resize(650, 550)
        Dialog_Enter_Decisions_for_company.setMinimumSize(QtCore.QSize(650, 550))
        Dialog_Enter_Decisions_for_company.setMaximumSize(QtCore.QSize(650, 550))
        Dialog_Enter_Decisions_for_company.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Enter_Decisions_for_company = QtWidgets.QLabel(Dialog_Enter_Decisions_for_company)
        self.label_Enter_Decisions_for_company.setGeometry(QtCore.QRect(16, 0, 618, 60))
        self.label_Enter_Decisions_for_company.setStyleSheet("color: #1E1E1E;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 100% */")
        self.label_Enter_Decisions_for_company.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Enter_Decisions_for_company.setObjectName("label_Enter_Decisions_for_company")
        self.frame_decisions = QtWidgets.QFrame(Dialog_Enter_Decisions_for_company)
        self.frame_decisions.setGeometry(QtCore.QRect(16, 70, 270, 470))
        self.frame_decisions.setStyleSheet("border-radius: 20px;\n"
"background: #DCDCDC;")
        self.frame_decisions.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_decisions.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_decisions.setObjectName("frame_decisions")
        self.label_decisions = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions.setGeometry(QtCore.QRect(0, 0, 270, 40))
        self.label_decisions.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_decisions.setObjectName("label_decisions")
        self.lineEdit_price = QtWidgets.QLineEdit(self.frame_decisions)
        self.lineEdit_price.setGeometry(QtCore.QRect(16, 77, 209, 38))
        self.lineEdit_price.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.label_decisions_price = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_price.setGeometry(QtCore.QRect(16, 49, 209, 24))
        self.label_decisions_price.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_price.setObjectName("label_decisions_price")
        self.label_decisions_price_dollar = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_price_dollar.setGeometry(QtCore.QRect(235, 80, 15, 30))
        self.label_decisions_price_dollar.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_price_dollar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_decisions_price_dollar.setObjectName("label_decisions_price_dollar")
        self.label_decisions_price_error = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_price_error.setGeometry(QtCore.QRect(16, 115, 209, 20))
        self.label_decisions_price_error.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 12px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_price_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_price_error.setObjectName("label_decisions_price_error")
        self.label_decisions_prod_error = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_prod_error.setGeometry(QtCore.QRect(16, 198, 209, 20))
        self.label_decisions_prod_error.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 12px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_prod_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_prod_error.setObjectName("label_decisions_prod_error")
        self.lineEdit_prod = QtWidgets.QLineEdit(self.frame_decisions)
        self.lineEdit_prod.setGeometry(QtCore.QRect(16, 160, 209, 38))
        self.lineEdit_prod.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_prod.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_prod.setObjectName("lineEdit_prod")
        self.label_decisions_prod_dollar = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_prod_dollar.setGeometry(QtCore.QRect(235, 164, 15, 30))
        self.label_decisions_prod_dollar.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_prod_dollar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_decisions_prod_dollar.setObjectName("label_decisions_prod_dollar")
        self.label_decisions_prod = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_prod.setGeometry(QtCore.QRect(16, 132, 209, 24))
        self.label_decisions_prod.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_prod.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_prod.setObjectName("label_decisions_prod")
        self.label_decisions_marketing_error = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_marketing_error.setGeometry(QtCore.QRect(16, 281, 209, 20))
        self.label_decisions_marketing_error.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 12px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_marketing_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_marketing_error.setObjectName("label_decisions_marketing_error")
        self.lineEdit_marketing = QtWidgets.QLineEdit(self.frame_decisions)
        self.lineEdit_marketing.setGeometry(QtCore.QRect(16, 243, 209, 38))
        self.lineEdit_marketing.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_marketing.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_marketing.setObjectName("lineEdit_marketing")
        self.label_decisions_marketing_dollar = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_marketing_dollar.setGeometry(QtCore.QRect(235, 246, 15, 30))
        self.label_decisions_marketing_dollar.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_marketing_dollar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_decisions_marketing_dollar.setObjectName("label_decisions_marketing_dollar")
        self.label_decisions_marketing = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_marketing.setGeometry(QtCore.QRect(16, 215, 209, 24))
        self.label_decisions_marketing.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_marketing.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_marketing.setObjectName("label_decisions_marketing")
        self.label_decisions_CapInv_error = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_CapInv_error.setGeometry(QtCore.QRect(16, 364, 209, 20))
        self.label_decisions_CapInv_error.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 12px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_CapInv_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_CapInv_error.setObjectName("label_decisions_CapInv_error")
        self.lineEdit_CapInv = QtWidgets.QLineEdit(self.frame_decisions)
        self.lineEdit_CapInv.setGeometry(QtCore.QRect(16, 326, 209, 38))
        self.lineEdit_CapInv.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_CapInv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_CapInv.setObjectName("lineEdit_CapInv")
        self.label_decisions_CapInv_dollar = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_CapInv_dollar.setGeometry(QtCore.QRect(235, 329, 15, 30))
        self.label_decisions_CapInv_dollar.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_CapInv_dollar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_decisions_CapInv_dollar.setObjectName("label_decisions_CapInv_dollar")
        self.label_decisions_CapInv = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_CapInv.setGeometry(QtCore.QRect(16, 298, 209, 24))
        self.label_decisions_CapInv.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_CapInv.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_CapInv.setObjectName("label_decisions_CapInv")
        self.label_decisions_RandD_error = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_RandD_error.setGeometry(QtCore.QRect(16, 447, 209, 20))
        self.label_decisions_RandD_error.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 12px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_RandD_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_RandD_error.setObjectName("label_decisions_RandD_error")
        self.lineEdit_RandD = QtWidgets.QLineEdit(self.frame_decisions)
        self.lineEdit_RandD.setGeometry(QtCore.QRect(16, 409, 209, 38))
        self.lineEdit_RandD.setStyleSheet("border-radius: 12px;\n"
"border: 2px solid #1E1E1E;\n"
"padding-top: -1px;\n"
"\n"
"color: #1E1E1E;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"\n"
"padding-top: -1px;")
        self.lineEdit_RandD.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_RandD.setObjectName("lineEdit_RandD")
        self.label_decisions_RandD_dollar = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_RandD_dollar.setGeometry(QtCore.QRect(235, 412, 15, 30))
        self.label_decisions_RandD_dollar.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_RandD_dollar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_decisions_RandD_dollar.setObjectName("label_decisions_RandD_dollar")
        self.label_decisions_RandD = QtWidgets.QLabel(self.frame_decisions)
        self.label_decisions_RandD.setGeometry(QtCore.QRect(16, 381, 209, 24))
        self.label_decisions_RandD.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_decisions_RandD.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_decisions_RandD.setObjectName("label_decisions_RandD")
        self.frame_calculate = QtWidgets.QFrame(Dialog_Enter_Decisions_for_company)
        self.frame_calculate.setGeometry(QtCore.QRect(296, 70, 338, 405))
        self.frame_calculate.setStyleSheet("border-radius: 20px;\n"
"background: #DCDCDC;")
        self.frame_calculate.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_calculate.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_calculate.setObjectName("frame_calculate")
        self.label_calculate = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate.setGeometry(QtCore.QRect(0, 0, 338, 40))
        self.label_calculate.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_calculate.setObjectName("label_calculate")
        self.circle_1 = QtWidgets.QFrame(self.frame_calculate)
        self.circle_1.setGeometry(QtCore.QRect(155, 90, 12, 12))
        self.circle_1.setStyleSheet("background-color: rgb(20, 184, 166);\n"
"border-radius: 6px;\n"
"\n"
"")
        self.circle_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.circle_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circle_1.setObjectName("circle_1")
        self.circle_2 = QtWidgets.QFrame(self.frame_calculate)
        self.circle_2.setGeometry(QtCore.QRect(155, 135, 12, 12))
        self.circle_2.setStyleSheet("background-color: #3B82F6;\n"
"border-radius: 6px;\n"
"\n"
"")
        self.circle_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.circle_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circle_2.setObjectName("circle_2")
        self.circle_3 = QtWidgets.QFrame(self.frame_calculate)
        self.circle_3.setGeometry(QtCore.QRect(155, 203, 12, 12))
        self.circle_3.setStyleSheet("background-color: #F2B60C;\n"
"border-radius: 6px;\n"
"\n"
"")
        self.circle_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.circle_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circle_3.setObjectName("circle_3")
        self.circle_4 = QtWidgets.QFrame(self.frame_calculate)
        self.circle_4.setGeometry(QtCore.QRect(155, 248, 12, 12))
        self.circle_4.setStyleSheet("background-color: #DB6300;\n"
"border-radius: 6px;\n"
"\n"
"")
        self.circle_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.circle_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circle_4.setObjectName("circle_4")
        self.circle_5 = QtWidgets.QFrame(self.frame_calculate)
        self.circle_5.setGeometry(QtCore.QRect(155, 295, 12, 12))
        self.circle_5.setStyleSheet("background-color: #F2220C;\n"
"border-radius: 6px;\n"
"\n"
"")
        self.circle_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.circle_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circle_5.setObjectName("circle_5")
        self.circle_6 = QtWidgets.QFrame(self.frame_calculate)
        self.circle_6.setGeometry(QtCore.QRect(155, 340, 12, 12))
        self.circle_6.setStyleSheet("background-color:#E80CD2;\n"
"border-radius: 6px;\n"
"\n"
"")
        self.circle_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.circle_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circle_6.setObjectName("circle_6")
        self.label_circle_diagram_funds_available = QtWidgets.QLabel(self.frame_calculate)
        self.label_circle_diagram_funds_available.setGeometry(QtCore.QRect(13, 55, 132, 132))
        self.label_circle_diagram_funds_available.setText("")
        self.label_circle_diagram_funds_available.setPixmap(QtGui.QPixmap("UI\\../../../../../Downloads/Chart Area.png"))
        self.label_circle_diagram_funds_available.setScaledContents(True)
        self.label_circle_diagram_funds_available.setObjectName("label_circle_diagram_funds_available")
        self.label_circle_diagram_funds_sepent = QtWidgets.QLabel(self.frame_calculate)
        self.label_circle_diagram_funds_sepent.setGeometry(QtCore.QRect(13, 213, 134, 132))
        self.label_circle_diagram_funds_sepent.setText("")
        self.label_circle_diagram_funds_sepent.setPixmap(QtGui.QPixmap("UI\\../../../../../Downloads/Chart Area.png"))
        self.label_circle_diagram_funds_sepent.setScaledContents(True)
        self.label_circle_diagram_funds_sepent.setObjectName("label_circle_diagram_funds_sepent")
        self.label_calculate_diagram_fundsAvailable_AvilableCash = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsAvailable_AvilableCash.setGeometry(QtCore.QRect(175, 70, 81, 41))
        self.label_calculate_diagram_fundsAvailable_AvilableCash.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsAvailable_AvilableCash.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsAvailable_AvilableCash.setObjectName("label_calculate_diagram_fundsAvailable_AvilableCash")
        self.label_calculate_diagram_fundsAvailable_CreditLine = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsAvailable_CreditLine.setGeometry(QtCore.QRect(175, 120, 51, 41))
        self.label_calculate_diagram_fundsAvailable_CreditLine.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsAvailable_CreditLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsAvailable_CreditLine.setObjectName("label_calculate_diagram_fundsAvailable_CreditLine")
        self.label_calculate_diagram_fundsAvailable_CreditLine_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsAvailable_CreditLine_value.setGeometry(QtCore.QRect(230, 120, 101, 41))
        self.label_calculate_diagram_fundsAvailable_CreditLine_value.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsAvailable_CreditLine_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsAvailable_CreditLine_value.setObjectName("label_calculate_diagram_fundsAvailable_CreditLine_value")
        self.label_calculate_diagram_fundsAvailable_AvilableCash_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsAvailable_AvilableCash_value.setGeometry(QtCore.QRect(240, 70, 91, 41))
        self.label_calculate_diagram_fundsAvailable_AvilableCash_value.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsAvailable_AvilableCash_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsAvailable_AvilableCash_value.setObjectName("label_calculate_diagram_fundsAvailable_AvilableCash_value")
        self.label_calculate_diagram_fundsAvailable_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsAvailable_value.setGeometry(QtCore.QRect(19, 119, 121, 21))
        self.label_calculate_diagram_fundsAvailable_value.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsAvailable_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_calculate_diagram_fundsAvailable_value.setObjectName("label_calculate_diagram_fundsAvailable_value")
        self.label_calculate_diagram_fundsAvailable = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsAvailable.setGeometry(QtCore.QRect(24, 83, 111, 34))
        self.label_calculate_diagram_fundsAvailable.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat Bold;\n"
"font-size: 14px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsAvailable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_calculate_diagram_fundsAvailable.setObjectName("label_calculate_diagram_fundsAvailable")
        self.label_calculate_diagram_fundsSpent = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent.setGeometry(QtCore.QRect(25, 240, 111, 34))
        self.label_calculate_diagram_fundsSpent.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat Bold;\n"
"font-size: 14px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsSpent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_calculate_diagram_fundsSpent.setObjectName("label_calculate_diagram_fundsSpent")
        self.label_calculate_diagram_fundsSpent_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_value.setGeometry(QtCore.QRect(20, 276, 121, 21))
        self.label_calculate_diagram_fundsSpent_value.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsSpent_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_calculate_diagram_fundsSpent_value.setObjectName("label_calculate_diagram_fundsSpent_value")
        self.label_calculate_diagram_fundsSpent_ProdCost_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_ProdCost_value.setGeometry(QtCore.QRect(240, 185, 91, 41))
        self.label_calculate_diagram_fundsSpent_ProdCost_value.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsSpent_ProdCost_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_ProdCost_value.setObjectName("label_calculate_diagram_fundsSpent_ProdCost_value")
        self.label_calculate_diagram_fundsSpent_MarkCost_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_MarkCost_value.setGeometry(QtCore.QRect(230, 233, 101, 41))
        self.label_calculate_diagram_fundsSpent_MarkCost_value.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsSpent_MarkCost_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_MarkCost_value.setObjectName("label_calculate_diagram_fundsSpent_MarkCost_value")
        self.label_calculate_diagram_fundsSpent_MarkCost = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_MarkCost.setGeometry(QtCore.QRect(175, 233, 91, 41))
        self.label_calculate_diagram_fundsSpent_MarkCost.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsSpent_MarkCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_MarkCost.setObjectName("label_calculate_diagram_fundsSpent_MarkCost")
        self.label_calculate_diagram_fundsSpent_ProdCost = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_ProdCost.setGeometry(QtCore.QRect(175, 185, 81, 41))
        self.label_calculate_diagram_fundsSpent_ProdCost.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsSpent_ProdCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_ProdCost.setObjectName("label_calculate_diagram_fundsSpent_ProdCost")
        self.label_calculate_diagram_fundsSpent_NetInv_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_NetInv_value.setGeometry(QtCore.QRect(240, 277, 91, 41))
        self.label_calculate_diagram_fundsSpent_NetInv_value.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_calculate_diagram_fundsSpent_NetInv_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_NetInv_value.setObjectName("label_calculate_diagram_fundsSpent_NetInv_value")
        self.label_calculate_diagram_fundsSpent_RandDCost_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_RandDCost_value.setGeometry(QtCore.QRect(230, 325, 101, 41))
        self.label_calculate_diagram_fundsSpent_RandDCost_value.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsSpent_RandDCost_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_RandDCost_value.setObjectName("label_calculate_diagram_fundsSpent_RandDCost_value")
        self.label_calculate_diagram_fundsSpent_RandDCost = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_RandDCost.setGeometry(QtCore.QRect(175, 325, 51, 41))
        self.label_calculate_diagram_fundsSpent_RandDCost.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsSpent_RandDCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_RandDCost.setObjectName("label_calculate_diagram_fundsSpent_RandDCost")
        self.label_calculate_diagram_fundsSpent_NetInv = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_diagram_fundsSpent_NetInv.setGeometry(QtCore.QRect(175, 277, 81, 41))
        self.label_calculate_diagram_fundsSpent_NetInv.setStyleSheet("color: #1E1E1E;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_diagram_fundsSpent_NetInv.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_diagram_fundsSpent_NetInv.setObjectName("label_calculate_diagram_fundsSpent_NetInv")
        self.label_calculate_fundsRemaining_or_creditLimit = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_fundsRemaining_or_creditLimit.setGeometry(QtCore.QRect(15, 375, 221, 20))
        self.label_calculate_fundsRemaining_or_creditLimit.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_fundsRemaining_or_creditLimit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_fundsRemaining_or_creditLimit.setObjectName("label_calculate_fundsRemaining_or_creditLimit")
        self.label_calculate_fundsRemaining_or_creditLimit_value = QtWidgets.QLabel(self.frame_calculate)
        self.label_calculate_fundsRemaining_or_creditLimit_value.setGeometry(QtCore.QRect(239, 375, 91, 20))
        self.label_calculate_fundsRemaining_or_creditLimit_value.setStyleSheet("color: #EF0009;\n"
"text-align: center;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;")
        self.label_calculate_fundsRemaining_or_creditLimit_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_calculate_fundsRemaining_or_creditLimit_value.setObjectName("label_calculate_fundsRemaining_or_creditLimit_value")
        self.line = QtWidgets.QFrame(self.frame_calculate)
        self.line.setGeometry(QtCore.QRect(180, 175, 150, 1))
        self.line.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.pushButton_create = QtWidgets.QPushButton(Dialog_Enter_Decisions_for_company)
        self.pushButton_create.setGeometry(QtCore.QRect(296, 491, 165, 40))
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
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_Enter_Decisions_for_company)
        self.pushButton_cancel.setGeometry(QtCore.QRect(469, 491, 165, 40))
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

        self.retranslateUi(Dialog_Enter_Decisions_for_company)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Enter_Decisions_for_company)

    def retranslateUi(self, Dialog_Enter_Decisions_for_company):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Enter_Decisions_for_company.setWindowTitle(_translate("Dialog_Enter_Decisions_for_company", "Enter Decisions for COMPANY N"))
        self.label_Enter_Decisions_for_company.setText(_translate("Dialog_Enter_Decisions_for_company", "Ввод решений для MNOGroup"))
        self.label_decisions.setText(_translate("Dialog_Enter_Decisions_for_company", "Решения"))
        self.lineEdit_price.setPlaceholderText(_translate("Dialog_Enter_Decisions_for_company", "Обязательное поле"))
        self.label_decisions_price.setText(_translate("Dialog_Enter_Decisions_for_company", "Цена за ед. товара "))
        self.label_decisions_price_dollar.setText(_translate("Dialog_Enter_Decisions_for_company", "$"))
        self.label_decisions_price_error.setText(_translate("Dialog_Enter_Decisions_for_company", "Макс. кол-во = 525"))
        self.label_decisions_prod_error.setText(_translate("Dialog_Enter_Decisions_for_company", "Макс. кол-во = 525 шт."))
        self.lineEdit_prod.setPlaceholderText(_translate("Dialog_Enter_Decisions_for_company", "Обязательное поле"))
        self.label_decisions_prod_dollar.setText(_translate("Dialog_Enter_Decisions_for_company", "$"))
        self.label_decisions_prod.setText(_translate("Dialog_Enter_Decisions_for_company", "Производство"))
        self.label_decisions_marketing_error.setText(_translate("Dialog_Enter_Decisions_for_company", "Макс. кол-во = 525"))
        self.lineEdit_marketing.setPlaceholderText(_translate("Dialog_Enter_Decisions_for_company", "Обязательное поле"))
        self.label_decisions_marketing_dollar.setText(_translate("Dialog_Enter_Decisions_for_company", "$"))
        self.label_decisions_marketing.setText(_translate("Dialog_Enter_Decisions_for_company", "Маркетинг"))
        self.label_decisions_CapInv_error.setText(_translate("Dialog_Enter_Decisions_for_company", "Амортизация = 1050 $"))
        self.lineEdit_CapInv.setPlaceholderText(_translate("Dialog_Enter_Decisions_for_company", "Обязательное поле"))
        self.label_decisions_CapInv_dollar.setText(_translate("Dialog_Enter_Decisions_for_company", "$"))
        self.label_decisions_CapInv.setText(_translate("Dialog_Enter_Decisions_for_company", "Капитальные инв."))
        self.label_decisions_RandD_error.setText(_translate("Dialog_Enter_Decisions_for_company", "Макс. кол-во = 525"))
        self.lineEdit_RandD.setPlaceholderText(_translate("Dialog_Enter_Decisions_for_company", "Обязательное поле"))
        self.label_decisions_RandD_dollar.setText(_translate("Dialog_Enter_Decisions_for_company", "$"))
        self.label_decisions_RandD.setText(_translate("Dialog_Enter_Decisions_for_company", "Научные разработки"))
        self.label_calculate.setText(_translate("Dialog_Enter_Decisions_for_company", "Расчет"))
        self.label_calculate_diagram_fundsAvailable_AvilableCash.setText(_translate("Dialog_Enter_Decisions_for_company", "<html><head/><body><p>Available<br>Cash</p></body></html>"))
        self.label_calculate_diagram_fundsAvailable_CreditLine.setText(_translate("Dialog_Enter_Decisions_for_company", "<html><head/><body><p>Credit<br>Line</p></body></html>"))
        self.label_calculate_diagram_fundsAvailable_CreditLine_value.setText(_translate("Dialog_Enter_Decisions_for_company", "9999999$"))
        self.label_calculate_diagram_fundsAvailable_AvilableCash_value.setText(_translate("Dialog_Enter_Decisions_for_company", "999999$"))
        self.label_calculate_diagram_fundsAvailable_value.setText(_translate("Dialog_Enter_Decisions_for_company", "0$"))
        self.label_calculate_diagram_fundsAvailable.setText(_translate("Dialog_Enter_Decisions_for_company", "Funds<br>Available"))
        self.label_calculate_diagram_fundsSpent.setText(_translate("Dialog_Enter_Decisions_for_company", "Funds<br>Spent"))
        self.label_calculate_diagram_fundsSpent_value.setText(_translate("Dialog_Enter_Decisions_for_company", "9999999$"))
        self.label_calculate_diagram_fundsSpent_ProdCost_value.setText(_translate("Dialog_Enter_Decisions_for_company", "999999$"))
        self.label_calculate_diagram_fundsSpent_MarkCost_value.setText(_translate("Dialog_Enter_Decisions_for_company", "99999$"))
        self.label_calculate_diagram_fundsSpent_MarkCost.setText(_translate("Dialog_Enter_Decisions_for_company", "<html><head/><body><p>Marketing<br>Cost</p></body></html>"))
        self.label_calculate_diagram_fundsSpent_ProdCost.setText(_translate("Dialog_Enter_Decisions_for_company", "<html><head/><body><p>Prod.<br>Cost</p></body></html>"))
        self.label_calculate_diagram_fundsSpent_NetInv_value.setText(_translate("Dialog_Enter_Decisions_for_company", "999999$"))
        self.label_calculate_diagram_fundsSpent_RandDCost_value.setText(_translate("Dialog_Enter_Decisions_for_company", "9999999$"))
        self.label_calculate_diagram_fundsSpent_RandDCost.setText(_translate("Dialog_Enter_Decisions_for_company", "<html><head/><body><p>R&D<br>Cost</p></body></html>"))
        self.label_calculate_diagram_fundsSpent_NetInv.setText(_translate("Dialog_Enter_Decisions_for_company", "<html><head/><body><p>Net<br>Invest.</p></body></html>"))
        self.label_calculate_fundsRemaining_or_creditLimit.setText(_translate("Dialog_Enter_Decisions_for_company", "Exceeded the credit limit"))
        self.label_calculate_fundsRemaining_or_creditLimit_value.setText(_translate("Dialog_Enter_Decisions_for_company", "9999999$"))
        self.pushButton_create.setText(_translate("Dialog_Enter_Decisions_for_company", "Сохранить"))
        self.pushButton_cancel.setText(_translate("Dialog_Enter_Decisions_for_company", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Enter_Decisions_for_company = QtWidgets.QDialog()
    ui = Ui_Dialog_Enter_Decisions_for_company()
    ui.setupUi(Dialog_Enter_Decisions_for_company)
    Dialog_Enter_Decisions_for_company.show()
    sys.exit(app.exec())
