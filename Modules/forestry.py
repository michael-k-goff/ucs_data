# Calculations related to the forestry section
# -*- coding: utf-8 -*-

import helper

land_use_table = [
    ["<b>Fiber Source</b>","<b>Yield, tons/ha/yr</b>"],
    # Mostly from Table 1, reference paper_yield2
    ["Eucalyptus","15-40"],
    ["Softwood","0.8-1.5"],
    ["Acacia","12-22.3"],
    ["Hemp","6.72-20"],
    ["Flax","0.9"],
    ["Arundo donax","7-39"],
    ["Bamboo","4-4.5"],
    ["Kenaf","15"],
    ["Elephant grass","12-45"],
    ["Wheat Straw","2-4"],
    ["Bagasse","9"],
    ["Hardwood","0.37-0.64"], # Table 2, reference paper_yield
    ["Pine","2.5-4.4"] # Table 2, reference paper_yield
]

helper.save_image({
    "filename":"fiber_land_use.jpg",
    "status":"Done",
    "table":land_use_table,
    "details":"Estimated yields for various sources of fiber. The hardwood and pine figures come from Hart, and the rest are from Favero et al.",
    "references":["paper_yield","paper_yield2"],
    "source_file":"forestry.py"
})

########################

# Enhanced version of the forest products graphic

forest_products_table = [
    ["<b>Product</b>","<b>Annual Production, millions of cubic meters, est. 2016</b>"],
    ["Wood Panels",416],
    ["Fiber Finish",415],
    ["Wood Fuel, Charcoal, Pellets",1863],
    ["Corrugated Paper/Packaging",409*240.211/412.645],
    ["Newsprint",409*22.199/412.645],
    ["Corrugated Paper/Packaging",409*240.211/412.645],
    ["Graphic Paper",409*121.309/412.645],
    ["Other Paper",409*29/412.645]
]

helper.save_image({
    "filename":"wood_products2.jpg",
    "status":"Done",
    "table":forest_products_table,
    "details":"This is an enhancement of the old wood_products.jpg graphic, with the Paper section broken down into four categories. Graphic paper is a general term for paper for publishing and writing. The 2016 FAO reference is used for the major categories (same as before), and the 2017 reference is used to estimate the breakdown of paper into four subcategories. Note that the filename has a 2 because I am, for the moment, using this file in a different place than the original.",
    "references":["fao_wood2016","forest_yearbook"],
    "source_file":"forestry.py"
})

########################

# Agroforestry yield plot.

ler_table = [
    ["<b>System</b>","<b>Land Equivalency Ratio</b>","<b>Details</b>","<b>Reference</b>"],
    ["Cocoa Agroforestry","1.61","Bolivia field trial","Schneider et al."],
    ["Rubber Agroforestry","0.89","Thailand. Biodiversity benefits found.","Warren-Thomas et al."],
    ["Pear, maize, faba intercrop","2.98-3.03","Guatemala field trial","Jose and Gordon"],
    ["Wheat and peanut","1.50","Bangladesh field trial","Uddin et al."],
    ["Roselle/Cowpea","1.151-1.226","Egypt field trial","Gendy et al."],
    ["Agroforestry systems","2-3","Systems in Brandenburg and Lower Saxony, Germany","Seserman et al."],
    ["Jackfruit/Eggplant","2.17","Study in Bangladesh","Rahaman et al."],
    ["Oil palm/Cocoa","1.44","Study in Indonesia","Khasanah et al."],
    ["Oil palm/Pepper","0.99","Study in Indonesia","Khasanah et al."],
    ["Apple/Peanut","1.43-1.45","Nine year Chinese study","Xu et al."],
    ["Apple/Millet","1.41-1.43","Nine year Chinese study","Xu et al."],
    ["Apple/Maize","1.39-1.45","Nine year Chinese study","Xu et al."],
    ["Apricot/Peanut","1.34","Field experiment in semi-arid Khorchin region in Liaoning, China","Bai et al."],
    ["Apricot/Millet","1.44","Field experiment in semi-arid Khorchin region in Liaoning, China","Bai et al."],
    ["Apricot/Sweet potato","1.33","Field experiment in semi-arid Khorchin region in Liaoning, China","Bai et al."],
    ["Leucaena/maize","1.17","Field experiment in Kenya","Jama et al."],
    ["Senna/maize","1.34","Field experiment in Kenya","Jama et al."],
    ["Lemon-based Agroforestry","1.59-1.73","Five field trials in Bangladesh","Hasan et al."]
]

helper.save_image({
    "filename":"agroforestry_ler.jpg",
    "status":"Done",
    "table":ler_table,
    "details":"A review of several studies of land equivalency ratios for agroforestry systems. The land equivalency ratio is the ratio of the amount of land that would be required to grow all products on monocultures in the same climate to the land required for the mixed crop system. An LER greater than 1 implies that the agroforestry system is more efficient with land. Where available, I've included the crops grown, the location of the study, and other relevant details.",
    "references":["ler1","ler2","ler3","ler4","ler5","ler6","ler7","ler8","ler9","ler10","ler11","ler12"],
    "source_file":"forestry.py"
})

########################

# Forest carbon sequestration potential

c_seq_table = [
    ["<b>Method</b>","<b>Annual carbon sequestration potential, billions of tons CO<sub>2</sub></b>","<b>Source</b>"],
    ["Tropical reforestration at $30/ton CO<sub>2</sub>",0.49,"Busch et al."],
    ["Tropical reforestration at $50/ton CO<sub>2</sub>",0.84,"Busch et al."],
    ["Tropical reforestration at $100/ton CO<sub>2</sub>",1.84,"Busch et al."],
    ["Agroforestry",3.4,"Kim et al."],
    ["<b>Method</b>","<b>Total potential carbon sequestration potential, billions of tons CO<sub>2</sub>e</b>","<b>Source</b>"],
    ["Forestation",205*22./8,"Bastin et al."],
    ["Forestation","214.5-297","Lewis et al."], # Based on four estimates provided in the text.
    ["Natural tropical regeneration over 40 years",31.09,"Chazdon et al."],
    ["Biosphere carbon potential","357.5-371.25","Lal et al."]
]

helper.save_image({
    "filename":"forest_c_seq.jpg",
    "status":"Done",
    "table":c_seq_table,
    "details":"Summary of the ability of forests to sequester carbon. Overlaps with geoengineering material. The tropical reforestation figures are from Busch et al. and agroforestry from Kim et al.",
    "references":["busch","agroforestry_c","bastin","lewis","chazdon","biosphere_c"],
    "source_file":"forestry.py"
})

########################

# Wildfire damages

helper.save_image({
    "filename":"wildfire_losses.jpg",
    "status":"Done",
    "details":"Simple plot. Portray annual wildfire losses in the United States as follows. Costs (preparation and firefighting) are $7.6-62.8 billion, and damages are $63.5-285.0 billion. That's 2016 USD.",
    "references":["wildfire_loss"],
    "source_file":"forestry.py"
})

helper.save_image({
    "filename":"fire_cause.jpg",
    "status":"Done",
    "details":"Another simple plot. Show basic stats on fires caused by humans and by lightning (the only two categories in the Fire Center's chart). From 2001 to 2018 there were on average 60,467 human-caused wildfires per year and 2,036,378 acres burned. There were 9753 lightning-caused fires and 3,815,064 acres burned. Thus the lightning-caused fires tend to be bigger on average. The reference has a weird retro look to it.",
    "references":["nifc"],
    "source_file":"forestry.py"
})

helper.save_image({
    "filename":"wui.jpg",
    "status":"Done",
    "details":"Another simple one. Show evolution of wildland-urban interface, which is the development that is exposed to wildfire risk. In 1990, 30.8 million houses and 581,000 km<sup>2</sup> developed area were in the WUI. In 2010, the figures were 43.4 million houses and 770,000 km<sup>2</sup>. In the actual fire perimeters from all wildfires from 1990-2015, there were 177,000 houses in 1990 and 286,000 houses in 2010.",
    "references":["wui"],
    "source_file":"forestry.py"
})

helper.save_image({
    "filename":"wildfire_deaths.jpg",
    "status":"Done",
    "details":"This should be another easy one. The figures are 3753 direct deaths from wildfires per year (Doerr and Santin) and 339,000 estimated deaths per year from particulates (Johnston et al.).",
    "references":["doerr","wildfire_deaths"],
    "source_file":"forestry.py"
})

wf_table = [
    ["<b>Year</b>","<b>(Average) hectares burned</b>","<b>Source</b>"],
    ["17th Century","500,000-1.6 million","Reynolds and Pierson"],
    ["Pre-1800","1.8 million","Stephens et al."],
    ["1979-1988","136,000","Buechi et al."],
    ["1989-1998","110,000","Buechi et al."],
    ["1999-2008","280,000","Buechi et al."],
    ["2009-2018","287,000","Buechi et al."],
    ["2018","770,000","Ricón"],
    ["2019","80,000","Ricón"],
    ["2020","1.8 million","Ricón"]
]

helper.save_image({
    "filename":"wildfire_trends.jpg",
    "status":"Done",
    "details":"A basic plot showing trends in annual acres burnt in California.",
    "table":wf_table,
    "references":["stephens_wildfire","wildfire_17th","wildfire_buechi","wildfire_nintel"],
    "source_file":"forestry.py"
})

########################

# Drivers of deforestation

deforest_table = [
    ["<b>Factor</b>","<b>Percentage of Deforestation, 2001-15</b>"], # Sample-based estimates instead of map-based estimates.
    ["Commodity Agriculture","27%"],
    ["Forestry","26%"],
    ["Subsistence Agriculture","24%"],
    ["Wildfire","23%"],
    ["Urbanization","0.6%"],
    ["<b>Region</b>","<b>Tree Cover Loss, 2001-15, millions of hectares</b>"], # Table S1. Remember to scroll down.
    ["North America","70"],
    ["Latin America","78"],
    ["Europe","15"],
    ["Africa","39"],
    ["Russia, China, and South Asia","64"],
    ["Southeast Asia","39"],
    ["Austrialia and Oceania","10"]
]

helper.save_image({
    "filename":"deforestation_causes.jpg",
    "status":"Done",
    "table":deforest_table,
    "details":"A two-in-one plot, deforestation by major cause and the total tree loss by major region. The paper actually uses the term 'shifting agriculture' instead of 'subsistence agriculture', basically referring to how small and medium farms convert forest and shrub land. I think they mean the same thing but am not 100% sure.",
    "references":["deforestation"],
    "source_file":"forestry.py"
})

deforest_table2 = [
    ["<b>Commodity</b>","<b>Annual deforestation, thousands of acres, average 2005-2013</b>"],
    ["Cattle","2110"],
    ["Oilseeds","950.609"],
    ["Forestry Logging","678.744"],
    ["Cereals (excluding rice, wheat)","445.902"],
    ["Vegetables, fruits, nuts","379.251"],
    ["Paddy Rice","287.785"],
    ["Other Crops","184.02"],
    ["Sugarcane/Sugarbeet","57.796"],
    ["Wheat","53.342"],
    ["Fiber Crops","25.297"]
]

helper.save_image({
    "filename":"deforestation_causes2.jpg",
    "status":"Done",
    "details":"Drivers of deforestation again, this time by crop that land is cleared for. This only covers tropical deforestation, which is about 95% of all deforestation according to the paper. The data fundamentally comes from Pendrill et al., but I used figures from the OWID page for convenience.",
    "references":["deforestation2","deforestation3"],
    "table":deforest_table2,
    "source_file":"forestry.py"
})