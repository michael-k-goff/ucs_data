# Methanol!

import helper

# From iea_hydrogen, p. 106.
# Costs in USD/ton, given as ranges.
methanol_cost = [
    ["<b>Feedstock</b>","<b>Cost (USD/ton, low estimate)</b>","<b>Cost (USD/ton, high estimate)</b>"],
    ["Natural Gas",120,440],
    ["Coal",150,360],
    ["Natural Gas with CCS",175,460],
    ["Coal with CCS",320,470],
    ["Electrolysis",200,1260],
    ["Biomass",970,1320]
]

methanol_cost = [ # Going with IRENA figures instead of IEA figures.
    ["<b>Feedstock</b>","<b>Cost (USD/ton, low estimate)</b>","<b>Cost (USD/ton, high estimate)</b>"],
    ["Biomass",327,1013], # Table 16.
    ["MSW",414,764], # Table 16
    ["Natural Gas (Western Europe)",329,329], # Table 19
    ["Biomethane",706,706],
    ["Wood Pulp",540,800],
    ["Electrolysis",820,1620],
    ["Electrolysis with Direct Air Capture",1220,2380],
    ["Natural Gas",100,200],
    ["Coal",150,250],
    ["Natural Gas with CCS",175,460],
    ["Coal with CCS",320,470]
]

im_methanol_cost = {
    "filename":"methanol_cost.jpg",
    "status":"Done",
    "details":"Chris Chatterton of the Methanol Institute suggested the IRENA/MI report as a better source of cost figures. Most of the figures comes from IRENA/MI, while the CCS value still come from the IEA report.",
    "table":methanol_cost,
    "references":["iea_hydrogen","irena_methanol"],
    "source_file":"methanol.py"
}
helper.save_image(im_methanol_cost)

######################################### Greenhouse gas emissions

# Some calculations for electrolysis
electrolysis_efficiency = 0.5 # dana. See Table 1, PFP for MeOH is half of the eta parameter, so it must be 50% conversion from electricity.
electricity_emissions = 48. # g/kWh, from techco2. Assuming solar power.
electromethanol_emissions_gj = electricity_emissions / electrolysis_efficiency * (1000/3.6) # Grams per GH
electromethanol_emissions_ton = electromethanol_emissions_gj*22./10**6 # https://hypertextbook.com/facts/2005/JennyHua.shtml. Tons CO2 per ton MeOH.

# See table on p. 13 of methanol_ng
gas_methanol = 91.* 22000 / 10**6 # 22 GJ per ton (see above reference).

# Units are tons CO2e per ton methanol
methanol_ghg = [
    ["Coal",2.971], # methanol_coal
    ["Gas",gas_methanol], # methanol_ng
    ["Biomass - Coppice",0.64], # etsap_methanol
    ["Biomass - Forest Residue",0.56], # etsap_methanol
    ["Coal with CCS",2.971*0.351], # methanol_coal
    ["Gas with CCS",gas_methanol*0.351], # Guessing the same capture rate as coal. Based on above values
    ["Electrolysis - Solar",electromethanol_emissions_ton]
]
for i in range(len(methanol_ghg)):
    methanol_ghg[i][1] *= 1000./22
methanol_ghg.append(["Gasoline",103.6])

im_methanol_ghg = {
    "filename":"methanol_ghg.jpg",
    "status":"Done",
    "details":"Greenhouse gases from various methods of methanol, based of various feedstocks and whether CCS is used. Figure are kg CO2e per GJ. Gasoline shown for comparison; give it a special shading.",
    "table":methanol_ghg,
    "references":["methanol_coal","methanol_ng","etsap_methanol","dana","techco2","epa_biofuel"],
    "source_file":"methanol.py"
}
helper.save_image(im_methanol_ghg)

################################## Conversion efficiency

from primary_energy_factors import primary_factors # Source is 'energycode'

# Figures are ratios from methanol energy content to primary energy input
# First number is low estimate, second is high estimate
methanol_efficiency = [
    ["Natural Gas",64,72], # methanol_efficiency
    ["Coal",65,65],
    ["Biomass",50,60],
    ["Electricity",50/primary_factors["Electricity"], 50/primary_factors["Electricity"]] # Efficiency from 'dana'
]

im_methanol_efficiency = {
    "filename":"methanol_efficiency.jpg",
    "status":"Done",
    "details":"Show the conversion efficiencies from primary energy into methanol by various pathways. Figures are percentages. Note that the electricity figure measures efficiency from the primary energy source behind electricity, not electricity itself.",
    "table":methanol_efficiency,
    "references":["dana","energycode","methanol_efficiency"],
    "source_file":"methanol.py"
}
helper.save_image(im_methanol_efficiency)

#######################################################
# Methanol economy
methanol_economy = [
    ["<b>Role</b>","<b>Current mainstream option</b>","<b>Rationale</b>","<b>Challenges</b>"],
    ["Transportation fuel - direct use","Petroleum-derived fuels","Can be blended into current gasoline stock","Low volumetric and gravimetric density."], # olah
    ["Small devices","Batteries, petroleum-derived fuels","Simplicity","Low efficiency"], # dmfc1, dmfc2
    ["Synthetic hydrocarbons","Petroleum-based fuels","Potential low-carbon alternative","High cost"]
]

helper.save_image({
    "filename":"methanol_economy.jpg",
    "status":"Done",
    "details":"Major potential uses for methanol in the energy system. The list is more limited than for hydrogen and ammonia. It is possible that we will want to expand this section and graphic to cover different alcohol-based fuels, but for now, it's just methanol.",
    "table":methanol_economy,
    "references":["olah","dmfc1","dmfc2"],
    "source_file":"methanol.py"
})

######################################## Cost comparison and carbon abatement

# Dollars per ton
methanol_costs = {
    "smr_ccs":317.5,
    "smr_noccs":280,
    "elec":730
}

# The website comingles tons and kg. Using the conversion 1 kg = 22.7 MJ. https://www.world-nuclear.org/information-library/facts-and-figures/heat-values-of-various-fuels.aspx

# Given per GJ
scc = 50
carbon_content = {
    "smr_ccs":31.9 / 22.7,
    "smr_noccs":91. / 22.7,
    "elec":26.7 / 22.7
}
def abatement(key):
    return (methanol_costs[key]-methanol_costs["smr_noccs"])/(carbon_content["smr_noccs"]-carbon_content[key])

methanol_table = [
    ["<b>Method</b>","<b>Cost</b>","<b>Baseline method</b>","<b>Cost</b>","<b>Carbon abatement cost</b>"],
    ["Natural gas SMR with CCS",10**6*(methanol_costs["smr_ccs"]),"Natural gas without CCS",10**6*(methanol_costs["smr_noccs"]),abatement("smr_ccs")],
    ["Electrolysis",10**6*(methanol_costs["elec"]),"Natural gas without CCS",10**6*(methanol_costs["smr_noccs"]),abatement("elec")]
] 

# Plant size: one million tons per year for a large plant. http://www.gasprocessingnews.com/features/201510/small-scale-methanol-technologies-offer-flexibility,-cost-effectiveness.aspx

helper.save_image({
    "filename":"methanol_costs.jpg",
    "status":"Solution",
    "details":"Costs of producing low carbon methanol vs. regular production. Cost of carbon abatement is shown, and for the Costs columns, an SCC of $50/ton is assumed. Costs and GHG content of these methods are elsewhere on the page. These figures are for a 1 million ton per year plant, which according to the source is the threshhold for a plant being considered large.",
    "table":methanol_table,
    "references":["methanol_plant"],
    "source_file":"methanol.py"
})

######################################## Methanol blending in gasoline

# Scenario: replace 5% of gasoline with methanol, such as by replacing 50% of gasoline as M10, or a third as M15.
# Not replacing ethanol, which is a separate analysis.

fraction_us_gasoline_replaced = 0.05

us_gasoline = 9309000*365 # Barrels in 2019
# Based on this, I guess a barrel of gasoline is 42 gallons, and a gallon is 120286 BTU. https://www.eia.gov/energyexplained/units-and-calculators/
# Would be 17165.65059342 TBTU = 18.1097613760581 EJ. Is also 142.70697 billion gallons.
# Average gasoline price: $1.8541666666666667/gallon, according to https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMA_EPM0_PWG_NUS_DPG&f=M

financial_cost_gasoline = 9309000*365*42*1.8541666666666667 * fraction_us_gasoline_replaced

energy_displaced = 9309000*365*42*120286*1055 * fraction_us_gasoline_replaced # In Joules
gasoline_ghg_cost = energy_displaced / 10**12 * 103.6 * scc # In dollars

financial_cost_methanol = energy_displaced / (22.7*10**9) * 150 # With natural gas, without CCS
methanol_ghg_cost = energy_displaced / 10**12 * 91 * scc

blending_table = [
    ["<b>Costs/benefits</b>","<b>Billions of dollars</b>"],
    ["Gasoline, financial",financial_cost_gasoline/10**9],
    ["Gasoline, GHG",gasoline_ghg_cost/10**9],
    ["Methanol, financial",financial_cost_methanol/10**9],
    ["Methanol, GHG",methanol_ghg_cost/10**9]
]

helper.save_image({
    "filename":"methanol_blending.jpg",
    "status":"Done",
    "details":"This revision updates the methanol cost figures to the new values that Chris Chatterton suggested.",
    "table":blending_table,
    "references":["wholesale_gas2021"],
    "source_file":"methanol.py"
})

######################################## High methanol blends, up to M-100

car_upgrade_cost = 583.36 # From https://www.ourenergypolicy.org/wp-content/uploads/2012/04/TIAX-Methanol-Fuel-Blending-Report.pdf. Is 490 in the report, CPI-adjusting from 2010 to 2020.
car_km = 150000 # From some other pages, how car a car is driven
car_efficiency = 25.4 # MPG, 2018. See reference [auto_trends] and consider updating.
car_gallons = car_km / car_efficiency # How many gallons of gasoline a car will use over its lifetime.
car_energy = car_km / car_efficiency * 120286*1055 # How many joules of fuel a car will use over its lifetime.

financial_cost_gasoline = 1.8541666666666667 * car_gallons
gasoline_ghg_cost = car_energy / 10**12 * 103.6 * scc # In dollars

financial_cost_methanol = car_energy / (22.7*10**9) * 280 # With natural gas, without CCS
methanol_ghg_cost = car_energy / 10**12 * 91 * scc

fleet_size = 1000 # Number of cars affected.

blending_table2 = [
    ["<b>Costs/benefits</b>","<b>Millions of dollars</b>"],
    ["Gasoline, financial",financial_cost_gasoline*fleet_size / 10**6],
    ["Gasoline, GHG",gasoline_ghg_cost*fleet_size / 10**6],
    ["Methanol, financial",financial_cost_methanol*fleet_size / 10**6],
    ["Methanol, GHG",methanol_ghg_cost*fleet_size / 10**6],
    ["Engine upgrades",car_upgrade_cost * fleet_size / 10**6]
]

helper.save_image({
    "filename":"methanol_blending2.jpg",
    "status":"Done",
    "details":"Another analysis of methanol blending. This was is for higher blend ratios, up to 100%, so that they necessitate upgrades to engines (see the reference for cost figures, CPI-adjusted to 2020), which are accounted for as a cost. This applies to a hypothetical fleet of 1000 cars. Aside from the cost of engine upgrades, all figures are as in the other methanol blending solution.",
    "table":blending_table2,
    "references":["meoh_upgrade"],
    "source_file":"methanol.py"
})

################################## Some DME calculations

dme_price = 10.43 # Dollars per MMBTU. There are several figures; going with this one. From https://www.sciencedirect.com/science/article/abs/pii/S0306261919300455
# Plant size is 2647 million tons per day.
dme_price_gj = dme_price * 1.055 # Convert to GJ, so price is in $/GJ
# https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMA_EPD2D_PWG_NUS_DPG&f=M . Converting per-gallon to per-MMBTU
diesel_price = (1.789+1.950+2.02+2.1+2.106+1.874+1.938+1.865+1.955+1.984+1.974+1.943)/12*7.194244604316546 

dme_mmbtu_per_ton = dme_price_gj * 31.7 # On Transportation Fuels page, 31.7 MJ/kg - 31.7 GJ/ton.
dme_annual_tons = 2647*365
dme_value = dme_mmbtu_per_ton * dme_annual_tons

dme_fuel_economy_equiv = 5.30/6.02 # See https://afdc.energy.gov/files/u/publication/ornl_dme_tm-2014-59.pdf, p. 19. On a BTU basis, the
diesel_value = dme_value * diesel_price / dme_price * dme_fuel_economy_equiv

dme_emissions = 88.9 * 31.7 * dme_annual_tons / 1000 * scc # https://www.sciencedirect.com/science/article/pii/S0959652620335265
# Assumes DME made from methanol that is produced from natural gas reforming.
diesel_emissions = dme_emissions * dme_fuel_economy_equiv * 97/88.9 # The 97 from https://www.epa.gov/fuels-registration-reporting-and-compliance-help/lifecycle-greenhouse-gas-results

dme_table = [
    ["<b>Factor</b>","<b>Cost/Benefit</b>"],
    ["DME cost",dme_value],
    ["DME greenhouse gases",dme_emissions],
    ["Diesel cost",diesel_value],
    ["Diesel greenhouse gases",diesel_emissions]
]

helper.save_image({
    "filename":"dme.jpg",
    "status":"Done",
    "details":"Analysis of a dimethyl ether plant for trucking. Cost of producing DME from Mevawala et al. Diesel prices are the average wholesale price in 2019 (as 2020 was an unusual year) and are taken from the EIA. DME has a lower fuel economy, even accounting for energy density, than diesel, and the fuel economy is accounted for and taken from Szybist et al. Emissions from DME are taken from Al-Breiki and Bicer, and from diesel are from the EPA. I would like to include a figure on the cost of upgrading trucks to use DME but haven't found a good figure yet. To be clear, the DME values are costs and the (avoided) diesel values are benefits.",
    "table":dme_table,
    "references":["dme_price","diesel_price","dme_fuel_economy","dme_emissions","epa_biofuel"],
    "source_file":"methanol.py"
})

#######################################################

# Current status

meoh_production = [
    ["<b>Purpose</b>","<b>Share of Demand</b>"],
    ["Methyl tert-butyl ether (MTBE)","11%"],
    ["Gasoline blending","14%"],
    ["Biodiesel","3%"],
    ["Dimethyl Ether","3%"],
    ["Methanol to olefins","25%"],
    ["Formaldehyde","25%"],
    ["Other chemicals","19%"]
]

helper.save_image({
    "filename":"meoh_demand.jpg",
    "status":"Done",
    "details":"Rough estimate of demand for methanol. I combined several chemicals into the 'other chemicals' category. Do something to visually distinguish the energy uses of methanol (the first four on the list) from the chemical uses.",
    "table":meoh_production,
    "references":["irena_methanol"],
    "source_file":"methanol.py"
})

helper.save_image({
    "filename":"meoh_production.jpg",
    "status":"Done",
    "details":"Some information about methanol production. The amounts are 65% from natural gas, 35% from coal, and <1% from other sources. If doing this as a bar graph, portray the other sources as a small bar.",
    "references":["irena_methanol"],
    "source_file":"methanol.py"
})