# Eutrophication. See also planetary_boundaries.py

import helper

# See the big spreadsheet to get eutrophication per functional unit. I am using
eu_table = [
    ["<b>Food item</b>","<b>Eutrophication Potential, grams PO<sub>4</sub><sup>3</sup>-eq per nutritional unit</b>"],
    ["Maize",0.9],
    ["Potato",4.8],
    ["Apple",1.5],
    ["Wheat and Rye bread",2.7],
    ["Barley (for beer)",0.4],
    ["Oatmeal",4.3],
    ["Rice",10],
    ["Coffee",1.7],
    ["Milk",11],
    ["Cheese",45],
    ["Eggs",20],
    ["Farmed fish",103],
    ["Poultry",28],
    ["Pig meat",47],
    ["Mutton",49],
    ["Beef (beef herd)",151],
    ["Tomato",7.5],
    ["Tofu",3.9],
    ["Peas",3.4],
    ["Nuts",12]
]

helper.save_image({
    "filename":"eutrophication_by_food.jpg",
    "status":"Done",
    "table":eu_table,
    "details":"Eutrophication by select food item. The units are pretty weird. The grams PO<sub>4</sub><sup>3</sup>-eq part, I don't really have an intuition for what that is, but the point is to compare the different items. The 'per nutritional unit' part is 1000 kcal for most of them, or 100 grams of protein for the protein-rich items. They are roughly equivalent in general, and this is how Poore and Nemecek choose to do the comparison instead of on a strict calorie basis. They have more food items, but I think this is enough for now.",
    "references":["poore"],
    "source_file":"eutrophication.py"
})

########################

# A scenario for diets. This is just based on Poore and Nemecek, no complex calculations like with the other diet plots.

eutrophication_diet_table = [
    ["<b>Diet</b>","<b>Overall eutrophication, millions of tons PO<sub>4</sub><sup>3</sup>-eq</b>"],
    ["World Diet as of 2010",64.7],
    ["No beef herds or mutton",58.8],
    ["No beef, mutton, milk, or cheese", 48.3],
    ["No animal products except eggs and fish",46.6],
    ["No animal products",32.7]
]

helper.save_image({
    "filename":"eutrophication_diet.jpg",
    "status":"Done",
    "table":eutrophication_diet_table,
    "details":"Eutrophication by world diet. Instead of using the diets defined elsewhere in the Diet analysis, I lifted the figures directly from Poore and Nemecek since they define their own diet scenarios by which animal products are allowed.",
    "references":["poore"],
    "source_file":"eutrophication.py"
})

########################

# Sources of phosphorus pollution

helper.save_image({
    "filename":"phos_sources.jpg",
    "status":"Done",
    "details":"High level review of the main sources of phosphorus pollution. They are 54.2% from domestic source (mostly sewer systems), 7.9% from industrial resources, and 37.9% from agriculture.",
    "references":["phos_sources"],
    "source_file":"eutrophication.py"
})

ag_p_table = [
    ["<b>Class of Crops</b>","<b>World P pollution, thousands of metric tons</b>"],
    ["Cereals",0.118],
    ["Vegetables",0.063],
    ["Oil Crops",0.055],
    ["Fruit",0.049],
    ["Pulses",0.019],
    ["Roots",0.018],
    ["Sugar Crops",0.014],
    ["Nuts",0.01],
    ["Spices",0.005],
    ["Stimulants",0.005],
    ["Fibers",0.004],
    ["Other Crops",0.018]
]
for i in range(1,len(ag_p_table)):
    ag_p_table[i][1] *= 1470.

helper.save_image({
    "filename":"phos_sources_ag.jpg",
    "status":"Done",
    "details":"A more detailed breakdown of what crops are responsible for the agricultural phosphorus sources. The table from which this data is pulled refers to 'nutes', which is evidently a slang term for nutrients in plant science, but I think it's a typo for 'Nuts'. I was originally planning on having this on a separate page from the other P plot, but I decided to make it the same page, so consider whether it is better to combine the two plots.",
    "table":ag_p_table,
    "references":["phos_sources"],
    "source_file":"eutrophication.py"
})