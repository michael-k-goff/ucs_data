# CCS

import helper

# CO2 abatement costs with CCS
# CCS application, reduction proportion, low abatement cost, high abatement cost in dollars per ton
ccs_abatement_costs = [
    ["<b>Method (Industry)</b>","","<b>Cost, USD/ton CO<sub>2</sub>e, Low Estimate</b>","<b>Cost, High Estimate</b>"],
    ["Heavy Industry, General","Depends on Amount",34,165], # folger
#    ["Hydrogen","Depends on Amount",6,80], # folger
#    ["Ammonia","Depends on Amount",6,80], # folger
#    ["Refining","67%",80,80], # ccs_roadmap
#    ["Refining","Almost All",105,105], # ccs_roadmap
    ["Refining","Depends on Amount",80,105], # ccs_roadmap above, aggregating the two
#    ["Iron and Steel","50%",55,55], # ccs_roadmap
#    ["Iron and Steel","Almost All",85,85], # ccs_roadmap
#    ["Chemicals","33%",35,35], # ccs_roadmap
#    ["Chemicals","Almost All",105,105], # ccs_roadmap
    ["Chemicals","Depends on Amount",35,105], # Aggregating the two above from ccs_roadmap
    ["Paper and Pulp","Almost All",60,60], # ccs_roadmap
 #   ["Cement","Almost All",60,60], # ccs_roadmap
    ["Natural Gas Processing","Unspecified",15,25], # industry_ccus
    ["Coal to Chemicals","Unspecified",15,25], # industry_ccus
    ["Ammonia","Unspecified",25,35], # industry_ccus
    ["Bioethanol","Unspecified",25,35], # industry_ccus
    ["Ethylene Oxide","Unspecified",25,35], # industry_ccus
    ["Hydrgen from SMR","Unspecified",15,60], # industry_ccus
    ["Iron and Steel","Unspecified",60,120], # industry_ccus
    ["Cement","Unspecified",60,120], # industry_ccus
    ["<b>Method (Power)</b>","","",""],
    ["Coal Power","Depends on Amount",35,95], # gillingham, hardisty, hu, rubin
    ["Natural Gas Power","Depends on Amount",58,121], # rubin, budinis
    ["<b>Method (Environmental Removal)</b>","","",""],
    ["BECCS","N/A",60,250], # ipcc_emissions
    ["Direct Air Capture, 2020","N/A",241,241], # dac, convert 220 Euros to USD at an exchange rate of 1.09
    ["Direct Air Capture, 2050","N/A",59,59] # dac
]

for i in range(len(ccs_abatement_costs)):
    ccs_abatement_costs[i] = [ccs_abatement_costs[i][0], ccs_abatement_costs[i][2], ccs_abatement_costs[i][3]]
    
ccs_im = {
    "filename":"ccs_abatement_cost.jpg",
    "status":"Done",
    "details":"Spell out acronyms, like SMR and BECCS. Also, Hydrogen is spelled wrong.",
    "table":ccs_abatement_costs,
    "references":["ccs_roadmap","folger","industry_ccus","gillingham","hardisty","hu","rubin","budinis","ipcc_emissions","dac"],
    "source_file":"ccs.py"
}

helper.save_image(ccs_im)

# Energy cost of carbon capture methods

from primary_energy_factors import primary_factors # Source is 'energycode'

# Sources: electrofuel_overview, vonderassen, energycode

ccs_energy_costs = [
    ["Direct Air Capture",4.19+1.29*primary_factors["Electricity"]],
    ["Gas Power Plant",0+1.6*primary_factors["Electricity"]],
    ["Coal Power Plant",0+1.22*primary_factors["Electricity"]],
    ["Paper and Pulp",1.57+0.04*primary_factors["Electricity"]],
    ["Iron and Steel",0.95+0.87*primary_factors["Electricity"]],
    ["Cement",3.35+0.09*primary_factors["Electricity"]],
    ["Ammonia",0.01+0.4*primary_factors["Electricity"]]
]
ccs_energy_im = {
    "filename":"ccs_energy_cost.jpg",
    "status":"Done",
    "details":"Primary energy cost of carbon capture, in MJ per kilogram.",
    "table":ccs_energy_costs,
    "references":["electrofuel_overview","vonderassen","energycode"],
    "source_file":"ccs.py"
}
helper.save_image(ccs_energy_im)

# Usage of CCS
# See p. 20 for the numbers.
ccs_usage_im = {
    "filename":"ccs_usage.jpg",
    "status":"Done",
    "details":"Show main ways in which captured CO<sub>2</sub> is used today. There are only two that are significant: Enhanced Oil Recovery at about 33 million tons, and Geological Storage at about 8 million tons. Figures are estimates for 2019.",
    "references":["ccs_institute"],
    "source_file":"ccs.py"
}
helper.save_image(ccs_usage_im)

############################################################

# Sources of carbon

carbon_sources_table = [
    ["<b>Source</b>","<b>Carbon available, millions of tons per year</b>"],
    ["Bioethanol","250"],
    ["Biogas","150"],
    ["Paper and pulp","550"],
    ["Waste to Energy","350"],
    ["Biomass for heat and power","2500"],
    ["Direct air capture","Virtually unlimited"]
]

helper.save_image({
    "filename":"c_sources.jpg",
    "status":"Done",
    "details":"Estimates of renewable (e.g. doesn't involve fossil fuels) sources of carbon ahd how much will be available at midcentury. Direct air capture may be expensive but at least there is plenty of it possible, unlike other options. I'd like to augment this later with more sources and comparisons with other carbon figures, such as how much it would take to replace all transportation fuels with electrolyzed fuels for instance.",
    "table":carbon_sources_table,
    "references":["irena_methanol"],
    "source_file":"ccs.py"
})