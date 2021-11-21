# Overall energy plots

import helper

#######################################################################

# World energy forecast

# Initially in quads; convert to EJ
energy_forecast_table = [
    ["<b>Date</b>","<b>World Energy Demand, EJ</b>"],
    ["2010",537.5],
    ["2020",635.0],
    ["2030",705.2],
    ["2040",794.9],
    ["2050",910.7]
]

for i in range(1,len(energy_forecast_table)):
    energy_forecast_table[i][1] *= 1.05506
    
helper.save_image({
    "filename":"energy_forecast.jpg",
    "status":"On Hold",
    "details":"Maybe a god summary plot, but since the draft of the Energy Priorities section on which it was to appear has been scrapped, it is now homeless. World energy forecast. This is the EIA's 2019 forecast; the 2010 value is historical and the rest are forecasts obviously. This plot appears in the Energy Priorites page.",
    "table":energy_forecast_table,
    "references":["ieo2019"],
    "source_file":"energy.py"
})

#######################################################################

# Energy efficiency potential

energy_efficiency_table = [
    ["<b>Tool</b>","<b>Potential Energy Savings, EJ/year</b>"],
    ["Compact Development","190"],
    ["Best Practices for Major Commodities","21.512253978370514"],
    ["New Technology for Major Commodities","32.86396398254263"],
    ["100% Recycling of Municipal Solid Waste","10.236056633873275"],
    ["Efficient Steam and Motor Systems","17.3394988-26.8278308"],
    ["Improve Material Efficiency","15.32104355416269"],
    ["Passenger Car Fuel Economy","19.17707801333333"],
    ["Convert All Cars to Electric","28.656492543916247"],
    ["Efficiency in Trucking, Shipping, and Aviation","10.003"]
]

helper.save_image({
    "filename":"efficiency_estimate.jpg",
    "status":"On Hold",
    "details":"This was planned for the now-scrapped previous draft of the Energy Priorities section. It probably will not reappear in anything resembling the form here described, but I am leaving it up for now.<br><br>We won't include source information here and instead refer the reader to the sections were we discuss these tools in more detail. Two notes here: first, as the Compact Cities entry towers over the rest, that number should be subjected to greater scrutiny. It is based on a single paper, and I'm not sure I fully trust it. I want to perhaps do some of my own independent calculations on the topic, analogous to what I did for US compact city growth a while back. Second, there are other important urban energy efficiency measures (e.g. LED lighting, building enveloped) for which we have US figures but not world figures. If I can get those, they should be added here. For now, this is the version we will go with.",
    "table":energy_efficiency_table,
    "references":[],
    "source_file":"energy.py"
})

#######################################################################

# World energy in one picture, based on the IEA Sankey Diagrams.
# Yes, we are working through the numbers again.
# Figures are all as of 2017.

# End uses
pef = {
    "Oil Products":181.025/177.486
}
# In the following, oil products in agriculture, forestry, and fishing is transfered from other_heat to transportation_fuel
transportation_fuel = {
    "Oil Products":108.376+4.481,
    "Natural Gas":4.384,
    "Biomass and Biofuels":3.500,
    "Coal":0.003
}
industrial_heat = {
    "Oil":0.245,
    "Oil Products":13.187,
    "Coal":34.232,
    "Natural Gas":23.764,
    "Biomass and Biofuels":8.671,
    "Geothermal":0.024,
    "Heat":5.764
}
other_heat = {
    "Oil":0.001,
    "Oil Products":18.137-4.481,
    "Coal":6.352,
    "Natural Gas":26.966,
    "Biomass and Biofuels":31.278,
    "Geothermal":0.544,
    "Wind/Solar/Ocean":1.311,
    "Heat":6.357
}
electricity = { # Input
    "Oil Products":7.733,
    "Heat":222.461-7.733 # Everything but oil products, which should come in primary form
}
feedstock = {
    "Oil Products":26.524,
    "Heat":36.791-26.524 # Everything else is primary
}

# Sectoral energy
industry = { # Industry + non-energy industry
    "Oil Products":13.187 + 24.631,
    "Electricity":32.201,
    "Heat":118.088-13.187-32.201 + 34.886-24.631
}
transportation = { # Transportation + non-energy in transportation
    "Oil Products":108.376+0.461,
    "Electricity":1.309,
    "Heat":117.572-108.376-1.309
}
residential = {
    "Oil Products":8.991,
    "Electricity":20.791,
    "Heat":86.427-8.991-20.791
}
commercial = {
    "Oil Products":3.554,
    "Electricity":16.694,
    "Heat":32.847-3.554-10.694
}
ag = { # Ag + Fishing
    "Oil Products":4.481+0.257,
    "Electricity":2.31+0.027,
    "Heat":8.579-4.481-2.31
}
other = { # Other energy + Other non-energy
    "Oil Products":0.863+1.431,
    "Electricity":3.606,
    "Heat":6.228-0.863-3.606+0.012
}

def secondary_to_primary(secondary):
    total = 0
    for key in secondary:
        if key in pef:
            total += secondary[key]*pef[key]
        else:
            total += secondary[key]
    return total
pef["Electricity"] = secondary_to_primary(electricity) / 76.938

sankey_table = [
    ["<b>Source</b>","<b>Annual primary production, EJ</b>"], #
    ["Oil",187.452],
    ["Coal",157.986],
    ["Natural Gas",132.424],
    ["Biomass and Biofuels",55.438],
    ["Geothermal",3.595],
    ["Wind/Solar/Ocean",7.158],
    ["Hydro",14.697],
    ["Nuclear",28.783],
    ["<b>Energy Form</b>","Annual primary energy demand, EJ"],
    ["Electricity",secondary_to_primary(electricity)],
    ["Transportation Fuel",secondary_to_primary(transportation_fuel)],
    ["Industrial Heat",secondary_to_primary(industrial_heat)],
    ["Nonindustrial Heat",secondary_to_primary(other_heat)],
    ["Feedstock",secondary_to_primary(feedstock)],
    ["<b>Energy By End Use</b>","Annual primary energy demand, EJ"],
    ["Industry",secondary_to_primary(industry)],
    ["Transportation",secondary_to_primary(transportation)],
    ["Residential",secondary_to_primary(residential)],
    ["Commercial and Public Services",secondary_to_primary(commercial)],
    ["Agriculture, Forestry, Fishing",secondary_to_primary(ag)],
    ["Other",secondary_to_primary(other)]
]

helper.save_image({
    "filename":"energy_demand.jpg",
    "status":"On Hold",
    "table":sankey_table,
    "details":"World primary energy by source, form, and end use sector. The sums of each of the three categories should be roughly equal but are not exactly equal due to whatever statistical issues are going on in the IEA figures. I think this is a good summary plot of world energy demand, but due to the scrapping of the previous draft of the Energy Priorities section, it doesn't have a home right now.",
    "references":["iea_sankey"],
    "source_file":"energy.py"
})

####################### Plots for the Future Energy Demand subsection of the Population, Energy, and Emissions page

energy_change_table = [
    ["<b>Energy Source</b>","<b>Change, 2019-20</b>"],
    ["Coal","-6.7%"],
    ["Natural Gas","-3.3%"],
    ["Oil","-8.5%"],
    ["Nuclear","-4.5%"],
    ["Renewables","+0.9%"],
    ["Total Energy Demand","-5.3%"],
    ["CO<sub>2</sub> Emissions","-6.6%"],
    ["Energy Investment","-18.3%"]
]

helper.save_image({
    "filename":"energy_change201920.jpg",
    "status":"Done",
    "table":energy_change_table,
    "details":"How world energy metric changed from 2019 to 2020",
    "references":["energy_forecast"],
    "source_file":"energy.py"
})

energy_2030_table = [
    ["<b>Energy Source</b>","<b>2019 Demand</b>","<b>Projected 2030 Demand</b>"],
    ["Coal",3775,3775-271],
    ["Oil",4525,4525+249],
    ["Gas",3340,3340+475],
    ["Nuclear",727,727+76],
    ["Renewables",1451,1451+864],
    ["Traditional Biomass",588,588-44],
    ["Total","",""]
]

running_sum = [0,0]
for i in range(1,len(energy_2030_table)-1):
    energy_2030_table[i][1] = float(energy_2030_table[i][1]) * 0.041868
    energy_2030_table[i][2] = float(energy_2030_table[i][2]) * 0.041868
    running_sum[0] += energy_2030_table[i][1]
    running_sum[1] += energy_2030_table[i][2]
energy_2030_table[-1][1]= running_sum[0]
energy_2030_table[-1][2]= running_sum[1]

helper.save_image({
    "filename":"energy_change201930.jpg",
    "status":"Done",
    "table":energy_2030_table,
    "details":"Expected change in the world energy system from 2019 to 2030. This is based on the Stated Policies Scenario of the IEA World Energy Outlook, the closest thing to a 'business as usual' scenario they portray.",
    "references":["energy_forecast"],
    "source_file":"energy.py"
})

energy_2040_table = [
    ["<b>Metric</b>",1990,2018,2040],
    ["Population (millions)",5279,7602,9172],
    ["Primary Energy (EJ)",369.26955,599.27172,732.20876],
    ["Greenhouse gas emissions from energy, billions of tons",20.5, 33, 35.6],
    ["GDP, PPP, trillions of dollars",53, 135, 279]
]

helper.save_image({
    "filename":"energy_change201940.jpg",
    "status":"Done",
    "table":energy_2040_table,
    "details":"Change in selected metrics from the International Energy Agency's STEPS (Stated Policies) forecast. It is the closest thing to a 'business as usual' forecast on the list of forecasts and close to the median values.",
    "references":["rff_forecast"],
    "source_file":"energy.py"
})

####################### Energy stocks
# From https://gcep.stanford.edu/pdfs/GCEP_Exergy_Poster_web.pdf

energy_stock_table = [
    ["<b>Source</b>","<b>Stocks, zetajoules</b>","<b>Energy Form</b>"],
    ["Crustal thermal energy",1500000,"Geothermal"],
    ["Plants",30,"Biomass"],
    ["Coal",270,"Fossil Fuels"],
    ["Oil",110,"Fossil Fuels"],
    ["Natural Gas",50,"Fossil Fuels"],
    ["Methane Hydrates",200,"Fossil Fuels"],
    ["Uranium (except seawater)",1000,"Nuclear fission"],
    ["Thorium",300,"Nuclear fission"],
    ["Uranium in Seawater",360000,"Nuclear fission"],
    ["Deuterium",10000000000,"Nuclear fusion"],
    ["Lithium",3100,"Storage"]
]

helper.save_image({
    "filename":"energy_reserves.jpg",
    "status":"Done",
    "table":energy_stock_table,
    "details":"Another plot showing energy reserves. I like that it has more energy sources than the existing R/P plot, but the data is a bit older, and I'm not sure exactly how to interpret sources that are not well developed now. I am presenting this as a separate plot for now, but I am thinking that we might instead combine it with the existing R/P plot. See <a href=\"https://gcep.stanford.edu/pdfs/GCEP_Exergy_Poster_web.pdf\">Stanford's diagram</a> for how they did this. I am only including the reserves here and not the flux.",
    "references":["stanford_flux"],
    "source_file":"energy.py"
})

################################
# Energy production by major source.
# The proximate cause of making this graphic is for use in a presentation.
# It may be replaced/augmented later on with an update to the

energy_table = [
    ["<b>Source</b>","<b>Consumption in 2020, exajoules</b>"],
    ["Oil",173.73],
    ["Natural Gas",137.62],
    ["Coal",151.42],
    ["Nuclear",23.98],
    ["Hydroelectricity",38.16],
    ["Renewables",31.71],
    ["Solar",7.6],
    ["Wind",14.13],
    ["Biofuels",3.76],
    ["Other Renewables",6.22],
    ["Primary Energy",556.63] # The above add up to 552.86
]

helper.save_image({
    "filename":"energy_by_source2021.jpg",
    "status":"Done",
    "table":energy_table,
    "details":"This graphic is needed by October 20, 2021 for use in a presentation. It portrays primary energy as reported by BP, and primary energy broken up into six components: oil, gas, coal, nuclear, hydropower, and renewables (not counting hydro). Renewables are further broken down into solar, wind, biofuels, and other renewables (geothermal, biomass, ocean). Unfortunately the total for renewables is not exactly equal to the sum of the four pieces, and after looking over the statistics for a while, I'm not sure exactly why. I applied a primary energy factor of about 0.4, which was not explicit in the data, to make them equal; I hope this is right. Anyway, I think the best thing graphically would be to show total primary energy, then break it down into all the pieces shown here, execpt 'Renewables' because that encompasses four subcategories. At some point we might want to update the time series graphic of energy by source, but not right now.",
    "references":["bp2021"],
    "source_file":"energy.py"
})

helper.save_image({
    "filename":"energy_by_source2021",
    "status":"Done",
    "details":"",
    "references":[],
    "source_file":""
})
