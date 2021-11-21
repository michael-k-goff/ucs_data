# Energy in agriculture

import helper
import primary_energy_factors

# For energy intensity of pesticides, see Estimation_of....pdf in the Energy in Agriculture folder.
# See the Bennetzen paper for energy intensity of fertilizers.
# FAO for fertilizer and pesticide usage data.

# http://www.fao.org/faostat/en/#data/GN
# World + (Total), Consumption in Agriculture, all Items, year 2012
# Values are in TJ
direct_energy_use = {
    "Diesel": 4520246, # Gas-diesel oil
    "Gasoline": 392055 + 287935.783, # Crops + fisheries
    "Natural Gas (Buildings)": 389618, # Not sure if "buildings" is right, but at least it's gas.
    "LPG": 145163.7,
    "Fuel Oil":61852.4 + 32271.6412, # Crops + fisheries 
    "Coal":1008934.8,
    "Electricity":1843016.4 # Crops + irrigation. FAO doesn't specificy what kind of energy is used in irrigation, so I am guessing electricity
}

pf = primary_energy_factors.primary_factors # Cite 'energycode' for primary energy conversion.
pf["LPG"] = 1.05

direct_energy = sum([direct_energy_use[key]*pf[key] / 10**6 for key in direct_energy_use])
machine_energy = sum([direct_energy_use[key]*0.4 / 10**6 for key in direct_energy_use]) # The 40% is from Bennetzen, which in turn is from Woods.
# Also in the Energy FAOSTAT data set.
irrigation_energy = 358767.3881 * pf["Electricity"] / 10**6

pesticide_usage = 4113591.25 # Tons. See http://www.fao.org/faostat/en/#data/RP, world total, 2017.
pesticide_energy = pesticide_usage * 370. / 10**9 # Estimation_of....pdf, 370 MJ/kg for pesticides overall.

fertilizer_usage = {
    "N":109137240.84,
    "P":45451398.29,
    "K":37635817.93
} # http://www.fao.org/faostat/en/#data/RFN, 2017
fertilizer_enf = {
    "N":0.065,
    "P":0.009,
    "K":0.006
} # From Bennetzen, TJ/ton
fertilizer_energy = sum([fertilizer_usage[key]*fertilizer_enf[key] / 10**6 for key in fertilizer_usage])

draft_animals = 193821180 # From http://ricestat.irri.org:8080/wrsv3/entrypoint.htm
# Select Continent/Region from the Geographic Extent dropdown. Figure is 2013, the most recent available.
animal_energy = draft_animals * 0.00365 / 10**6 # Conversion from Bennetzen.

table = [
    ["<b>Purposes</b>","<b>Energy consumption, EJ/year</b>"],
    ["Direct energy usage",direct_energy],
    ["Manufacture of equipment and buildings",machine_energy],
    ["Irrigation",irrigation_energy],
    ["Fertilizers",fertilizer_energy],
    ["Pesticides",pesticide_energy],
    ["Animal traction",animal_energy]
]

helper.save_image({
    "filename":"energy_in_ag.jpg",
    "status":"Done",
    "table":table,
    "details":"World energy usage in agriculture, in EJ per year. See the caption in the Environmental Impacts of Agriculture section for details on where these numbers came from.",
    "references":["faostat","energycode","bennetzen","audsley","irri"],
    "source_file":"energy_in_ag.py"
})

#########################################

# US food system. Pulling the figures from ag_energy_system that were already on the site.

# From RECS, energy for food-related purposes, residential
us_electricity = {
    "refrigeration":88.7+20.5, # Billions of kWh, refrigeration and freezing
    "cooking":18.1+13.8, # Cooking + microwave
    "dishwasher":7.2
}
us_gas_propane = {
    "cooking":113+94 # Trillions of BTU
}
us_commercial_cooking = 517 # CBECS. Trillions of BTU. In 2012
us_food_energy = {
    "refrigeration":us_electricity["refrigeration"]*3.6,
    "cooking":us_electricity["refrigeration"]*3.6 + us_gas_propane["cooking"]*1.055,
    "dishwasher":us_electricity["dishwasher"]*3.6
}
us_final_consumption_2012 = 60552.
us_final_consumption_2015 = 63287. # PJ, 2015. See IEA Sankey Diagram.
us_home_share = sum([us_food_energy[key] for key in us_food_energy]) / us_final_consumption_2015 + us_commercial_cooking*1.055/us_final_consumption_2012

us_table = [
    ["<b>Food sector</b>","<b>Share of total US energy consumption</b>"],
    ["Crop production (direct, fertilizer, pesticide)",str(15.7*0.24)+"%"],
    ["Food processing",str(15.7*0.32)+"%"],
    ["Packaging",str(15.7*0.10)+"%"],
    ["Freight",str(15.7*0.06)+"%"],
    ["Wholesale and retail",str(15.7*0.28)+"%"],
    ["Home usage (refrigeration, cooking, dishwasher) and commercial cooking",str(100*us_home_share)+"%"]
]

helper.save_image({
    "filename":"us_food_system.jpg",
    "status":"Done",
    "table":us_table,
    "details":"Energy in the US food system. These percentages are shares of entire US energy consumption. See the caption in the Environmental Impacts of Agriculture section for explanations of where the numbers come from.",
    "references":["ag_energy_system","iea_sankey","recs","cbecs"],
    "source_file":"energy_in_ag.py"
})