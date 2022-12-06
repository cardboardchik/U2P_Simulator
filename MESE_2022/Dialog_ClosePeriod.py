
##by karton4ik

from PyQt6 import QtCore, QtGui, QtWidgets
import json
from ast import literal_eval

import engine



class Ui_Dialog_ClosePeriod(object):
    def setupUi(self, Dialog_ClosePeriod):
        
        self.file_setup = literal_eval(open("Dialog_Setup.txt", "r").readline())
        self.file_result = open("result.txt", "r").readline()
        
        Dialog_ClosePeriod.setObjectName("Dialog_ClosePeriod")
        Dialog_ClosePeriod.resize(350, 130)
        Dialog_ClosePeriod.setMinimumSize(QtCore.QSize(350, 130))
        Dialog_ClosePeriod.setMaximumSize(QtCore.QSize(350, 130))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_ClosePeriod.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_ClosePeriod)
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
        self.label = QtWidgets.QLabel(Dialog_ClosePeriod)
        self.label.setGeometry(QtCore.QRect(27, 40, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_ClosePeriod)
        self.buttonBox.accepted.connect(self.yes_was_clicked)
        self.buttonBox.accepted.connect(Dialog_ClosePeriod.accept)
        
        self.buttonBox.rejected.connect(Dialog_ClosePeriod.reject)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog_ClosePeriod)

    def retranslateUi(self, Dialog_ClosePeriod):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ClosePeriod.setWindowTitle(_translate("Dialog_ClosePeriod", "Close the Period?"))
        self.label.setText(_translate("Dialog_ClosePeriod", "Do you really want to close the period?"))

    def yes_was_clicked(self):
        
        
        file_pre_result = open("result.txt", "w")
        
        if self.file_result == "":
            result_1 = engine.exec(engine.init(len(self.file_setup)))
            file_pre_result.write(str(result_1))
        
            file_pre_result.close()
        else:
            file_settings = literal_eval(open("settings.txt", "r").readline())
            result_literal_eval = literal_eval(self.file_result)
            #game settings 
            result_literal_eval["settings"]["price_max"] = file_settings["MaxPrice"]
            result_literal_eval["settings"]["mk_limit"] = file_settings["MaxMarketing"] * result_literal_eval["player_count"]
            result_literal_eval["settings"]["ci_limit"] = file_settings["MaxCapInv"] * result_literal_eval["player_count"]
            result_literal_eval["settings"]["rd_limit"] = file_settings["MaxRandD"] * result_literal_eval["player_count"]
            result_literal_eval["settings"]["loan_limit"] = file_settings["LoanLimit"] * result_literal_eval["player_count"]
            result_literal_eval["settings"]["interest_rate_loan"] = file_settings["InterestRate"] * 0.01
            result_literal_eval["settings"]["tax_rate"] = file_settings["TaxRate"] * 0.01
            result_literal_eval["settings"]["demand"] += file_settings["DemandChange"] * 0.01
            result_literal_eval["settings"]["demand_price"] += file_settings["PriceImpact"] * 0.01
            result_literal_eval["settings"]["demand_mk"] += file_settings["MarketingImpact"] * 0.01
            result_literal_eval["settings"]["demand_rd"] += file_settings["RandDImpact"] * 0.01
            result_literal_eval["settings"]["share_price"] = file_settings["Price"] * 0.01
            result_literal_eval["settings"]["share_mk"] = file_settings["Marketing"] * 0.01
            result_literal_eval["settings"]["share_rd"] = file_settings["RandD"] * 0.01
            
            
            file_setup_len = len(self.file_setup)
            #game decisions
            result_literal_eval["decisions"]["price"] = [30 for i in range(file_setup_len)]
            result_literal_eval["decisions"]["prod_rate"] = [0.8 for i in range(file_setup_len)]
            result_literal_eval["decisions"]["mk"] = [1050 for i in range(file_setup_len)]
            result_literal_eval["decisions"]["ci"] = [1050 for i in range(file_setup_len)]
            result_literal_eval["decisions"]["rd"] = [420 for i in range(file_setup_len)]
            
            
            #correct order
            result = [None for i in range(file_setup_len)]
            
            
            #sort decisions
            with open("data.json",'r') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                #from data.json take dictionaries and sort it.
                for array in file_data["input_data"]:
                    for key, company in self.file_setup.items():
                        if array["company"] == company:
                            result[int(key[-1])-1] = array 
                
            #write decisions
            if result[0] != None:
                
                i = 0
                for decisions in result:
                    result_literal_eval["decisions"]["price"][i] = int(decisions["UnitPrice"])
                    result_literal_eval["decisions"]["prod_rate"][i] = float(decisions["Production"]) / result_literal_eval["data"]["size"][i]
                    result_literal_eval["decisions"]["mk"][i] = int(decisions["Marketing"])
                    result_literal_eval["decisions"]["ci"][i] = int(decisions["CI"])
                    result_literal_eval["decisions"]["rd"][i] = int(decisions["RandD"])
        
                    i += 1
                               
            print (result)
            result_2 = engine.exec(result_literal_eval)
            file_pre_result.write(str(result_2))
            
            file_pre_result.close()
        
        open("data.json", "w").write('''
{
    "input_data": [
        
    ]
}
                                     ''')
        open("ClosePeriod_log.txt", "w").close()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ClosePeriod = QtWidgets.QDialog()
    ui = Ui_Dialog_ClosePeriod()
    ui.setupUi(Dialog_ClosePeriod)
    Dialog_ClosePeriod.show()
    sys.exit(app.exec())
