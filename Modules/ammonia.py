# Ammonia. There is also an ammonia.py in the parent folder. This one actually generates images. May merge the two eventually.

import helper

ammonia_economy = [
    ["<b>Role</b>","<b>Current Dominant Methods</b>","<b>Rationale</b>","<b>Challenges</b>"],
    ["Seasonal Energy Storage","Pumped Hydro","More efficient, lower storage cost than hydrogen",""], # ammonia_density
    ["Transportation of Hydrogen","Local production, pipeline, liquefaction, compression","More efficient, lower cost",""], # ammonia_density
    ["Load Balancing","Gas peaking","Ammonia electrolyzers can be run intermittently","Increases cost of ammonia"], # iea_industry_ren
    ["Thermal power","Rankine cycle (water)","Kalina cycle would improve thermal plant performance, especially for geothermal and OTEC",""], # ammonia_density
    ["Carbon capture and sequestration","","Improved efficiency and lower cost","Design challenges, R&D needed"], # ammonia_density
    ["Transportation fuel","Petroleum-derived fuels","Little or no modification of combustion engines required","Low volumetric and gravimetric density, high combustion temperature, toxicity"] # ammonia_transportation
]

helper.save_image({
    "filename":"ammonia_economy.jpg",
    "status":"Done",
    "details":"Infographic showing various ways in which ammonia can be used in a low-carbon energy system.",
    "table":ammonia_economy,
    "references":["ammonia_density","iea_industry_ren","ammonia_transportation"],
    "source_file":"ammonia.py"
})

helper.save_image({
    "filename":"ammonia_ghg.jpg",
    "status":"Done",
    "details":"Natural gas steam methane reforming was missing the CCS value, so I'm adding it here. Let's go with 1.466 kg CO2e/kg ammonia, based on the reference and the value that's in the table.",
    "references":["ammonia_ccs"],
    "source_file":"ammonia.py"
})

################################ Abatement costs

# Based on reference 'ammonia_size', going with 500 million tons per day (the threshhold between small and large plants)
# Average costs are reported and an SCC of $50/ton.

ammonia_costs = {
    "smr_ccs":320,
    "smr_noccs":300,
    "elec_3_8500":370,
    "elec_3_4000":420,
    "elec_6_8500":630,
    "elec_6_4000":680
}

carbon_content = {
    "smr_ccs":1.466,
    "smr_noccs":3.032,
    "elec_3_8500":0.496, # Assuming wind
    "elec_3_4000":0.496,
    "elec_6_8500":0.496,
    "elec_6_4000":0.496
}

ammonia_size = 500 * 365
scc = 50

def total_cost(key):
    return ammonia_costs[key]+carbon_content[key]*scc
def carbon_abatement(key):
    return (ammonia_costs["smr_noccs"]-ammonia_costs[key])/(carbon_content[key]-carbon_content["smr_noccs"])

ammonia_cost = [
    ["<b>Method</b>","<b>Cost per Year</b>","<b>Baseline</b>","<b>Cost per Year</b>","<b>CO2 abatement cost</b>"],
    ["Natural Gas Steam Methane Reforming with CCS",total_cost("smr_ccs")*ammonia_size, "Without CCS", total_cost("smr_noccs")*ammonia_size,carbon_abatement("smr_ccs")],
    ["Eletrolysis, 6 cents/kWh, 4000 hr/yr",total_cost("elec_6_4000")*ammonia_size, "Without CCS", total_cost("smr_noccs")*ammonia_size,carbon_abatement("elec_6_4000")],
    ["Eletrolysis, 6 cents/kWh, 8500 hr/yr",total_cost("elec_6_8500")*ammonia_size, "Without CCS", total_cost("smr_noccs")*ammonia_size,carbon_abatement("elec_6_8500")],
    ["Eletrolysis, 3 cents/kWh, 4000 hr/yr",total_cost("elec_3_4000")*ammonia_size, "Without CCS", total_cost("smr_noccs")*ammonia_size,carbon_abatement("elec_3_4000")],
    ["Eletrolysis, 3 cents/kWh, 8500 hr/yr",total_cost("elec_3_8500")*ammonia_size, "Without CCS", total_cost("smr_noccs")*ammonia_size,carbon_abatement("elec_3_8500")],
]

helper.save_image({
    "filename":"ammonia_carbon.jpg",
    "status":"Solution",
    "details":"Cost comparision of ammonia plants and carbon mitigation cost. The cost per year metric assumes a social cost of carbon of $50/ton. The plant size is 500 tons per day, which is the threshhold between small and large plants that ThyssenKrupp gives.",
    "table":ammonia_cost,
    "references":["ammonia_size"],
    "source_file":"ammonia.py"
})

############################## Shipping to Japan

shipping_table = [
    ["<b>Area</b>","<b>Cost in 2035 (USD)</b>"],
    ["Ocean Shipping",40.40],
    ["Coastal Tanker",12.50],
    ["Terminal",10.00],
    ["Total",62.90]
]

helper.save_image({
    "filename":"ammonia_shipping.jpg",
    "status":"Done",
    "details":"An illustration of the breakdown of the cost of shipping ammonia from the Middle East to Japan in 2035, as estimated by the report.",
    "table":shipping_table,
    "references":["ieej"],
    "source_file":"ammonia.py"
})

############################## Some minor fixes

helper.save_image({
    "filename":"ammonia_energy.jpg",
    "status":"Done",
    "details":"At John's suggestion the 'World Average' bar should be renamed to 'Existing Plants'.",
    "references":[],
    "source_file":"ammonia.py"
})

############################## Ammonia for shipping. One of the solutions

ammonia_baseline_price = 246.27450980392157 # Derived from https://www.sciencedirect.com/science/article/pii/S2352484720312312, Table 3
ammonia_price_ccs = 420
base_price = 830
ammonia_price_electrolysis = 830

nh3_distribution_cost = 6*1.15 # Based on https://smartport.nl/wp-content/uploads/2020/09/Cost-Analysis-Power-2-Fuel_def_2020.pdf, p. 13, distribution cost for E-NH3 for maritime, $6/ton. Exchange rate of 1.15 is estimated.

nh3_engine_cost = 12300000*1.15*13500/30000 / 10**6 # Euros, converted to USD, based on https://smartport.nl/wp-content/uploads/2020/09/Cost-Analysis-Power-2-Fuel_def_2020.pdf
# For the 2500 TEU vessel considered, a main engine capacity of 13.5 MW is considered, while 30,000 kW is in the paper above. Hence the conversion.

hfo_price = [95.832, 9.801, 3.267]
ammonia_price = [371.1372 * (ammonia_baseline_price+nh3_distribution_cost)/base_price, hfo_price[1]+nh3_engine_cost, 2.3052]
smr_ccs_price = [371.1372 * (ammonia_price_ccs+nh3_distribution_cost)/base_price, hfo_price[1]+nh3_engine_cost, 2.3052]
elec_price = [371.1372 * (ammonia_price_electrolysis+nh3_distribution_cost)/base_price, hfo_price[1]+nh3_engine_cost, 2.3052]
hfo_emissions = 48400*25 # I am guessing these are annual emissions figures, over a 25 year life.
ammonia_emissions = 4400 * 3.032/1.277 * 25 # Based on the Kim study, assuming solar PV electrolysis, and adjusting with numbers on the site.
smr_ccs_emissions = 6000 * 25
elec_emissions = 4400 * 25

shipping_table = [
    ["<b>Factor</b>","<b>Cost or Benefit (million of dollars)</b>"],
    ["Heavy Fuel Oil, Fuel",hfo_price[0]],
    ["Heavy Fuel Oil, CAPEX",hfo_price[1]],
    ["Heavy Fuel Oil, O&M",hfo_price[2]],
    ["Ammonia (no CCS), Fuel",ammonia_price[0]],
    ["Ammonia (no CCS), CAPEX",ammonia_price[1]],
    ["Ammonia (no CCS), O&M",ammonia_price[2]],
    ["Ammonia (SMR+CCS), Fuel",smr_ccs_price[0]],
    ["Ammonia (SMR+CCS), CAPEX",smr_ccs_price[1]],
    ["Ammonia (SMR+CCS), O&M",smr_ccs_price[2]],
    ["Ammonia (Electrolysis), Fuel",elec_price[0]], # Assumes ammonia at $830/ton
    ["Ammonia (Electrolysis), CAPEX",elec_price[1]],
    ["Ammonia (Electrolysis), O&M",elec_price[2]],
    ["<b>Greenhouse gas emissions</b>","<b>Tons CO<sub>2</sub>e</b>"],
    ["Heavy Fuel Oil",hfo_emissions],
    ["Ammonia (no CCS)",ammonia_emissions],
    ["Ammonia (SMR+CCS)",smr_ccs_emissions],
    ["Ammonia (Electrolysis)",elec_emissions],
    ["<b>Carbon Abatement Costs Relative to HFO</b>","<b>Dollars per ton of CO<sub>2</sub> reduced.</b>"],
    ["Ammonia (no CCS)",(sum(ammonia_price)-sum(hfo_price))/(hfo_emissions-ammonia_emissions)*10**6],
    ["Ammonia (SMR+CCS)",(sum(smr_ccs_price)-sum(hfo_price))/(hfo_emissions-smr_ccs_emissions)*10**6],
    ["Ammonia (Electrolysis)",(sum(elec_price)-sum(hfo_price))/(hfo_emissions-elec_emissions)*10**6]
]

helper.save_image({
    "filename":"ammonia_shipping_cost.jpg",
    "status":"Solution",
    "table":shipping_table,
    "details":"This is an analysis of building a 2500 TEU (Twenty-foot equivalent unit) feeder ship using heavy fuel oil, as is most common now, with ammonia (steam methaned reform without carbon capture and sequestration), ammonia produced from SMR with CCS, and ammonia produced from electrolysis from low-carbon electricity sources. Assumptions include $830/ton to produce ammonia from electrolysis, as in the paper, and $420/ton for SMR+CSS, the upper end I have on the site already, and about $246 for SMR ammonia without CCS, as calculated from Al-Breiki and Bicer. Most other figures are from Kim et al. A distribution cost of about $7/ton is estimated from TNO. I also don't trust the fact that the CAPEX+O&M costs are basically the same in the Kim et al. report, so I am using the incrementental CAPEX cost in the TNO report for the ammonia solutions.<br><br>The baseline is shipping with HFO, and the three solutions there are shipping with the three ammonia options.",
    "references":["ammonia_shipping","ammonia_distribution","bicer2"],
    "source_file":"ammonia.py"
})