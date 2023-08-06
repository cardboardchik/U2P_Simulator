
## by Karton4ik

import math


def init(count):
    game = {
        "player_count": count,
        "total_tick": 99,
        "now_tick": 0,
        "now_period": 1,
        "delta": 0.01,
    

        "settings": {
            "price_max": 99,
            "price_min": 2,
            "mk_limit": 120000, #15000 * count
            "ci_limit": 120000, # 15000 * count
            "rd_limit": 120000 , # 15000 * count
            "loan_limit": 400000, # 50000 * count
            
            "prod_rate_initial": 0.75,
            "prod_rate_balanced": 0.8,
            "prod_rate_pow": 2,
            "prod_cost_factor_rate_over": 69,
            "prod_cost_factor_rate_under": 138,
            "prod_cost_factor_size": 15,
            "prod_cost_factor_const": 3,
            
            "employees_const": 5,
            "layoff_charge_cost_const": 10,

            "unit_fee": 40,
            "depreciation_rate": 0.05,

            "initial_cash": 14700, # 1837.5 * count
            "initial_loan": 58240, # 7280 * count
            "initial_capital": 168000, # 21000 * 8

            "interest_rate_cash": 0.0125,
            "interest_rate_loan": 0.035,
            "inventory_fee": 1,
            "tax_rate": 0.25,

            "mk_overload": 16800, #2100 * 8
            "mk_compression": 0.25,

            "demand": 500, # 62.5 * 8
            "demand_price": 1,
            "demand_mk": 5.3,
            "demand_rd": 1,

            "demand_ref_price": 30,
            "demand_ref_mk": 8400, # 1050 * 8
            "demand_ref_rd": 3150, #393.75 * 8
            "demand_pow_price": 1,
            "demand_pow_mk": 0.5,
            "demand_pow_rd": 1,

            "share_price": 0.7,
            "share_mk": 0.15,
            "share_rd": 0.15,
            "share_pow_price": 3,
            "share_pow_mk": 1.5,
            "share_pow_rd": 1,

            "price_overload": 40,

            "upi_retern_factor": 11155, # 1394.375 * count
            "upi_factor_a": 50,
            "upi_factor_b": 10,
            "upi_factor_c": 10,
            "upi_factor_d": 10,
            "upi_factor_e": 10,
            "upi_factor_f": 10,
            
        },
    
        "decisions": {
            "price": [0 for i in range(count)],
            "prod_rate": [0 for i in range(count)],
            "mk": [0 for i in range(count)],
            "ci": [0 for i in range(count)],
            "rd": [0 for i in range(count)],
        },

        "data": {
            "prod": [0 for i in range(count)],
            "prod_over": [0 for i in range(count)],
            "prod_cost_unit": [0 for i in range(count)],
            "prod_cost_marginal": [0 for i in range(count)],
            "prod_cost": [0 for i in range(count)],
            
            "margin_unit_sold": [0 for i in range(count)],
            "total_cost_unit_sold": [0 for i in range(count)],

            "goods": [0 for i in range(count)],
            "goods_predicted": [0 for i in range(count)], 
            "goods_cost": [0 for i in range(count)],
            "goods_cost_predicted": [0 for i in range(count)], 
            "goods_max_sales": [0 for i in range(count)],

            "depreciation": [0 for i in range(count)],
            "capital": [0 for i in range(count)],
            "size": [0 for i in range(count)],
            "spending": [0 for i in range(count)],
            "balance_early": [0 for i in range(count)],
            "loan_early": [0 for i in range(count)],
            "interest": [0 for i in range(count)],

            "history_mk": [0 for i in range(count)],
            "history_rd": [0 for i in range(count)],

            "average_price_given": None,
            "average_price_planned": None,
            "average_price_mixed": None,
            "demand_effect_mk": None,
            "demand_effect_rd": None,
            "orders_demand": None,

            "share_effect_price": [0 for i in range(count)],
            "share_effect_mk": [0 for i in range(count)],
            "share_effect_rd": [0 for i in range(count)],
            "share": [0 for i in range(count)],
            "share_compressed": [0 for i in range(count)],

            "orders": [0 for i in range(count)],
            "sold": [0 for i in range(count)],
            "inventory": [0 for i in range(count)],
            "unfilled": [0 for i in range(count)],
            "employees": [0 for i in range(count)],

            "goods_cost_sold": [0 for i in range(count)],
            "goods_cost_inventory": [0 for i in range(count)],

            "sales": [0 for i in range(count)],
            "inventory_charge": [0 for i in range(count)],
            "cost_before_tax": [0 for i in range(count)],
            "profit_before_tax": [0 for i in range(count)],
            "tax_charge": [0 for i in range(count)],
            "layoff_charge": [0 for i in range(count)],
            "profit": [0 for i in range(count)],
            
            "tax_paid_to_period": None,
            "tax_paid_to_date": 0,

            "balance": [0 for i in range(count)],
            "loan": [0 for i in range(count)],
            "cash": [0 for i in range(count)],
            "retern": [0 for i in range(count)],

            "average_price": None,

            "upi_a": [0 for i in range(count)],
            "upi_b": [0 for i in range(count)],
            "upi_c": [0 for i in range(count)],
            "upi_d": [0 for i in range(count)],
            "upi_e": [0 for i in range(count)],
            "upi_f": [0 for i in range(count)],
            "upi": [0 for i in range(count)],
    
        },
       
    }
    i = 0
    while i < game["player_count"]:
        game["decisions"]["price"][i] = game["settings"]["demand_ref_price"]
        game["decisions"]["prod_rate"][i] = game["settings"]["prod_rate_initial"]
        game["decisions"]["mk"][i] = game["settings"]["demand_ref_mk"] / game["player_count"]
        game["decisions"]["ci"][i] = game["settings"]["initial_capital"] / game["player_count"] * game["settings"]["depreciation_rate"]
        game["decisions"]["rd"][i] = game["settings"]["demand_ref_rd"] / game["player_count"]
        
        game["data"]["capital"][i] = round(game["settings"]["initial_capital"] / game["player_count"], 1)
        game["data"]["size"][i] = math.trunc(game["data"]["capital"][i] / game["settings"]["unit_fee"])
        game["data"]["employees"][i] = math.trunc((game["data"]["size"][i] * game["settings"]["prod_rate_initial"]) / game["settings"]["employees_const"])
        game["data"]["history_mk"][i] = 0 #game["decisions"]["mk"][i]
        game["data"]["history_rd"][i] = 0 #game["decisions"]["rd"][i]
        
        game["data"]["inventory"][i] = 0
        game["data"]["goods_cost_inventory"][i] = 0

        game["data"]["loan"][i] = 0 #game["settings"]["initial_loan"] / game["player_count"]
        game["data"]["cash"][i] = round(game["settings"]["initial_cash"] / game["player_count"], 1)
        game["data"]["retern"][i] = 0 #game["settings"]["upi_retern_factor"]
                        
        i += 1
    game["data"]["average_price"] = game["settings"]["demand_ref_price"]
    
    return game

def exec(game):
    def minmax(a, min_1, max_1):
        return min(max(a, min_1), max_1)
    
    
    def div (a, b, e):
        if b == 0:
            return e
        else:
            return a / b    
    
    def sum(data):
        s = 0
        i = 0
        while i < game["player_count"]:
            s += data[i]
            
            i += 1
        return s
    
    def each(callback):
        i = 0
        while i < game["player_count"]:
               
            callback(i)
            i += 1
            
    #def MESE_CASH(value):
    #    return (0.01 * round(100 * (value)))
            
            

    if game["now_tick"] >= game["total_tick"]:
        return False
    
    game["now_tick"] += 1
    game["now_period"] += game["delta"]
    
    
    def fun_1(i):
        
        
        game["decisions"]["price"][i] = minmax(
            game["decisions"]["price"][i],
            game["settings"]["price_min"], game["settings"]["price_max"]
        )

        game["decisions"]["prod_rate"][i] = minmax(
            game["decisions"]["prod_rate"][i], 0, 1
        )
        
        game["decisions"]["mk"][i] = minmax(
            game["decisions"]["mk"][i], 0,
            game["settings"]["mk_limit"] / game["player_count"]
        )
        
        game["decisions"]["ci"][i] = minmax(
            game["decisions"]["ci"][i], 
            0, game["settings"]["ci_limit"] / game["player_count"]
        )
        
        game["decisions"]["rd"][i] = minmax(
            game["decisions"]["rd"][i], 
            0, game["settings"]["rd_limit"] / game["player_count"]
        )
        
        
        
        #if game["data"]["loan"][i] > game["settings"]["loan_limit"] / game["player_count"]:
            #game["decisions"]["prod_rate"][i] = 0
            #game["decisions"]["mk"][i] = 0
            #game["decisions"]["ci"][i] = 0
            #game["decisions"]["rd"][i] = 0
            
            
        
        game["data"]["prod"][i] = math.trunc(game["decisions"]["prod_rate"][i] * game["data"]["size"][i])
        game["data"]["prod_over"][i] = game["decisions"]["prod_rate"][i] - game["settings"]["prod_rate_balanced"]
        
        prod_cost_factor_rate = game["data"]["prod_over"][i]
        
        if prod_cost_factor_rate > 0:
            prod_cost_factor_rate = game["settings"]["prod_cost_factor_rate_over"]
        else:
            prod_cost_factor_rate = game["settings"]["prod_cost_factor_rate_under"]
        
        
        game["data"]["prod_cost_unit"][i] = prod_cost_factor_rate * math.pow(game["data"]["prod_over"][i], game["settings"]["prod_rate_pow"]) + game["settings"]["prod_cost_factor_size"] * game["settings"]["initial_capital"] / game["data"]["capital"][i] / game["player_count"] + game["settings"]["prod_cost_factor_const"]
        
        game["data"]["prod_cost_marginal"][i] = prod_cost_factor_rate * game["settings"]["prod_rate_pow"] * game["decisions"]["prod_rate"][i] * math.pow(game["data"]["prod_over"][i], game["settings"]["prod_rate_pow"] - 1) + game["data"]["prod_cost_unit"][i]

        game["data"]["prod_cost"][i] = game["data"]["prod_cost_unit"][i] * game["data"]["prod"][i]
        
        game["data"]["goods"][i] = game["data"]["inventory"][i] + game["data"]["prod"][i] #* game["delta"]
        #game["data"]["goods_predicted"][i] = math.trunc(game["data"]["inventory"][i] + game["data"]["prod"][i])
        game["data"]["goods_cost"][i] = game["data"]["goods_cost_inventory"][i] + game["data"]["prod_cost"][i] #* game["delta"]
        #game["data"]["goods_cost_predicted"][i] = round(game["data"]["goods_cost_inventory"][i] + game["data"]["prod_cost"][i], 1)
        game["data"]["goods_max_sales"][i] = round(game["decisions"]["price"][i] * game["data"]["goods"][i], 1)
        
        game["data"]["depreciation"][i] = round(game["settings"]["depreciation_rate"] * game["data"]["capital"][i], 1)
        game["data"]["capital"][i] += round(game["decisions"]["ci"][i] - game["data"]["depreciation"][i], 1)# * game["delta"]
        game["data"]["size"][i] = round(game["data"]["capital"][i] / game["settings"]["unit_fee"])
        
        if game["data"]["employees"][i] <= game["data"]["prod"][i] // game["settings"]["employees_const"]:
            game["data"]["layoff_charge"][i] = 0
        else:
            game["data"]["layoff_charge"][i] = round((game["data"]["employees"][i] - (game["data"]["prod"][i] // game["settings"]["employees_const"])) * game["settings"]["layoff_charge_cost_const"], 1)
        
        game["data"]["employees"][i] = math.trunc(game["data"]["prod"][i] / game["settings"]["employees_const"])
        
        game["data"]["spending"][i] = round(game["data"]["prod_cost"][i] + game["decisions"]["ci"][i] - game["data"]["depreciation"][i] + game["decisions"]["mk"][i] + game["decisions"]["rd"][i], 1)
        game["data"]["balance_early"][i] = round(game["data"]["cash"][i] - game["data"]["loan"][i] - game["data"]["spending"][i], 1) #* game["delta"]
        game["data"]["loan_early"][i] = round(max(-game["data"]["balance_early"][i], 0), 1)
        
        
        
        game["data"]["interest"][i] = round(game["data"]["balance_early"][i], 1)
        
        if game["data"]["balance_early"][i] >= 0:
            game["data"]["interest"][i] = game["settings"]["interest_rate_cash"] * game["data"]["balance_early"][i]
        else:
            game["data"]["interest"][i] = game["settings"]["interest_rate_loan"] * game["data"]["balance_early"][i]
        
        game["data"]["history_mk"][i] += game["decisions"]["mk"][i] #* game["delta"]
        game["data"]["history_rd"][i] += game["decisions"]["rd"][i] #* game["delta"]
        
    each(fun_1)
    
    sum_mk = sum(game["decisions"]["mk"])
    sum_mk_compressed = min(
        game["settings"]["mk_compression"] * (sum_mk - game["settings"]["mk_overload"]) + 
        game["settings"]["mk_overload"], 
        sum_mk
    )
        
    sum_history_mk = sum(game["data"]["history_mk"])
    sum_history_rd = sum(game["data"]["history_rd"])
        
    game["data"]["average_price_given"] = round(sum(game["decisions"]["price"]) / game["player_count"], 2)
    game["data"]["average_price_planned"] = round(div(sum(game["data"]["goods_max_sales"]), sum(game["data"]["goods"]), game["data"]["average_price_given"]), 2)
    game["data"]["average_price_mixed"] = round(game["settings"]["demand_price"] * game["data"]["average_price_planned"] + (1 - game["settings"]["demand_price"]) * game["data"]["average_price"], 2)
    
        
    game ["data"]["demand_effect_mk"] = game["settings"]["demand_mk"] * math.pow(
        sum_mk_compressed / game["settings"]["demand_ref_mk"], 
        game["settings"]["demand_pow_mk"]
    ) / math.pow(
        game["data"]["average_price_mixed"] / game["settings"]["demand_ref_price"],
            game["settings"]["demand_pow_price"]
    )
        
    game["data"]["demand_effect_rd"] = game["settings"]["demand_rd"] * math.pow(
        sum_history_rd / game["now_tick"] / game["settings"]["demand_ref_rd"],
        game["settings"]["demand_pow_rd"]
    )
    game["data"]["orders_demand"] = math.trunc(game["settings"]["demand"] * (
        game["data"]["demand_effect_rd"] + game["data"]["demand_effect_mk"]
    ))
        
    def fun_2(i):
        game["data"]["share_effect_price"][i] = math.pow(
            game["data"]["average_price_mixed"] / game["decisions"]["price"][i],
            game["settings"]["share_pow_price"]
        )
        game["data"]["share_effect_mk"][i] = math.pow(
            game["decisions"]["mk"][i] / game["decisions"]["price"][i],
            game["settings"]["share_pow_mk"]
        )
        game["data"]["share_effect_rd"][i] = math.pow(
            game["data"]["history_rd"][i], 
            game["settings"]["share_pow_rd"]
        )
    
    each(fun_2)
    
    sum_share_effect_price = sum(game["data"]["share_effect_price"])
    sum_share_effect_mk = sum(game["data"]["share_effect_mk"])
    sum_share_effect_rd = sum(game["data"]["share_effect_rd"])
    
    def fun_3(i):
        #orders
        game["data"]["share"][i] = game["settings"]["share_price"] * div(
            game["data"]["share_effect_price"][i],
            sum_share_effect_price,
            0
            ) + game["settings"]["share_mk"] * div(
                game["data"]["share_effect_mk"][i],
                sum_share_effect_mk,
                0
            ) + game["settings"]["share_rd"] * div(
                game["data"]["share_effect_rd"][i],
                sum_share_effect_rd,
                0
            )
            
        
        game["data"]["share_compressed"][i] = min(game["data"]["share"][i] * game["settings"]["price_overload"] / game["decisions"]["price"][i], game["data"]["share"][i])
        
        game["data"]["orders"][i] = math.trunc(game["data"]["orders_demand"] * game["data"]["share_compressed"][i])
        game["data"]["sold"][i] = math.trunc(min(game["data"]["orders"][i], game["data"]["goods"][i]))
        game["data"]["inventory"][i] = math.trunc(game["data"]["goods"][i] - game["data"]["sold"][i])
        game["data"]["unfilled"][i] = math.trunc(game["data"]["orders"][i] - game["data"]["sold"][i])
        
        #goods
        
        game["data"]["goods_cost_sold"][i] = round(game["data"]["goods_cost"][i] * div(
            game["data"]["sold"][i],
            game["data"]["goods"][i],
            0
        ), 1)
        game["data"]["goods_cost_inventory"][i] = round(game["data"]["goods_cost"][i] - game["data"]["goods_cost_sold"][i], 1)
        
        #cash Flow
        
        game["data"]["sales"][i] = round(game["decisions"]["price"][i] * game["data"]["sold"][i], 1)
        
        game["data"]["inventory_charge"][i] = round(game["settings"]["inventory_fee"] * min(
            game["data"]["inventory"][i],
            game["data"]["inventory"][i]
        ), 1)
        
        game["data"]["cost_before_tax"][i] = round(game["data"]["goods_cost_sold"][i] + game["data"]["depreciation"][i] + game["decisions"]["mk"][i] + game["decisions"]["rd"][i] - game["data"]["interest"][i] + game["data"]["inventory_charge"][i] + game["data"]["layoff_charge"][i], 1)
        game["data"]["profit_before_tax"][i] = round(game["data"]["sales"][i] - game["data"]["cost_before_tax"][i], 1)
        game["data"]["tax_charge"][i] = max(round(game["settings"]["tax_rate"] * game["data"]["profit_before_tax"][i], 1), 0)
        game["data"]["profit"][i] = round(game["data"]["profit_before_tax"][i] - game["data"]["tax_charge"][i], 2)
        
        game["data"]["balance"][i] = round(game["data"]["cash"][i] - game["data"]["loan"][i] + game["data"]["loan_early"][i] + game["data"]["profit"][i] - game["decisions"]["ci"][i] + game["data"]["depreciation"][i] + game["data"]["goods_cost_sold"][i] - game["data"]["prod_cost"][i] - game["data"]["layoff_charge"][i], 1) #game["data"]["cash"][i] - game["data"]["loan"][i] + game["data"]["loan_early"][i] + game["data"]["profit"][i] - game["decisions"]["ci"][i] + game["data"]["depreciation"][i] + game["data"]["goods_cost_sold"][i] - game["data"]["prod_cost"][i]
        
        game["data"]["loan"][i] = round(max(game["data"]["loan_early"][i], game["data"]["loan_early"][i] - game["data"]["balance"][i]), 1)
        game["data"]["cash"][i] = round(max(game["data"]["balance"][i], 0), 1)
        game["data"]["retern"][i] += round(game["data"]["profit"][i], 1) #* game["delta"]
        
        
        
    
    each(fun_3)
    
    game["data"]["average_price"] = div(
        sum(game["data"]["sales"]),
        sum(game["data"]["sold"]),
        game["data"]["average_price_given"]
    )
    sum_size = sum(game["data"]["size"])
    sum_sold = sum(game["data"]["sold"])
    
    
    
    
    
    def fun_4(i):

        game["data"]["margin_unit_sold"][i] = round(game["data"]["profit"][i] / game["data"]["sold"][i], 2)
        game["data"]["total_cost_unit_sold"][i] = round(game["decisions"]["price"][i] - game["data"]["margin_unit_sold"][i], 2)
        
        game["data"]["tax_paid_to_period"] = round(sum(game["data"]["tax_charge"]))
        game["data"]["tax_paid_to_date"] += game["data"]["tax_paid_to_period"]
        
        
        
        game["data"]["upi_a"][i] = round(game["settings"]["upi_factor_a"] * game["player_count"] * (
            game["data"]["retern"][i] / game["now_tick"] / game["settings"]["upi_retern_factor"]
        ))
        game["data"]["upi_b"][i] = round(game["settings"]["upi_factor_b"] * game["player_count"] * (
            (game["data"]["history_rd"][i] + game["data"]["history_mk"][i]) / (sum_history_rd + sum_history_mk)
        ))
        game["data"]["upi_c"][i] = round(game["settings"]["upi_factor_c"] * game["player_count"] * (
            game["data"]["size"][i] / sum_size
        ))
        game["data"]["upi_d"][i] = round(game["settings"]["upi_factor_d"] * (
            1 - abs(game["data"]["prod_over"][i])
        ))
        game["data"]["upi_e"][i] = round(game["settings"]["upi_factor_e"] * game["player_count"] * (
            div(
                game["data"]["sold"][i],
                sum_sold,
                0
            )
        ))
        
        game["data"]["upi_f"][i] = game["settings"]["upi_factor_f"]
        
        game["data"]["upi"][i] = round(game["data"]["upi_a"][i] + game["data"]["upi_b"][i] + 
                                       game["data"]["upi_c"][i] + game["data"]["upi_d"][i] + 
                                       game["data"]["upi_e"][i] + game["data"]["upi_f"][i])
    each(fun_4)

    return game

#by Karton4ik