# Environmental impacts of agriculture.
# This module is created for (at least initially) plots for the Environmental Impacts of Agriculture section.

import helper
import diet

#######################################

# Overall land use stuff

helper.save_image({
    "filename":"ag_land_trends.jpg",
    "status":"Done",
    "details":"Plot the land taken up worldwide by crops and pasture. For this one, I will ask you to fetch the data from FAOSTAT, which shouldn't be any harder than me trying to process it here. Go to the <a href=\"http://www.fao.org/faostat/en/#data/RL\">land use page</a>. For the upper left box on countries, click the 'Regions' tab and select 'World + (Total). For the 'Elements' box, select 'Area'. For the 'Items' box, select 'Cropland'. For the 'Year' box, click 'Select All'. That should give a time series of world crop land by year from 1961 to 2017; make a time series plot out of it. Now do all taht again, except for 'Items', select 'Land under perm. meadows and pastures'. Put these two time series plots side by side and give them the same y-axis scale.",
    "references":["faostat"],
    "source_file":"ag_environment.py"
})

#######################################

# Area required by various crops

yields, yield_keys = diet.get_yields()
food_share_world = diet.get_caloric_intake("Modules/FAO/per_cap3.csv")
diet.add_yields(food_share_world, yields, yield_keys)
table_keys = ["Eggs","Apples and products","Bananas","Oranges, Mandarines","Barley and products","Oats","Soyabeans","Beans","Mutton & Goat Meat","Bovine Meat","Potatoes and products","Coffee and products","Nuts and products","Wheat and products","Tomatoes and products","Poultry Meat","Pelagic Fish","Pigmeat","Milk - Excluding Butter","Maize and products","Rice (Milled Equivalent)"]

crop_land_table = [
    ["<b>Crop</b>","<b>Area required: m^2 per kcal per day</b>"]
]

for i in range(len(table_keys)):
    crop = food_share_world[table_keys[i]]
    # Units are m^2/kcal/day
    # Lettuce is from looking up land use in the table and applying the nutritive factor of 12 kcal per 100 grams.
    # Cauliflour and Spinach are similar
    crop_land_table = crop_land_table + [[table_keys[i],10000.*crop["Yield"]*crop["Food supply quantity (kg/capita/yr)"]/crop["Food supply (kcal/capita/day)"]]]
crop_land_table = crop_land_table + [["Lettuce",1.39],["Cauliflower",1/186250./9*10000*365],["Spinach",1/299926./16*10000*365]]

helper.save_image({
    "filename":"area_by_crop.jpg",
    "status":"Done",
    "details":"Show area taken up by select crops, in square meters per kcal per day. All crop figures come from the FAO, though the Nutritive Factors page was used to convert crops from mass to calorie content. The fish item assumes aquaculture production. With the exception of using the nutritive factors page for Lettuce, Cauliflower, and Broccoli, the method of calculating area taken up by crops is exactly the same as it is for the diet land use plot, except now we are looking at individual crops rather than whole diets. Let me know if there are any other particular crops that really ought to be included here, though we can't list everything because the FAO has hundreds of them.",
    "table":crop_land_table,
    "references":["faostat","nutritive","meat_land_use","aq_land_use"],
    "source_file":"ag_environment.py"
})

########################################

# Greenhouse gases from various crops. Builds off the land area stuff above.

# Taking out a few of the keys due to questionable numbers
table_keys = ["Eggs","Apples and products","Barley and products","Oats","Soyabeans","Beans","Mutton & Goat Meat","Bovine Meat","Potatoes and products","Coffee and products","Wheat and products","Tomatoes and products","Poultry Meat","Pelagic Fish","Pigmeat","Milk - Excluding Butter","Maize and products","Rice (Milled Equivalent)"]

crop_ghg_table = [
    ["<b>Crop</b>","<b>GHG emissions: grams CO2e per kcal</b>"],
]

for i in range(len(table_keys)):
    crop = food_share_world[table_keys[i]]
    # Units are m^2/kcal/day
    crop_ghg_table = crop_ghg_table + [[table_keys[i],crop["GHG"]*crop["Food supply quantity (kg/capita/yr)"]/crop["Food supply (kcal/capita/day)"]]]
crop_ghg_table = crop_ghg_table + [["Lettuce",10.94], ["Mealworm",food_share_world["Poultry Meat"]["GHG"]/2.0]]
# For mealworm, there are several studies cited in the 'mealworm' reference. The factor is a ballpark.

helper.save_image({
    "filename":"ghg_by_crop.jpg",
    "status":"Done",
    "details":"Show greenhouse gases from select crops, in square meters per kcal per day. All emissions figures come from Clark and Tilman, with FAOSTAT to convert mass to calories (and the nutritive factors page to convert mass to calories for Lettuce), except the mealworm figures are from van Huis and Oonincx. Unlike the land use plot, the studies on fish are a mix of aquaculture and wild catch. Lettuce may strike the reader as odd, and this comparison is a bit unfair to our leafy green friend because it is assessed on a strictly calorific basis.",
    "table":crop_ghg_table,
    "references":["faostat","nutritive","meat_land_use","mealworm"],
    "source_file":"ag_environment.py"
})

########################################

# World greenhouse gases from agriculture

ghg_dict = {
    # http://www.fao.org/faostat/en/#data/GT
    "Enteric Fermentation":2100076.4158,
    "Manure Management":349705.3685,
    "Rice Cultivation":533245.4818,
    "Synthetic Fertilizers":704441.912,
    "Manure applied to Soils":191129.0905,
    "Manure left on Pasture":866872.6649,
    "Crop Residues":223915.1636,
    "Cultivation of Organic Soils":127889.6925,
    "Burning - Crop residues":30848.4542,
    "Burning - Savanna":282352.7424,
    # From http://www.fao.org/faostat/en/#data/GN
    "Energy usage":882589.2226,
    # The rest are from http://www.fao.org/faostat/en/#data/GL
    "Forest Land":1067201.1242,
    "Cropland":667092.8584,
    "Grassland":46263.4602,
    "Burning Biomass":1370513.3511
}

ghg_table = [
    ["<b>Source</b>","<b>Thousands of tons CO2e per year</b>"],
    ["Enteric Fermentation",2100076.4158],
    ["Manure",ghg_dict["Manure Management"]+ghg_dict["Manure applied to Soils"]+ghg_dict["Manure left on Pasture"]],
    ["Rice Cultivation",533245.4818],
    ["Synthetic Fertilizers",704441.912],
    ["Nitrous Oxide from Crop Residues",223915.1636],
    ["Nitrous Oxide from Organic Soils",127889.6925],
    ["Burning",ghg_dict["Burning - Crop residues"]+ghg_dict["Burning - Savanna"]],
    ["Energy Usage",882589.2226],
    ["Land Use Change",ghg_dict["Forest Land"]+ghg_dict["Cropland"]+ghg_dict["Grassland"]+ghg_dict["Burning Biomass"]]
]

helper.save_image({
    "filename":"ghg_ag.jpg",
    "status":"Done",
    "table":ghg_table,
    "details":"Major sources of greenhouse gases from agriculture. Figures all come from the FAO, though I consolidated some of the categories.",
    "references":["faostat"],
    "source_file":"ag_environment.py"
})

###########################################################

# Water intensity

# See p. 16 for a table of water per kg/kcal for major crop families. https://waterfootprint.org/media/downloads/Report47-WaterFootprintCrops-Vol1.pdf
# For animal products, see https://waterfootprint.org/en/water-footprint/product-water-footprint/water-footprint-crop-and-animal-products/ and associated PDF.

water_table = [
    ["<b>Crop</b>","<b>Water requirement: liters/kcal</b>"],
    # From the crop study, p. 16 for overall impact of crops. Liters per kg.
    ["Sugar crops",0.68],
    ["Vegetables",1.34],
    ["Roots and Tubers",0.47],
    ["Fruits",2.1],
    ["Cereals",0.51],
    ["Oil Crops",0.81],
    ["Pulses",1.19],
    ["Spices",2.35],
    ["Nuts",3.63],
    ["Stimulants",16.4],
    # Some specific values from the crop study. Conversion from kg to kcal from the nutritive factors page.
    ["Maize",1222./10./356.],
    ["Wheat",1827./10./334.],
    ["Almonds",8047./10./236.],
    ["Lettuce",237./10./12.],
    # From the animal products study
    ["Milk",1.82],
    ["Eggs",2.29],
    ["Poultry",3.0],
    ["Butter",0.72],
    ["Pork",2.15],
    ["Mutton",4.25],
    ["Beef",10.19],
    # From 'mealworm'
    ["Mealworm",2.0] # Study says poultry is 50% more than mealworm, on an edible protein basis. Here I am doing calories.
]

helper.save_image({
    "filename":"water_crops.jpg",
    "status":"Done",
    "details":"Show water consumption per kcal of various crops and foods. Data on crops come from the first Mekonnen and Hoekstra study, and data on animal products come from the second Mekonnen and Hoekstra study. Mealworm data from van Huis and Oonincx. For maize, wheat, almonds, and lettuce, the FAO's nutritive factors page was used to convert mass to calories. There are hundreds of crops that could be added, but here I am keeping it to broad families and a few major specific crops.",
    "table":water_table,
    "references":["water_crops1","water_crops2","nutritive","mealworm"],
    "source_file":"ag_environment.py"
})

####################################

# Phosphorous conservation

# Old text on the site that was here: 

# If forests or perennial plants are adjacent to arable land, then soil phosphorus losses are reduced by 60-90% [pasture_p].

#Phosphorus can be recovered from municipal water systems, but feasibility at scale is uncertain [muni_p]. Each person produces an estimated 1.96 grams of phosphorous per day through municipal water systems [muni_p_recovery], or about 5 million tons annually, or 4% of world demand, worldwide.
helper.save_image({
    "filename":"phosphorous_conservation.jpg",
    "status":"Done",
    "details":"Show phosphorous conservation opportunities. They are 60-90% from planting forests or perennial plants adjacent to arable land (Udawatta et al.), and 4% from municipal wastewater recovery (Gilmour et al.). Also note, via Sartorious et al., that the logistical feasibility of wastewater recovery is uncertain. More might be added here if there are other good ideas, but this is a low priority topic.",
    "references":["pasture_p","muni_p_recovery","muni_p"],
    "source_file":"ag_environment.py"
})

# Older first paragraph: Phosphorous is a critical element in the manufacture of fertilizers. In 2014, the world produced 223 million tons (mmt) of phosphate rock [usgs2016], of which 82% rock was used to produce fertilizer as of 2010 [phosphate_critique]. World reserves, defined as phosphate resources that can be produced economically (about $100/ton [ifdc]) have been estimated at 60,000 million tons [ifdc] to 69,000 mmt [usgs2016]--140 years of production if fertilizer demand doubles. However, most known reserves are in Morocco [usgs2016], posing a risk to security of supply, and the aforementioned reserve estimates are in doubt [phosphate_critique]. More pessimistic projections put the date of a peak in phosphorous production as early as 2030 [peak_p]. We are more inclined to believe the optimistic projections, but with limited transparent data, an international organization such as the Food and Agriculture Organization of the United Nations should undertake a more thorough analysis.

####################################################################

# Greenhouse gas intensity, based on this 2021 paper: https://www.nature.com/articles/s43016-021-00358-x
# See supplementary material: https://static-content.springer.com/esm/art%3A10.1038%2Fs43016-021-00358-x/MediaObjects/43016_2021_358_MOESM1_ESM.pdf

ghg_table_2021 = [
    ["<b>Crop Family</b>","<b>Greenhouse gas emissions (millions of tons CO<sub>2</sub>e)</b>"],
    ["Plant-based food",5109],
    ["Animal-based food",9796],
    ["Other (e.g. industrial crops)",2413],
    ["Total",17318],
    ["<b>By agriculture operation</b>",""],
    ["Mining, manufacturing, and transporting agricultural materials",666],
    ["Processing and transportation of food",1457],
    ["Fuel and energy use on farm",169],
    ["Farmland emissions",3084],
    ["Rice cultivation",1274],
    ["Synthetic fertilizers and manure",1969],
    ["Enteric fermentation",3160],
    ["Manure management",317+130],
    ["Land use change",5096]
]

helper.save_image({
    "filename":"ghg_ag_2021.jpg",
    "status":"Not Done",
    "table":ghg_table_2021,
    "details":"An update to agricultural emissions by phase of production and by crop type. This supersedes an older graphic from FAOSTAT.",
    "references":["ag_ghg_2021"],
    "source_file":"ag_environment.py"
})