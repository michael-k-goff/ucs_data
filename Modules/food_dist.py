# Food distribution calculations

import helper

########################################## World GHG in food distribution system

# From https://science.sciencemag.org/content/360/6392/987, poore
# See the Supplemental spreadsheet, Results - Global Totals tab. For each GHG column, take the dot product of the vector of column B and columns F-L respectively.
ghg_table = [
    ["<b>Category</b>","<b>World emissions: thousands of tons CO<sub>2</sub>e per year</b>"],
    ["Land Use Change",2379470],
    ["Feed",1098395],
    ["Farming operations",7463342],
    ["Processing",604298],
    ["Transportation",801404],
    ["Packaging",626871],
    ["Retail",394203],
    ["Cookstoves",1100000] # cookstoves. Abstract says 1.0 to 1.2 billion tons.
]

helper.save_image({
    "filename":"world_food_ghg.jpg",
    "status":"Done",
    "table":ghg_table,
    "references":["cookstoves","poore"],
    "details":"Greenhouse gas emissions from various points in the food system. The Cookstoves value was taken from Bailis et al. (median of the 1.0 to 1.2 billion tons CO2 they give), and the rest are from Poore and Nemecek. Cookstoves refer to stoves with traditional biomass cooking fuel and not modern cooking, so that is not a full accounting of emissions from cooking, but it was all I could find readily.",
    "source_file":"food_dist.py"
})

########################################

# Food waste statistics
# Copying the tables in Annex 4 of http://www.fao.org/3/mb060e/mb060e.pdf
# See Figure 1, p. 4 for production volumes

production_volumes = {
    "Europe":{
        "Cereals":405,
        "Roots and tubers":160,
        "Oilcrops and pulses":55,
        "Fruits and vegetables":205,
        "Meat":50,
        "Fish":15,
        "Dairy":230
    },
    "North America, Oceania":{
        "Cereals":490,
        "Roots and tubers":30,
        "Oilcrops and pulses":105,
        "Fruits and vegetables":90,
        "Meat":50,
        "Fish":10,
        "Dairy":120
    },
    "Industrialized Asia":{
        "Cereals":485,
        "Roots and tubers":185,
        "Oilcrops and pulses":60,
        "Fruits and vegetables":630,
        "Meat":75,
        "Fish":55,
        "Dairy":85
    },
    "Sub-Saharan Africa":{
        "Cereals":105,
        "Roots and tubers":205,
        "Oilcrops and pulses":25,
        "Fruits and vegetables":90,
        "Meat":10,
        "Fish":5,
        "Dairy":20
    },
    "North Africa, West and Central Asia":{
        "Cereals":110,
        "Roots and tubers":15,
        "Oilcrops and pulses":15,
        "Fruits and vegetables":140,
        "Meat":10,
        "Fish":5,
        "Dairy":40
    },
    "South and Southeast Asia":{
        "Cereals":615,
        "Roots and tubers":120,
        "Oilcrops and pulses":140,
        "Fruits and vegetables":305,
        "Meat":25,
        "Fish":30,
        "Dairy":170
    },
    "Latin America":{
        "Cereals":185,
        "Roots and tubers":65,
        "Oilcrops and pulses":140,
        "Fruits and vegetables":185,
        "Meat":40,
        "Fish":20,
        "Dairy":80
    }
}

# See Annex 4
# Each loss rate is an array, arranged as [Agricultural production, postharvest handling and storage, processing and packaging, distribution, consumption]
# All numbers are percentage loss rates at that step (so over multiply steps, multiply the surviving portion.)
# For packaging and processing, when there are two numbers, I assume they are additive
loss_rates = {
    "Europe":{
        "Cereals":[2,4,0.5+10,2,25],
        "Roots and tubers":[20,9,15,7,17],
        "Oilcrops and pulses":[10,1,5,1,4],
        "Fruits and vegetables":[20,5,2,10,19],
        "Meat":[3.1,0.7,5,4,11],
        "Fish":[9.4,0.5,6,9,11],
        "Dairy":[3.5,0.5,1.2,0.5,7]
    },
    "North America, Oceania":{
        "Cereals":[2,2,0.5+10,2,27],
        "Roots and tubers":[20,10,15,7,30],
        "Oilcrops and pulses":[12,0,5,1,4],
        "Fruits and vegetables":[20,4,2,12,28],
        "Meat":[3.5,1,5,4,11],
        "Fish":[12,0.5,6,9,33],
        "Dairy":[3.5,0.5,1.2,0.5,15]
    },
    "Industrialized Asia":{
        "Cereals":[2,10,0.5+10,2,20],
        "Roots and tubers":[20,7,15,9,10],
        "Oilcrops and pulses":[6,3,5,1,4],
        "Fruits and vegetables":[10,8,2,8,15],
        "Meat":[2.9,0.6,5,6,8],
        "Fish":[15,2,6,11,8],
        "Dairy":[3.5,1,1.2,0.5,5]
    },
    "Sub-Saharan Africa":{
        "Cereals":[6,8,3.5,2,1],
        "Roots and tubers":[14,18,15,5,2],
        "Oilcrops and pulses":[12,8,8,2,1],
        "Fruits and vegetables":[10,9,25,7,5],
        "Meat":[15,0.7,5,7,2],
        "Fish":[5.7,6,9,15,2],
        "Dairy":[6,11,0.1,10,0.1]
    },
    "North Africa, West and Central Asia":{
        "Cereals":[6,8,2+7,4,12],
        "Roots and tubers":[6,10,12,4,6],
        "Oilcrops and pulses":[17,10,20,15,12],
        "Fruits and vegetables":[17,10,20,15,12],
        "Meat":[6.6,0.2,5,5,8],
        "Fish":[6.6,5,9,10,4],
        "Dairy":[3.5,6,2,8,2]
    },
    "South and Southeast Asia":{
        "Cereals":[6,7,3.5,2,3],
        "Roots and tubers":[6,19,10,11,3],
        "Oilcrops and pulses":[7,12,8,2,1],
        "Fruits and vegetables":[15,9,25,10,7],
        "Meat":[5.1,0.3,5,7,4],
        "Fish":[8.2,6,9,15,2],
        "Dairy":[3.5,6,2,10,1]
    },
    "Latin America":{
        "Cereals":[6,4,2+7,4,10],
        "Roots and tubers":[14,14,12,3,4],
        "Oilcrops and pulses":[6,3,8,2,2],
        "Fruits and vegetables":[20,10,20,12,10],
        "Meat":[5.3,1.1,5,5,6],
        "Fish":[5.7,5,9,10,4],
        "Dairy":[3.5,6,2,8,4]
    }
}

# Combined loss rates by region
loss_rates_mult = {}
for reg in loss_rates:
    loss_rates_mult[reg] = {}
    for crop in loss_rates[reg]:
        loss_rates_mult[reg][crop] = 1-(1-loss_rates[reg][crop][0]/100.)*(1-loss_rates[reg][crop][1]/100.)*(1-loss_rates[reg][crop][2]/100.)*(1-loss_rates[reg][crop][3]/100.)*(1-loss_rates[reg][crop][4]/100.)

# By region
loss_by_region = {}
for key in loss_rates_mult:
    loss_by_region[key] = sum([loss_rates_mult[key][crop]*production_volumes[key][crop] for crop in loss_rates_mult[key]]) / sum([production_volumes[key][crop] for crop in production_volumes[key]])
loss_by_region["World"] = sum([loss_by_region[key]*sum([production_volumes[key][crop] for crop in production_volumes[key]]) for key in loss_by_region]) / sum([sum([production_volumes[key][crop] for crop in production_volumes[key]]) for key in production_volumes])

# By crop family
loss_by_crop = {}
for crop in loss_rates_mult["Europe"]:
    loss_by_crop[crop] = sum([loss_rates_mult[key][crop]*production_volumes[key][crop] for key in loss_rates_mult]) / sum([production_volumes[key][crop] for key in loss_rates_mult])

# By phase
loss_by_phase = [0,0,0,0,0]
for i in range(5):
    loss_by_region_i = {key:sum([(1-loss_rates[key][crop][i]/100.)*production_volumes[key][crop] for crop in loss_rates_mult[key]]) / sum([production_volumes[key][crop] for crop in production_volumes[key]]) for key in loss_rates}
    loss_by_phase[i] = 1-sum([loss_by_region_i[key]*sum([production_volumes[key][crop] for crop in production_volumes[key]]) for key in loss_by_region_i]) / sum([sum([production_volumes[key][crop] for crop in production_volumes[key]]) for key in production_volumes])

loss_table = [
    ["<b>Region</b>","<b>Loss rate</b>"]
]
for key in loss_by_region:
    loss_table = loss_table + [[key,loss_by_region[key]]]
loss_table = loss_table + [["<b>Crop</b>","<b>Loss rate</b>"]]
for key in loss_by_crop:
    loss_table = loss_table + [[key,loss_by_crop[key]]]
loss_table = loss_table + [["<b>Production phase</b>","<b>Loss rate</b>"],["Agricultural production",loss_by_phase[0]],["Postharvest handling and storage",loss_by_phase[1]],["Processing and packaging",loss_by_phase[2]],["Distribution",loss_by_phase[3]],["Consumption",loss_by_phase[4]]]

helper.save_image({
    "filename":"food_loss.jpg",
    "status":"Done",
    "details":"Three bar plots for the price of one here. Show food losses by world region, by crop family, and by phase of production. Rates are presented as decimals (e.g. 0.12 means 12% loss). For phase of production, rates are compounding. This means, for instance, if there is a 0.1 loss at each of the five phases, the total loss is about 0.41. Losses are measured by mass, and I didn't make any attempt to weight crops by monetary value. Values are estimated as of 2007 and are not very reliable, but it was the best I could find. When setting up the bar plot, keep the phase of production bars in the order shown here, since this is the correct sequential order.",
    "references":["food_loss"],
    "table":loss_table,
    "source_file":"food_dist.py"
})

########################################

# Overeating. From 'overeat'

# For total production, go to Food Balances, 2013 and add up totals for all commodities (it won't give grand total for whatever reason).
overall_food = 1029.021+443.353+32.246+172.912+50.467+16.408+51.909+79.593+982.974+544.877+18.778+8.73+260.697+302.411+15.67+23.232+64.332+629.745+132.829+15.562+0.768
overeat_table = [
    ["<b>Metric</b>","<b>Impact of Overeating</b>","<b>Share of Total Agriculture</b>"],
    ["By mass","140.7 million tons",140.7/overall_food],
    ["Land use","3784918 square km",(3784918)/(32664228.335+17365981.086+1989105.844)], # See land use plot. See also, faostat.
    ["Greenhouse gases","239,408 thousand tons",239408/(2100076.4158+3151071+1407707+882859+704442+533245+313201+223915+127890)],
    ["Water consumption","343.316 cubic km",(343.316/(0.7*(3600*0.6+5400*0.4)))] # Based on facts_trends. May revise
]

helper.save_image({
    "filename":"overeat.jpg",
    "status":"Done",
    "details":"Show impacts of overeating, per year. That is, food consumed in excess of recommended intake. Impacts are shown in absolute terms and as share of world agriculture impacts. Overeating figures come from Toti et al. Total land use and GHG figures from the ever-reliable FAOSTAT. Total water from the WBCSD report, though that is outdated and I may replace it later as I review the water material. Toti et al. had some unit conversion mistakes in their original version, so hopefully I've been able to clear them up here. They also don't make it clear how they measure land, water, and GHG impacts, and their measurements might not be the same as how I got overall figures.",
    "table":overeat_table,
    "references":["faostat","overeat","facts_trends"],
    "source_file":"food_dist.py"
})