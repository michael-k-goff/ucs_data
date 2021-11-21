# Cause of death

import helper

# See http://ghdx.healthdata.org/gbd-results-tool

total_deaths = 55945729.74

# Primary cause of death. These categories are exclusive and comprehensive.
primary_cause = {
    "Injuries":4484722.08,
    "Non-communicable diseases":41071133.49,
    "Communicable, maternal, neonatal, and nutritional diseases":10389874.17
}

secondary_cause = {
    "Injuries":{
        "Transport Injuries":1335003.75,
        "Unintentional Injuries":1804869.51,
        "Self-harm and interpersonal violence":1344848.82
    },
    "Non-communicable diseases":{
        "Musculoskeletal disorders":121268.54,
        "Other non-communicable diseases":1153268.70,
        "Skin and subcutaneous diseases":100284.40,
        "Cancer":9556244.81,
        "Cardiovascular":17790948.90,
        "Digestive diseases":2377684.94,
        "Chronic respiratory diseases":3914196.03,
        "Neurological disorders":3094164.34,
        "Mental Disorders":326.47,
        "Substance use disorders":351546.79,
        "Diabetes and kidney diseases":2611199.58
    },
    "Communicable, maternal, neonatal, and nutritional diseases":{
        "Sexually transmitted infections excluding HIV":119092.92,
        "HIV/AIDS":954491.75,
        "Neglected tropical diseases and malaria":720059.61,
        "Enteric infections":1765992.00,
        "Other infectious diseases":830494.10,
        "Nutritional deficiencies":269996.92, # Seems low
        "Respiratory infections and tuberculosis":3752337.77,
        "Maternal and Neonatal Disorders":1977409.11
    }
}

# For violent deaths
tertiary_cause = {
    "Suicide":793823.47,
    "Homicide":405346.24,
    "War and Terrorism":129720.15,
    "Executions and Police":15958.96
}

table = [
    ["<b>Cause</b>","<b>Estimated number of deaths in 2017</b>"],
    ["Total",total_deaths],
    ["",""]
]
for key in primary_cause:
    table.append([key,primary_cause[key]])
    for key2 in secondary_cause[key]:
        table.append(["---"+key2,secondary_cause[key][key2]])
        if key2 == "Self-harm and interpersonal violence":
            for key3 in tertiary_cause:
                table.append(["------"+key3, tertiary_cause[key3] ])
                
helper.save_image({
    "filename":"cause_of_death.jpg",
    "status":"Done",
    "details":"Cause of death. The following a breakdown by primary and secondary causes (and some tertiary causes too). The causes listed here are comprehensive, in that they cover all deaths, and every death has one cause. There is all sorts of statistical ninjitsu that goes into these figures, creating values that are not integers. For the purposes of this plot, round them. I'm thinking that an area plot would be good for this. There would be three big sections for the three top categories, each of which would be broken into subcategories. There is only one where I separate out subsubcategories--violent deaths--since those get high levels of attention. The GBDC source has much more detail.",
    "table":table,
    "references":["disease_burden","owid_causeofdeath"],
    "source_file":"cause_of_death.py"
})

risk_factors = [
    ["<b>Factor</b>","<b>Number of Deaths in 2017</b>"],
    ["Unsafe Sex",1028619.95],
    ["Domestic Violence",70725.75+7913.30], # Intimate partner + child maltreatment
    ["Occupational Risks",1159767.62],
    ["Low Physical Activity",1263051.29],
    ["Dietary Risks",10885706.22], 
    ["Metabolic Risks",17579416.66], 
    ["Drug Use",585348.18],
    ["Alcohol",2842854.20],
    ["Tobacco",8101890.98],
    ["Unsafe water, sanitation, and handwashing",1613692.09],
#    ["Air Pollution",4895476.00], # Detail
    ["Outdoor Particulate",2937087.20],
    ["Indoor Particulate",1640599.78],
    ["Ozone",471790.43],
    ["Other Environmental Risks",1142110.37], # Mostly lead
    ["Child and maternal malnutrition",3189913.77],
    ["Climate Change (estimate for 2030)",250000] # who_cc
]

helper.save_image({
    "filename":"death_risk_factors.jpg",
    "status":"Done",
    "details":"Death risk factors, by how many deaths each factor contributes to. Unlike the cause of death plot, not every death has a risk factor associated with it, and some deaths have multiple risk factors associated. Most data comes from the GBDC and are for 2017, except the climate change number comes from the WHO and is for 2030. I think this one is best presented as a regular old bar plot.",
    "table":risk_factors,
    "references":["disease_burden","owid_causeofdeath","who_cc"],
    "source_file":"cause_of_death.py"
})

climate_table = [
    ["<b>Risk Factor</b>","<b>Annual Deaths in 2030</b>"],
    ["Nutrition",95176],
    ["Tropical Diseases",60091+258],
    ["Diarrhoeal Disease",48114],
    ["Heat",37588]
]

helper.save_image({
    "filename":"climate_deaths.jpg",
    "status":"Done",
    "details":"Estimated number of deaths attributable to climate change in 2030 by cause. There is also a category of flooding and storms, but no numerical estimate that is precise enough to include. All these numbers here have wide error bounds too.",
    "table":climate_table,
    "references":["who_cc"],
    "source_file":"cause_of_death.py"
})
