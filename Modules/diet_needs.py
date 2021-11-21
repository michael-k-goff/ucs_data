# Dietary needs plots

import helper

# Intake is based on the cited chart and a 2200 calorie male diet.
diet_needs_chart = [
    ["<b>Food Group</b>","<b>Recommended Intake</b>","<b>Recommended Intake, Calories</b>","<b>Notes</b>"],
    ["<b>Macronutrients</b>"],
    ["Protein","52 g","220-660"],
    ["Carbohydrates","130 g","990-1430"],
    ["Dietary Fiber","30.8 g",""],
    ["Added Sugar","---","<220","Part of the Carbohydrate budget"],
    ["Fat","---","550-770"],
    ["Saturated Fat","---","<220","Part of the overall fat budget"],
    ["Linoleic Acid","16 g","","A type of Omega acid"],
    ["Linolenic Acid","1.6 g","","Another type of Omega acid, not to be confused with linoleic acid."],
    ["<b>Minerals</b>"],
    ["Calcium","1300 mg"],
    ["Iron","11 mg"],
    ["Magnesium","410 mg"],
    ["Phosphorus","1250 mg"],
    ["Potassium","4700 mg"],
    ["Sodium","2300 mg"],
    ["Zinc","11 mg"],
    ["Copper","0.89 mg"],
    ["Manganese","2.2 mg"],
    ["Selenium","0.055 mg"],
    ["<b>Vitamins</b>"],
    ["Vitamin A","0.9 mg"],
    ["Vitamin E","15 mg"],
    ["Vitamin D","0.015 mg"], # For conversion of IU to mg, see https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional
    ["Vitamin C","0.075 mg"],
    ["Thiamin","1.2 mg"],
    ["Riboflavin","1.3 mg"],
    ["Niacin","16 mg"],
    ["Vitamin B<sub>6</sub>","1.3 mg"],
    ["Vitamin B<sub>12</sub>","0.0024 mg"],
    ["Choline","550 mg","","An essential nutrient for several functions."],
    ["Vitamin K","0.075 mg"],
    ["Folate","0.4 mg"]
]

excess_chart = [
    ["<b>Food Group</b>","<b>% of Americans who fall below recommendations or exceed limit</b>","<b>Notes</b>"],
    ["Vegetables","86%","Too little"],
    ["Fruit","76%","Too little"],
    ["Grains","45%","Too little"],
    ["Dairy","85%","Too little"],
    ["Protein Food","42%","Too little"],
    ["Oils","73%","Too little"],
    ["Added Sugar","70%","Too much"],
    ["Saturated Fat","72%","Too much"],
    ["Sodium","90%","Too much"]
    
]

helper.save_image({
    "filename":"dietary_needs.jpg",
    "status":"Done",
    "table":diet_needs_chart,
    "details":"An illustration of dietary needs, by calorie where application and by mass.",
    "references":["nutrition_needs"],
    "source_file":"diet_needs.py"
})

helper.save_image({
    "filename":"dietary_needs2.jpg",
    "status":"Done",
    "table":excess_chart,
    "details":"How many Americans either have too much of a given food intake or fail to meet guidelines. Basically, whatever is 'bad' here.",
    "references":["nutrition_needs"],
    "source_file":"diet_needs.py"
})

obesity_table = [
    ["<b>Country</b>","<b>Obesity rate</b>"],
    ["Nauru","61% (highest in data set)"],
    ["United States","36.2%"],
    ["United Kingdom","27.8%"],
    ["Russia","23.1%"],
    ["Germany","22.3%"],
    ["World","13%"], # From Our World in Data, World Health Organization
    ["China","6.2%"],
    ["Vietnam","2.1% (lowest in data set)"]
]

helper.save_image({
    "filename":"obesity.jpg",
    "status":"Done",
    "table":obesity_table,
    "details":"World obesity rate for select countries. The World data comes from the WHO and the rest from the CIA. See the WHO page for a detailed explanation of how obesity and overweight is defined.",
    "references":["obesity1","obesity2"],
    "source_file":"diet_needs.py"
})

micronutrient_table = [
    ["<b>Micronutrient Deficiency</b>","<b>Malady</b>","<b>Description</b>","<b>Prevalence</b>"],
    ["Iron or B<sub>12</sub>","Anemia","Caused by a lack of red blood cells, leads to other maladies.","32.8% of women of reproductive age, 41.7% of children, worldwide"],
    ["Vitamin A","Blindness","Causes or exacerbates other illnesses too.","Above 20% of preganant women and 10% of children in poor countries."],
    ["Zinc","Stunting","Lack of protein causes several illnesses.","Above 30% in poor countries."],
    ["Iodine","Brain damage","","About 25% of world population (~2 billion people)."], # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6284174/
    ["Vitamin D","Bone conditions","","Believed to be prevalent but data is lacking."]
]

helper.save_image({
    "filename":"micronutrient_deficiency.jpg",
    "status":"Done",
    "table":micronutrient_table,
    "details":"Major diseases resulting from lack of micronutrients and their main effects. Vitamin D summary from Roth et al., prevalence of iodine deficiency from Biban and Lichiardopol, the others from OWID.",
    "references":["owid_micronutrient","vitamin_d","iodine_deficiency"],
    "source_file":"diet_needs.py"
})

hidden_hunger_table = [
    ["<b>Region</b>","<b>Hidden Hunger Rate</b>"],
    ["World","51%"],
    ["Middle Africa","76%"],
    ["Eastern Africa","69%"],
    ["Western Africa","67%"],
    ["Southern Africa","64%"],
    ["Northern Africa","47%"],
    ["South-Central Asia","64%"],
    ["South-Easter Asia","46%"],
    ["Western Asia","41%"],
    ["Eastern Asia","27%"],
    ["Eastern Europe","31%"],
    ["Southern Europe","21%"],
    ["Northern Europe","19%"],
    ["Western Europe","19%"],
    ["Caribbean","46%"],
    ["Central America","37%"],
    ["South America","36%"],
    ["Northern America","11%"],
    ["Oceana","33%"]
]

helper.save_image({
    "filename":"hidden_hunger.jpg",
    "status":"Done",
    "table":hidden_hunger_table,
    "details":"'Hidden hunger' is defined to be the presence of at least one micronutrient deficiency. These are some stats by region.",
    "references":["state_children"],
    "source_file":"diet_needs.py"
})