# Hydrogen
# There is a hydrogen.py file in the parent folder. This one actually generates files, and the other may be merged into it with time.

import helper
import data_lcoe

# Levelized cost of hydrogen. This goes up here because I am using it in multiple places.
lcoh_table = [
    ["<b>Fuel</b>","<b>Cost, USD per GJ</b>"],
    ["Natural Gas (steam methane reforming)","5.6 - 12.8"],
    ["Natural Gas with CCS (SMR)","9.6 - 16.8"],
    ["Coal","15.2-20"],
    ["Coal with CCS","16.8 - 20.8"],
    ["Electrolysis","25.6 - 61.6"],
    ["Biomass","17.23"],
    ["Biomass with CCS","25.92"],
    ["Methane Pyrolysis","13.54"],
    ["Nuclear Thermochemical (under development)","15.15"],
    ["Solar Thermochemical (under development)","14.40-35.74"], # Conversion factor is used, 1 USD = 1.3 Australian dollars.
    ["Solar Photochemical (under development)","12.80-83.20"]
]

hydrogen_economy = [
    ["<b>Usage</b>","<b>Current Dominant Method</b>","<b>Rationale</b>","<b>Challenges</b>"],
    ["Residential and Commercial Heating and Cooking","Natural gas, electricity, fuel oil, biomass","Can be added to existing gas pipelines; augment heat pumps on cold days.","Safety; Competition with electricity and district heating"], # hydrogen_ccc, dodds for the safety point
    ["Automobiles","Gasoline from crude oil","Gravimetric density of hydrogen, vehicle range","Lack of infrastructure; high cost of vehicles and fuel"], # fcev_bev
    ["Trucking","Diesel from crude oil","Few low-carbon options","Infrastructure; high cost"], # hydrogen_truck
    ["Aviation","Kerosene from crude oil","Few low-carbon options","Significant R&D needed"], # hydrogen_plane
    ["Shipping","Diesel from crude oil","Few low-carbon options","High cost"], # hydrogen_cargo, hydrogen_cargo2 for cost
    ["Rail Transport","Diesel, electricity","Lower capital cost than electric","Competes with electric rail; not suitable for freight"], # hydrail
    ["Synthetic Hydrocarbons","Fossil Fuels","Fits with current transportation infrastructure","High cost"],
    ["Seasonal Energy Storage","Pumped Hydro","Limited seasonal storage options","Low efficiency"],
    ["Grid Load Balancing","Various Strategies","Demand response can balance a high-renewable grid","Increases cost of hydrogen"], # iea_hydrogen
    ["Steel","Coke from coal","Few low-carbon options","Significant R&D needed"], # fisch
    ["Industrial Heat","Coal and natural gas","Best low-carbon option for some heat applications","High cost"], # ccc_hydrogen
    ["Plastics and Other Chemicals","Petrochemical feedstocks","Few low-carbon options","High cost"], # iea_hydrogen
    ["Distributed Energy","Diesel generators, solar","Remote applications, resilience, local energy storage","---"],
    ["Ammonia","Haber-Bosch Process","Could fulfill several important roles in the energy system","---"],
    ["Methanol","Synthesis Gas (mostly from fossil fuels)","Could fulfill several important roles in the energy system","---"]
]

helper.save_image({
    "filename":"hydrogen_economy.jpg",
    "status":"Done",
    "table":hydrogen_economy,
    "details":"Infographic showing how hydrogen could fit into the energy system. Hydrogen could conceivably be used for almost all non-electricity end uses, though in many cases is still a ways from being practical. Some sources are included, but the figure caption will also link to other pages. The Hydrogen page is still meant to focus more on how to produce hydrogen than on how to use it.",
    "references":["hydrogen_ccc","dodds","fcev_bev","hydrogen_truck","hydrogen_plane","hydrogen_cargo","hydrogen_cargo2","hydrail","iea_hydrogen","fisch","ccc_hydrogen"],
    "source_file":"hydrogen.py"
})

# Hydrogen solutions

# As per this source, we assume 50,000 kg hydrogen per day, which is at the boundary between medium and large plants.
# https://www.energy.gov/sites/prod/files/2017/11/f46/HPTT%20Roadmap%20FY17%20Final_Nov%202017.pdf

baseline_smr = ((5.6+12.8)/2+ 0.93)*50000*365
baseline_ccs = ((9.6+16.8)/2 + 0.83)*50000*365
baseline_elec = ((25.6+61.8)/2 + 3.37)*50000*365
plant_table = [
    ["<b>Option</b>","<b>Option cost</b>","<b>Baseline</b>","<b>Baseline cost</b>","<b>Carbon abatement cost</b>"],
    # Financial cost, externalities, and CO2 (at $50/ton) for overall hydrogen cost
    ["Hydrogen plant, electrolysis",baseline_elec + (9.9*data_lcoe.scc/10**3)*50000*365,"Hydrogen plant with SMR",baseline_smr +(101.8*data_lcoe.scc/10**3)*50000*365,(baseline_elec-baseline_smr)/(101.8-9.9)*1000/50000/365],
    ["Add CCS to an SMR plant",baseline_ccs + (43.2*data_lcoe.scc/10**3)*50000*365,"Hydrogen plant without CCS",baseline_smr +(101.8*data_lcoe.scc/10**3)*50000*365,(baseline_ccs-baseline_smr)/(101.8-43.2)*1000/50000/365]
]

helper.save_image({
    "filename":"h2_production.jpg",
    "status":"Done",
    "table":plant_table,
    "details":"Another update. For now we are just reporting H2 production (at least here), and not the various other things that can be done with the hydrogen economy. Costs are in dollars per year for a 50,000 kg/day hydrogen plant (see the reference). These figures account for financial, GHG, and non-GHG external costs, but not land use. Recently added is the rightmost column, the carbon abatement cost. This is what the social cost of carbon should be for the two options to be equal to each other. In other words, if the SCC is greater than $67/ton, then blue hydrogen makes sense, and if it is less than $67/ton, it doesn't make sense. For the other costs, an SCC of $50/ton is assumed.<br><br>This plot is not part of a solution box.",
    "references":["hydrogen_plant"],
    "source_file":"hydrogen.py"
})

########################## Levelized cost of hydrogen

helper.save_image({
    "filename":"lcoh.jpg",
    "status":"Done",
    "table":lcoh_table,
    "details":"I am updating this chart with some figures from the IEA, which I think are better when they exist. SMR (with and without CCS), Coal (with and without CCS), and Electrolysis come from the IEA; the solar thermochemical figures from Hinkey et al.;the solar photochemical figure from Pinaud et al.; and the rest are from Parkinson et al. as before. A conversion was used of $1.30 ASD = $1 USD. These calculations are based on 125 MJ per kg of hydrogen.",
    "references":["lcoh","iea_lcoh","solar_hydrogen","photochem"],
    "source_file":"hydrogen.py"
})

########################### Electrolyzer comparison

electrolyzer_table = [
    ["<b>Metric</b>","<b>ALK 2017</b>","<b>ALK 2025</b>","<b>PEM 2017</b>","<b>PEM 2025</b>"],
    ["Low Heating Value","65%","68%","57%","64%"],
    ["Stack Lifetime","80,000 hr","90,000 hr","40,000 hr","50,000 hr"],
    ["CAPEX, USD/kW","$910","$583","$1457","$850"],
    ["Ramping Rate","0.2-20%/second","","100%/second",""],
    ["Start-up Time","1-10 minutes","","1 second - 5 minutes",""]
]

helper.save_image({
    "filename":"electrolyzer.jpg",
    "status":"Done",
    "table":electrolyzer_table,
    "details":"Comparison of electrolyzers. I selected only a few metrics to show. ALK = alkaline and PEM = proton exchange membrane. SOEC (solid oxide electrolyser cell) is not shown.<br><br>This is not part of a solution box.",
    "references":["irena_h2"],
    "source_file":"hydrogen.py"
})