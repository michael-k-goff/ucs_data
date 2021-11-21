# Air pollution

import helper

table_pollutant = [
    ["<b>Pollutant</b>","<b>Monetized Damages in the US (billions of dollars)</b>"],
    ["VOC",102.59],
    ["PM<sub>2.5</b>",333.73],
    ["NH<sub>3</sub>",145.48],
    ["SO<sub>2</sub>",135.56],
    ["NO<sub>x</sub>",168.22]
]

helper.save_image({
    "filename":"by_pollutant.jpg",
    "status":"Done",
    "details":"Monetized damages by criterion air pollutant in the US.",
    "table":table_pollutant,
    "references":["air_pollution_damages"],
    "source_file":"air_pollution.py"
})

# PM damages by sector/activity. Billions of dollars of damages
by_sector = {
    "Fuel combustion: coal - electric":118.44,
    "Mobile: road - light gas vehicles":94.1,
    "Agriculture: livestock waste":70.52,
    "Mobile: road - heavy diesel vehicles":58.11,
    "Fuel combustion: wood - residential": 50.04,
    "Fires - prescribed": 47.17,
    "Mobile: non-road - diesel vehicles":34.61,
    "Agriculture - fertilizer application":33.95,
    "Mobile: non-road - gas vehicles":26.65,
    "Commercial cooking":23.62,
    "Dust: unpaved roads":21.94,
    "Agriculture: fugitive dust":19.87,
    "Fuel combustion: biomass - industrial":19.75,
    "Industrial processes - not categories":18.65,
    "Dust: construction":16.91,
    "Industrial processes - oil/gas production":16.73,
    "Dust: paved roads":16.31,
    "Waste disposal":16.25,
    "Solvent: consumer & commercial":15.94,
    "Fuel combustion: natural gas - residential":13.72,
    "Mobile: locomotives":12.4,
    "Fuel combustion: coal - industrial":11.03,
    "Mobile: commercial marine vehicles":10.58,
    "Fuel combustion: natural gas - industrial":10.08,
    "Solvent: industrial surface coating":6.61,
    "Industrial processes: chemical manufacture":6.18,
    "Industrial processes: petroleum refineries":6.09,
    "Fuel combustion: natural gas - commercial":6.03,
    "Industrial processes: storage & transfer":5.73,
    "Fuel combustion: oil - residential":5.59,
    "Fuel combustion: oil - commercial":5.55,
    "Gas stations":5.43,
    "Fuel combustion: natural gas - electric":4.87,
    "Fuel combustion: oil - industrial":4.06,
    "Fires: agricultural field burning":4.04,
    "Mobile: road - light diesel vehicles":3.82,
    "Solvent: non-industrial surface coating":3.71,
    "Mobile: aircraft":3.65,
    "Industrial processes: ferrous metals":3.29,
    "Industrial processes: cement manufacture":3.23,
    "Fuel combustion: other - industrial":3.17,
    "Miscellaneous: non-industrial not categories":3.05,
    "Industrial processes: non-ferrous metals":3.03,
    "Industrial processes: pulp & paper":2.97,
    "Mobile: non-road - other":2.74,
    "Industrial processes: mining":2.52,
    "Fuel combustion: biomass - commercial": 2.38,
    "Mobile: road - heavy gas vehicles":1.92,
    "Solvent: degreasing":1.58,
    "Fuel combustion: coal - commercial":1.54,
    "Bulk gasoline terminals":1.13,
    "Fuel combustion: oil - electric":1.00,
    "Fuel combustion: other - electric":1.00,
    "Solvents: graphic arts":0.86,
    "Fuel combustion: other - residential":0.83,
    "Fuel combustion: other - commercial":0.31,
    "Fuel combustion: biomass - electric":0.2,
    "Solvent: dry cleaning":0.1
}

consolidated_sectors = {
    "Electricity":
    {
        "Electricity from Coal":["Fuel combustion: coal - electric"],
        "Electricity from Other Sources":["Fuel combustion: oil - electric","Fuel combustion: other - electric","Fuel combustion: biomass - electric","Fuel combustion: natural gas - electric"]
    },
    "Transportation":
    {
        "Fuel for Road Vehicles (including gas stations)":["Mobile: road - light gas vehicles","Mobile: road - heavy diesel vehicles","Gas stations","Mobile: road - light diesel vehicles","Mobile: road - heavy gas vehicles"],
        "Road Dust":["Dust: unpaved roads","Dust: paved roads"],
        "Other Transportation":["Mobile: non-road - diesel vehicles","Mobile: non-road - gas vehicles","Mobile: locomotives","Mobile: commercial marine vehicles","Mobile: aircraft","Mobile: non-road - other"]
    },
    "Industry":
    {
        "Fuel Combustion in Industry":["Fuel combustion: biomass - industrial", "Fuel combustion: coal - industrial", "Fuel combustion: natural gas - industrial","Fuel combustion: oil - industrial","Fuel combustion: other - industrial"],
        "Oil & Gas Production and Refining":["Industrial processes - oil/gas production","Industrial processes: petroleum refineries","Bulk gasoline terminals"],
        "Industrial Processes":["Industrial processes - not categories", "Solvent: industrial surface coating","Industrial processes: chemical manufacture","Industrial processes: storage & transfer","Industrial processes: ferrous metals","Industrial processes: cement manufacture","Industrial processes: non-ferrous metals","Industrial processes: pulp & paper","Industrial processes: mining"]
    },
    "Agriculture":
    {
        "Agriculture (except fire)":["Agriculture: livestock waste","Agriculture: fugitive dust","Agriculture - fertilizer application"]
    },
    "Residential":
    {
        "Residential Fuel":["Fuel combustion: wood - residential", "Fuel combustion: natural gas - residential","Fuel combustion: oil - residential","Fuel combustion: other - residential"]
    },
    "Commercial":
    {
        "Commercial Fuel":["Commercial cooking","Fuel combustion: natural gas - commercial","Fuel combustion: oil - commercial","Fuel combustion: biomass - commercial","Fuel combustion: coal - commercial","Fuel combustion: other - commercial"]
    },
    "Fire":
    {
        "Fire":["Fires - prescribed","Fires: agricultural field burning"]
    },
    "Other":{
        "Construction":["Dust: construction"],
        "Waste":["Waste disposal"],
        "Solvents (except industrial)":["Solvent: consumer & commercial","Solvent: non-industrial surface coating","Solvent: degreasing","Solvents: graphic arts","Solvent: dry cleaning"],
        "Miscellaneous":["Miscellaneous: non-industrial not categories"]
    }
}

# Make sure all categories are covered and none are covered more than once
#for key in by_sector:
#    num_covered = 0
#    for key2 in consolidated_sectors:
#        for key3 in consolidated_sectors[key2]:
#            if key in consolidated_sectors[key2][key3]:
#                num_covered += 1
#    if num_covered != 1:
#        print(key+": Appears "+str(num_covered)+ " times.")

by_sector_table = [["<b>Source</b>","<b>Pollution damages (billions of dollars)</b>"]]
for key in consolidated_sectors:
    for key2 in consolidated_sectors[key]:
        val = str(sum([by_sector[consolidated_sectors[key][key2][i]] for i in range(len(consolidated_sectors[key][key2]))]))
        by_sector_table.append([key2, val])

#print(by_sector_table)

helper.save_image({
    "filename":"air_pollution_sources.jpg",
    "status":"Done",
    "details":"Show sources of certain air pollutants (VOC, PM2.5, NH3, SO2, NOx) in the United States, by billions of dollars of monetized damages. Note that the damages done by a pollutant depend both on what the pollutant is and where it is released (i.e. generally more damage if released in a highly populated area). These pollutants do not comprehensively cover all air pollution (e.g. does not cover lead, carbon monoxide, ozone), but I think they cover most of the air pollution damages. The original source gives damage by the five pollutants and 58 categories; here I consolidated them into the following categories and combined then into general pollution damages. Think about how best to present this; either a bar plot as the figures are, or some thematic grouping.",
    "table":by_sector_table,
    "references":["air_pollution_damages"],
    "source_file":"air_pollution.py"
})

# Some pollution stats from the Lancet report.

global_pollution_table = [
    ["<b>Type of pollution</b>","<b>Deaths, millions</b>"], # Table 1 of the report. Using the GBD figures.
    ["Air - overall",6.5],
    ["Household air",2.9],
    ["Ambient air",4.2],
    ["Ozone",0.3],
    ["Water - overall",1.8],
    ["Unsafe sanitation",0.8],
    ["Unsafe water source",1.3],
    ["Occupational pollution",0.8],
    ["Occupational - carcinogens",0.4],
    ["Occupational - particulates",0.5],
    ["Soil, heavy metals, and chemicals",0.5],
    ["Lead",0.5],
    ["<b>Type of pollution</b>","<b>World damages, billions of dollars</b>"], # Table 5 of the report
    ["Air (ambient and household)",3767],
    ["Water and sanitation",404],
    ["Lead",451]
]

helper.save_image({
    "filename":"pollution_damages.jpg",
    "status":"Done",
    "details":"A 2-1 graphic here: show deaths and monetized damages for main classes of pollutants. Pollution deaths are counting all deaths for which the type of pollutant is considered to have contributed. Since there may be several types of pollution that contribute to the same death, the totals for air, water, and occupational are less than the sum of the subcategories. Data is from 2015. For deaths, partition the graphic so the air, water, and occupational figures together. Unfortunately, I don't have monetized damages for soil pollution. There is a supplementary file to the main report that I haven't been able to access; maybe there are more details there.",
    "table":global_pollution_table,
    "references":["lancet_pollution"],
    "source_file":"air_pollution.py"
})

##########################3

# World sources of PM

world_pm_table = [
    ["<b>Sector</b>","<b>PM<sub>10</sub></b>","<b>PM<sub>2.5</sub></b>","<b>PM<sub>1</sub></b>","<b>Black Carbon</b>","<b>Organic Carbon</b>","<b>Organic Matter</b>"],
    ["Agriculture",6555,3848,2883,337,1313,2364],
    ["Residential combustion",23078,21857,20742,4163,8852,15329],
    ["Industrial processes",12162,8340,4135,462,633,823],
    ["Power plants",11561,6420,3812,136,164,248],
    ["Oil and gas, mining",1706,571,412,226,93,120],
    ["Transport - road",3339,2925,2524,1349,1116,1451],
    ["Transport - non-road",861+1856+30, 923+1758+30, 795+1612+28, 363+120+10, 217+398+10, 283+517+13], # Including international shipping and aviation
    ["Waste",1388,1272,876,97,751,977],
    ["Forest and savannah fires",48207,33014,33014,2268,19489,31363]
]

helper.save_image({
    "filename":"pm_source.jpg",
    "status":"Done",
    "table":world_pm_table,
    "details":"Sources of world particulate emissions by sector, as of 2010. All figures are in thousands of tons.",
    "references":["iiasa_pollution"],
    "source_file":"air_pollution.py"
})

# See the table on pp. 16-17. Reference ef_cook.
cooking_table = [
    ["<b>Fuel Source</b>","<b>Particulates released, grams per kg fuel</b>"],
    ["Wood","1.5-3.5"], # Reporting the range of the average values over the four wood classes
    ["Dung","2.45-3.4"], # The averages of the two dung classes
    ["Crop Residue","3.2-11"], # Average of the two crop residue classes
    ["Charcoal","1.77-4.8"], # Averages over the three charcoal classes, included briquettes
    ["Lignite Coal","4.4-6.6"], # Two averages
    ["Briquettes","0.19-1.8"], # Three averages. What kind of briquettes are we talking here, and are they differeint from charcoal briquettes?
    ["Kerosene","0.29"],
    ["Liquified Petroleum Gas (LPG)","0.35"],
    ["Natural Gas","0.16"],
    ["Electricity","No onsite emissions"] # Not in the document, but I figured I'd throw it in.
]

helper.save_image({
    "filename":"cook_pm.jpg",
    "status":"Done",
    "table":cooking_table,
    "details":"Show particulate matter, which is the main form that indoor air pollution takes, from various methods of cooking. Where there are ranges, I took the range of average values across each fuel type as reported in the study. They don't have electricity explicity mentioned, but I added it for comparison (if we really want to split hairs, the g/kg metric doesn't apply to electricity because it doesn't have a mass, but whatever. Of course, there may be particulates from the generation of electricity, but they are not released in the household.).",
    "references":["ef_cook"],
    "source_file":"air_pollution.py"
})

################################

# Sources of aerosols, from reference 'aerosol_source'

aerosol_table = [
    ["<b>Natural Sources</b>","<b>Millions of tons per year</b>"],
    ["Sea Salt","3000-20000"],
    ["Mineral Dust","1000-2150"],
    ["Organic, from life (direct and indirect)","23-153"], # Adding the "Biogenic primary organic" and "Biogenic secondary organic" categories
    ["Organic, from burning biomass","26-70"],
    ["Volcanic","6-107"], # Adding two volcano categories
    ["Cosmic Dust","0.0002-0.04"],
    ["Sulfates","107-374"],
    ["Nitrates","12-27"],
    ["Isoprene, monoterpenes, and VOCs, from life","835-1000"],
    ["<b>From Human Activity</b>",""],
    ["Mineral Dust","50-250"],
    ["Organic, from burning biomass","12-270"],
    ["Sulfates","50-112"],
    ["Nitrates","90-118"],
    ["Industrial Dust","40-130"],
    ["Carbonaceous from hydrocarbons and VOCs","15-90"],
    ["Black Carbon","8-14"]
]

helper.save_image({
    "filename":"aerosol_source.jpg",
    "status":"Done",
    "table":aerosol_table,
    "details":"Main sources of atmospheric aerosols, divided by natural and artificial. While sources are mostly natural, aerosol loading is a concern for the as yet not fully understood effect of aerosol loading being outside of historic ranges. For sea salt, the average reported value is 7068. Visually, portray it as that to avoid disrupting the scale, but textually note that range of 3000 to 20000.",
    "references":["aerosol_source"],
    "source_file":"air_pollution.py"
})

#####################################

# World acidifying emissions

world_acid_table = [
    ["<b>Pollutant</b>","<b>Acidifying Potential (thousands of tons SO<sub>2</sub>-equivalent/year)</b>","<b>Emissions, thousands of tons/year</b>"],
    ["Sulfur Dioxide (SO<sub>2</sub>)",15217+9385+5216,15217+9385+5216], # Greenpeace. Does not include volcanoes.
    ["Nitrogen Oxide (NO<sub>x</sub>)",67133*0.7,67133],
    ["Ammonia (NH<sub>3</sub>)",(65400-8600-2500-2400+11000)*1.88*11./8.,65400-8600-2500-2400+11000] # The 11/8 is to adjust for N instead of NH3.
]

helper.save_image({
    "filename":"acidification.jpg",
    "status":"Done",
    "table":world_acid_table,
    "details":"Acidification from major sources. In presenting this graphically, the acidification potential column is the more relevant figure for comparison, but I also included emissions in tons. For ammonia, tonnage is in tons of N. SO2 emissions from the Greenpeace report, NOx from the UN data, ammonia from Sutton et al., and acidification potentials from Lindley et al. Only anthropogenic sources are shown; there are some additional natural sources of SO2 and ammonia. Consider combining with the plots of NOx, SO2, and ammonia emissions if feasible.",
    "references":["greenpeace_sox","nox_source","ammonia_source","lindley"],
    "source_file":"air_pollution.py"
})

#####################################

ammonia_table = [
    ["<b>Source</b>","<b>Emissions, thousands of tons N/year</b>"],
    ["<b>Artificial Sources</b>",""],
    ["Exectra from domestic animals",8700],
    ["Synthetic nitrogen fertilizers",11000],
    ["Agricultural soils and crops",28300],
    ["Biomass Burning",5500],
    ["Industrial and fossil fuel burning",1600],
    ["Human population and pets",3300],
    ["Waste composting & processing",4400],
    ["<b>Natural Sources</b>",""],
    ["Soils under natural vegetation",2400],
    ["Excreta from wild animals",2500],
    ["Oceans and Volcanoes",8600]
]

helper.save_image({
    "filename":"ammonia_source.jpg",
    "status":"Done",
    "table":ammonia_table,
    "details":"Sources of ammonia emissions, worldwide.",
    "references":["ammonia_source"],
    "source_file":"air_pollution.py"
})

#####################################

sox_table = [
    ["<b>Source</b>","<b>Emissions, thousands of tons/year</b>"],
    ["Volcanoes",19868],
    ["Coal",15217],
    ["Oil and Gas",9385],
    ["Smelters",5216]
]

helper.save_image({
    "filename":"so2_source.jpg",
    "status":"Done",
    "table":sox_table,
    "details":"Sources of SO2 emissions. In the acidification.jpg plot, I excluded the volcano figure since that only portrays artificial sources.",
    "references":["greenpeace_sox"],
    "source_file":"air_pollution.py"
})

#####################################

# US NOx emissions. We'll see how this gets used. From https://www.epa.gov/air-emissions-inventories/2014-national-emissions-inventory-nei-data

us_nox_table = [
    ["<b>Source</b>","<b>Emissions in 2014, tons</b>"],
    # Everything to start with are the figures taken from the source.
#    ["Mobile - On-Road non-Diesel Light Duty Vehicles",2510022.21442440701],
#    ["Mobile - On-Road Diesel Heavy Duty Vehicles",2115493.807954973705],
#    ["Fuel Comb - Electric Generation - Coal",1515650.1968273001],
#    ["Mobile - Commercial Marine Vessels",1244627.27607785525],
#    ["Mobile - Non-Road Equipment - Diesel",1099016.567009694594612422549633628], # You think that's enough digits?
#    ["Biogenics - Vegetation and Soil",903149.8105],
#    ["Mobile - Locomotives",712189.6176848813],
#    ["Industrial Processes - Oil & Gas Production",710933.7138722840557],
#    ["Fuel Comb - Industrial Boilers, ICEs - Natural Gas",642540.657706709174],
#    ["Mobile - Non-Road Equipment - Gasoline",235238.19493125660250863275279191072],
#    ["Fuel Comb - Residential - Natural Gas",227612.815848],
#    ["Mobile - On-Road Diesel Light Duty Vehicles",172578.6516205237318],
#    ["Industrial Processes - NEC",170522.93136053155],
#    ["Fuel Comb - Comm/Institutional - Natural Gas",165323.54020325538],
#    ["Fires - Prescribed Fires",152426.2700739405],
#    ["Mobile - Aircraft",146698.9919009162777],
#    ["Fuel Comb - Electric Generation - Natural Gas",145598.57985380726],
#    ["Fires - Wildfires",119147.156089842693],
#    ["Fuel Comb - Industrial Boilers, ICEs - Coal",118903.610091941],
#    ["Industrial Processes - Cement Manuf",118184.0559276],
#    ["Fuel Comb - Industrial Boilers, ICEs - Biomass",115046.42093804],
#    ["Waste Disposal",110266.77165890398],
#    ["Fuel Comb - Industrial Boilers, ICEs - Oil",88390.402378348136],
#    ["Mobile - On-Road non-Diesel Heavy Duty Vehicles",81039.3558080999926],
#    ["Industrial Processes - Pulp & Paper",73721.36235279],
#    ["Industrial Processes - Chemical Manuf",72435.739891994],
#    ["Fuel Comb - Electric Generation - Oil",71949.2108531629],
#    ["Industrial Processes - Petroleum Refineries",69383.83988621804],
#    ["Mobile - Non-Road Equipment - Other",66858.3455026605526201586119635343],
#    ["Industrial Processes - Ferrous Metals",59850.215464695],
#    ["Fuel Comb - Industrial Boilers, ICEs - Other	",56806.65623424155],
#    ["Fuel Comb - Comm/Institutional - Oil",47882.254799940074138115],
#    ["Fuel Comb - Residential - Oil",35528.75872293563],
#    ["Fuel Comb - Residential - Other",34645.72136724],
#    ["Fuel Comb - Residential - Wood",30652.19006798352439],
#    ["Fuel Comb - Electric Generation - Other",25134.882457719],
#    ["Fires - Agricultural Field Burning",20358.4399271808],
#    ["Industrial Processes - Non-ferrous Metals",16424.143726821],
#    ["Fuel Comb - Comm/Institutional - Other",12295.73220001728],
#    ["Fuel Comb - Electric Generation - Biomass",12098.32399],
#    ["Fuel Comb - Comm/Institutional - Coal	",9274.185298508],
#    ["Fuel Comb - Comm/Institutional - Biomass",8553.012918299],
#    ["Miscellaneous Non-Industrial NEC",7053.7410156504],
#    ["Industrial Processes - Storage and Transfer",5737.57602756105],
#    ["Industrial Processes - Mining",5495.2439986],
 #   ["Solvent - Industrial Surface Coating & Solvent Use",2817.63852950915],
#    ["Bulk Gasoline Terminals",451.51866066],
#    ["Solvent - Graphic Arts",126.75700865],
#    ["Dust - Construction Dust",84.69407629],
#    ["Gas Stations",13.54695],
#    ["Solvent - Degreasing",10.91194500005],
#    ["Solvent - Dry Cleaning",0.744]
    # Starting here are consolidated categories
    ["Transportation",2510022.21442440701+2115493.807954973705+1244627.27607785525+1099016.567009694594612422549633628+712189.6176848813+ 235238.19493125660250863275279191072+172578.6516205237318+146698.9919009162777+81039.3558080999926+66858.3455026605526201586119635343 + 451.51866066+13.54695], # All "Mobile ..." categories, "Bulk Gasoline Terminals", "Gas Stations"
    ["Electricity",1515650.1968273001+145598.57985380726+71949.2108531629+25134.882457719+12098.32399], # "Fuel Comb - Electric Generation - ..."
    ["Biogenic, Fire",903149.8105+152426.2700739405+119147.156089842693+20358.4399271808], # "Biogenic ...", "Fires ..."
    ["Industry",710933.7138722840557+642540.657706709174+170522.93136053155+118903.610091941+118184.0559276+115046.42093804+88390.402378348136 + 73721.36235279+72435.739891994+69383.83988621804+59850.215464695+56806.65623424155+16424.143726821+5737.57602756105], # "Industrial Processes ..." and "Fuel Comb - Industrial ..."
    ["Residential",227612.815848+35528.75872293563+34645.72136724+30652.19006798352439], # "Fuel Comb - Residential..."
    ["Commercial and Institutional",165323.54020325538+47882.254799940074138115+12295.73220001728+9274.185298508+8553.012918299+5495.2439986+2817.63852950915], # "Fuel Comb - Comm/Institutional ..."
    ["Waste",110266.77165890398], # "Waste Disposal"
    ["Solvents, Other",7053.7410156504+126.75700865+84.69407629+10.91194500005+0.744] # "Miscellaneous Non-Industrial NEC", "Solvents ...", "Dust - Construction Dust"
]

helper.save_image({
    "filename":"us_nox.jpg",
    "status":"Done",
    "details":"Major sources of NOx emissions in the United States. There were 57 categores given (a few with zero value), and I consolidated them into this short list. Transportation include gas stations and bulk gasoline terminals.",
    "table":us_nox_table,
    "references":["nei2014"],
    "source_file":"air_pollution.py"
})