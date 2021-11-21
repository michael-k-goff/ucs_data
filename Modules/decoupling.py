# -*- coding: utf-8 -*-
# Decoupling

import helper

# Plan:
# 1) Collect a bunch of growths/declines of environmental impacts over periods of time. Ideally, all the same (initially, trying for 1990-2018)
# 2) For each one, show over the time series it's
#   - Average annual growth/decline
#   - Average annual per capita growth/decline
#   - Average annual growth/decline relative to GDP

# See kaya.py for population and GDP time series.

# Impacts to consider:

# GHG
# Fresh water
# Urban land
# Land use: crop, pasture, forestry, meadow
# Usage of copper, iron, steel, cement, plastics, aluminum, paper, any other critical materials
# People in extreme poverty
# NOx emissions
# SOx emissions
# Ozone depletion
# Nitrogen

# See kaya.py: some keys values
pop = {
    1965:3339584.0,
    1990:5414289.0,
    1992:5581598.0,
    2000:6222627.0,
    2002:6381185.0,
    2010:7041194.0,
    2012:7210582.0,
    2014:7379797.0,
    2015:7464022.0,
    2017:7631091.0,
    2018:7713468.0
}

oecd_pop = {
    1990:1104000,
    2017:1345000
}

# See kaya.py: some keys values
gdp = {
    1965:50.995*14.825/37.905,
    1990:50.955,
    1992:52.431,
    2000:67.648,
    2002:71.089,
    2010:95.964,
    2012:102.804,
    2014:109.787,
    2015:113.421,
    2017:121.415,
    2018:125.773,
}

oecd_gdp = {
    1990:18.129,
    2017:57.528
}

# For all impacts, the metric, the 1990 value, and the 2018 value unless otherwise noted
impacts = [
#    ["CO2",21331.5,34007.9], # bp2020
    ["CO<sub>2</sub>",6.05399+1.32166, 9.86716+1.38842,1990,2017,"Le Quéré et al."], # From the carbon_budget reference, emissions (tons C) from fossil fuels and land use. Probably better than BP
    ["Methane",6668380,8014066.562,1990,2012,"World Bank"], # wb_methane
    ["Primary Energy",342.23, 576.23,1990,2018,"BP"], # bp2020, 1990-2018
    
    # Land use in agriculture from FAOSTAT. All in thousands of hectares, 1990 - 2017.
    # ["Agricultural Land Area",4818095.72,4852880.5548], 
    ["Cropland",1486011.7,1561336.753,1990,2017,"FAOSTAT"],
    # ["Land Under Permanent Crops",115572.3,167877.4475],
    ["Permanent Meadows and Pastures",3332084.02,3266422.8335,1990,2017,"FAOSTAT"],
    ["Land for Forestry",4128269.484,3999133.622,1990,2017,"FAOSTAT"],
    ["Urban Land",25934.6812, 55248.2573,1992,2015,"FAOSTAT"], # 1992-2015. FAOSTAT's Land Cover data set. From the CCI_LC data.
    
    # Air pollution. From reference oecd_air.
    # Figures are OECD, 1990 - 2017.
    ["Nitogen Oxide (OECD)",47963.4,25094.9,1990,2017,"OECD"],
    ["Carbon Monoxide (OECD)",219571.3,78971.,1990,2017,"OECD"],
    ["Sulphur Oxides (OECD)",52395.7,11412.6,1990,2017,"OECD"],
    ["Volatile Organic Compounds (OECD)",46964.8,25380.4,1990,2017,"OECD"],
    
    # Water. At the moment AQUASTAT is down. I think the following figures come from AQUASTAT but are pulled from https://www.worldometers.info/water/
    # Check AQUASTAT for correctness and more recent figures later
    ["Water Withdrawal",3321357.298152, 3985681.6,1990,2014,"Worldometer"], # Reference 'worldometer' for now.
    
    # Socioeconomic figures
    ["Extreme Poverty",1900., 733.48,1990,2015,"Roser and Ortiz-Ospina","NoGDP"], # Millions of people, 1990-2015. 'extreme_poverty'. Defined as income below $1.90/day, PPP.
    ["Lack of Access to Safe Drinking Water",2.36,2.13, 2000, 2015,"Ritchie and Roser","NoGDP"], # Billions of people, 2000-2015. 'water_access'
    
    # Raw materials. See Table 4, reference 'krausmann'. See krausmann2009 for methodological notes on the data sets. All from 2002-2015
    ["Biomass (tonnage)",1, 1.021**13, 2002, 2015, "Krausmann et al."],
    ["Ores (by metal content, tonnage)",1, 1.057**13, 2002, 2015, "Krausmann et al."],
    ["Minerals (tonnage)",1, 1.04**13, 2002, 2015, "Krausmann et al."], # E.g. stone, sand, gravel
    
    ["Ozone Depleting Emissions",1320-165, 320-165-50, 1990, 2018, "World Meteorological Organization"], # Cite as ozone2018. Figures are 1990-2018. Numbers are from the OWID page (https://ourworldindata.org/ozone-layer), and a -50 as a visual adjustment based on the image at the top of https://www.esrl.noaa.gov/csl/assessments/ozone/2018/twentyquestions/. 
    
    ["Nitrogen Fertilizer Usage",83407234.87, 109137240.84, 2002, 2017, "FAOSTAT"], # From FAOSTAT, 2002-2017
    
    ["Municipal Solid Waste", 635, 1999, 1965, 2015,"Chen et al.","Long"], # 1965-2015. Will have to use exchange rate GDP figures here. Reference 'msw_history'
    
    ["Lead Production",3.187, 4.737, 1990, 2012,"International Lead Association"], # Millions of tonnes, 1990-2012. Reference 'ila'
    ["Mercury Emissions",2890,2280, 1990, 2010,"Zhang et al."] # 1990-2010.
]

def impact_row(raw_row):
    # Growth rate in the impact
    growth_rate = (raw_row[2]/float(raw_row[1]))**(1/(raw_row[4]-raw_row[3]))
    shown_growth_rate = str(round((growth_rate-1)*100,3))+"%"
    
    # Get annual population growth rate over the period
    pops = [0,0]
    if (raw_row[-1]=="OECD"):
        pops= [pop[raw_row[3]], pop[raw_row[4]]]
    else:
        pops= [pop[raw_row[3]], pop[raw_row[4]]]
    pop_growth_rate = (float(pops[1])/pops[0])**(1/(raw_row[4]-raw_row[3]))
    percap_growth_rate = growth_rate / pop_growth_rate
    percap_growth_rate = str(round((percap_growth_rate-1)*100,3))+"%"
    
    # Get GDP growth rate
    gdps = [0,0]
    if (raw_row[-1]=="OECD"):
        gdps= [gdp[raw_row[3]], gdp[raw_row[4]]]
    else:
        gdps= [gdp[raw_row[3]], gdp[raw_row[4]]]
    gdp_growth_rate = (float(gdps[1])/gdps[0])**(1/(raw_row[4]-raw_row[3]))
    per_gdp_growth_rate = growth_rate / gdp_growth_rate
    per_gdp_growth_rate = str(round((per_gdp_growth_rate-1)*100,3))+"%"
    if (raw_row[-1] == "NoGDP"):
        per_gdp_growth_rate = "---"
    
    return [raw_row[0], str(raw_row[3])+"-"+str(raw_row[4]), shown_growth_rate, percap_growth_rate, per_gdp_growth_rate, raw_row[5]]
    
impact_table = [
    ["<b>Impact</b>","<b>Time Frame</b>","<b>Annual Growth Rate</b>","<b>Annual per Capital Growth Rate</b>","<b>Annual Growth Rate, per $GDP</b>","<b>Source</b>"]
]

for i in range(len(impacts)):
    impact_table = impact_table + [impact_row(impacts[i])]
    
helper.save_image({
    "filename":"decoupling.jpg",
    "status":"Done",
    "details":"Here we show how certain environmental and impacts are changing over time. We show, in terms of annual percent change over a period, the absolute impact, per capita impact, and impact relative to the size of the economy. See the context of the image in the Decoupling page for some technical notes on how these quantities are measured.",
    "table":impact_table,
    "references":["wpp2019", "world_bank_ppp2019", "bp2020", "carbon_budget", "wb_methane", "faostat", "oecd_air", "worldometer", "extreme_poverty","water_access", "krausmann2009", "ozone2018", "msw_history", "ila", "mercury_emissions"],
    "source_file":"decoupling.py"
})

########################### Environmental Kuznets Curves

kuznets_table = [
    ["<b>Impact</b>","<b>Peak Income</b>","<b>Source</b>"],
    ["Sulphur Dioxide","$1377-3389","Cole et al."],
    ["Sulphur Dioxide (transportation)","$1433-2220","Cole et al."],
    ["Suspended Particulate Matter","$646-1540","Cole et al."],
    ["Suspended Particulate Matter","$1114-2709","Cole et al."],
    ["Carbon Monoxide","$2724-6624","Cole et al."],
    ["Nitrogen Dioxide","$1435-1853","Cole et al."],
    ["Nitrogen Dioxide (transportation)","$1218-3861","Cole et al."],
    ["Nitrates","$941-16576","Cole et al."],
    ["Arsenic Pollution","$11982","Yandle et al."],
    ["Cadmium Pollution","$12226","Yandle et al."],
    ["Lead Pollution","$25765","Yandle et al."],
    ["Carbon Dioxide","Inconclusive","Shahbaz and Sinha"]
]

helper.save_image({
    "filename":"kuznets.jpg",
    "status":"Done",
    "details":"Some results on Kuznets curves. These values represent the income at which pollution from the given source is at a peak. I generally reviewed meta-studies for this, and some meta-studies themselves report multiple studies, so that's why there are multiple values from a single source. All peak incomes are CPI-adjusted to 2020 values. Some of these studies report ranges of values, others a single value. There's tons of material on Kuznets curves out there, and while we could probably go a lot farther with this graphic, it's not a high priority right now.",
    "table":kuznets_table,
    "references":["kuznets1","kuznets2","kuznets3"],
    "source_file":"decoupling.py"
})