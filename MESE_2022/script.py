
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_author("Karton4ik")
        # Company Report for NNN Period N
        self.set_xy(0, 0)
        self.set_font("Arial", "", 13)
        self.set_text_color(0, 0, 0)
        self.cell(w=210, h=10, align="C", txt="Company Report for 000 Period 0", border=0)
        
        
    def footer(self):
        # Lines for Income Statement
        self.rect(5, 10, 100, 92.5)
        
        # Income Statement
        self.set_xy(35, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=30, align="L", txt="Income Statement", border=0)
        
        
        # Sales
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=55, align="L", txt="Sales", border=0)
        
        # Sales_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=55, align="R", txt="100000  $", border=0)
        
        # Sales_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=55, align="R", txt="100%", border=0)
        
        
        # COGS
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=65, align="L", txt="COGS (Cost of Goods)", border=0)
        
        # COGS_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=65, align="R", txt="-1000  $", border=0)
        
        # COGS_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=65, align="R", txt="-100%", border=0)
        
        
        # line
        self.set_xy(58, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=71, align="L", txt="_________________", border=0)
        
        
        # Gross Margin
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=85, align="L", txt="Gross Margin", border=0)
        
        # Gross Margin_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=85, align="R", txt="-1000  $", border=0)
        
        # Gross Margin_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=85, align="R", txt="-100%", border=0)
        
        
        # Marketing
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=95, align="L", txt="Marketing", border=0)
        
        
        # Marketing_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=95, align="R", txt="-1000  $", border=0)
        
        # Marketing_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=95, align="R", txt="-100%", border=0)
        
        
        
        # Depreciation
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=105, align="L", txt="Depreciation", border=0)
        
        
        # Depreciation_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=105, align="R", txt="-1000  $", border=0)
        
        
        # Depreciation_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=105, align="R", txt="-100%", border=0)
        
        
        # R & D
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=115, align="L", txt="R & D", border=0)
        
        # R & D_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=115, align="R", txt="-1000  $", border=0)
        
        
        # R & D_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=115, align="R", txt="-100%", border=0)
        
        
        # Layoff Charge
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=125, align="L", txt="Layoff Charge", border=0)
        
        # Layoff Charge_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=125, align="R", txt="-1000  $", border=0)
        
        # Layoff Charge_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=125, align="R", txt="-100%", border=0)
        
        
        # Inventory Charge
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=135, align="L", txt="Inventory Charge", border=0)
        
        # Inventory Charge_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=135, align="R", txt="-1000  $", border=0)
        
        # Inventory Charge_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=135, align="R", txt="-100%", border=0)
        
        
        # Interest
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=145, align="L", txt="Interest", border=0)

        # Interest_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=145, align="R", txt="-1000  $", border=0)

        # Interest_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=145, align="R", txt="-100%", border=0)
        
        
        # line
        self.set_xy(58, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=151, align="L", txt="_________________", border=0)
        
        
        # Profit before Tax
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=165, align="L", txt="Profit before Tax", border=0)

        # Profit before Tax_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=165, align="R", txt="-1000  $", border=0)

        # Profit before Tax_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=165, align="R", txt="-100%", border=0)
        
        
        # Tax
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=175, align="L", txt="Tax", border=0)

        # Tax_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=175, align="R", txt="-1000  $", border=0)

        # Tax_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=175, align="R", txt="-100%", border=0)
        
        
        # line
        self.set_xy(58, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=181, align="L", txt="_________________", border=0)
        
        
        # Net Profit
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=195, align="L", txt="Net Profit", border=0)

        # Net Profit_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=195, align="R", txt="-1000  $", border=0)

        # Net Profit_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=195, align="R", txt="-100%", border=0)
        
        
        
        # Lines for Operations Reports
        self.rect(105, 10, 100, 170)
        
        #Operations Reports
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=30, align="C", txt="Operations Reports", border=0)
        
        
        
        # Decisions
        self.rect(110, 20, 90, 37.5)
        
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=50, align="C", txt="Decisions", border=0)
        
        # Price
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=65, align="L", txt="Price", border=0)
        
        # Price_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=65, align="R", txt="1000", border=0)
        
        # Price of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=65, align="L", txt="$", border=0)
        
        
        # Production
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=75, align="L", txt="Production", border=0)
        
        # Production_units
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=75, align="R", txt="420", border=0)
        
        # Production of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=75, align="L", txt="units", border=0)
        
        
        # Marketing
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=85, align="L", txt="Marketing", border=0)
        
        # Marketing_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=85, align="R", txt="1000", border=0)
        
        # Marketing of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=85, align="L", txt="$", border=0)
        
        
        # Investment
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=95, align="L", txt="Investment", border=0)
        
        # Investment_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=95, align="R", txt="1000", border=0)
        
        # Investment of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=95, align="L", txt="$", border=0)
        
        
        # R & D
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=105, align="L", txt="R & D", border=0)
        
        # R & D_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=105, align="R", txt="1000", border=0)
        
        # Investment of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=105, align="L", txt="$", border=0)
        
        
        
        #Production Report
        self.rect(110, 60, 90, 42.5)
        
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=130, align="C", txt="Production Report", border=0)
        
        
        # Production
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=145, align="L", txt="Production", border=0)
        
        # Production_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=145, align="R", txt="420", border=0)
        
        # Production_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=145, align="L", txt="units", border=0)
        
        
        # Factory Capacity
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=155, align="L", txt="Factory Capacity", border=0)
        
        # Factory Capacity_INT
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=155, align="R", txt="420", border=0)
        
        # Factory Capacity_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=155, align="L", txt="units", border=0)
        
        
        # Capacity Utilization
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=165, align="L", txt="Capacity Utilization", border=0)
        
        # Capacity Utilization_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=165, align="R", txt="1000", border=0)
        
        # Capacity Utilization_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=165, align="L", txt="%", border=0)
        
        
        # Production Cost/Unit
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=175, align="L", txt="Production Cost/Unit", border=0)
       
        # Production Cost/Unit_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=175, align="R", txt="1000", border=0)
        
        # Production Cost/Unit_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=175, align="L", txt="$", border=0)
        
        
        # Inventory Cost/Unit
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=185, align="L", txt="Inventory", border=0)
       
        # Production Cost/Unit_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=185, align="R", txt="1000", border=0)
        
        # Production Cost/Unit_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=185, align="L", txt="units", border=0)
        
        
        # Employees 
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=195, align="L", txt="Employees", border=0)
        
        # Employees_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=195, align="R", txt="1000", border=0)
        
        # Employees_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=195, align="L", txt="workers", border=0)
       
        
        
        # Marketing Report
        self.rect(110, 105, 90, 42.5)
        
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=220, align="C", txt="Marketing Report", border=0)
        
        
        # Orders Received
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=235, align="L", txt="Orders Received", border=0)
        
        # Orders Received_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=235, align="R", txt="1000", border=0)
        
        # Orders Received_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=235, align="L", txt="units", border=0)
        
        
        # Sales Made
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=245, align="L", txt="Sales Made", border=0)
        
        # Sales Made_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=245, align="R", txt="1000", border=0)
        
        # Sales Made_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=245, align="L", txt="units", border=0)
        
        
        # Unfilled Orders
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=255, align="L", txt="Unfilled Orders", border=0)
        
        # Unfilled Orders_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=255, align="R", txt="1000", border=0)
        
        # Unfilled Orders_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=255, align="L", txt="units", border=0)
        
        
        # Price/Unit Sold
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=265, align="L", txt="Price/Unit Sold", border=0)
        
        # Price/Unit Sold_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=265, align="R", txt="1000", border=0)
        
        # Price/Unit Sold_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=265, align="L", txt="$", border=0)
        
        
        # Total Cost/Unit Sold
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=275, align="L", txt="Total Cost/Unit Sold", border=0)
        
        # Total Cost/Unit Sold_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=275, align="R", txt="1000", border=0)
        
        # Total Cost/Unit Sold_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=275, align="L", txt="$", border=0)
        
        
        # Margin/Unit Sold
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=285, align="L", txt="Margin/Unit Sold", border=0)
        
        # Margin/Unit Sold_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=185, h=285, align="R", txt="1000", border=0)
        
        # Margin/Unit Sold_unit of measurement
        self.set_xy(184, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=285, align="L", txt="$", border=0)
        
        
        
        # Investment Report
        self.rect(110, 150, 90, 30)
        
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=307.5, align="C", txt="Investment Report", border=0)
        
        
        # Factory Size
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=320, align="L", txt="Margin/Unit Sold", border=0)
        
        # Factory Size_int_$
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=170, h=320, align="R", txt="1000 $", border=0)
        
        # Factory Size_int_units
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=190, h=320, align="R", txt="1000", border=0)
        
        # Factory Size_unit of measurement
        self.set_xy(189, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=320, align="L", txt="units", border=0)
        
        
        # Net Investment
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=330, align="L", txt="Net Investment", border=0)
        
        # Net Investment_int_$
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=170, h=330, align="R", txt="1000 $", border=0)
        
        # Net Investment_int_units
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=190, h=330, align="R", txt="1000", border=0)
        
        # Net Investment_unit of measurement
        self.set_xy(189, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=330, align="L", txt="units", border=0)
        
        
        #line
        self.set_xy(153, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=336, align="L", txt="________________", border=0)
        
        
        # Size Next Period
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=350, align="L", txt="Size Next Period", border=0)
        
        #Size Next Period_int_$
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=170, h=350, align="R", txt="1000 $", border=0)
        
        # Size Next Period_int_units
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=190, h=350, align="R", txt="1000", border=0)
        
        # Size Next Period_unit of measurement
        self.set_xy(189, 0)
        self.set_font("Arial", "I", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=350, align="L", txt="units", border=0)
        
        
        
        
        # Lines for Balance Sheet
        self.rect(5, 102.5, 100, 77.5)
        
        # Balance Sheet
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=107.5, h=215, align="C", txt="Balance Sheet", border=0)
        
        
        # Cash
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=240, align="L", txt="Cash", border=0)

        # Cash_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=240, align="R", txt="-1000  $", border=0)

        # Cash_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=240, align="R", txt="-100%", border=0)
        
        
        # Inventory
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=250, align="L", txt="Inventory", border=0)

        # Inventory_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=250, align="R", txt="-1000  $", border=0)

        # Inventory_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=250, align="R", txt="-100%", border=0)
        
        
        # Capital Investment
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=260, align="L", txt="Capital Investment", border=0)

        # Capital Investment_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=260, align="R", txt="-1000  $", border=0)

        # Capital Investment_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=260, align="R", txt="-100%", border=0)
        
        
        #line
        self.set_xy(58, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=266, align="L", txt="_________________", border=0)
        
        
        # Total Assets
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=280, align="L", txt="Total Assets", border=0)

        # Total Assets_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=280, align="R", txt="-1000  $", border=0)

        # Total Assets_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=280, align="R", txt="-100%", border=0)
        
        
        
        # Loans
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=310, align="L", txt="Loans", border=0)

        # Loans_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=310, align="R", txt="-1000  $", border=0)

        # Loans%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=310, align="R", txt="-100%", border=0)
        
        
        # Retained Earnings
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=320, align="L", txt="Retained Earnings", border=0)

        # Retained Earnings_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=320, align="R", txt="-1000  $", border=0)

        # Retained Earnings_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=320, align="R", txt="-100%", border=0)
        
        
        # Capital
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=330, align="L", txt="Capital", border=0)

        # Capital_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=330, align="R", txt="-1000  $", border=0)

        # Capital_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=330, align="R", txt="-100%", border=0)
        
        
        #line
        self.set_xy(58, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=336, align="L", txt="_________________", border=0)
        
        
        # Liabilities+Equity
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=350, align="L", txt="Liabilities+Equity", border=0)

        # Liabilities+Equity_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=350, align="R", txt="-1000  $", border=0)

        # Liabilities+Equity_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=350, align="R", txt="-100%", border=0)
        
        
        # Industry Report for Period NNN
        self.rect(5, 190, 100, 32.5)
        self.rect(105, 190, 100, 32.5)
        self.rect(5, 222.5, 100, 32.5)
        self.rect(105, 222.5, 100, 32.5)
       
        self.set_xy(0, 0)
        self.set_font("Arial", "", 13)
        self.set_text_color(0, 0, 0)
        self.cell(w=210, h=370, align="C", txt="Industry Report for Period 0", border=0)
        
       
       # Units
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=107.5, h=385, align="C", txt="Units", border=0)
        
        
        # Total Orders
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=400, align="L", txt="Total Orders", border=0)

        # Total Orders_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=400, align="R", txt="-1000  $", border=0)

        # Total Orders_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=400, align="R", txt="-100%", border=0)
       
       
       # Total Produced
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=410, align="L", txt="Total Produced", border=0)

        # Total Produced_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=410, align="R", txt="-1000  $", border=0)

        # Total Produced_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=410, align="R", txt="-100%", border=0)
        
        
        # Total Sold
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=420, align="L", txt="Total Sold", border=0)

        # Total Sold_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=420, align="R", txt="-1000  $", border=0)

        # Total Sold_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=420, align="R", txt="-100%", border=0)
        
        
        # Total Capacity
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=430, align="L", txt="Total Capacity", border=0)

        # Total Capacity_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=430, align="R", txt="-1000  $", border=0)

        # Total Capacity_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=430, align="R", txt="-100%", border=0)
       
       
       # Inventory
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=440, align="L", txt="Inventory", border=0)

        # Inventory_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=440, align="R", txt="-1000  $", border=0)

        # Inventory_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=440, align="R", txt="-100%", border=0)
       
       
       
       
       # Productivity
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=107.5, h=450, align="C", txt="Productivity", border=0)
        
        
        # Employment
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=465, align="L", txt="Employment", border=0)

        # Employment_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=465, align="R", txt="1000    ", border=0)

        # Employment_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=465, align="R", txt="-100%", border=0)
        
        
        # Sales/Employee
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=475, align="L", txt="Sales/Employee", border=0)

        # Sales/Employee_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=475, align="R", txt="1000  $", border=0)

        # Sales/Employee_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=475, align="R", txt="-100%", border=0)
        
        
        # Units/Employee
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=485, align="L", txt="Units/Employee", border=0)

        # Units/Employee_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=485, align="R", txt="1000    ", border=0)

        # Units/Employee_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=485, align="R", txt="-100%", border=0)
        
        
        # Cap. Investment
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=495, align="L", txt="Cap. Investment", border=0)

        # Cap. Investment_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=495, align="R", txt="1000  $", border=0)

        # Cap. Investment_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=495, align="R", txt="-100%", border=0)
        
        
        # Capacity Util.
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=505, align="L", txt="Capacity Util.", border=0)

        # Capacity Util._int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=80, h=505, align="R", txt="000 %", border=0)

        # Capacity Util._%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100, h=505, align="R", txt="-100%", border=0)
       
       
       
        # Dollars
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=385, align="C", txt="Dollars", border=0)
       
       
        # Industry Sales
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=400, align="L", txt="Industry Sales", border=0)

        # Industry Sales_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=400, align="R", txt="1000  $", border=0)

        # Industry Sales_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=400, align="R", txt="-100%", border=0)
        
        
        # Average Price
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=410, align="L", txt="Average Price", border=0)

        # Average Price_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=410, align="R", txt="1000  $", border=0)

        # Average Price_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=410, align="R", txt="-100%", border=0)
        
        
        # Total Production
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=420, align="L", txt="Total Production", border=0)

        # Total Production_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=420, align="R", txt="1000  $", border=0)

        # Total Production_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=420, align="R", txt="-100%", border=0)
        
        
        # Avg Pdtn Cost
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=430, align="L", txt="Avg Pdtn Cost", border=0)

        # Avg Pdtn Cost_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=430, align="R", txt="1000  $", border=0)

        # Avg Pdtn Cost_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=430, align="R", txt="-100%", border=0)
        
        
        # Avg Total Cost
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=440, align="L", txt="Avg Total Cost", border=0)

        # Avg Total Cost_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=440, align="R", txt="1000  $", border=0)

        # Avg Total Cost_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=440, align="R", txt="-100%", border=0)
       
       
       
        # Period Settings
        self.set_xy(110, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=450, align="C", txt="Period Settings", border=0)
        
        
        
        # Prime Rate
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=465, align="L", txt="Prime Rate", border=0)

        # Prime Rate_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=465, align="R", txt="000 %", border=0)

        # Prime Rate_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=465, align="R", txt="-100%", border=0)
        
        
        # Loan Limit
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=475, align="L", txt="Loan Limit", border=0)

        # Loan Limit_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=475, align="R", txt="1000  $", border=0)

        # Loan Limit_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=475, align="R", txt="-100%", border=0)
        
        
        # Tax Rate
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=485, align="L", txt="Tax Rate", border=0)

        # Tax Rate_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=485, align="R", txt="000 %", border=0)

        # Tax Rate_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=485, align="R", txt="-100%", border=0)
        
        
        # Tax Paid in Period
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=495, align="L", txt="Tax Paid in Period", border=0)

        # Tax Paid in Period_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=495, align="R", txt="1000  $", border=0)

        # Tax Paid in Period_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=495, align="R", txt="-100%", border=0)
        
        
        # Tax Paid to Date
        self.set_xy(105, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=505, align="L", txt="Tax Paid to Date", border=0)

        # Tax Paid to Date_int
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=180, h=505, align="R", txt="1000  $", border=0)

        # Tax Paid to Date_%
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=200, h=505, align="R", txt="-100%", border=0)
        
        
        
        # Company 1
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=46, h=517.5, align="R", txt="11111111", border=0)
        
        # Company 2
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=68.5, h=517.5, align="R", txt="22222222", border=0)
        
        # Company 3
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=91, h=517.5, align="R", txt="33333333", border=0)
        
        # Company 4
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=113.5, h=517.5, align="R", txt="44444444", border=0)
        
        # Company 5
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=136, h=517.5, align="R", txt="55555555", border=0)
        
        # Company 6
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=158.5, h=517.5, align="R", txt="66666666", border=0)
        
        # Company 7
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=181, h=517.5, align="R", txt="77777777", border=0)
        
        # Company 8
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=203.5, h=517.5, align="R", txt="88888888", border=0)
        
        
        
        
        
        
        # 1
        self.set_xy(25, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        # 2
        self.set_xy(47.5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        # 3
        self.set_xy(70, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        # 4
        self.set_xy(92.5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        # 5
        self.set_xy(115, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        # 6
        self.set_xy(137.5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        # 7
        self.set_xy(160, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        # 8
        self.set_xy(182.5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=520, align="L", txt="________", border=0)
        
        
        
        
        
        
        # Sales
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=530, align="L", txt="Sales", border=0)
        
        
        # Profit
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=540, align="L", txt="Profit", border=0)
        
        # Price
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=550, align="L", txt="Price", border=0)
        
        # RetErn
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=560, align="L", txt="RetErn", border=0)
        
        # Un Shr
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=570, align="L", txt="Un Shr", border=0)
        
        # MPI
        self.set_xy(5, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=580, align="L", txt="MPI", border=0)
        
        
        
        
        # Sales for Company 1
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=46, h=530, align="R", txt="11790 $", border=0)
        
        # Sales for Company 2
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=68.5, h=530, align="R", txt="11790 $", border=0)
        
        # Sales for Company 3
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=91, h=530, align="R", txt="11790 $", border=0)
        
        # Sales for Company 4
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=113.5, h=530, align="R", txt="11790 $", border=0)
        
        # Sales for Company 5
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=136, h=530, align="R", txt="11790 $", border=0)
        
        # Sales for Company 6
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=158.5, h=530, align="R", txt="11790 $", border=0)
        
        # Sales for Company 7
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=181, h=530, align="R", txt="11790 $", border=0)
        
        # Sales for Company 8
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=203.5, h=530, align="R", txt="11790 $", border=0)
        
        
        # Profit for Company 1
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=46, h=540, align="R", txt="11790 $", border=0)
        
        # Profit for Company 2
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=68.5, h=540, align="R", txt="11790 $", border=0)
        
        # Profit for Company 3
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=91, h=540, align="R", txt="11790 $", border=0)
        
        # Profit for Company 4
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=113.5, h=540, align="R", txt="11790 $", border=0)
        
        # Profit for Company 5
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=136, h=540, align="R", txt="11790 $", border=0)
        
        # Profit for Company 6
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=158.5, h=540, align="R", txt="11790 $", border=0)
        
        # Profit for Company 7
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=181, h=540, align="R", txt="11790 $", border=0)
        
        # Profit for Company 8
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=203.5, h=540, align="R", txt="11790 $", border=0)
        
        
        # Price for Company 1
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=46, h=550, align="R", txt="11790 $", border=0)
        
        # Price for Company 2
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=68.5, h=550, align="R", txt="11790 $", border=0)
        
        # Price for Company 3
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=91, h=550, align="R", txt="11790 $", border=0)
        
        # Price for Company 4
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=113.5, h=550, align="R", txt="11790 $", border=0)
        
        # Price for Company 5
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=136, h=550, align="R", txt="11790 $", border=0)
        
        # Price for Company 6
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=158.5, h=550, align="R", txt="11790 $", border=0)
        
        # Price for Company 7
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=181, h=550, align="R", txt="11790 $", border=0)
        
        # Price for Company 8
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=203.5, h=550, align="R", txt="11790 $", border=0)
        
        
        # RetErn for Company 1
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=46, h=560, align="R", txt="11790 $", border=0)
        
        # RetErn for Company 2
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=68.5, h=560, align="R", txt="11790 $", border=0)
        
        # RetErn for Company 3
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=91, h=560, align="R", txt="11790 $", border=0)
        
        # RetErn for Company 4
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=113.5, h=560, align="R", txt="11790 $", border=0)
        
        # RetErn for Company 5
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=136, h=560, align="R", txt="11790 $", border=0)
        
        # RetErn for Company 6
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=158.5, h=560, align="R", txt="11790 $", border=0)
        
        # RetErn for Company 7
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=181, h=560, align="R", txt="11790 $", border=0)
        
        # RetErn for Company 8
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=203.5, h=560, align="R", txt="11790 $", border=0)
        
        
        # Un Shr for Company 1
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=46, h=570, align="R", txt="13%", border=0)
        
        # Un Shr for Company 2
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=68.5, h=570, align="R", txt="13%", border=0)
        
        # Un Shr for Company 3
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=91, h=570, align="R", txt="13%", border=0)
        
        # Un Shr for Company 4
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=113.5, h=570, align="R", txt="13%", border=0)
        
        # Un Shr for Company 5
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=136, h=570, align="R", txt="13%", border=0)
        
        # Un Shr for Company 6
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=158.5, h=570, align="R", txt="13%", border=0)
        
        # Un Shr for Company 7
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=181, h=570, align="R", txt="13%", border=0)
        
        # Un Shr for Company 8
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=203.5, h=570, align="R", txt="13%", border=0)
        
        
        # MPI for Company 1
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=46, h=580, align="R", txt="100   ", border=0)
        
        # MPI for Company 2
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=68.5, h=580, align="R", txt="100   ", border=0)
        
        # MPI for Company 3
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=91, h=580, align="R", txt="100   ", border=0)
        
        # MPI for Company 4
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=113.5, h=580, align="R", txt="100   ", border=0)
        
        # MPI for Company 5
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=136, h=580, align="R", txt="100   ", border=0)
        
        # MPI for Company 6
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=158.5, h=580, align="R", txt="100   ", border=0)
        
        # MPI for Company 7
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=181, h=580, align="R", txt="100   ", border=0)
        
        # MPI for Company 8
        self.set_xy(0, 0)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=203.5, h=580, align="R", txt="100   ", border=0)
        
        
pdf = PDF()

pdf.output("1.pdf", "F")

