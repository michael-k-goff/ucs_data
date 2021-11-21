# Risk in agriculture

import helper

# See disease.py
risks = {'Antimicrobial agent use': 65, 'International travel & commerce': 26, 'Land use changes': 36, 'Human demographics & behavior': 10, 'Unspecified': 15, 'Human susceptibility to infection': 70, 'Medical industry changes': 12, 'War & famine': 19, 'Agricultural industry changes': 31, 'Food industry changes': 27, 'Climate & weather': 10, 'Breakdown of public health measures': 9, 'Bushmeat': 4, 'Other': 1}
total = 335

risk_table = [
    ["<b>Main cause</b>","<b>Number of disease outbreaks</b>","<b>Notes</b>"],
    ["Antimicrobial agent use",65,""],
    ["International travel & commerce",26,""],
    ["Land use changes",36,""],
    ["Human demographics & behavior",10,""],
    ["Unspecified and Other",16,""],
    ["Human susceptibility to infection",70,"Largest cluster is diseases associated with HIV/AIDS"],
    ["Medical industry changes",12,""],
    ["War & famine",19,""],
    ["Agricultural industry changes",31,""],
    ["Food industry changes",27,""],
    ["Climate & weather",10,""],
    ["Breakdown of public health measures",9,""],
    ["Bushmeat",4,""]
]

helper.save_image({
    "filename":"eid_risk.jpg",
    "status":"Done",
    "details":"These figures come from a study of 335 emerging infectious disease outbreaks from 1940 to 2004 and classifies them by their main cause. Several causes might contribute to an outbreak; only the most significant (in the judgment of the authors of the study) are counted.<br><br>Add an additional table to the same plot indicating that 60.3% of these diseases are zoonotic in origin, and 43.3% are zoonotic and can be traced to wildlife.",
    "table":risk_table,
    "references":["eid"],
    "source_file":"ag_risk.py"
})

# Foodborne illnesses

foodborne_table = [
    ["<b>Food Category</b>","<b>Share out Outbreaks Attributed</b>","<b>Share of US Food Supply, 2006</b>"],
    ["Aquatic animals",1189/4607., 37/3783.], # Fish/Seafood
    ["Land animals",2174/4607., (1048-37)/3783.],
    ["Plants",1079/4607., 2735/3783.], # Vegetal products
    ["Other",165/4607.],
    ["<b>Select Secondary Categories</b>","<b>Share out Outbreaks Attributed</b>","<b>Share of US Food Supply, 2006</b>"],
    ["Fish",794/4218., 27/3783.],
    ["Crustaceans",95/4218., 7/3783.],
    ["Mollusks",261/4218., 2/3783.],
    ["Dairy",265/4218., (378+41)/3783.], # Milk and butter
    ["Eggs",168/4218., 56/3783.],
    ["Beef",630/4218., 117/3783.],
    ["Pork",267/4218., 127/3783.],
    ["Poultry",(8+175+434)/4218., 209/3783.], # Includes chicken, turkey, and other poultry
    ["Grains and Beans",155/4218., (816+27)/3783.], # Cereal crops used for grains
    ["Oil/Sugar",11/4218.,(637+63+669)/3783.],
    ["Fruits",210/4218.,79/3783.],
    ["Vegetables",(213+29+120)/4218.,117/3783.],
    ["Roots/underground",72/4218., 97/3783.]
]

helper.save_image({
    "filename":"foodborne.jpg",
    "status":"Done",
    "details":"Foodborne illnesses. This is a study of 18,203 foodborne illness outbreaks in the United States from 1998-2014. Of them, 4607 could be assigned to high level categories of food, and 4218 can be assigned to secondary categories. The first set of rows shows a breakdown into the four top level categories. The second set of rows is the share of illness attributable to the given food group, among those that are attributable to any secondary food group. The share of food supply column is on a calorie basis. Of those outbreaks that are not attributed to any type of food, either there are multiple foods involved for it is impossible to get the data (e.g. attributed to 'buffet' or there simply isn't any data). The 'Other' category includes things like coffee, tea, spices, etc. (which I know are plant-based but they are categorized separately in the study). Illness data from Richardson et al. and calorie intake data from FAOSTAT.",
    "table":foodborne_table,
    "references":["foodborne","faostat"],
    "source_file":"ag_risk.py"
})

######################################################

# Antimicrobial usage

amu_table = [
    ["<b>Purpose</b>","<b>Annual antibiotic use in the US, tons</b>"],
    ["Livestock",13540],
    ["Crops",70],
    ["Aquaculture",150],
    ["Pets",150],
    ["Humans",3290]
]

helper.save_image({
    "filename":"amu_us.jpg",
    "status":"Done",
    "details":"Antibiotic use in the United States.",
    "table":amu_table,
    "references":["amr_us"],
    "source_file":"ag_risk.py"
})