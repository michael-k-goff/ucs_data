# Plots related to ecosystem services

import helper

urban_table = [
    ["<b>Biome</b>","<b>Hectares Developed into Urban Land, 1973-1980</b>","<b>1980-1986</b>","<b>1986-1992</b>","<b>1992-2000</b>","<b>Total</b>"],
    ["Forest",347100,314800,466700,708500],
    ["Grassland/Shrubland",161000,107700,192500,203200],
    ["Agriculture",542200,427100,610000,1146000],
    ["Wetland",93700,0,0,0]
]

for i in range(1,len(urban_table)):
    urban_table[i].append( sum(urban_table[i][1:5]) )
    
helper.save_image({
    "filename":"urban_esv.jpg",
    "status":"Not Done",
    "details":"Figures from the USGS on how much land, of which biomes, have been converted into cities from 1973-2000 in the United States. They also give 1973-2000 totals, but they are not equal to the sums of the values for the four time periods. I am going with the latter for this plot.",
    "table":urban_table,
    "references":["usgs_esv"],
    "source_file":"ecosystem_services.py"
})

urban_esv_vale_table = [
    ["<b>Biome</b>","<b>Value, USD/hectare</b>"],
    ["Grassland",254],
    ["Cultivated Areas",513],
    ["Woodland and Shrubland",374],
    ["Temperate Forests",1113],
    ["Wetlands (United States)",4965]
]

helper.save_image({
    "filename":"urban_esv_value.jpg",
    "status":"Done",
    "details":"ESV value of lands that are relevant for urban conversion. This material may be duplicated in part as we build out ESV material elsewhere on the site.",
    "table":urban_esv_vale_table,
    "references":["esvd"],
    "source_file":"ecosystem_services.py"
})

valuation = { # Dollars per hectares
    "Forest":1113,
    "Grassland/Shrubland":(254+374)/2., # Average of 'Grassland' and 'Woodland and Shrubland' biomes.
    "Agriculture":513,
    "Wetland":4965
}
hectares = {
    "Forest":urban_table[1][5],
    "Grassland/Shrubland":urban_table[2][5], 
    "Agriculture":urban_table[3][5],
    "Wetland":urban_table[4][5]
}

total_hectares = sum([hectares[key] for key in hectares])
#print("Total hectares converted: " + str(total_hectares))

total_valuation = sum([hectares[key]*valuation[key] for key in hectares])
#print("Total valuation: " + str(total_valuation))

#print("Weighted average of valuation (dollars per hectares): " + str(total_valuation/total_hectares))
# 0.1011714
#print("Valuation on a 1/4 acres lot: "+str(total_valuation/total_hectares*0.1011714))

############################

# Acres that have been converted to farmland in the US from 1973-2000
ag_table = [
    ["<b>Biome</b>","<b>Hectares Converted, 1973-2000, Low Estimate</b>","<b>Median Estimate</b>","<b>High Estimate</b>"],
    ["Water",-1400,4400,10200],
    ["Mining",-3200,4300+13900,8800+30800],
    ["Barren",-300,400,1100],
    ["Forest",375800+229700+111000+131000,1693900,1127100+760100+341000+312400],
    ["Grassland/Shrubland",1527500+808100+532900+1426900,8058200, 3895500+2711300+1610700+3603500],
    ["Wetland",49700-6500+14700-500,194500, 193900+79300+41300+17100]
]

helper.save_image({
    "filename":"ag_esv.jpg",
    "status":"Not Done",
    "table":ag_table,
    "details":"Very similar to urban_esv, including the fact that I am adding the values for four separate time periods rather than using the total, which is a bit different.",
    "references":["usgs_esv"],
    "source_file":"ecosystem_services.py"
})

ag_esv_gain_table = [
    ["<b>Biome</b>","<b>Gain or loss from converting (millions of USD), 1973-2000, Low Estimate</b>","<b>Median Estimate</b>","<b>High Estimate</b>"]
]

total_gain = 0
totals = [0,0,0]
for i in range(4,7):
    new_row = ["",0,0,0]
    ecosystem = ag_table[i][0]
    new_row[0] = ecosystem
    new_row[1] = ag_table[i][1]*(valuation["Agriculture"]-valuation[ecosystem]) / 10**6
    totals[0] += new_row[1]
    new_row[2] = ag_table[i][2]*(valuation["Agriculture"]-valuation[ecosystem]) / 10**6
    totals[1] += new_row[2]
    new_row[3] = ag_table[i][3]*(valuation["Agriculture"]-valuation[ecosystem]) / 10**6
    totals[2] += new_row[3]
    ag_esv_gain_table.append(new_row)
ag_esv_gain_table.append(["Total",totals[0],totals[1],totals[2]])

helper.save_image({
    "filename":"ag_total_esv.jpg",
    "status":"Not Done",
    "table":ag_esv_gain_table,
    "details":"The total gain or loss of ecosystem service values for the conversion of various biomes into agriculture. No source information because this is shown in other graphics. The low and high estimates are the lows and highs of land conversion, not necessarily of monetary value. Positive values show a gain of ecosystem service value and negative values indicate a loss.",
    "references":[],
    "source_file":"ecosystem_services.py"
})