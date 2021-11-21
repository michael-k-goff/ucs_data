# Consumerism

import helper

green_consumerism_table = [
    ["<b>Product</b>","<b>2001</b>","<b>2002</b>","<b>2003</b>","<b>2004</b>","<b>2005</b>","<b>2006</b>","<b>2007</b>","<b>2008</b>","<b>2009</b>","<b>2010</b>","<b>2011</b>"],
    ["Organic Food","1.4","1.6","1.9","2.2","2.5","2.9","3.2","3.6","3.7","4.0","4.2"],
    ["Organic Non-Food","","","0.1","0.2","0.2","0.3","0.3","0.4","0.5","0.5","0.6"],
    ["Green Buildings","","","","","1.74","","","11.79","","30.72","38.03"],
    ["Social Responsible Investing","11.7","","11.3","","9.4","","10.8","","","12.2",""],
    ["Renewable Energy","0.58","0.66","0.77","0.87","0.98","1.24","1.56","2.23","2.76","3.21","3.67"],
    ["Hybrid Vehicle Sales","0.1","0.2","0.3","0.6","1.4","1.8","2.5","2.4","2.8","2.4","2.1"],
    ["Fair Trade Food","","9.8","19.5","33.9","46.1","67.2","69.4","93.0","112.4","111.4","151.9"]
]


for i in range(2,len(green_consumerism_table[0])):
    green_consumerism_table[-1][i] = str(float(green_consumerism_table[-1][i]) * 0.453592)

helper.save_image({
    "filename":"green_consumerism.jpg",
    "status":"Not Done",
    "details":"Some figures on how options marketed as environmentally or socially responsible fare as a percentage of overall demand for the given produced in the US. For example, from 2001-2011, organic food range from 1.4% to 4.2% of total food sales in the US. The exception is fair trade, where I don't have good percentages (the values seemed to get cut off in the paper, and I'm not sure what the proper baseline total is to use derived from other sources), so for that the figures are total US sales in millions of kilograms.",
    "table":green_consumerism_table,
    "references":["green_consumerism"],
    "source_file":"consumerism.py"
})

#######################################

# Breakdown of US economy

us_economy_table = [
    ["<b>Spending Area</b>","<b>Explanation</b>","<b>Share of US GDP, 2019</b>","<b>Value in 2019, trillions</b>"],
    ["Durable Goods","Cars, furniture, large appliances, etc.",1.77,""],
    ["Non-Durable Goods","Food, fuel, clothing, etc.",3.01,""],
    ["Services","Banking, health care, education, etc.",8.56,""],
    ["Business Investment - Real Estate","Commercial and residential real estate for business purposes",0.54+0.59,""],
    ["Business Investment - Capital Goods","",1.27,""],
    ["Business Investment - Intellectual","Mostly software",0.97,""],
    ["Business Investment - Change in Inventory","",0.07,""],
    ["Exports","Adds to total GDP",2.53,""],
    ["Imports","Subtracts from total GDP",3.49,""],
    ["Federal Spending, Defense","",0.77,""],
    ["Federal Spending, except Defense","",1.28-0.77,""],
    ["State and Local Governments","",2.02,""],
    ["Total GDP","",19.07,""]
]

total_gdp = 19.07

for i in range(1,len(us_economy_table)):
    us_economy_table[i][3] = us_economy_table[i][2]
    us_economy_table[i][2] /= total_gdp

    
helper.save_image({
    "filename":"us_gdp_breakdown.jpg",
    "status":"Done",
    "details":"Breakdown of US GDP in 2019.",
    "references":["amadeo"],
    "table":us_economy_table,
    "source_file":"consumerism.py"
})