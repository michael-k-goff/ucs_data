# Industrial systems

import helper
from primary_energy_factors import primary_factors # Source is 'energycode'

primary_factors["Oil"]=1
primary_factors["Oil Products"]=1.05
primary_factors["Natural Gas"]=1.05
primary_factors["Biofuel"]=1.05
primary_factors["Heat"]=1
primary_factors["Geothermal"]=1

# Motor systems energy savings
industrial_electricity = 10700*primary_factors["Electricity"]*0.0036 # u4e, TWh
motor_systems_industry_electricity = industrial_electricity * 0.57
# From iea_eff, efficiency improvement potential
motor_systems_efficiency_bau = 1.14
motor_systems_efficiency_policy = 1.35

# Combined Heat and Power
chp_potential = 240644 # In MW capacity, doe_chp2
industrial_chp_potential = 65381+81048
new_industrial_chp_potential = industrial_chp_potential - (82700-11577)
new_industrial_chp_potential = new_industrial_chp_potential * 0.5 # Guesstimating that half is economic, based on aga_chp
new_industrial_chp_potential = new_industrial_chp_potential*8760./10**12*3600. 
# Assuming 70-80% efficiency for the CHP and 45% efficiency for what is being displaced
new_industrial_chp_potential_low = new_industrial_chp_potential * (1/0.45-1/0.70)
new_industrial_chp_potential_high = new_industrial_chp_potential * (1/0.45-1/0.80)

# Waste Heat to Power potential estimates
whp_us = 2904 # Economic capacity, in MW, from ornl_whp
whp_us = whp_us * 8760./10**12*3600. * primary_factors["Electricity"]
whp_eu = 21.6 * 0.0036 * primary_factors["Electricity"] # http://www.diva-portal.org/smash/get/diva2:842699/FULLTEXT01.pdf

# Total primary energy into industry for various regions for the purposes of calculation. From iea_sankey
industry_world = {
    "Oil":245+364,
    "Oil Products":13187+24631,
    "Coal":34232+2105,
    "Natural Gas":23764+7786,
    "Biofuel":8671,
    "Geothermal":24,
    "Electricity":32201,
    "Heat":5764
}
industry_world_total = sum([industry_world[key]*primary_factors[key] for key in industry_world])/1000
# Also from iea_sankey
industry_us = {
    "Oil":0+185,
    "Oil Products":769+4575,
    "Coal":693,
    "Natural Gas":5219+1007,
    "Biofuel":1269,
    "Electricity":2802,
    "Heat":194
}
industry_us_total = sum([industry_us[key]*primary_factors[key] for key in industry_us])/1000

ms_low = motor_systems_industry_electricity*(1-1/motor_systems_efficiency_bau)
ms_high = motor_systems_industry_electricity*(1-1/motor_systems_efficiency_policy)

energy_savings = [
    ["<b>Tool</b>","<b>Primary Energy Savings, Low Estimate</b>","PE Savings, High Estimate","PE Savings as Share of Total Industry, Low Estimate","..., High Estimate","Region"],
    ["Benchmarking",23,31,23./industry_world_total, 31./industry_world_total,"World"], # unido2010
    ["Motor Systems",ms_low, ms_high, ms_low/industry_world_total, ms_high / industry_world_total,"World"],
    ["Steam Systems",8.8,8.8, 8.8/industry_world_total, 8.8/industry_world_total,"World"], # From the source 'gea'
    ["Combined Heat and Power",new_industrial_chp_potential_low,new_industrial_chp_potential_high,new_industrial_chp_potential_low/industry_us_total,new_industrial_chp_potential_high/industry_us_total,"United States"],
    ["Waste Heat to Power",whp_us,whp_us,whp_us/industry_us_total,whp_us/industry_us_total,"United States"]
]

im_industrial_systems = {
    "filename":"industrial_systems.jpg",
    "status":"Done",
    "details":"Primary energy savings potential from several kinds of industrial efficiency. In the case of Combined Heat and Power and Waste Heat to Power, savings are in the form of primary energy displaced from power plants. For CHP, I assume the CHP plant operates at 80% efficiency and displaces electricity and heat at 45% effciency. I am taking technical potential from [doe_chp2] and assuming that half the technical potential is economically viable, based on [aga_chp]. For motor systems, I am using the IEA report's estimate of savings potential for industrial motor systems only; motors in buildings and vehicles are a separate thing.<br><br>For the graphic, present bars in terms of savings as share of the region's total industrial energy, as I think this gives us the best way to compare across regions. Put labels but not bars indicating the region and absolute energy savings.<br><br>These figures may be subject to revision, as I would like to have worldwide estimates for CHP and WHP, and perhaps also add figures on additive manufacturing, industrial heat efficiency, something more up to date on steam systems, etc.",
    "table":energy_savings,
    "references":["energycode","iea_sankey","gea","ornl_whp","u4e","doe_chp2","aga_chp","iea_eff","unido2010"],
    "source_file":"industrial_systems.py"
}
helper.save_image(im_industrial_systems)

##########################################

# Waste heat recovery solution

helper.save_image({
    "filename":"waste_heat_recovery.jpg",
    "status":"Solution",
    "details":"These are numbers for Industrial Heat Recovery Loan Program on the Industrial Systems page. Costs are estimated at $10-12 billion over 10 years, benefits are estimated at $19-21 billion over 10 years. The environmental benefit is estimated at 149 million tons CO<sub>2</sub>. See sources in that solution for more details on source information.",
    "references":[],
    "source_file":"industrial_systems.py"
})