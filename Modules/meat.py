# Meat-related figures

import helper

# Meat, as share of total caloric intake

# All from FAOSTAT. Go to Old Food Balances, Region is World, select the given years, and for products (aggregated), take (Meat + (Total) + Seafood + (Total)) / Grand Total + (Total)
meat_intake = [
    ["<b>Year</b>","<b>Portion of caloric intake from meat, worldwide</b>"],
    ["1961",(110.+17.)/2196],
    ["1980",(155.+23.)/2490],
    ["2000",(203.+28.)/2727],
    ["2013",(237.+34.)/2884],
    ["<b>Region</b>","<b>Portion of caloric intake from meat, 2013</b>"],
    ["World",(237.+34.)/2884],
    ["Africa",(90.+20.)/2624],
    ["Europe",(351.+47.)/3367],
    ["China",(483.+50.)/3108],
    ["India",(15.+9.)/2459],
    ["United States",(424.+35.)/3682],
    ["South America",(381.+18.)/3027]
]

helper.save_image({
    "filename":"meat_share.jpg",
    "status":"Done",
    "table":meat_intake,
    "details":"Two side-by-side tables showing how meat and seafood consumption, as a share of total caloric intake, has generally gone up over time and varies by world region. We could do a year-by-year time series from 1961 to 2013 (and with some effort extend it to 2017) if desired, and we could add any region or country to the list as well. Feel free to suggest additions or add them yourself from the FAOSTAT Food Balances data set.",
    "references":["faostat"],
    "source_file":"meat.py"
})

############################################

# Energy density of foods.
# These are done by going to the Old Food Balances page and looking up (Worldwide, 2013, though it shouldn't matter) Food Supply, calorie supply, protein supply, fat supply.
density_table = [
    ["<b>Food Group</b>","<b>Calorie Density (kcal per gram food)<b>","<b>Protein Density (grams protein per gram food)</b>","<b>Fat Density (grams fat per gram food)<b>"],
    ["Cereals",1292/ (147.06/365*1000), 0.06780607557137935, 5.83 / (147.06/365*1000)],
    ["Starchy Roots",141 / (63.36/365*1000), 2.27/(63.36/365*1000), 0.26/(63.36/365*1000)],
    ["Meat (land-based)",237 / (43.22/365*1000), 14.54/(43.22/365*1000), 19.33/(43.22/365*1000)],
    ["Seafood",34. / (18.98/365*1000), 5.22/(18.98/365*1000), 1.18/(18.98/365*1000)],
    ["Vegetables",95. / (140.48/365*1000), 4.91/(140.48/365*1000), 0.81/(140.48/365*1000)],
    ["Fruit",97. / (77.87/365*1000), 1.13/(77.87/365*1000), 0.63/(77.87/365*1000)],
    ["Eggs",36. / (9.19/365*1000), 2.79/(9.19/365*1000), 2.53/(9.19/365*1000)],
    ["Milk",138. / (90./365*1000), 8.22/(90./365*1000), 7.47/(90./365*1000)]
]

helper.save_image({
    "filename":"nutrient_density.jpg",
    "status":"Done",
    "table":density_table,
    "details":"The protein density of cereals has been revised down a bit. The others are the same. I still think the protein density of cereals is suspiciously high here, but that seems to be what FAOSTAT says. I'll look into it more later. I checked protein density for other foods and they seem fine.",
    "references":["faostat"],
    "source_file":"meat.py"
})

#########################################3

# Feed conversion ratios

fcr_table = [
    ["<b>Animal Product</b>","<b>Feed conversion ratio: ratio of feed in to animal product out, by mass</b>"],
    # From alexander_fcr
    ["Poultry",3.3],
    ["Pork",6.4],
    ["Beef",25],
    ["Lamb and Mutton",15],
    ["Eggs",2.3],
    ["Milk",0.7],
    # From alexander_fcr2
    ["Mealworm",1.8],
    ["Crickets",2.1],
    ["Tilapia",4.6],
    ["Chinese carp",4.9],
    ["Cultured meat",4],
    ["Imitation meat (based on soy)",0.29],
    # From aq_land_use
    ["Crustacean",1.4/0.3] # Average FCR for crustacean (supplementary material, Table S5), divided by edible biomass figure (Table S1)
]

helper.save_image({
    "filename":"fcr.jpg",
    "status":"Done",
    "details":"Show feed conversion efficiency for various meat and animal products and substitutes. FCE is the ratio of feed consumed to edible biomass produced, by mass. It is not to be confused with the related concept feed conversion ratio. Crustaceans are from Froehlich et al.; mealworm, crickets, tilapia, Chinese carp, cultured meat, and imitation meat are from Alexander et al. (2017), and the rest are from Alexander et al. (2016).",
    "table":fcr_table,
    "references":["alexander_fcr","alexander_fcr2","aq_land_use"],
    "source_file":"meat.py"
})

########################################

# Yield per animal

# Based on Livestock Primary, World, Yield, 2017. http://www.fao.org/faostat/en/#data/QL
# All figures are in kg, per slaughter or per year, unless otherwise noted
yield_animal = {
    "Eggs":10.2175,
    "Beef":217.6, # Cattle
    "Poultry":1.6383, # Chicken
    "Goat":12.6, # Goat
    "Pork": 80.7, # Pig
    "Milk":2430.2, # Cow milk
    "Duck": 1.4809,
    "Rabbit":1.5252,
    "Mutton":16.7, # Sheep
    "Turkey":8.9635
}

# Lifespan
# Hens typically lay eggs for about 1 year. fao_egg
# Based on dairy_cow_life, 4 years for dairy cow.

yield_animal["Milk"] *= 4

# Convert mass to kcal. Based on 'nutritive'. kcal per 100 grams.
ess_factors = {
    "Eggs":163,
    "Beef":233, # Based on "Beef Canned"
    "Poultry":185,
    "Goat":123,
    "Pork":220,
    "Milk":61, # Cow milk
    "Duck":291,
    "Rabbit":118,
    "Mutton":263,
    "Turkey":126
}

for key in yield_animal:
    yield_animal[key] *= ess_factors[key]*10

# Human lifetime. Assume 73 year life expectancy, 2884 kcal per day.
num_an_table = [["<b>Food source</b>","<b>Animals required</b>"]] + [[key,73*365.2425*2884.*0.05/yield_animal[key]] for key in yield_animal]

helper.save_image({
    "filename":"animal_count.jpg",
    "status":"Done",
    "table":num_an_table,
    "details":"This plot shows the number of animals that are slaughtered, or who produce eggs or milk over their lifetimes, to provide a human diet. The assumptions are that the animal product provides 5% of a person's caloric intake (a bit high for a single product, but whatever), over a 73 year lifespan. This assumes 2884 calories per day, including loss and wastage. Yields from animals are given from FAOSTAT, with the Nutritive Factors page to convert from mass to calories. I assume a 1 year productive lifespan for egg-laying hens (see FAO egg book) and 4 years for dairy cows (see the Compassion in World Farming reference).",
    "references":["faostat","dairy_cow_life","fao_egg","nutritive"],
    "source_file":"meat.py"
})

###########################

# US beef efficiency
eff_table = [
    ["<b>Metric</b>","<b>Improvement, 1977-2007</b>"],
    ["Greenhouse gas emissions","16%"],
    ["Land use","33%"],
    ["Water","12%"],
    ["Feed consumption","19%"]
]

helper.save_image({
    "filename":"beef_improvement.jpg",
    "status":"Done",
    "table":eff_table,
    "details":"Overall efficiency gains in US beef production from 1977-2007",
    "references":["grassfed"],
    "source_file":"meat.py"
})

############################

# Grass-fed beef comparison
grass_fed_table = [
    ["<b>Metric</b>","<b>Impact of grass-fed beef, relative to feedlot</b>"],
    ["Greenhouse Gases","168%"],
    ["GHG (Lupo et al., no SOC)","137%"],
    ["GHG (Lupo et al., SOC)","76-85%"],
    ["Fossil Fuel Energy","140%"],
    ["Number of Cattle","178%"],
    ["Manure","200%"],
    ["Nitrogen Pollution","200%"],
    ["Phosphorous Excretion","200%"],
    ["Land Use (Tichenor et al.)","718%"],
    ["Fossil Fuel Energy (Tichenor et al.)","83%"],
    ["Water (Tichenor et al.)","76%"],
    ["Eutrophication (Tichenor et al.)","244%"],
    ["Acidification (Tichenor et al.)","238%"]
]

helper.save_image({
    "filename":"grass_fed.jpg",
    "status":"Done",
    "table":grass_fed_table,
    "details":"Various environmental impacts of grass-fed beef, relative to conventional. The most controversial of these is greenhouse gases, and in particular the magnitude of the soil carbon sequestration effect. I don't know what the right answer on that, so I am including values with and without. All figures are from the Clapper study unless indicated otherwise. SOC stands for soil organic carbon and indicates whether SOC is incorporated into the estimate.",
    "references":["grassfed","grassfed2","grassfed3"],
    "source_file":"meat.py"
})

################################

# Aquaculture statistics

# See http://www.fao.org/3/ca5495t/CA5495T.pdf, p. 24 of the PDF.
aqua_table = [
    ["<b>Year</b>","<b>Aquaculture: millions of tons</b>","<b>Wild catch: millions of tons</b>"],
    ["1980",4.7,67.2],
    ["1990",13.1,84.7],
    ["2000",32.4,93.6],
    ["2010",57.7,87.1],
    ["2017",80.1,92.5]
]

helper.save_image({
    "filename":"aquaculture_stats.jpg",
    "status":"Done",
    "table":aqua_table,
    "details":"Aquaculture and wild catch statistics. Do a time series plot with the wild catch figures on the bottom, and the aquaculture figures on top of them. This should show clearly the aquaculture is augmenting, not replacing, the wild catch supply.",
    "references":["fao_aqua"],
    "source_file":"meat.py"
})

##################################

# Fish in fish out
fifo_table = [
    ["<b>Product</b>","<b>Fish-in-fish-out, 2015</b>"],
    ["Crustaceans",0.46],
    ["Marine Fish",0.53],
    ["Salmon & Trout",0.82],
    ["Eels",1.75],
    ["Cyprinids",0.02],
    ["Tilapias",0.15],
    ["Other Freshwater",0.13],
    ["Aquaculture overall",0.22],
    ["Aquaculture overall, 2000",0.63]
]

helper.save_image({
    "filename":"fifo.jpg",
    "status":"Done",
    "table":fifo_table,
    "details":"Fish-in-fish-out ratio for various aquaculture products. All figures are as of 2015, except for the last one, which is overall aquaculture as of 2000. FIFO is the ratio, on a mass basis, between the wild fish input into an aquacutlure system and the fish grown.",
    "references":["iffo_fifo"],
    "source_file":"meat.py"
})

####################################

# GHG comparison of different fishing methods
ghg_fish_table = [
    ["<b>Method</b>","<b>Emissions: grams CO<sub>2</sub>e per g protein</b>"],
    ["Fisheries, non-trawl","26-36"],
    ["Fisheries, trawl","60-105"],
    ["Aquaculture: non-recirculating","36-54"],
    ["Aquaculture: recirculating","60-160"]
]

helper.save_image({
    "filename":"fishing_methods.jpg",
    "status":"Done",
    "table":ghg_fish_table,
    "details":"Comparision of greenhouse gas emissions of four methods of producing seafood. Assessed on the basis of protein produced.",
    "references":["meat_land_use"],
    "source_file":"meat.py"
})

######################################

# Comparison of flow-through vs. recirculating aquaculture system for trout.
# See Tables 3 and 5 of https://archimer.ifremer.fr/doc/2009/publication-6510.pdf
# Note that I am skipping Net Primary Production.
trout_table = [
    ["<b>Impact</b>","<b>Flow through</b>","<b>Recirculating</b>","<b>Units</b>"],
    ["Global Warming Potential","2015","1602","kg CO<sub>2</sub>e"],
    ["Energy","34869","57659","MJ"],
    ["Eutrophication Potential","28.5","17.8","kg PO<sub>4</sub>-eq"],
    ["Acidification Potential","13.4","10.5","kg SO<sub>2</sub>-eq"],
    ["Water Depencence","98804","6634","Cubic meters"],
    ["Surface Use","2737","2097","Square meters"]
]

helper.save_image({
    "filename":"aquaculture_methods.jpg",
    "status":"Done",
    "table":trout_table,
    "details":"Compare the two main aquaculture methods for trout. This summarizes the results of a single LCA study, but the general picture is representative of other studies on the topic. Scale all the bars so the flow-through bars are the same length, and then we can see how the RAS impacts are relative to flow-through.",
    "references":["trout"],
    "source_file":"meat.py"
})

#########################################

# Meat and alternative price comparison

# Mostly from the McKinsey study, unless otherwise noted
# Where division occurs, is uses the ESS nutritive factors page to convert from mass to kg protein
price_table = [
    ["<b>Product</b>","<b>Price per kg protein, USD</b>"],
    ["Ground Beef",16],
    ["Soy Protein",2],
    ["Pea Protein",5],
    ["Insect Protein",41],
    ["Mycoprotein",13],
    ["Cultured Meat",300],
    ["Whey Protein",7.5],
    ["Poultry",1.9/0.124], # https://www.indexmundi.com/commodities/?commodity=chicken
    ["Salmon",7./0.25], # Price from https://www.indexmundi.com/commodities/?commodity=fish&months=120
    # and Protein density from http://www.dietandfitnesstoday.com/protein-in-salmon.php
    ["Pork",0.67*2.205/0.18] # Price from https://www.indexmundi.com/commodities/?commodity=pork, given in cents per pound for some reason.
]

helper.save_image({
    "filename":"protein_price.jpg",
    "status":"Done",
    "table":price_table,
    "details":"Price of a kilogram of protein for various meats and meat alternatives. Note that insect and cultured meat options are still under development, and those prices will likely decrease. I would shade the bars so beef, poultry, salmon, and pork are one shade, and the others are a different shade. Have the cultured meat bar run off the plot because otherwise it would foul up the scaling. Most of the figures are from the McKinsey reference. Current prices for poultry, salmon, and pork are taken from IndexMundi. The ESS nutritive factors were used to convert overall mass to protein mass, except for salmon, where the Diet and Fitness reference was used.",
    "references":["nutritive","mckinsey_altmeat","indexmundi","salmon_protein"],
    "source_file":"meat.py"
})

#####################################

# Feed sources

feed_table = [
    ["<b>Feed Source</b>","<b>Millions of tons per year</b>","<b>Examples</b>"],
    ["Crop Grains",325+236],
    ["Other Forage",140+27],
    ["Grazing Feed",142+886,"Straw, hay"],
    ["Crop Residue",17+507],
    ["Scavenging",23+26,"Kitchen waste"],
    ["Grass Forage",122]
]

helper.save_image({
    "filename":"feed_sources.jpg",
    "status":"Done",
    "table":feed_table,
    "details":"Where feed for livestock comes from. This could be broken down further into ruminant and monogastric animals, but I'll forego that.",
    "references":["ag_ghg_2021"],
    "source_file":"meat.py"
})

##################################

# Environmental impacts

seafood_impact_table = [
    ["<b>Product</b>","<b>Greenhouse gases, farmed< (kg CO<sub>2</sub>e/ton)/b>","<b>Greenhouse gases, wild</b>","<b>Nitrogen, farmed (kg N/ton)</b>","<b>Phosphorus, farmed (kg P/ton)</b>","<b>Freshwater usage, cubic meters per ton</b>"],
    ["Bivalves",1400,11700,-129.83,-24.28,0],
    ["Catfish",7770,"",132.88,20.82,2090],
    ["Milkfish",6430,"",146.54,23.92,280],
    ["Carp, miscellaneous",6950,"",147.8,20.26,3520],
    ["Diadromous fish, miscellaneous (migrate between fresh and salt water)",19000,"",156.05,37.5,400],
    ["Marine fish, miscellaneous",11600,"",234.55,50.18,400],
    ["Shrimp",9430,12000,123.04,23.98,220],
    ["Silver and bighead carp",3510,"",43.28,6.56,9280],
    ["Tilapia",10680,"",199.83,24.41,1230],
    ["Chicken",8340,"",204.1,30.5,450],
    ["Cods, hakes, haddocks","",5130,"","",""],
    ["Flounders, halibuts, soles","",20310,"","",""],
    ["Herrings, sardines, anchovies","",3880,"","",""],
    ["Jacks, mullets, sauries","",9500,"","",""],
    ["Lobster","",19440,"","","",""],
    ["Redfishes, basses, congers","","9670-9910","","",""],
    ["Salmons, Trouts, Smelts",5000,"5100-6880","98.89-110.56","23.32-26.62","110-160"],
    ["Squid, cuttlefish, octopus","",8180,"","",""],
    ["Tunas, bonitos, bullfishes","",7630,"","",""],
    ["Seaweed",1090,"",-14.65,-10.14,0]
]

helper.save_image({
    "filename":"seafood_impacts.jpg",
    "status":"Not Done",
    "table":seafood_impact_table,
    "details":"I haven't seen these numbers stated explicitly, so I had to estimate based on a chart. Figures are from the Gephart source, read from the Nature immersive article.",
    "references":["seafood_impact","seafood_impact2"],
    "source_file":"meat.py"
})