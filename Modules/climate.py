# -*- coding: utf-8 -*-
# Climate-related calculations

import helper

# Crop yield figures are based on the YTOT variable, Figure 6.
scenario_table = [
    ["<b>Scenario</b>","<b>Radiative Forcing in 2100</b>","<b>Anticipated global warming in 2100 (degrees C)</b>","<b>Anticipated Sea Level Rise in 2100 (meters)</b>","<b>Atmospheric CO<sub>2</sub> concentration, parts per million</b>","<b>Loss to World GDP in 2100</b>","<b>Decrease in Crop Yields</b>"],
    ["RCP2.6","2.6 W/m<sup>2</sup>","0.3-1.7","0.26-0.55","421","0.58-1.57% (Kahn et al.), 6-21% (Burke et al.)","---"],
    ["RCP4.5","4.5 W/m<sup>2</sup>","1.1-2.6","0.32-0.63","538","1.8% (Kompas et al.), 14-28% (Burke et al.)","2-7%"],
    ["RCP6.0","6.0 W/m<sup>2</sup>","1.4-3.1","0.33-0.63","670","3.0% (Kompas et al.), 18-29% (Burke et al.)","3-7%"],
    ["RCP8.5","8.5 W/m<sup>2</sup>","2.6-4.8","0.45-0.82","936","7.2% (Kompas et al.), 4.44-9.96% (Kahn et al.), 22-37% (Burke et al.)","5-11%"]
]

helper.save_image({
    "filename":"rcp.jpg",
    "status":"Done",
    "table":scenario_table,
    "details":"The main goal here is to summarize the impacts of climate change, using the IPCC's four major scenarios. The IPCC summary defines the scenarios (which are named after the radiative forcing in 2100) and reports estimated warming and sea level rise. Lafakis et al. give the numbers for atmospheric CO2 concentration. Several references are noted in the table for the impact on GDP. For the Kompas et al. figures, they report GDP impacts in terms of 2C, 3C, and 4C scenarios, which I am mapping onto the RCP4.5, RCP6.0, and RCP8.5 scenarios respectively, but that's not perfect. Crop yield figures are from Wiebe et al. They do not account for CO<sub>2</sub> fertilization effects and thus might be pessimistic. Their study aggregates estimates for coarse grains, rice, wheat, oilseeds and sugar crops. It is possible we might add more data, such as additional results on economic or crop yield impact, severity on flooding or natural disasters, or biodiversity impacts, but this should be enough for now. Consider breaking this into multiple plots if appropriate.",
    "references":["rcp","moodys","kompas","kahn","burke","wiebe"],
    "source_file":"climate.py"
})

#######################################
# World emissions by sector. See http://cait.wri.org/, country profiles.

# See 2016 figures.
world_emissions = {
    "Industrial Processes":2771.08,
    "Total including LUCF":49358.03,
    "Energy":36013.52,
    "Transportation":7866,
    "Waste":1560.85,
    "Fugitive Emissions":2883.17,
    "Total excluding LUCF":46140.95,
    "Other Fuel Combustion":1429.15,
    "Manufacturing/Construction":6109.3,
    "Land Use Change and Forestry":3217.07,
    "Bunker Fuels":1240.1,
    "Agriculture":5795.51,
    "Building":2720.7,
    "Electricity/Heat":15005.3
}

world_emissions_table = [
    ["Industrial Processes",2771.08],
    ["Transportation",7866],
    ["Waste",1560.85],
    ["Fugitive Emissions",2883.17],
    ["Total excluding LUCF",46140.95],
    ["Other Fuel Combustion",1429.15],
    ["Manufacturing/Construction",6109.3],
    ["Land Use Change and Forestry",3217.07],
    ["Bunker Fuels",1240.1],
    ["Agriculture",5795.51],
    ["Building",2720.7],
    ["Electricity/Heat",15005.3]
]

helper.save_image({
    "filename":"emissions_by_sector.jpg",
    "status":"Done",
    "table":world_emissions_table,
    "details":"I can't believe I forgot to make a plot like this earlier, showing greenhouse gas emissions by sector. Figures are as of 2016, the most recent date reported in the data set.",
    "references":["cait"],
    "source_file":"climate.py"
})

helper.save_image({
    "filename":"emissions_dest.jpg",
    "status":"Done",
    "details":"Simple plot showing where carbon emissions go in the short term. 45% stay in the atmosphere, 25% go to the ocean, and 30% are taken up by land.",
    "references":["emissions_dest"],
    "source_file":"climate.py"
})

# Ecosystem impact of acidification. From acidification_ocean

acidification_table = [
    ["<b>Class of life</b>","<b>Survival</b>","<b>Calcification</b>","<b>Growth</b>","<b>Photosynthesis/Development</b>","<b>Abundance</b>","<b>Notes</b>"],
    ["Calcifying Algae","?","---","?","-28%","-80%",""],
    ["Corals","---","-32%","---","---","-47%",""],
    ["Coccolithophores","?","-23%","---","---","---","A type of plankton that looks armored."],
    ["Mollusks","-34%","-40%","-17%","-25%","---",""],
    ["Echinoderms","---","---","-10%","-11%","?","Examples include starfish, sea urchins, sand dollars, sea cucumbers, sea lilies."],
    ["Crustaceans","---","---","---","---","---",""],
    ["Fish","?","?","---","?","?",""],
    ["Fleshy Algae","?","?","+22%","---","---",""],
    ["Seagrasses","?","?","?","---","?",""],
    ["Diatoms","?","?","+17%","+12%","---","The most common type of plankton."]
]

helper.save_image({
    "filename":"acidification_impact.jpg",
    "status":"Done",
    "table":acidification_table,
    "details":"These are results from a meta-analysis on the impact of ocean acidification resulting from the level of CO<sub>2</sub> emissions that would result in 2-3 &#8451;. A --- means that the results are not statistically significant, and a ? means that there are not enough studies in the review to make a determination. I added some notes explaing what these critters are for those that are not household names.",
    "references":["acidification_ocean"],
    "source_file":"climate.py"
})

#############################

# CO2 fertilization of crops

fertilization_table = [
    ["<b>Crop</b>","<b>Yield increase, low</b>","<b>Yield increase, high</b>"],
    ["Wheat","2.8%","16.4%"],
    ["Potatoes","12.3%","24.4%"],
    ["Maize","0.8%","12.7%"],
    ["Rice","5.4%","17.5%"],
    ["Sorghum","-1.9%","10.2%"],
    ["Soybeans","8.7%","19.5%"]
]

helper.save_image({
    "filename":"crop_fert.jpg",
    "status":"Done",
    "table":fertilization_table,
    "details":"This table summarizes results from a study on the impact of an increase of 100 parts per million CO<sub>2</sub> concentration on crop yields. Yields mostly go up, but this accounts only directly for the fertilization effect, and not for the impact of climate change. The factor driving variance in values is the amount of moisture crops have access to.",
    "references":["co2fert"],
    "source_file":"climate.py"
})

#############################

# Social cost of carbon

scc_table = [
    ["<b>Source</b>","<b>Estimated Social Cost of Carbon, per ton CO<sub>2</sub>e</b>"],
    ["U.S. Federal Government","$52.23"], # $42, 2007 USD. See the 2020 entry, 3% discount rate.
    ["Moore and Diaz","$236.95"], # $220, 2015 USD (I'm not sure if that's really the date, but it's the paper's publication date)
    ["Wang et al., metastudy average","$54.70"],
    ["Wang et al., metastudy average, pure time rate preference of 3%","$30.78"],
    ["Nordhaus","$36.01"], # $31, 2010 USD
    ["Hänsel et al., Use of DICE model with damage recalibrated","$101"],
    ["Ricke et al., recalibration of model","$417"],
    ["<b>Discount Rate</b>","<b>SCC estimate (Rennert and Kingdon)</b>"],
    ["2.5%","$75"],
    ["3% (most commonly used)","$50"],
    ["5%","$14"],
    ["7%","$5"]
]

helper.save_image({
    "filename":"scc.jpg",
    "status":"Done",
    "table":scc_table,
    "details":"The latter two SCC estimates are new here. I am in a process of rethinking the social cost of carbon for our own calculations. Some estimates of the social cost of carbon. Let's do this two-in-one, where one piece is the list of estimates and the other shows how estimates vary by discount rate. There are hundreds of estimates out there, ranging from negative values into the thousands of dollars, so we have to pick the most prominent, mainstream values. The extreme outliers are not generally peer reviewed and should not be taken too seriously. All figures are CPI-adjusted to 2019 as best I can.",
    "references":["social_cost_carbon","stanford_scc","scc_meta","scc_nordhaus","rennert","hansel","scc_country"],
    "source_file":"climate.py"
})

#############################

# Total carbon storage

c_table = [
    ["<b>Source</b>","<b>Carbon storage, billions of tons</b>"],
    ["Atmosphere",800],
    ["Ocean Surface",1000],
    ["Deep Ocean",37000],
    ["Reactive Sediments",6000],
    ["Plant Biomass",550],
    ["Soil",2300],
    ["Fossils",10000]
]

helper.save_image({
    "filename":"c_storage.jpg",
    "status":"Done",
    "table":c_table,
    "details":"This data shows approximately how much carbon (not CO<sub>2</sub>) is stored in various places near the Earth's surface. Far larger amounts are contained in the mantle, and this carbon exchanges with surface carbon via plate tectonics and volcanoes over geologic time scales. 'Reactive Sediments' are, as far as I can tell, carbon that is stored in sedimentary layers of the crust. Maybe we could just say 'sediments' here. To portray this, take a look at the graphic in the source and see if there is something more creative than the usual bar plot we could so with.",
    "references":["carbon_storage"],
    "source_file":"climate.py"
})

helper.save_image({
    "filename":"soil_carbon_transport.jpg",
    "status":"Done",
    "details":"Some information about the annual carbon flow in and out of soils. It is 120 billion tons into soils each year from plant photosynthesis, 60 billion tons out from plant respiration, and 60 billion tons out from microbial respiration and decomposition. By way of comparison, emissions from industrial sources are 9 billion tons (note that this is carbon, not CO2).",
    "references":["carbon_storage"],
    "source_file":"climate.py"
})

############################

# Warming by decade
# From figure SPM.1 here: https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SPM.pdf
# Figures calculated from data here: https://data.ceda.ac.uk/badc/ar6_wg1/data/spm/spm_01/v20210809/panel_b

decade_table = [
    ["<b>Decade</b>","<b>Warming</b>"],
    ["1850s","-0.0161417468"],
    ["1860s","-0.0027081558000000013"],
    ["1870s","0.042392143800000004"],
    ["1880s","-0.0484226131"],
    ["1890s","0.017932515400000001"],
    ["1900s","-0.0170648027"],
    ["1910s","0.0140269888"],
    ["1920s","0.13439225849999998"],
    ["1930s","0.16252596559999999"],
    ["1940s","0.1991000246"],
    ["1950s","0.21448206849999996"],
    ["1960s","0.1073557871"],
    ["1970s","0.1946899595"],
    ["1980s","0.3329721704"],
    ["1990s","0.4563001445"],
    ["2000s","0.8044300113"],
    ["2010s","1.0361308972000002"]
]

helper.save_image({
    "filename":"warming_by_decade.jpg",
    "status":"Done",
    "table":decade_table,
    "details":"This table replicates table SPM.1 in the cited document, though I've compressed the annual time series into decade averages. Warming figures are average temperature deviations from the 1850-1900 mean in degrees Celcius.",
    "references":["ipcc2021"],
    "source_file":"climate.py"
})

#############################

future_warming_table = [
    ["<b>Scenario</b>","<b>Expecting warming, low end</b>","<b>Expecting warming, median</b>","<b>Expecting warming, high end</b>"],
    ["No climate policies",2.0,4.6,7.7],
    ["Current policies",2.0, 3.0, 5.0],
    ["Stated policies",1.7, 2.4, 4.0]
]

helper.save_image({
    "filename":"expected_warming.jpg",
    "status":"Not Done",
    "table":future_warming_table,
    "details":"A simplified presentation from BTI on how much warming we should expected, based on policy. Temperature changes are degrees of warming above preindustrial (1850-1900 average) centigrade. The ranges take into account both uncertainty in the carbon cycle and climate sensitivity. I think the range are meant to reflect the 10-90% probability, so, for instance, under current policies, there is a 10% that warming will be less than 2.0 degrees and a 10% chance it will be more than 5 degrees.",
    "references":["bti_climate"],
    "source_file":"climate.py"
})