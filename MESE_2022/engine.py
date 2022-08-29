
#by Karton4ik

import math


def init(count):
    zero = [0 for i in range(count)]
    game = {
        "player_count": count,
        "total_tick": 99,
        "now_tick": 0,
        "now_period": 1,
        "delta": 0.01,
    

        "settings": {
            "price_max": 99,
            "price_min": 2,
            "mk_limit": 15000 * count,
            "ci_limit": 15000 * count,
            "rd_limit": 15000 * count ,
            "loan_limit": 30000 * count,
            
            "prod_rate_initial": 0.8,
            "prod_rate_balanced": 0.8,
            "prod_rate_pow": 2,
            "prod_cost_factor_rate_over": 63,
            "prod_cost_factor_rate_under": 63,
            "prod_cost_factor_size": 15,
            "prod_cost_factor_const": 3,

            "unit_fee": 40,
            "depreciation_rate": 0.05,

            "initial_cash": 1750 * count,
            "initial_loan": 7280 * count,
            "initial_capital": 21000 * count,

            "interest_rate_cash": 0.025,
            "interest_rate_loan": 0.05,
            "inventory_fee": 1,
            "tax_rate": 0.25,

            "mk_overload": 2100 * count,
            "mk_compression": 0.25,

            "demand": 70 * count,
            "demand_price": 1,
            "demand_mk": 5,
            "demand_rd": 1,

            "demand_ref_price": 30,
            "demand_ref_mk": 1050 * count,
            "demand_ref_rd": 420 * count,
            "demand_pow_price": 1,
            "demand_pow_mk": 0.5,
            "demand_pow_rd": 1,

            "share_price": 0.4,
            "share_mk": 0.3,
            "share_rd": 0.3,
            "share_pow_price": 3,
            "share_pow_mk": 1.5,
            "share_pow_rd": 1,

            "price_overload": 40,

            "mpi_retern_factor": 1617 * count,
            "mpi_factor_a": 50,
            "mpi_factor_b": 10,
            "mpi_factor_c": 10,
            "mpi_factor_d": 10,
            "mpi_factor_e": 10,
            "mpi_factor_f": 10,
            
        },
    
        "decisions": {
            "price": zero,
            "prod_rate": zero,
            "mk": zero,
            "ci": zero,
            "rd": zero,
        },

        "data": {
            "prod": zero,
            "prod_over": zero,
            "prod_cost_unit": zero,
            "prod_cost_marginal": zero,
            "prod_cost": zero,
            
            "margin_unit_sold": zero,
            "total_cost_unit_sold": zero,

            "goods": zero,
            "goods_predicted": zero, 
            "goods_cost": zero,
            "goods_cost_predicted": zero, 
            "goods_max_sales": zero,

            "depreciation": zero,
            "capital": zero,
            "size": zero,
            "spending": zero,
            "balance_early": zero,
            "loan_early": zero,
            "interest": zero,

            "history_mk": zero,
            "history_rd": zero,

            "average_price_given": None,
            "average_price_planned": None,
            "average_price_mixed": None,
            "demand_effect_mk": None,
            "demand_effect_rd": None,
            "orders_demand": None,

            "share_effect_price": zero,
            "share_effect_mk": zero,
            "share_effect_rd": zero,
            "share": zero,
            "share_compressed": zero,

            "orders": zero,
            "sold": zero,
            "inventory": zero,
            "unfilled": zero,

            "goods_cost_sold": zero,
            "goods_cost_inventory": zero,

            "sales": zero,
            "inventory_charge": zero,
            "cost_before_tax": zero,
            "profit_before_tax": zero,
            "tax_charge": zero,
            "profit": zero,
            
            "tax_paid_to_period": None,
            "tax_paid_to_date": None,

            "balance": zero,
            "loan": zero,
            "cash": zero,
            "retern": zero,

            "average_price": None,

            "mpi_a": zero,
            "mpi_b": zero,
            "mpi_c": zero,
            "mpi_d": zero,
            "mpi_e": zero,
            "mpi_f": zero,
            "mpi": zero,
    
        },
       
    }
    i = 0
    while i < game["player_count"]:
        game["decisions"]["price"][i] = game["settings"]["demand_ref_price"]
        game["decisions"]["prod_rate"][i] = game["settings"]["prod_rate_initial"]
        game["decisions"]["mk"][i] = game["settings"]["demand_ref_mk"] / game["player_count"]
        game["decisions"]["ci"][i] = game["settings"]["initial_capital"] / game["player_count"] * game["settings"]["depreciation_rate"]
        game["decisions"]["rd"][i] = game["settings"]["demand_ref_rd"] / game["player_count"]
        
        game["data"]["capital"][i] = game["settings"]["initial_capital"] / game["player_count"]
        game["data"]["size"][i] = game["data"]["capital"][i] / game["settings"]["unit_fee"]
        game["data"]["history_mk"][i] = 0 #game["decisions"]["mk"][i]
        game["data"]["history_rd"][i] = 0 #game["decisions"]["rd"][i]
        
        game["data"]["inventory"][i] = 0
        game["data"]["goods_cost_inventory"][i] = 0

        game["data"]["loan"][i] = 0 #game["settings"]["initial_loan"] / game["player_count"]
        game["data"]["cash"][i] = game["settings"]["initial_cash"]
        game["data"]["retern"][i] = 0 #game["settings"]["mpi_retern_factor"]
                        
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
            
            
        #goooooooooooooooooooooooo! :)
        
        game["data"]["prod"][i] = game["decisions"]["prod_rate"][i] * game["data"]["size"][i]
        game["data"]["prod_over"][i] = game["decisions"]["prod_rate"][i] - game["settings"]["prod_rate_balanced"]
        
        prod_cost_factor_rate = game["data"]["prod_over"][i]
        
        if prod_cost_factor_rate > 0:
            prod_cost_factor_rate = game["settings"]["prod_cost_factor_rate_over"]
        else:
            prod_cost_factor_rate = game["settings"]["prod_cost_factor_rate_under"]
        
        
        game["data"]["prod_cost_unit"][i] = prod_cost_factor_rate * math.pow(game["data"]["prod_over"][i], game["settings"]["prod_rate_pow"]) + game["settings"]["prod_cost_factor_size"] * game["settings"]["initial_capital"] / game["data"]["capital"][i] / game["player_count"] + game["settings"]["prod_cost_factor_const"]
        
        game["data"]["prod_cost_marginal"][i] = prod_cost_factor_rate * game["settings"]["prod_rate_pow"] * game["decisions"]["prod_rate"][i] * math.pow(game["data"]["prod_over"][i], game["settings"]["prod_rate_pow"] - 1) + game["data"]["prod_cost_unit"][i]

        game["data"]["prod_cost"][i] = game["data"]["prod_cost_unit"][i] * game["data"]["prod"][i]
        
        game["data"]["goods"][i] = game["data"]["inventory"][i] + game["data"]["prod"][i] * game["delta"]
        game["data"]["goods_predicted"][i] = game["data"]["inventory"][i] + game["data"]["prod"][i]
        game["data"]["goods_cost"][i] = game["data"]["goods_cost_inventory"][i] + game["data"]["prod_cost"][i] * game["delta"]
        game["data"]["goods_cost_predicted"][i] = game["data"]["goods_cost_inventory"][i] + game["data"]["prod_cost"][i]
        game["data"]["goods_max_sales"][i] = game["decisions"]["price"][i] * game["data"]["goods_predicted"][i]
        
        game["data"]["depreciation"][i] = game["settings"]["depreciation_rate"] * game["data"]["capital"][i]
        game["data"]["capital"][i] += (game["decisions"]["ci"][i] - game["data"]["depreciation"][i])# * game["delta"]
        game["data"]["size"][i] = game["data"]["capital"][i] / game["settings"]["unit_fee"]
        
        game["data"]["spending"][i] = game["data"]["prod_cost"][i] + game["decisions"]["ci"][i] - game["data"]["depreciation"][i] + game["decisions"]["mk"][i] + game["decisions"]["rd"][i]
        game["data"]["balance_early"][i] = game["data"]["cash"][i] - game["data"]["loan"][i] - game["data"]["spending"][i] #* game["delta"]
        game["data"]["loan_early"][i] = max(-game["data"]["balance_early"][i], 0)
        
        
        
        game["data"]["interest"][i] = game["data"]["balance_early"][i]
        
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
        
    game["data"]["average_price_given"] = sum(game["decisions"]["price"]) / game["player_count"]
    game["data"]["average_price_planned"] = div(sum(game["data"]["goods_max_sales"]), sum(game["data"]["goods_predicted"]), game["data"]["average_price_given"])
    game["data"]["average_price_mixed"] = game["settings"]["demand_price"] * game["data"]["average_price_planned"] + (1 - game["settings"]["demand_price"]) * game["data"]["average_price"]
    
        
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
    game["data"]["orders_demand"] = game["settings"]["demand"] * (
        game["data"]["demand_effect_rd"] + game["data"]["demand_effect_mk"]
    )
        
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
        
        game["data"]["orders"][i] = round(game["data"]["orders_demand"] * game["data"]["share_compressed"][i])
        game["data"]["sold"][i] = min(game["data"]["orders"][i], game["data"]["goods"][i] / game["delta"])
        game["data"]["inventory"][i] = game["data"]["goods"][i] - game["data"]["sold"][i] * game["delta"]
        game["data"]["unfilled"][i] = game["data"]["orders"][i] - game["data"]["sold"][i]
        
        #goods
        
        game["data"]["goods_cost_sold"][i] = game["data"]["goods_cost"][i] * div(
            game["data"]["sold"][i],
            game["data"]["goods"][i],
            0
        )
        game["data"]["goods_cost_inventory"][i] = game["data"]["goods_cost"][i] - game["data"]["goods_cost_sold"][i] * game["delta"]
        
        #cash Flow
        
        game["data"]["sales"][i] = game["decisions"]["price"][i] * game["data"]["sold"][i]
        
        game["data"]["inventory_charge"][i] = game["settings"]["inventory_fee"] * min(
            game["data"]["inventory"][i],
            game["data"]["inventory"][i]
        )
        
        game["data"]["cost_before_tax"][i] = game["data"]["goods_cost_sold"][i] + game["data"]["depreciation"][i] + game["decisions"]["mk"][i] + game["decisions"]["rd"][i] - game["data"]["interest"][i] + game["data"]["inventory_charge"][i]
        game["data"]["profit_before_tax"][i] = game["data"]["sales"][i] - game["data"]["cost_before_tax"][i]
        game["data"]["tax_charge"][i] = game["settings"]["tax_rate"] * game["data"]["profit_before_tax"][i]
        game["data"]["profit"][i] = round(game["data"]["profit_before_tax"][i] - game["data"]["tax_charge"][i], 2)
        
        game["data"]["balance"][i] = game["data"]["balance_early"][i] + game["data"]["loan_early"][i] + game["data"]["sales"][i] - game["data"]["depreciation"][i] + game["data"]["interest"][i] - game["data"]["inventory_charge"][i] - game["data"]["tax_charge"][i] #game["data"]["cash"][i] - game["data"]["loan"][i] + game["data"]["loan_early"][i] + game["data"]["profit"][i] - game["decisions"]["ci"][i] + game["data"]["depreciation"][i] + game["data"]["goods_cost_sold"][i] - game["data"]["prod_cost"][i]
        
        game["data"]["loan"][i] = max(game["data"]["loan_early"][i], game["data"]["loan_early"][i] - game["data"]["balance"][i])
        game["data"]["cash"][i] = max(game["data"]["balance"][i], 0)
        game["data"]["retern"][i] += game["data"]["profit"][i] #* game["delta"]
        
        # :)
        game["data"]["margin_unit_sold"][i] = round(game["data"]["profit"][i] / game["data"]["sold"][i], 2)
        game["data"]["total_cost_unit_sold"][i] = round(game["decisions"]["price"][i] - game["data"]["margin_unit_sold"][i], 2)
        
        game["data"]["tax_paid_to_period"] = round(sum(game["data"]["tax_charge"]))
        game["data"]["tax_paid_to_date"] += game["data"]["tax_paid_to_period"]
    
    each(fun_3)
    
    game["data"]["average_price"] = div(
        sum(game["data"]["sales"]),
        sum(game["data"]["sold"]),
        game["data"]["average_price_given"]
    )
    sum_size = sum(game["data"]["size"])
    sum_sold = sum(game["data"]["sold"])
    
    
    def fun_4(i):
        game["data"]["mpi_a"][i] = game["settings"]["mpi_factor_a"] * game["player_count"] * (
            game["data"]["retern"][i] / game["now_tick"] / game["settings"]["mpi_retern_factor"]
        )
        game["data"]["mpi_b"][i] = game["settings"]["mpi_factor_b"] * game["player_count"] * (
            (game["data"]["history_rd"][i] + game["data"]["history_mk"][i]) / (sum_history_rd + sum_history_mk)
        )
        game["data"]["mpi_c"][i] = game["settings"]["mpi_factor_c"] * game["player_count"] * (
            game["data"]["size"][i] / sum_size
        )
        game["data"]["mpi_d"][i] = game["settings"]["mpi_factor_d"] * (
            1 - abs(game["data"]["prod_over"][i])
        )
        game["data"]["mpi_e"][i] = game["settings"]["mpi_factor_e"] * game["player_count"] * (
            div(
                game["data"]["sold"][i],
                sum_sold,
                0
            )
        )
        
    
        game["data"]["mpi_f"][i] = game["settings"]["mpi_factor_f"]
        
        game["data"]["mpi"][i] = round(game["data"]["mpi_a"][i] + game["data"]["mpi_b"][i] + game["data"]["mpi_c"][i] + game["data"]["mpi_d"][i] + game["data"]["mpi_e"][i] + game["data"]["mpi_f"][i])
    each(fun_4)

    return game

#by Karton4ik