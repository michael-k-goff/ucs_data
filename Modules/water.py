# Data for images related to water.

import helper

# See the reference, section 11.1. Source of World Water
water_budget_table = [
    ["<b>Source</b>","<b>Water volume, thousands of km<sup>3</sup></b>"],
    ["Oceans and Salt Water Seas",2000000],
    ["Frozen",50000],
    ["Aquifers",10000],
    ["Annual Rainfall",109],
    ["Natural Lakes",19],
    ["Reservoirs",5],
    ["Rivers",2.12]
]

helper.save_image({
    "filename":"water_budget.jpg",
    "status":"Done",
    "table":water_budget_table,
    "details":"Water available on the surface of the earth. For ths one, due to the extreme scales, you will have to get a bit creative in how the relative values are portrayed. All values are from the Mohajan reference except the annual rainfall, which is from AQUASTAT.",
    "references":["mohajan","aquastat"],
    "source_file":"water.py"
})

##########

# AQUASTAT: http://www.fao.org/nr/water/aquastat/data/query/index.html?lang=en
# To get the following figures, select variables under Water Use / Water withdrawal by sector. Add up over all countries.
# I did this by opening the spreadsheet in Numbers and highlighting the cells.

# From water_crops2, 29% of agricultural water is for animal products. Of that, 1463/2422 is for feed crops, 913/2422 is for grazing, and 46/2422 for direct use.
# See Table 9 to break it down by animal.
animal_water = {
    "Beef Cattle":798,
    "Dairy Cattle":469,
    "Pig":458,
    "Chicken":255+167,
    "Other Animals":180+71+24
}
animal_share = 0.29
animal_sum = sum([animal_water[key] for key in animal_water])

# For crops, see Appendix 1 of https://waterfootprint.org/media/downloads/Report47-WaterFootprintCrops-Vol2_1.pdf (water_crops1 reference) for production by crop family
# Adding up all crops by production mass in a given family.
# For water impact by crop family, see Table 3 of water_crops1, Total column.
crop_water = {
    "Cereal":1644*2117.17,
    "Roots and Tubers":387*684.2,
    "Sugar Crops":197*1525.76,
    "Pulses":4055*57.13,
    "Nuts":9063*8.64,
    "Oil Crops":2364*537.66,
    "Vegetables":322*733.3499999999999,
    "Fruit":967*466.09,
    "Stimulants, Spices, Tobacco":14443*13.74 + 7048*6.18 + 2925*6.82, # Three terms added in that order
#    "Spices":7048*6.18,
#    "Fibers":3837*4.81,
#    "Tobacco":2925*6.82,
    "Rubber, Fibers":13748*7.59 + 3837*4.81 # Two terms added in that order
}
crop_share = 1-animal_share
crop_sum = sum([crop_water[key] for key in crop_water])
ag_water = 2875.15

# Overall industry figure
industry_water = 676.64

# Municipal
municipal_water = 475.88

water_withdrawal_table = [
    ["<b>Use</b>","<b>Withdrawal, km<sup>3</sup></b>"],
#    ["Agriculture",2875.15],
    # See Table 1 of iea_water for breakdown of water withdrawal in the energy sector.
    ["<b>Industry</b>",""],
    ["Industry (excluding energy)",industry_water-398],
    ["Fossil power plants",230],
    ["Nuclear power plants",112],
    ["Renewable power, except hydro",9],
    ["Coal mining",11],
    ["Oil production",8],
    ["Natural gas production",2],
    ["Biofuel production",26],
    ["<b>Municipal</b>",""],
    ["Municipal",municipal_water],
    ["<b>Agricultural</b>",""],
    ["<i>Crops</i>"],
#    ["Total",4008.34], # Not exactly equal to the sum of ag, industry, and muni, which is ~4028
]
for key in crop_water:
    water_withdrawal_table = water_withdrawal_table + [[ key, float(crop_water[key])/crop_sum*crop_share*ag_water ]]
water_withdrawal_table += [["<i>Animal products</i>",""]]
for key in animal_water:
    water_withdrawal_table = water_withdrawal_table + [[ key, float(animal_water[key])/animal_sum*animal_share*ag_water ]]

helper.save_image({
    "filename":"water_by_sector.jpg",
    "status":"Done",
    "table":water_withdrawal_table,
    "details":"World water consumption by sector. For this one, let's do another area plot, like we have with land use. The three top level categories are Agriculture, Municipal, and Industry, and those figures are given by AQUASTAT. The breakdown of Industry into energy and non-energy, as well as all the energy subcategories, is given by the IEA report. For the agriculture stuff, first we have that 29% of agriculture water is for animal products and 71% for crops, and that division is given by the second Mekonnen and Hoekstra source. The second Mekonnen and Hoekstra also breaks down water by type of animal. The first Mekonnen and Hoekstra source gives the breakdown by crop family (if we really wanted to, we could subdivide those into more subcategories, but I think this is enough detail for our purposes). It should be noted that both of the Mekonnen and Hoekstra sources have what appears to be a different method of accounting for water withdrawal, as their figures are larger than the AQUASTAT figures, so what I did was take the shares of total water in agriculture in the Mekonnen and Hoekstra sources and scaled them to the water in agriculture as reported by AQUASTAT. It would be nice to get some subcategories for Municipal water also, but I haven't found those yet. Set up the plot so that all Industry gives grouped together and all Agriculture figures are grouped together, and within Agriculture, group the animal and non-animal figures.",
    "references":["aquastat", "water_crops1","water_crops2","iea_water"],
    "source_file":"water.py"
})

####################################

# US water withdrawal

us_water = [
    ["<b>Purpose</b>","<b>Volume, km<sup>3</sup>/year</b>"],
    ["Public Supply",39],
    ["Self-supply, domestic",3.26],
    ["Irrigation",118],
    ["Livestock",2],
    ["Aquaculture",7.55],
    ["Self-supplied, industrial",14.8],
    ["Mining",4],
    ["Thermoelectric power",133]
]

for i in range(1,len(us_water)):
    us_water[i][1] *= 3.78541 * 365. / 1000.
    
helper.save_image({
    "filename":"us_water.jpg",
    "status":"Done",
    "table":us_water,
    "details":"Withdrawals of water in the US by major category.<br><br>EDIT: On February 28, 2020, I found an error in the figures; Irrigation was reported as much higher than it should have been. That has now been corrected. Hopefully you haven't started making the plot with the older figure yet.",
    "references":["us_water2"],
    "source_file":"water.py"
})

################################

muni_water_table = [
    ["<b>City or country</b>","<b>Municipal water usage, cubic meters per person per year.</b>"],
    ["Rural India",40*0.365],
    ["India, large cities",150*0.365],
    ["Mumbai",300*0.365],
    ["United States",650*0.365],
    ["New York City, 1980",806*0.365],
    ["New York City, 2010",481*0.365]
]

helper.save_image({
    "filename":"muni_water.jpg",
    "status":"Done",
    "table":muni_water_table,
    "details":"Municipal water demand per person for select cities and countries.",
    "references":["un_water2014"],
    "source_file":"water.py"
})

##################################

# Power plant cooling systems. From the reference 'cooling'.

cooling_table = [
    ["<b>Method</b>","<b>Coal, consumption</b>","<b>Coal, withdrawal</b>","<b>Natural gas, consumption</b>","<b>Natural gas, withdrawal</b>","<b>Nuclear, consumption</b>","<b>Nuclear, withdrawal</b>","<b>Fossil/biomass, consumption</b>","<b>Fossil/biomass, withdrawal</b>","<b>Concentrated solar, consumption</b>","<b>CSP, withdrawal</b>","<b>Geothermal, consumption</b>","<b>Geothermal, withdrawal</b>"],
    ["Dry Cooling","0","0.31-0.59","0-0.38","0-0.38","---","---","---","---","---","---","---","---"],
    ["Once-through Cooling","0.4-2","76-189","0.05-3.23","4.6-533.7","1.7","136.3","---","---","---","---","---","---"],
    ["Closed Loop","0.38-4.2","0.95-132.5","0.68-4.4","0.87-5.5","---","---","---","---","---","---","---","---"],
    ["Cooling Pond","0.2-2.7","1.1-90.9","---","---","2.1-2.73","1.9-49.2","1.82","1.89-2.27","---","---","---","---"],
    ["Hybrid System","---","---","---","---","---","---","---","---","0.4-1.5","0.4-1.5","0.8-2.7","0.8-2.7"]
]

helper.save_image({
    "filename":"power_cooling.jpg",
    "status":"Done",
    "table":cooling_table,
    "details":"Show water consumption and withdrawal for various power generating technologies and cooling systems. I think the best way to present this would be, for each cooling method, present several bars showing the range for the technology(ies) that may use that method. As you can see, not all methods apply to all thermal power sources. All figures are cubic meters per MWh.",
    "references":["cooling"],
    "source_file":"water.py"
})

###################################

# Water savings potential in the US by several methods.
# Here the focus is industrial (not power) and municipal. More methods may be added depending on data availability.

# Landscaping figures from the epa_landscaping reference.
# Convert 9 billion gallons/day to m^3/year
landscaping = 9 * 10**9 * 3.78 * 365. / 1000
# Half could be saved, it is claimed
landscaping *= 0.5

# The paper here gives (Table 2) a range of potential savings by industry. Maybe go with a flat 33% due to the age of the figures. https://www.osti.gov/biblio/1238179
# Savings by industry range from 15% (Beverages) to 74% (Petroleum Refining).
# The USGS study 'us_water2' says 14.8 billion gallons/per self-supplied industrial water, but that doesn't include industrial water from public supply.
industrial = 14.8 * 10**9 * 3.78 * 365. / 1000 # References: industry_water
industrial *= 0.33

# From 'water_appliances', 39600 gallons/year/household savings potential.
appliance_savings = (39600-10000) * 3.78 / 1000 # Per household. Subtracting the 10000 for irrigation, which should be covered under landscaping.
appliance_savings *= 118.2 * 10**6 # Number of households, via RECS.

water_savings_table = [
    ["<b>Method</b>","<b>Savings potential, km<sup>3</sup>/year</b>"],
    ["Industrial efficiency",industrial/float(10**9)],
    ["Residential appliances and plumbing",appliance_savings/float(10**9)],
    ["Landscaping",landscaping/float(10**9)]
]

helper.save_image({
    "filename":"water_savings.jpg",
    "status":"Done",
    "table":water_savings_table,
    "details":"Water savings by three methods. More may be added as appropriate. For industrial efficiency, there is a somewhat outdated chart of water savings potential by industry in Rao et al., with figures ranging from 15% to 74%. I guesstimated 33% savings is achievable, which is on the low end of the table, but I think that's appropriate because the table is old and some of the savings there should have already been achieved. That is applied to the Dieter et al. estimate of total industrial water usage, which unfortunately only counts self-supply and does not count industrial water from public supply, so altogether that might be a low estimate. For appliances and plumbing, I took the 39,600 gallons per year per household savings as in Chini et al., subtracted the irrigation numbers because that is considered separately under landscaping, and multiplied that by the 118.2 million households in the US as reported by RECS. For landscaping, I lifted that one straight from the WaterSense reference.",
    "references":["epa_landscaping","us_water2","industry_water","recs","water_appliances"]
})

######################################

# Available water resource

# Pulled from AQUASTAT. Again added over all countries.

water_resource_table = [
    ["<b>Source</b>","<b>Availability, km<sup>3</sup></b>"],
    ["Annual rainfall",109261],
    ["Annual renewable resource",54737],
    ["Annual economically exploitable resource",7748],
    ["Annual withdrawal",2875+677+476] # Ag + Industry + Muni
]

helper.save_image({
    "filename":"water_resource.jpg",
    "status":"Done",
    "table":water_resource_table,
    "details":"Water resource. Almost freshwater ultimately comes from rain, the first figure. The second figure is how much could theoretically be exploited sustainably. The third figure is how much could be exploited sustainably, taking economic constraints into account. The fourth is how much actually is exploited.",
    "references":["aquastat"],
    "source_file":"water.py"
})

#######################################

# Where water comes from

water_source_table = [
    ["<b>Source</b>","<b>Percentage of total water withdrawal</b>"],
    ["Fresh surface water",2535.0469],
    ["Fresh groundwater",859.5998],
    ["Desalination",10.6926],
    ["Direct use of treated municipal wastewater",16.6001],
    ["Direct use of agricultural drainage water",130.4]
]

# Convert the table to percentages
table_sum = sum([water_source_table[i][1] for i in range(1,len(water_source_table))])
for i in range(1,len(water_source_table)):
    water_source_table[i][1] = water_source_table[i][1]*100./table_sum
    
helper.save_image({
    "filename":"water_source.jpg",
    "status":"Done",
    "table":water_source_table,
    "references":["aquastat"],
    "details":"Show where water comes from. I am doing this as a percentage, rather than overall volume, because the AQUASTAT data is a bit spotty and only accounts for about 85% of total withdrawal. Hopefully the data that is present is representative of the missing data. But do note on the plot somewhere that there is some missing data in the AQUASTAT data set. We should also probably note that direct use of rainfall is not part of the AQUASTAT water budget, which is why that isn't included here.",
    "source_file":"water.py"
})

##################################

# Water process energy.

# From http://baseco.com/Publications/IETC%202015_Water%20and%20Embedded%20Energy%20Conservation%20in%20the%20Industrial%20Sector.pdf
# Numbers are kWh per million gallons. See Table 1. Two numbers are given, as a range from min to max.

water_energy1 = {
    "Ground Water":[790,3753],
    "Raw Water Conveyance":[2,1704],
    "Water Distribution":[37,1524],
    "Water Treatment":[43,6666],
    "Wastewater Pumps":[2,497],
    "Wastewater Treatment":[923,4941],
    "Recycled Water Treatment":[984,3771],
    "Recycled Water Distribution":[210,1304],
    "Desalination":[3819,3945],
    # From the next right above Table 1
    "Surface Water, overall":[1400,1500],
    "Groundwater, overall":[1824,1824]
}

# From https://www.sciencedirect.com/science/article/pii/S2588912517300085, Table 1. 'cooling' reference.
# This time numbers (again as ranges) are in kWh/m^3.

water_energy2 = {
    "Supply and Treatment":[0.12,0.79],
    "Conventional Treatment":[0.01,1.44],
    "Conveyance to Agricultural Uses, Surface":[0.25,1.55],
    "Conveyance to Agricultural Uses, Groundwater":[0.2, 0.55],
    "Collection and Conveyance, Wastewater":[0.25, 0.66],
    "Collection and Treatment, Wastewater":[0.53,0.53],
    "Treatment and Disposal, Wastewater":[0.2, 0.8],
    "Aerobic and anaerobic digestion, Wastewater":[0.6, 0.6],
    "Gravity Filtration, Wastewater":[0.005, 0.014],
    "Coagulation using polymers, Wastewater":[0.4, 0.7]
}

# Some more from this paper: https://watereuse.org/wp-content/uploads/2015/10/Power_consumption_white_paper.pdf
# See Table 2. Figures are kWh/thousand gallons. Groan.
# desal_energy

water_supply3 = {
    "Desalination":[9.1,14.0], # Covers a proposed California project, Pacific Ocean, Gulf of Mexico. Higher numbers for higher salinity
    "Brackish Desalination":[3.,5.],
    "Import: Colorado River to Southern CA":[6.8,9.5],
    "Reclaimed Water for Potable Use":[7.0,11.5]
}

# The figures I think we will go with here for the plot
water_supply_table = [
    ["<b>Water source</b>","<b>Electricity required, kWh/m<sup>3</sup>, low end</b>","<b>Electricity required, high end</b>"],
    ["Surface freshwater",water_energy2["Supply and Treatment"][0]+water_energy2["Conveyance to Agricultural Uses, Surface"][0],water_energy2["Supply and Treatment"][1]+water_energy2["Conveyance to Agricultural Uses, Surface"][1]],
    ["Groundwater",water_energy2["Supply and Treatment"][0]+water_energy2["Conveyance to Agricultural Uses, Groundwater"][0],water_energy2["Supply and Treatment"][1]+water_energy2["Conveyance to Agricultural Uses, Groundwater"][1]],
    ["Import: Colorado River to Southern California", water_supply3["Import: Colorado River to Southern CA"][0]/3.78, water_supply3["Import: Colorado River to Southern CA"][1]/3.78],
    ["Brackish Desalination",water_supply3["Brackish Desalination"][0]/3.78, water_supply3["Brackish Desalination"][1]/3.78],
    ["Reclaimed Water for Potable Use", water_supply3["Reclaimed Water for Potable Use"][0]/3.78, water_supply3["Reclaimed Water for Potable Use"][1]/3.78],
    ["Desalination - Reverse Osmosis",3.5, 5], # irena_desal
    # Water treatment from epri_water, via gandiglio
    ["Water Treatment",0.413, 0.87],
    ["Atmospheric Water Generation",300,650]
]

helper.save_image({
    "filename":"water_supply.jpg",
    "status":"Done",
    "table":water_supply_table,
    "details":"I figured out what the problem was. One of the surface freshwater items in the chart should have been groundwater instead. That has been fixed. Since we're making changes, I added some figures on atmospheric water generation, pulled from Inbar et al. Unfortunately this busts the scale, so we can't draw this one to scale like the others.",
    "references":["cooling","desal_energy","irena_desal","epri_water","gandiglio","inbar"],
    "source_file":"water.py"
})

#############################

# Cost of providing water

water_cost_table = [
    ["<b>Source</b>","<b>Cost, USD per cubic meter</b>"],
    # First three from 'cooley'
    ["Surface Water, California","$0.27"],
    ["Treated Stormwater, California","$1.26"],
    ["Treated Wastewater, California","$0.71"],
    # The rest from kaust_desal
    ["Desalination, low estimate","$0.50"],
    ["Desalination, high estimate","$1.00"],
    ["Brackish Desalination","$0.26"]
]

helper.save_image({
    "filename":"water_cost.jpg",
    "status":"Done",
    "table":water_cost_table,
    "details":"Several estimates of the cost of providing water by various means. For the non-desal options, California-specific estimates are included to show that desal might be competitive in expensive, water-constrained markets, but probably not elsewhere.",
    "references":["cooley","kaust_desal"],
    "source_file":"water.py"
})

##################################

# Water recycling.

water_recycling_table = [
    ["<b>Region</b>","<b>Wastewater treatment rate</b>"],
    ["World","20%"],
    ["Developing World","10%"],
    ["Israel","93%"],
    ["Israel, reclaimed water","79%"]
]

helper.save_image({
    "filename":"water_treatment.jpg",
    "status":"Done",
    "table":water_recycling_table,
    "details":"A simple plot showing that most discarded water in the world is not recovered, but in principle it could be, as is done in Israel. In practice, the Israeli case probably can't be economically replicated in areas where water is abundant and cheap. The reclaimed water figure for Israel is the fraction of wastewater that is then readded to the supply (some of it is treated but then lost or discarded). The Israel figures are from the Israeli Water Authority, and the others are from the UN report.",
    "references":["un_water2014","israel_water"],
    "source_file":"water.py"
})

######################################

# Some high level figures on blue and grey water. It would be nice to have the same level of details as with withdrawals, but oh well.
# From 'blue_grey_water'

blue_grey_table = [
    ["<b>Source</b>","<b>Blue Water</b>","<b>Grey Water</b>"],
    ["Crops",899,733],
    ["Animal Raising",46,"---"],
    ["Industry",38,362],
    ["Municipal",282,324]
]

helper.save_image({
    "filename":"blue_grey_water.jpg",
    "status":"Done",
    "table":blue_grey_table,
    "details":"Show blue and grey water pollution from major categories. Blue water is water that is consumed or evaporated and can't be returned to nature. Grey water is pollution, and specifically, when a pollutant is released into the water supply, the grey water impact is the amount of water that is required to dilute the pollutant down to whatever is deemed to be a safe level. It would be nice to have more detailed breakdowns here, but I don't have that.",
    "references":["blue_grey_water"],
    "source_file":"water.py"
})

###################### Images for the clean water and sanitation page

water_deaths_table = [
    ["<b>Year</b>","<b>Deaths per 100,000</b>","<b>Total Deaths, millions</b>"],
    ["1990","40.51",5280*0.004051],
    ["1995","36.01",5707*0.003601],
    ["2000","31.01",6114*0.003101],
    ["2005","26.04",6512*0.002604],
    ["2010","23.15",6922*0.002315],
    ["2015","17.84",7339*0.001784],
    ["2017","16.97",7509*0.001697]
]

helper.save_image({
    "filename":"water_deaths.jpg",
    "status":"Done",
    "table":water_deaths_table,
    "details":"Number of deaths that can be attributed to poor water or sanitation access. Deaths per 100,000 are reported by the Global Burden of Disease. There is information of this <a href=\"https://ourworldindata.org/water-access\">Our World in Data page</a> if you want to do a time series plot and have every year from 1990 to 2017 reported. I adjusted to total deaths using the World Bank's population figures.",
    "references":["disease_burden","wb_pop"],
    "source_file":"water.py"
})

improved_water_table = [
    ["<b>Year</b>","<b>Rate of access to improved water source</b>","<b>Access to Safe Drinking Water</b>"],
    ["1990","76.08%",""],
    ["1995","79.32%",""],
    ["2000","82.48%","61.42%"],
    ["2005","85.52%","66.09%"],
    ["2010","88.36%","70.82%"],
    ["2015","90.95%","71.16%"]
]

helper.save_image({
    "filename":"improved_water.jpg",
    "status":"Done",
    "table":improved_water_table,
    "details":"Rates of worldwide access to improved water sources and access to save drinking water. Improved water source data from the World Bank and safe drinking water data from WHO/UNICEF. Both are via Our World in Data. Feel free to visit the OWID site for data resolution down to a single year.",
    "references":["wb_water","owid_water","safe_drinking_water"],
    "source_file":"water.py"
})

water_cost_table = [
    ["<b>Area</b>","<b>Cost of providing clean water, billions of dollars, 2015 USD</b>"],
    ["Drinking Water",113],
    ["Sanitation",150],
    ["Pollution",153],
    ["Addressing Scarcity",445],
    ["Water Management",172]
]

helper.save_image({
    "filename":"clean_water_cost.jpg",
    "status":"Done",
    "table":water_cost_table,
    "details":"Cost in billion of USD of providing universal clean water.",
    "references":["water_abundance"],
    "source_file":"water.py"
})

helper.save_image({
    "filename":"water_cost.jpg",
    "status":"Done",
    "details":"",
    "references":[],
    "source_file":"water.py"
})