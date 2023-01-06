
##by karton4ik

from PyQt6 import QtCore, QtGui, QtWidgets
import json
from ast import literal_eval
from fpdf import FPDF
import os
from PyPDF2 import PdfMerger
import shutil


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
        self.buttonBox.rejected.connect(self.no_was_clicked)
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
              
            i = 0
            for decisions in result:
                if decisions != None:
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
        

        
        def create_pdf(company_name, company_num, result, company_names):
            pdf = FPDF()
            pdf.add_page()

            # Company Report for NNN Period N
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 13)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=210, h=30, align="C", txt=f"Company Report for {company_name} Period {result['now_tick'] - 1}", border=0)


            # Lines for Income Statement
            pdf.rect(5, 17.5, 100, 82.5)

            # Income Statement
            pdf.set_xy(35, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=40, align="L", txt="Income Statement", border=0)


            # Sales
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=55, align="L", txt="Sales", border=0)

            # Sales_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=55, align="R", txt=f"{round(result['data']['sales'][company_num])}  $", border=0)

            # Sales_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=55, align="R", txt="100%", border=0)


            # COGS
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=65, align="L", txt="COGS (Cost of Goods)", border=0)

            # COGS_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=65, align="R", txt=f"-{round(result['data']['goods_cost_predicted'][company_num])}  $", border=0)

            # COGS_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=65, align="R", txt="-100%", border=0)


            # line
            pdf.set_xy(58, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=71, align="L", txt="_________________", border=0)

            gross_margin = round(result["data"]["sales"][company_num] - result['data']['goods_cost_predicted'][company_num])
            # Gross Margin
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=85, align="L", txt="Gross Margin", border=0)

            # Gross Margin_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=85, align="R", txt=f"{gross_margin}  $", border=0)

            # Gross Margin_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=85, align="R", txt="-100%", border=0)


            # Marketing
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=95, align="L", txt="Marketing", border=0)


            # Marketing_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=95, align="R", txt=f"-{round(result['decisions']['mk'][company_num])}  $", border=0)

            # Marketing_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=95, align="R", txt="-100%", border=0)


            # Depreciation
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=105, align="L", txt="Depreciation", border=0)


            # Depreciation_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=105, align="R", txt=f"-{round(result['data']['depreciation'][company_num])}  $", border=0)


            # Depreciation_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=105, align="R", txt="-100%", border=0)


            # R & D
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=115, align="L", txt="R & D", border=0)

            # R & D_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=115, align="R", txt=f"-{round(result['decisions']['rd'][company_num])}  $", border=0)


            # R & D_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=115, align="R", txt="-100%", border=0)


            # Layoff Charge
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=125, align="L", txt="Layoff Charge", border=0)

            # Layoff Charge_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=125, align="R", txt="###  $", border=0)

            # Layoff Charge_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=125, align="R", txt="-100%", border=0)


            # Inventory Charge
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=135, align="L", txt="Inventory Charge", border=0)

            # Inventory Charge_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=135, align="R", txt=f"-{round(result['data']['inventory_charge'][company_num])}  $", border=0)

            # Inventory Charge_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=135, align="R", txt="-100%", border=0)


            # Interest
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=145, align="L", txt="Interest", border=0)

            # Interest_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=145, align="R", txt=f"{round(result['data']['interest'][company_num])}  $", border=0)

            # Interest_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=145, align="R", txt="-100%", border=0)


            # line
            pdf.set_xy(58, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=151, align="L", txt="_________________", border=0)


            # Profit before Tax
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=165, align="L", txt="Profit before Tax", border=0)

            # Profit before Tax_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=165, align="R", txt=f"{round(result['data']['profit_before_tax'][company_num])}  $", border=0)

            # Profit before Tax_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=165, align="R", txt="-100%", border=0)


            # Tax
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=175, align="L", txt="Tax", border=0)

            # Tax_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=175, align="R", txt=f"-{round(result['data']['tax_charge'][company_num])}  $", border=0)

            # Tax_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=175, align="R", txt="-100%", border=0)


            # line
            pdf.set_xy(58, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=181, align="L", txt="_________________", border=0)


            # Net Profit
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=195, align="L", txt="Net Profit", border=0)

            # Net Profit_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=195, align="R", txt=f"{round(result['data']['profit'][company_num])}  $", border=0)

            # Net Profit_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=195, align="R", txt="-100%", border=0)


            # Lines for Operations Reports
            pdf.rect(105, 17.5, 100, 147.5)

            # Operations Reports
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=40, align="C", txt="Operations Reports", border=0)


            # Decisions
            pdf.rect(110, 25, 90, 30)

            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=55, align="C", txt="Decisions", border=0)

            # Price
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=65, align="L", txt="Price", border=0)

            # Price_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=65, align="R", txt=str(result['decisions']['price'][company_num]), border=0)

            # Price of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=65, align="L", txt="$", border=0)


            # Production
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=75, align="L", txt="Production", border=0)

            # Production_units
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=75, align="R", txt=str(round(result['data']['prod'][company_num])), border=0)

            # Production of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=75, align="L", txt="units", border=0)


            # Marketing
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=85, align="L", txt="Marketing", border=0)

            # Marketing_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=85, align="R", txt=str(round(result['decisions']['mk'][company_num])), border=0)

            # Marketing of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=85, align="L", txt="$", border=0)


            # Investment
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=95, align="L", txt="Investment", border=0)

            # Investment_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=95, align="R", txt=str(round(result['decisions']['ci'][company_num])), border=0)

            # Investment of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=95, align="L", txt="$", border=0)


            # R & D
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=105, align="L", txt="R & D", border=0)

            # R & D_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=105, align="R", txt=str(round(result['decisions']['rd'][company_num])), border=0)

            # Investment of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=105, align="L", txt="$", border=0)


            # Production Report
            pdf.rect(110, 57.5, 90, 37.5)

            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=120, align="C", txt="Production Report", border=0)


            # Production
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=135, align="L", txt="Production", border=0)

            # Production_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=135, align="R", txt=str(round(result['data']['prod'][company_num])), border=0)

            # Production_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=135, align="L", txt="units", border=0)


            # Factory Capacity
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=145, align="L", txt="Factory Capacity", border=0)

            # Factory Capacity_INT
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=145, align="R", txt=str(round(result['data']['size'][company_num])), border=0)

            # Factory Capacity_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=145, align="L", txt="units", border=0)


            # Capacity Utilization
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=155, align="L", txt="Capacity Utilization", border=0)

            # Capacity Utilization_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=155, align="R", txt=str(round(result['decisions']['prod_rate'][company_num] * 100)), border=0)

            # Capacity Utilization_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=155, align="L", txt="%", border=0)


            # Production Cost/Unit
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=165, align="L", txt="Production Cost/Unit", border=0)

            # Production Cost/Unit_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=165, align="R", txt=str(round(result['data']['prod_cost_unit'][company_num], 2)), border=0)

            # Production Cost/Unit_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=165, align="L", txt="$", border=0)


            # Inventory
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=175, align="L", txt="Inventory", border=0)

            # Inventory_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=175, align="R", txt=str(round(result['data']['inventory'][company_num])), border=0)

            # Inventory_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=175, align="L", txt="units", border=0)


            # Employees
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=185, align="L", txt="Employees", border=0)

            # Employees_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=185, align="R", txt="###", border=0)

            # Employees_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=185, align="L", txt="workers", border=0)


            # Marketing Report
            pdf.rect(110, 97.5, 90, 37.5)

            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=200, align="C", txt="Marketing Report", border=0)


            # Orders Received
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=215, align="L", txt="Orders Received", border=0)

            # Orders Received_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=215, align="R", txt=str(round(result['data']['orders'][company_num])), border=0)

            # Orders Received_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=215, align="L", txt="units", border=0)


            # Sales Made
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=225, align="L", txt="Sales Made", border=0)

            # Sales Made_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=225, align="R", txt=str(round(result['data']['sold'][company_num])), border=0)

            # Sales Made_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=225, align="L", txt="units", border=0)


            # Unfilled Orders
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=235, align="L", txt="Unfilled Orders", border=0)

            # Unfilled Orders_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=235, align="R", txt=str(round(result['data']['unfilled'][company_num])), border=0)

            # Unfilled Orders_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=235, align="L", txt="units", border=0)


            # Price/Unit Sold
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=245, align="L", txt="Price/Unit Sold", border=0)

            # Price/Unit Sold_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=245, align="R", txt=str(round(result['decisions']['price'][company_num], 2)), border=0)

            # Price/Unit Sold_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=245, align="L", txt="$", border=0)


            # Total Cost/Unit Sold
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=255, align="L", txt="Total Cost/Unit Sold", border=0)

            Margin_Unit_Sold = round(result["data"]["margin_unit_sold"][company_num], 2)
            Total_Cost_Unit_Sold = round(result["data"]["total_cost_unit_sold"][company_num], 2)
            
            # Total Cost/Unit Sold_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=255, align="R", txt=str(Total_Cost_Unit_Sold), border=0)

            # Total Cost/Unit Sold_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=255, align="L", txt="$", border=0)


            # Margin/Unit Sold
            pdf.set_xy(110, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=265, align="L", txt="Margin/Unit Sold", border=0)

            # Margin/Unit Sold_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=185, h=265, align="R", txt=str(Margin_Unit_Sold), border=0)

            # Margin/Unit Sold_unit of measurement
            pdf.set_xy(184, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=265, align="L", txt="$", border=0)


            # Investment Report
            pdf.rect(110, 137.5, 90, 27.5)

            pdf.set_xy(110, 140)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="C", txt="Investment Report", border=0)


            # Factory Size
            pdf.set_xy(110, 147.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Factory Size", border=0)

            # Factory Size_int_$
            pdf.set_xy(0, 147.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=170, h=0, align="R", txt=f"{round(result['data']['capital'][company_num])} $", border=0)

            # Factory Size_int_units
            pdf.set_xy(0, 147.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=190, h=0, align="R", txt=str(round(result['data']['size'][company_num])), border=0)

            # Factory Size_unit of measurement
            pdf.set_xy(189, 147.5)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="units", border=0)


            # Net Investment
            pdf.set_xy(110, 152.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Net Investment", border=0)

            Net_Investment = round(result['decisions']['ci'][company_num] - result['data']['depreciation'][company_num])
            
            # Net Investment_int_$
            pdf.set_xy(0, 152.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=170, h=0, align="R", txt=f"{Net_Investment} $", border=0)

            Net_Investment_int_units = round(Net_Investment / result["settings"]["unit_fee"])
            
            # Net Investment_int_units
            pdf.set_xy(0, 152.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=190, h=0, align="R", txt=str(Net_Investment_int_units), border=0)

            # Net Investment_unit of measurement
            pdf.set_xy(189, 152.5)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="units", border=0)


            # line
            pdf.set_xy(153, 155.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="________________", border=0)


            # Size Next Period
            pdf.set_xy(110, 162.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Size Next Period", border=0)

            Size_Next_Period = round(result["data"]["capital"][company_num] + Net_Investment)
            
            # Size Next Period_int_$
            pdf.set_xy(0, 162.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=170, h=0, align="R", txt=f"{Size_Next_Period} $", border=0)

            # Size Next Period_int_units
            pdf.set_xy(0, 162.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=190, h=0, align="R", txt=str(round(Size_Next_Period / result['settings']['unit_fee'])), border=0)

            # Size Next Period_unit of measurement
            pdf.set_xy(189, 162.5)
            pdf.set_font("Arial", "I", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="units", border=0)


            # Lines for Balance Sheet
            pdf.rect(5, 100, 100, 65)

            # Balance Sheet
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=107.5, h=205, align="C", txt="Balance Sheet", border=0)


            # Cash
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=220, align="L", txt="Cash", border=0)

            # Cash_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=220, align="R", txt=f"{round(result['data']['cash'][company_num])}  $", border=0)

            # Cash_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=220, align="R", txt="-100%", border=0)


            # Inventory
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=230, align="L", txt="Inventory", border=0)

            # Inventory_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=230, align="R", txt=f"{round(result['data']['goods_cost_inventory'][company_num])}  $", border=0)

            # Inventory_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=230, align="R", txt="-100%", border=0)


            # Capital Investment
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=240, align="L", txt="Capital Investment", border=0)

            # Capital Investment_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            # line 996
            pdf.cell(w=80, h=240, align="R", txt=f"{Size_Next_Period}  $", border=0)

            # Capital Investment_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=240, align="R", txt="-100%", border=0)


            # line
            pdf.set_xy(58, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=246, align="L", txt="_________________", border=0)


            # Total Assets
            pdf.set_xy(5, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=260, align="L", txt="Total Assets", border=0)

            Total_Assets = round(result['data']['cash'][company_num] + result['data']['goods_cost_inventory'][company_num] + Size_Next_Period)

            # Total Assets_int
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=260, align="R", txt=f"{Total_Assets}  $", border=0)

            # Total Assets_%
            pdf.set_xy(0, 0)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=260, align="R", txt="-100%", border=0)
            

            # Loans
            pdf.set_xy(5, 142.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Loans", border=0)
            
            Loans =  round(result['data']['loan'][company_num])
            
            # Loans_int
            pdf.set_xy(0, 142.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Loans}  $", border=0)

            # Loans%
            pdf.set_xy(0, 142.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Retained Earnings
            pdf.set_xy(5, 147.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Retained Earnings", border=0)

            Retained_Earnings = round(result['data']['retern'][company_num])

            # Retained Earnings_int
            pdf.set_xy(0, 147.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Retained_Earnings}  $", border=0)

            # Retained Earnings_%
            pdf.set_xy(0, 147.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Capital
            pdf.set_xy(5, 152.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Capital", border=0)

            Capital = round(result['data']['capital'][company_num])

            # Capital_int
            pdf.set_xy(0, 152.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Capital}  $", border=0)

            # Capital_%
            pdf.set_xy(0, 152.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # line
            pdf.set_xy(58, 156)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="_________________", border=0)


            # Liabilities+Equity
            pdf.set_xy(5, 162.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Liabilities+Equity", border=0)

            Liabilities_plus_Equity = round(Loans + Retained_Earnings + Capital)

            # Liabilities+Equity_int
            pdf.set_xy(0, 162.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Liabilities_plus_Equity}  $", border=0)

            # Liabilities+Equity_%
            pdf.set_xy(0, 162.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Industry Report for Period NNN

            # lines for Units
            pdf.rect(5, 175, 100, 32.5)
            # lines for Dollars
            pdf.rect(105, 175, 100, 32.5)
            # lines for Productivity
            pdf.rect(5, 207.5, 100, 32.5)
            # lines for Period Settings
            pdf.rect(105, 207.5, 100, 32.5)

            pdf.set_xy(0, 170)
            pdf.set_font("Arial", "", 13)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=210, h=0, align="C", txt=f"Industry Report for Period {result['now_tick'] - 1}", border=0)


            # Units
            pdf.set_xy(0, 177.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=107.5, h=0, align="C", txt="Units", border=0)


            # Total Orders
            pdf.set_xy(5, 185)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Total Orders", border=0)

            Total_Orders = round(sum(result['data']['orders']))

            # Total Orders_int
            pdf.set_xy(0, 185)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Total_Orders}   ", border=0)

            # Total Orders_%
            pdf.set_xy(0, 185)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Total Produced
            pdf.set_xy(5, 190)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Total Produced", border=0)
            
            Total_Produced = round(sum(result['data']['goods_predicted']))

            # Total Produced_int
            pdf.set_xy(0, 190)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Total_Produced}   ", border=0)

            # Total Produced_%
            pdf.set_xy(0, 190)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Total Sold
            pdf.set_xy(5, 195)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Total Sold", border=0)

            Total_Sold = round(sum(result['data']['sold']))

            # Total Sold_int
            pdf.set_xy(0, 195)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Total_Sold}   ", border=0)

            # Total Sold_%
            pdf.set_xy(0, 195)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Total Capacity
            pdf.set_xy(5, 200)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Total Capacity", border=0)
            
            Total_Capacity = round(sum(result['data']['size']))

            # Total Capacity_int
            pdf.set_xy(0, 200)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Total_Capacity}   ", border=0)

            # Total Capacity_%
            pdf.set_xy(0, 200)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Inventory
            pdf.set_xy(5, 205)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Inventory", border=0)

            Inventory = round(sum(result['data']['inventory']))

            # Inventory_int
            pdf.set_xy(0, 205)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt=f"{Inventory}   ", border=0)

            # Inventory_%
            pdf.set_xy(0, 205)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Productivity
            pdf.set_xy(0, 210)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=107.5, h=0, align="C", txt="Productivity", border=0)


            # Employment
            pdf.set_xy(5, 217.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Employment", border=0)

            # Employment_int
            pdf.set_xy(0, 217.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt="###    ", border=0)

            # Employment_%
            pdf.set_xy(0, 217.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Sales/Employee
            pdf.set_xy(5, 222.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Sales/Employee", border=0)

            # Sales/Employee_int
            pdf.set_xy(0, 222.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt="###  $", border=0)

            # Sales/Employee_%
            pdf.set_xy(0, 222.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Units/Employee
            pdf.set_xy(5, 227.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Units/Employee", border=0)

            # Units/Employee_int
            pdf.set_xy(0, 227.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt="###    ", border=0)

            # Units/Employee_%
            pdf.set_xy(0, 227.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Cap. Investment
            pdf.set_xy(5, 232.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Cap. Investment", border=0)

            # Cap. Investment_int
            pdf.set_xy(0, 232.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt="###  $", border=0)

            # Cap. Investment_%
            pdf.set_xy(0, 232.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Capacity Util.
            pdf.set_xy(5, 237.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Capacity Util.", border=0)

            # Capacity Util._int
            pdf.set_xy(0, 237.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=80, h=0, align="R", txt="### %", border=0)

            # Capacity Util._%
            pdf.set_xy(0, 237.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=100, h=0, align="R", txt="-100%", border=0)


            # Dollars
            pdf.set_xy(110, 177.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="C", txt="Dollars", border=0)


            # Industry Sales
            pdf.set_xy(105, 185)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Industry Sales", border=0)


            Industry_Sales = round(sum(result['data']['sales']))

            # Industry Sales_int
            pdf.set_xy(0, 185)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{Industry_Sales}  $", border=0)

            # Industry Sales_%
            pdf.set_xy(0, 185)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Average Price
            pdf.set_xy(105, 190)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Average Price", border=0)

            # Average Price_int
            pdf.set_xy(0, 190)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{round(result['data']['average_price'], 2)}  $", border=0)

            # Average Price_%
            pdf.set_xy(0, 190)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Total Production
            pdf.set_xy(105, 195)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Total Production", border=0)

            Total_Production = round(sum(result['data']['prod_cost']))

            # Total Production_int
            pdf.set_xy(0, 195)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{Total_Production}  $", border=0)

            # Total Production_%
            pdf.set_xy(0, 195)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Avg Pdtn Cost
            pdf.set_xy(105, 200)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Avg Pdtn Cost", border=0)

            Avg_Pdtn_Cost = round(sum(result["data"]["prod_cost_unit"]) / result["player_count"], 2)

            # Avg Pdtn Cost_int
            pdf.set_xy(0, 200)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{Avg_Pdtn_Cost}  $", border=0)

            # Avg Pdtn Cost_%
            pdf.set_xy(0, 200)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Avg Total Cost
            pdf.set_xy(105, 205)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Avg Total Cost", border=0)

            Avg_Total_Cost = round(sum(result["data"]["total_cost_unit_sold"]) / result["player_count"], 2)

            # Avg Total Cost_int
            pdf.set_xy(0, 205)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{Avg_Total_Cost}  $", border=0)

            # Avg Total Cost_%
            pdf.set_xy(0, 205)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Period Settings
            pdf.set_xy(110, 210)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="C", txt="Period Settings", border=0)


            # Prime Rate
            pdf.set_xy(105, 217.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Prime Rate", border=0)

            # Prime Rate_int
            pdf.set_xy(0, 217.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt="10 %", border=0)

            # Prime Rate_%
            pdf.set_xy(0, 217.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Loan Limit
            pdf.set_xy(105, 222.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Loan Limit", border=0)

            loan_limit = round(result["settings"]["loan_limit"] / result["player_count"])

            # Loan Limit_int
            pdf.set_xy(0, 222.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{loan_limit}  $", border=0)

            # Loan Limit_%
            pdf.set_xy(0, 222.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Tax Rate
            pdf.set_xy(105, 227.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Tax Rate", border=0)

            Tax_Rate = round(result["settings"]["tax_rate"] * 100)

            # Tax Rate_int
            pdf.set_xy(0, 227.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{Tax_Rate} %", border=0)

            # Tax Rate_%
            pdf.set_xy(0, 227.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Tax Paid in Period
            pdf.set_xy(105, 232.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Tax Paid in Period", border=0)

            Tax_Paid_in_Period = round(result["data"]["tax_paid_to_period"])

            # Tax Paid in Period_int
            pdf.set_xy(0, 232.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{Tax_Paid_in_Period}  $", border=0)

            # Tax Paid in Period_%
            pdf.set_xy(0, 232.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)


            # Tax Paid to Date
            pdf.set_xy(105, 237.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Tax Paid to Date", border=0)

            tax_paid_to_date = round(result["data"]["tax_paid_to_date"])

            # Tax Paid to Date_int
            pdf.set_xy(0, 237.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=180, h=0, align="R", txt=f"{tax_paid_to_date}  $", border=0)

            # Tax Paid to Date_%
            pdf.set_xy(0, 237.5)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=200, h=0, align="R", txt="-100%", border=0)




            # Sales
            pdf.set_xy(5, 250)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Sales", border=0)


            # Profit
            pdf.set_xy(5, 255)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Profit", border=0)

            # Price
            pdf.set_xy(5, 260)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Price", border=0)

            # Un Shr
            pdf.set_xy(5, 265)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="Un Shr", border=0)

            # MPI
            pdf.set_xy(5, 270)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="MPI", border=0)
            
            
            company_names_len = len(company_names)
            
            
            # Company 1
            pdf.set_xy(0, 245)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=46, h=0, align="R", txt=company_names["Company_1"], border=0)
            
            # 1
            pdf.set_xy(25, 245)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="________", border=0)
            
            # Sales for Company 1
            pdf.set_xy(0, 250)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=46, h=0, align="R", txt=f"{round(result['data']['sales'][0])} $", border=0)
            
            # Profit for Company 1
            pdf.set_xy(0, 255)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=46, h=0, align="R", txt=f"{round(result['data']['profit'][0])} $", border=0)
            
            # Price for Company 1
            pdf.set_xy(0, 260)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=46, h=0, align="R", txt=f"{result['decisions']['price'][0]} $", border=0)
            
            # Un Shr for Company 1
            pdf.set_xy(0, 265)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=46, h=0, align="R", txt=f"{round(result['data']['share'][0], 3) * 100}%", border=0)
            
            # MPI for Company 1
            pdf.set_xy(0, 270)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=46, h=0, align="R", txt=f"{result['data']['mpi'][0]}   ", border=0)
            

            # Company 2
            pdf.set_xy(0, 245)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=68.5, h=0, align="R", txt=company_names["Company_2"], border=0)
            
            # 2
            pdf.set_xy(47.5, 245)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=0, h=0, align="L", txt="________", border=0)
            
            # Sales for Company 2
            pdf.set_xy(0, 250)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=68.5, h=0, align="R", txt=f"{round(result['data']['sales'][1])} $", border=0)
            
            # Profit for Company 2
            pdf.set_xy(0, 255)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=68.5, h=0, align="R", txt=f"{round(result['data']['profit'][1])} $", border=0)
            
            # Price for Company 2
            pdf.set_xy(0, 260)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=68.5, h=0, align="R", txt=f"{result['decisions']['price'][1]} $", border=0)
            
            # Un Shr for Company 2
            pdf.set_xy(0, 265)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=68.5, h=0, align="R", txt=f"{round(result['data']['share'][1], 3) * 100}%", border=0)
            
            # MPI for Company 2
            pdf.set_xy(0, 270)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(w=68.5, h=0, align="R", txt=f"{result['data']['mpi'][1]}   ", border=0)
            
            if company_names_len not in [2]:
                # Company 3
                pdf.set_xy(0, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=91, h=0, align="R", txt=company_names["Company_3"], border=0)
            
                # 3
                pdf.set_xy(70, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=0, h=0, align="L", txt="________", border=0)
            
                # Sales for Company 3
                pdf.set_xy(0, 250)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=91, h=0, align="R", txt=f"{round(result['data']['sales'][2])} $", border=0)
            
                # Profit for Company 3
                pdf.set_xy(0, 255)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=91, h=0, align="R", txt=f"{round(result['data']['profit'][2])} $", border=0)
            
                # Price for Company 3
                pdf.set_xy(0, 260)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=91, h=0, align="R", txt=f"{result['decisions']['price'][2]} $", border=0)
            
                # Un Shr for Company 3
                pdf.set_xy(0, 265)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=91, h=0, align="R", txt=f"{round(result['data']['share'][2], 3) * 100}%", border=0)
            
                # MPI for Company 3
                pdf.set_xy(0, 270)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=91, h=0, align="R", txt=f"{result['data']['mpi'][2]}   ", border=0)
            
            if company_names_len not in [3, 2]:
                # Company 4
                pdf.set_xy(0, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=113.5, h=0, align="R", txt=company_names["Company_4"], border=0)
            
                # 4
                pdf.set_xy(92.5, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=0, h=0, align="L", txt="________", border=0)
            
                # Sales for Company 4
                pdf.set_xy(0, 250)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=113.5, h=0, align="R", txt=f"{round(result['data']['sales'][3])} $", border=0)
            
                # Profit for Company 4
                pdf.set_xy(0, 255)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=113.5, h=0, align="R", txt=f"{round(result['data']['profit'][3])} $", border=0)
            
                # Price for Company 4
                pdf.set_xy(0, 260)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=113.5, h=0, align="R", txt=f"{result['decisions']['price'][3]} $", border=0)
            
                # Un Shr for Company 4
                pdf.set_xy(0, 265)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=113.5, h=0, align="R", txt=f"{round(result['data']['share'][3], 3) * 100}%", border=0)
            
                # MPI for Company 4
                pdf.set_xy(0, 270)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=113.5, h=0, align="R", txt=f"{result['data']['mpi'][3]}   ", border=0)
            
            if company_names_len not in [4, 3, 2]:
                # Company 5
                pdf.set_xy(0, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=136, h=0, align="R", txt=company_names["Company_5"], border=0)
            
                # 5
                pdf.set_xy(115, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=0, h=0, align="L", txt="________", border=0)
            
                # Sales for Company 5
                pdf.set_xy(0, 250)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=136, h=0, align="R", txt=f"{round(result['data']['sales'][4])} $", border=0)
            
                # Profit for Company 5
                pdf.set_xy(0, 255)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=136, h=0, align="R", txt=f"{round(result['data']['profit'][4])} $", border=0)
            
                # Price for Company 5
                pdf.set_xy(0, 260)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=136, h=0, align="R", txt=f"{result['decisions']['price'][4]} $", border=0)
            
                # Un Shr for Company 5
                pdf.set_xy(0, 265)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=136, h=0, align="R", txt=f"{round(result['data']['share'][4], 3) * 100}%", border=0)
            
                # MPI for Company 5
                pdf.set_xy(0, 270)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=136, h=0, align="R", txt=f"{result['data']['mpi'][4]}   ", border=0)
            
            if company_names_len not in [5, 4, 3, 2]:
                # Company 6
                pdf.set_xy(0, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=158.5, h=0, align="R", txt=company_names["Company_6"], border=0)
            
                # 6
                pdf.set_xy(137.5, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=0, h=0, align="L", txt="________", border=0)
            
                # Sales for Company 6
                pdf.set_xy(0, 250)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=158.5, h=0, align="R", txt=f"{round(result['data']['sales'][5])} $", border=0)
            
                # Profit for Company 6
                pdf.set_xy(0, 255)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=158.5, h=0, align="R", txt=f"{round(result['data']['profit'][5])} $", border=0)
            
                # Price for Company 6
                pdf.set_xy(0, 260)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=158.5, h=0, align="R", txt=f"{result['decisions']['price'][5]} $", border=0)
            
                # Un Shr for Company 6
                pdf.set_xy(0, 265)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=158.5, h=0, align="R", txt=f"{round(result['data']['share'][5], 3) * 100}%", border=0)
            
                # MPI for Company 6
                pdf.set_xy(0, 270)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=158.5, h=0, align="R", txt=f"{result['data']['mpi'][5]}   ", border=0)
            
            if company_names_len not in [6, 5, 4, 3, 2]:
                # Company 7
                pdf.set_xy(0, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=181, h=0, align="R", txt=company_names["Company_7"], border=0)
            
                # 7
                pdf.set_xy(160, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=0, h=0, align="L", txt="________", border=0)
            
                # Sales for Company 7
                pdf.set_xy(0, 250)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=181, h=0, align="R", txt=f"{round(result['data']['sales'][6])} $", border=0)
            
                # Profit for Company 7
                pdf.set_xy(0, 255)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=181, h=0, align="R", txt=f"{round(result['data']['profit'][6])} $", border=0)
            
                # Price for Company 7
                pdf.set_xy(0, 260)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=181, h=0, align="R", txt=f"{result['decisions']['price'][6]} $", border=0)
            
                # Un Shr for Company 7
                pdf.set_xy(0, 265)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=181, h=0, align="R", txt=f"{round(result['data']['share'][6], 3) * 100}%", border=0)
            
                # MPI for Company 7
                pdf.set_xy(0, 270)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=181, h=0, align="R", txt=f"{result['data']['mpi'][6]}   ", border=0)
            
            if company_names_len not in [7, 6, 5, 4, 3, 2]:
                # Company 8
                pdf.set_xy(0, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=203.5, h=0, align="R", txt=company_names["Company_8"], border=0)
 
                # 8
                pdf.set_xy(182.5, 245)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=0, h=0, align="L", txt="________", border=0)

                # Sales for Company 8
                pdf.set_xy(0, 250)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=203.5, h=0, align="R", txt=f"{round(result['data']['sales'][7])} $", border=0)

                # Profit for Company 8
                pdf.set_xy(0, 255)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=203.5, h=0, align="R", txt=f"{round(result['data']['profit'][7])} $", border=0)

                # Price for Company 8
                pdf.set_xy(0, 260)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=203.5, h=0, align="R", txt=f"{result['decisions']['price'][7]} $", border=0)

                # Un Shr for Company 8
                pdf.set_xy(0, 265)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=203.5, h=0, align="R", txt=f"{round(result['data']['share'][7], 3) * 100}%", border=0)

                # MPI for Company 8
                pdf.set_xy(0, 270)
                pdf.set_font("Arial", "", 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=203.5, h=0, align="R", txt=f"{result['data']['mpi'][7]}   ", border=0)

                # creation folder
            try:
                os.makedirs('./reports')
            except OSError:
                pass


            pdf.output(f"./reports/{company_num+1}.pdf", "F")


        result = literal_eval(open("result.txt", "r").readline())
        companies = literal_eval(open("Dialog_Setup.txt", "r").readline())
        
        # for merger
        pdf_array = []
        
        # creation PDF files
        for i in range(1, len(companies) + 1):
        
            create_pdf(companies[f"Company_{i}"], i - 1, result, companies)
                
            # for merger
            pdf_array.append(f'./reports/{i}.pdf')
        
        
        # merger PDF files
        merger = PdfMerger()

        for pdf in pdf_array:
            merger.append(pdf)

        merger.write("report.pdf")
        merger.close()
    def no_was_clicked(self):
        pass
        
        
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ClosePeriod = QtWidgets.QDialog()
    ui = Ui_Dialog_ClosePeriod()
    ui.setupUi(Dialog_ClosePeriod)
    Dialog_ClosePeriod.show()
    sys.exit(app.exec())
