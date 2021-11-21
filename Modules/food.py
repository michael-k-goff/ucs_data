# Basic food-related calculations.
# Intended (at least initially) for the Feeding the World plots.

import helper

###################### Current production
# World production fron New Food Balances.

total_production = {}
with open("Modules/FAO/new_food_balances.csv") as fp:
    line = fp.readline()
    count = 0
    while line:
        line = fp.readline()
        if line:
            count += 1
            fields = line.split('"')
            crop = fields[15]
            if crop not in total_production:
                total_production[crop] = 0
            total_production[crop] += float(fields[23])/4.

# Consolidate some categories
total_production["Meat, Fat, Offal"] = total_production["Offals"] + total_production["Animal fats"] + total_production["Meat"]
del total_production["Offals"]
del total_production["Animal fats"]
del total_production["Meat"]

total_production["Oil crops, vegetable oil"] = total_production["Oilcrops"] + total_production["Vegetable Oils"]
del total_production["Oilcrops"]
del total_production["Vegetable Oils"]

total_production["Seafood"] = total_production["Fish, Seafood"] + total_production["Aquatic Products, Other"]
del total_production["Fish, Seafood"]
del total_production["Aquatic Products, Other"]

total_production["Alcoholic Beverages, other"] = total_production["Stimulants"] + total_production["Spices"] + total_production["Miscellaneous"] + total_production["Alcoholic Beverages"]
del total_production["Stimulants"]
del total_production["Spices"]
del total_production["Miscellaneous"]
del total_production["Alcoholic Beverages"]

total_production["Sugar and sugar crops"] = total_production["Sugar Crops"] + total_production["Sugar & Sweeteners"]
del total_production["Sugar Crops"]
del total_production["Sugar & Sweeteners"]

table = [["<b>Food product</b>","Annual production, thousands of tons"]]
for key in total_production:
    table = table + [[key,total_production[key]]]

helper.save_image({
    "filename":"world_crop_production.jpg",
    "status":"Done",
    "table":table,
    "details":"Annual production of various families of crops. Data is from FAOSTAT and the average of 2014-17 figures. I took the categories of crops they report and did some additional consolidation to get this list. Values are in thousands of tons per year.",
    "references":["faostat"],
    "source_file":"food.py"
})

##########################

# More projections. This is distinct from the projections in world_ag_land_projected.jpg, which are done in ag_land_use.py.

projection_table = [
    ["<b>Crop</b>","<b>Projected growth, 2005-50</b>"],
    ["Total","60%"],
    ["Meat","76%"],
    ["Sugarcane/sugarbeet","75%"],
    ["Oilcrops","89%"],
    ["Cereals","46%"],
    ["Maize (corn)","67%"],
    ["Rice","42%"],
    ["Wheat","38%"],
    ["Soybeans","55%"]
]

helper.save_image({
    "filename":"projected_crop_growth.jpg",
    "status":"Done",
    "table":projection_table,
    "details":"Projections of how much demand for various food commodities will grow from 2005-50. This is more or less the same as what was on the site before, but one of the numbers was changed. The Total figure is from Tilman et al., the meat, sugarcane/beet, oilcrop, and cereal numbers are from Alexandratos and Bruinsma, and the maize, rice, wheat, and soybean numbers are from Ray et al.",
    "references":["tilman","ag203050","ray"],
    "source_file":"food.py"
})

#############################

# Stats on world hunger

# All stats from https://globalnutritionreport.org/reports/global-nutrition-report-2018/ unless otherwise noted
# See the data table from Chapter 2.
hunger_table = [
    ["<b>Condition</b>","<b>Number of people affected worldwide (millions)</b>"],
    ["Underweight adults",462], # https://www.who.int/news-room/fact-sheets/detail/malnutrition, 2014
    ["Overweight or obese adults",2005.1], # From the Global Nutrition Report
    ["Stunted children",150.8],
    ["Wasted children",50.5],
    ["Overweight or obese children",38.3],
    ["Anaemia (women of reproductive age)",613.2],
    ["Low birth weight",20],
    ["High blood pressure",1126.6]
]

helper.save_image({
    "filename":"malnutrition_stats.jpg",
    "status":"Done",
    "details":"Statistics on various nutrition-related problems. Note that these conditions are mutually exclusive. I would also like to have figures on nutrient deficiency, but I'm not satisfied with the data that are readily available. Most of the numbers are for 2017 and come from the Global Nutrition Report, except the Underweight Adult figure, which is from 2014 and from the WHO press release.<br><br>In addition to this plot, add a small bar plot showing decline in world hunger rates. There are just two values, which come from the FAO report: 18.6% of the world's population suffered from hunger from 1990-92, and 10.8% suffered from 2014-16.",
    "table":hunger_table,
    "references":["who_mal","nutrition_report","fao_stats"],
    "source_file":"food.py"
})

helper.save_image({
    "filename":"food_adequacy.jpg",
    "status":"Done",
    "details":"This one is easy peasy. Show how the world grows enough food with two numbers. World crop production was 113% of world dietary needs in 1990, and was 123% in 2014.",
    "references":["fao_stats"],
    "source_file":"food.py"
})

##################################

# Yield trends

# For the Ray et al. paper, I took the non-compounding figures they report and recalculated them to be compounding, assuming they apply over 40 years.
helper.save_image({
    "filename":"yield_trends.jpg",
    "status":"Done",
    "details":"Show trends in crop yields from three sources. There is the Our World in Data article (also credit FAOSTAT, from which OWID draws data), which shows a 2.2976% annual increase from 1961 to 2014. The FAO projected a 0.8% annual increase in their 2009 report to 2050. Mauser et al. show that 2.0388% could be achieved from 2005-50 through plant genetics, intensive planting, and spatial optimization. The Ray et al. paper predicts annual yield increases to 2050 of 1.29%, 0.8804%, 0.808%, and 1.1017% for maize, rice, wheat, and soybeans respectively (I adjusted the figures so that would be compounding). I give more exact numbers for the purposes of sizing the bars, but for writing the numbers, round to the nearest 0.1%.",
    "references":["owid_yield","faostat","fao_yield_proj","nature_yield","ray"],
    "source_file":"food.py"
})

###################################

# Impact of price increases on food consumption

impact_table = [
    ["<b>Scenario</b>","<b>Impact on low income countries</b>","<b>Impact on high income countries</b>"],
    ["Cereal price up 1%","Consumption down 0.61%","Consumption down 0.43%"],
    ["Meat price up 1%","Consumption down 0.78%","Consumption down 0.60%"]
]

helper.save_image({
    "filename":"food_price_impact.jpg",
    "status":"Done",
    "details":"Some estimates of price elasticity of food consumption, e.g. if prices go up, how much does consumption go down? I would like to link this more directly to malnutrition statistics to drive home the point that high food prices cause malnutrition, but instead we have reductions in consumption and are left to infer.",
    "table":impact_table,
    "references":["price_elas"],
    "source_file":"food.py"
})

#####################################

# Impact of biofuels on prices

# https://onlinelibrary.wiley.com/doi/abs/10.1111/sjoe.12177
# Look at Table 4 of the full text (p. 23). 16.74491392801252% increase as a result of mandate in 2022.
# Regulation consists of 36 billion gallons in the US, plus EU mandate.

# Another study showing that biofuel mandates increase food prices. Can't easily extract a number from it though. https://journals.aijr.in/index.php/ajss/article/view/381

# This paper finds to relationship between biofuel production and price. I'm not sure I accept the methodology. https://www.sciencedirect.com/science/article/pii/S0961953419300911

ethanol_energy = 76100.*1055 # Joules per gallon. Energy content from https://en.wikipedia.org/wiki/Gasoline_gallon_equivalent
ethanol_energy /= 10**9 # EJ/billion gallons

# For the third scenario, 36 billion gallons in the US are given. I'm not sure how much is for the EU
helper.save_image({
    "filename":"biofuel_food_price.jpg",
    "status":"Done",
    "details":"Show a few estimates of the impact of biofuel policies on food prices. The bioenergy produced is gross (i.e. not subtracting out input energy), and for the US+EU scenario, it only includes the US side because I'm not sure how much production the EU mandate should result in. Take a look at the context in the Feeding the World page and the caption, as it includes some references to some other papers that are part of this general exhibit but not portrayed graphically. I'm not sure how they should be portrayed in the image yet. All are from Chakravorty et al. Note that most studies confirm that biofuel production causes food price increases, with Ncube et al. as a reference, but Shrestha et al. dispute it. Also note somewhere that total world primary energy is about 600 EJ, so we can see how this biofuel production fits into overall energy supply.",
    "table":[
        ["<b>Scenario</b>","<b>Primary enrgy produced (EJ/year)</b>","<b>Food price increase</b>"],
        ["Biofuels in the US (no mandate)",10*ethanol_energy,"15%"],
        ["Biofuels in the US (mandate)",30*ethanol_energy,"32%"],
        ["Biofuel mandates in the US and EU",36*ethanol_energy,"16.7%"]
    ],
    "references":["biofuel_price","biofuel_price2","biofuel_price3"],
    "source_file":"food.py"
})