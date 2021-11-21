# Pesticide calculations

import helper

# Copying from FAO. Pesticides worldwide by year, 1990-2017. http://www.fao.org/faostat/en/#data/RP. In tons, for agricultural use.
world_pesticides = [2285881.41, 2262629.47, 2322056.76, 2385017.11, 2541995.25, 2689276.39, 2794872.5, 2918219.84, 2975070.97, 3088429.5, 3063140.39, 3030230.74, 3065980.97, 3161863.33, 3343301.03, 3415781.55, 3460307.62, 3746990.77, 3792117.56, 3706912.96, 3961986.76, 4052029.23, 4093183.59, 4045838.37, 4105783.12, 4061364.5, 4088247.57, 4113591.25]

# http://www.fao.org/faostat/en/#data/RL, select Cropland. In 1000s of ha, 1990-2017.
world_land_use = [1486011.7, 1489500.927, 1485904.78, 1486464.2, 1485405.5, 1485602, 1485988.36, 1491316.42, 1492236.42, 1495784.59, 1492312.22, 1489241.4608, 1485508.53, 1490154.68, 1496966.9, 1502550.03, 1496038.13, 1498490.81, 1500165.86, 1502592, 1505940.07, 1519998.13, 1530032.66, 1532703.5767, 1533862.6486, 1550527.1844, 1555726.3201, 1561336.753]

# Food supply, kcal per capita per day, 1990-2017. The 1990-2013 values from http://www.fao.org/faostat/en/#data/CC. 2014-17 from http://www.fao.org/faostat/en/#data/FBS
world_kcal = [2621, 2601, 2610, 2616, 2639, 2663, 2673, 2687, 2701, 2715, 2727, 2725, 2728, 2735, 2747, 2761, 2779, 2807, 2825, 2825, 2850, 2869, 2874, 2884, 2887, 2898, 2905, 2917]

# In 1000s of people. From http://www.fao.org/faostat/en/#data/OA
world_pop = [5327231.061, 5414289.444, 5498919.809, 5581597.546, 5663150.427, 5744212.979, 5824891.951, 5905045.788, 5984793.942, 6064239.055, 6143493.823, 6222626.606, 6301773.188, 6381185.114, 6461159.389, 6541907.027, 6623517.833, 6705946.61, 6789088.686, 6872767.093, 6956823.603, 7041194.301, 7125828.059, 7210581.976, 7295290.765, 7379797.139, 7464022.049, 7547858.925]

pesticide_table = [
    ["<b>Year</b>","<b>Pesticide usage, by active ingredient</b>","<b>Pesticide usage, per hectare cropland</b>","<b>Pesticide usage, per kcal food produced</b>"]
]

pesticide_table += [
    [1990+i, world_pesticides[i]/world_pesticides[0], (world_pesticides[i]/world_land_use[i])/(world_pesticides[0]/world_land_use[0]), (world_pesticides[i]/world_kcal[i]/world_pop[i])/(world_pesticides[0]/world_kcal[0]/world_pop[0])] for i in range(len(world_pesticides))
]

helper.save_image({
    "filename":"pesticide_trends.jpg",
    "status":"Done",
    "table":pesticide_table,
    "details":"Trends in pesticide usage from 1990 to 2017, in absolute terms, per hectare cropland, and per kcal food produced. All values are presented relative to the 1990 value so we can show trends rather than absolute values.",
    "references":["faostat"],
    "source_file":"pesticides.py"
})

################################

# Table 2, reference 'pesticide_trends'
pesticide_type_table = [
    ["<b>Pesticide Class</b>","<b>Global use, tons of active ingredient</b>"],
    ["Insecticide",47690.4+29972.53+8257.6+3914.79+1596.49+1349.96+491.1+177.34+147.51+23.91],
    ["Herbicide",327892.54+38333.54+23920.24+17242.99+15158.55+9493.33+6507.89+4003.5+2678.05+606.01],
    ["Fungicide/Bactericide",87257.16+56527.62+33354.76+15519.06+6988.88+3192.64+1754.42+932.4+444.74+408.18+360.75+43.68+23.62],
    ["Rodenticide",287.05+13.73+0.04]
]

helper.save_image({
    "filename":"pesticide_by_type.jpg",
    "status":"Done",
    "table":pesticide_type_table,
    "details":"World pesticide usage by type in 2014.",
    "references":["pesticide_trends"],
    "source_file":"pesticides.py"
})

helper.save_image({
    "filename":"pesticide_by_time.jpg",
    "status":"On Hold",
    "details":"",
    "source_file":"pesticides.py"
})

################################

# Table 2 of pesticide21, as of 2008. Units are millions of pounds of active ingredient.
pesticide_by_crop = {
    "Corn":203.73,
    "Soybeans":111.96,
    "Potatoes":52.53,
    "Cotton":37.56,
    "Wheat":23.31,
    "Sorghum":14.17,
    "Peanuts":10.32,
    "Rice":7.58,
    "Tomatoes":9.70,
    "Apples":7.28,
    "Grapes":7.90
}

# Convert to tons
for key in pesticide_by_crop:
    pesticide_by_crop[key] *= 0.453592 * 1000

# Tons, see http://www.fao.org/faostat/en/#data/CC
us_production_2008 = {
    "Corn":305911450,
    "Soybeans":80748700,
    "Potatoes":18826578,
    "Cotton":2792400+3901170, # Cotton lint + Cottonseed
    "Wheat":68016096,
    "Sorghum":12087270,
    "Peanuts":2341630, # Groundnut
    "Rice":9241170,
    "Tomatoes":13700670,
    "Apples":4365055,
    "Grapes":6639960
}

us_crop_table = [
    ["<b>Crop</b>","<b>Pesticide usage in the United States, 2008</b>"]
]

us_crop_table += [
    [key,pesticide_by_crop[key]/us_production_2008[key]] for key in pesticide_by_crop
]

helper.save_image({
    "filename":"pesticide_by_crop.jpg",
    "status":"Done",
    "table":us_crop_table,
    "details":"Pesticide usage by select crop in the US in 2008. Units are ton of pesticide (active ingredient) per ton of crop. Pesticide application figures from the USDA, overall production from FAOSTAT",
    "references":["pesticide21","faostat"],
    "source_file":"pesticides.py"
})

################################

yield_table = [
    ["<b>Scenario</b>","<b>World yield, monetary (billions of US dollars), 2002</b>"],
    ["No pest loss",1550],
    ["Actual, 2002",950],
    ["Without pesticides, 2002",455]
]

helper.save_image({
    "filename":"pesticide_yield.jpg",
    "status":"Done",
    "table":yield_table,
    "details":"World crop yield in monetary terms. What it would be without any pest loss, what it actually was in 2002, and what it would have been in 2002 without pesticides. Physical yields would have been better than monetary, but that's what we have. It would also be better to have something a bit more recent, but I am finding it difficult to find good data on this subject.",
    "references":["pesticide_yield1","pesticide_yield2"],
    "source_file":"pesticides.py"
})

################################

# Financial cost/benefit

cost_benefit_table = [
    ["<b>Factor</b>","<b>Annual value in United States (billions of dollars, ~2005)</b>"],
    ["Direct cost",9.2],
    ["Externalized costs",9.6],
    ["Benefit of increased yields",52.0],
    ["Other benefits",7.7]
]

helper.save_image({
    "filename":"pesticide_cost_benefit.jpg",
    "status":"Done",
    "table":cost_benefit_table,
    "details":"Monetized costs and benefits of pesticide usage in the United States. This pulls from different studies ranging from 2002-2008, so the figures aren't perfectly comparable, but they are close enough to being comparable. The point is that there pesticides provide a net benefit in agriculture but there are externalized costs. In the references below, I am only giving the one from which I pulled the figures, but in the site text, I will also list the references from which the study derived figures.",
    "references":["pesticide_yield3"],
    "source_file":"pesticdes.py"
})

################################

# External costs for the US.

# Divide by 0.8 to convert Euro to USD roughly. See https://www.poundsterlinglive.com/bank-of-england-spot/historical-spot-exchange-rates/usd/USD-to-EUR-2005
externality_table = [
    ["<b>External cost of pesticides</b>","<b>Annual damages in the US in 2005-06, millions of dollars</b>"],
    ["Drinking water contamination",851/0.8],
    ["Pollution, fish deaths, monitoring costs",122/0.8],
    ["Biodiversity and wildlife losses",157/0.8],
    ["Bee colony losses",109/0.8],
    ["Acute effects on human health",127/0.8]
]

helper.save_image({
    "filename":"pesticide_externalities.jpg",
    "status":"Done",
    "table":externality_table,
    "details":"A tally of external costs of pesticides. I pulled the numbers from Pretty and Bharucha, who in turn pulled them from Leach and Mumford, so both sources are being credited. Numbers are given in Euros, and I used an exchange rate of 1 USD = 0.8 Euro around 2005, which is only ballpark accurate.",
    "references":["pesticide_external","ipm"],
    "source_file":"pesticides.py"
})

helper.save_image({
    "filename":"pesticide_exteranlities.jpg",
    "status":"On Hold",
    "details":"",
    "references":[],
    "source_file":"pesticides.py"
})