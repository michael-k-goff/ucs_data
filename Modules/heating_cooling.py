# Heating and cooling calculations and figure.

import helper

# Estimate of cost and benefit of requiring heat pump water heaters in North Carolina.

# From https://www.sciencedirect.com/science/article/abs/pii/S0301421520308247
cost = 29.5 # Millions of dollars
energy_savings = 108.7 # Millions of dollars
co2_reduction = 441000 # Metrics tons
co2_price = 50 # Dollars per ton. Can vary this
co2_savings = co2_reduction * co2_price

hp_table = [
    ["<b>Cost/Benefit</b>","<b>Value, millions of dollars</b>"],
    ["<b>Increased Construction Cost</b>",cost],
    ["<b>Energy Savings</b>",energy_savings],
    ["<b>CO<sub>2</sub> Savings</b>",co2_savings / 10**6]
]

helper.save_image({
    "filename":"nc_hp_mandate.jpg",
    "status":"Done",
    "details":"Costs and benefits of mandating heat pumps in new residential construction in North Carolina. A larger value is reported by factoring in rebates from utilities to customers, but I am not going with that figure.",
    "table":hp_table,
    "references":["nc_hp"],
    "source_file":"heating_cooling.py"
})