# Recycling. Note: image creation functions are commented out at the moment.

import helper

# Emissions and energy factors for WARM model. https://www.epa.gov/warm/documentation-chapters-greenhouse-gas-emission-energy-and-economic-factors-used-waste-reduction

# In MMBTU/ton
# These were determined through warm15 by comparing one ton of landfilling with one ton of recycling for various commodities.
recycling_energy_savings = {
    "Paper": 20.41, # Mixed paper
    "Food Waste":-0.57,
    "Yard Trimmings":-0.43,
    "HDPE":50.5, # Overwritten below
    "PET":32.19, # Overwritten below
    "Aluminum":153.03, # Aluminum Cans
    "Steel":20.23, # Steel Cans
    "Glass":2.39,
    "Asphalt Concrete":1.49,
    "Asphalt Singles":2.68,
    "Concrete":0.38,
    "Wood":-0.35, # Dimensional Lumber
    "Tires":3.87,
    "Copper Wire":82.86
}

# MTCO2e/ton (metric tons CO2 per short ton of material)
recycling_co2_savings = {
    "Paper": 3.69, # Mixed paper
    "Food Waste":0.72,
    "Yard Trimmings":-0.03,
    "HDPE":0.87, # Overwritten below
    "PET":1.17, # Overwritten below
    "Aluminum":9.15, # Aluminum Cans
    "Steel":1.85, # Steel Cans
    "Glass":0.3,
    "Asphalt Concrete":0.1,
    "Asphalt Singles":0.11,
    "Concrete":0.03,
    "Wood":1.46, # Dimensional Lumber
    "Tires":0.4,
    "Copper Wire": 4.51
}

# In MMBTU/ton
# These were determined through warm15 by comparing one ton of landfilling with one ton of recycling for various commodities.
combustion_energy_savings = {
    "Paper": 6.51, # Mixed paper
    "Food Waste":2.24,
    "Yard Trimmings":2.79,
    "HDPE":19.09, # Overwritten below
    "PET":10.25, # Overwritten below
    "Aluminum":-0.05, # Aluminum Cans
    "Steel":17.68, # Steel Cans
    "Glass":-0.22,
    "Asphalt Concrete":0,
    "Asphalt Singles":9.07,
    "Concrete":0.0,
    "Wood":8.06, # Dimensional Lumber
    "Tires":29.06,
    "Copper Wire":82.86
}

# MTCO2e/ton (metric tons CO2 per short ton of material)
combustion_co2_savings = {
    "Paper": 0.63, # Mixed paper
    "Food Waste":0.68,
    "Yard Trimmings":-0.01,
    "HDPE":-1.27, # Overwritten below
    "PET":-1.22, # Overwritten below
    "Aluminum":-0.01, # Aluminum Cans
    "Steel":1.61, # Steel Cans
    "Glass":-0.01,
    "Asphalt Concrete":0.0,
    "Asphalt Singles":0.37,
    "Concrete":0.00,
    "Wood":-0.43, # Dimensional Lumber
    "Tires":-0.48,
    "Copper Wire": 4.51
}

# For below, see https://www.epa.gov/sites/production/files/2019-06/documents/warm_v15_organics.pdf for notes on yard waste and food waste.
# But I think I will avoid using virgin production figures for those.

# Energy for manufacturing from 100% virgin material
virgin_energy = {
    "Glass":7.08, # https://www.epa.gov/sites/production/files/2019-06/documents/warm_v15_containers_packaging_non-durable_goods.pdf, Exhibit 1.2
    "Aluminum":184.74+0.91, # Above, Exhibit 2.5
    "Steel": 31.58+4.6, # Exhibit 2.5
    "Copper Wire": 122.52+0.46, # Exhibit 2.5
    "Paper": 0.48*25.13 + 0.08*32.99 + 0.24*39.92 + 0.2*37.01, # Energy per paper class from Exhibit 3-13 and the mix for Mixed Paper from Exhibit 3-4
    "HDPE": 23.59+2.74, # Exhibits 5-8 and 5-9
    "PET": 28.06+2.79,
    "Asphalt Concrete":0.94+0.73, # https://www.epa.gov/sites/production/files/2019-06/documents/warm_v15_construction_materials.pdf, Exhibits 1-7 and 1-8.
    "Asphalt Shingles":2.15+0.58, # Exhibits 2-7 and 2-8
    "Wood":0.17, # Exhibit 11-7
    "Tires":73.79 # https://www.epa.gov/sites/production/files/2019-06/documents/warm_v15_tires.pdf, Exhibit 1-10
}
# Fixes for plastics. I wonder how many others are wrong.
recycling_energy_savings["HDPE"] = virgin_energy["HDPE"] - (5.19+2.31)
recycling_energy_savings["PET"] = virgin_energy["PET"] - (11.77+2.6)

virgin_co2 = {
    "Glass":0.6, # https://www.epa.gov/sites/production/files/2019-06/documents/warm_v15_containers_packaging_non-durable_goods.pdf, Exhibit 1.9
    "Aluminum":10.99, # Exhibit 2-11
    "Steel":3.64,
    "Copper Wire": 6.78,
    "Paper":7.61, # Exhibit 3-11
    "HDPE": 1.52, #Exhibit 5-6
    "PET":2.21, # Exhibit 5-6
    "Asphalt Concrete":0.11, # https://www.epa.gov/sites/production/files/2019-06/documents/warm_v15_construction_materials.pdf, Exhibit 1.5
    "Asphalt Shingles":0.19, # Exhibit 2-5.
    "Wood":2.02, # Exhibit 11-5
    "Tires":4.46 # https://www.epa.gov/sites/production/files/2019-06/documents/warm_v15_tires.pdf, Exhibit 1-7
}
    
# Unit conversion
for key in recycling_energy_savings:
    recycling_energy_savings[key] = recycling_energy_savings[key] / 1.055 / 0.907185 # Convert to GJ/metric ton
for key in recycling_co2_savings:
    recycling_co2_savings[key] = recycling_co2_savings[key] / 0.907185 # Convert to tons CO2e/metric ton
for key in combustion_energy_savings:
    combustion_energy_savings[key] = combustion_energy_savings[key] / 1.055 / 0.907185 # Convert to GJ/metric ton
for key in combustion_co2_savings:
    combustion_co2_savings[key] = combustion_co2_savings[key] / 0.907185 # Convert to tons CO2e/metric ton
for key in virgin_energy:
    virgin_energy[key] = virgin_energy[key] / 1.055 / 0.907185 # Convert to GJ/metric ton
for key in virgin_co2:
    virgin_co2[key] = virgin_co2[key] / 0.907185 # Convert to tons CO2e/metric ton

# Commodities for the first plots showing energy and GHG savings
plot1commodities = ["Aluminum","Steel","Copper Wire","HDPE","PET","Paper","Glass","Wood"]
plot_energy = [["<b>Commodity</b>","<b>Energy for Virgin Production (GJ/ton)</b>","<b>Energy for Production from Recycling (GJ/ton)</b>"]] + [ [ plot1commodities[i],virgin_energy[plot1commodities[i]],virgin_energy[plot1commodities[i]]-recycling_energy_savings[plot1commodities[i]] ] for i in range(len(plot1commodities))]
plot_energy_im = {
    "filename":"recycling_energy.jpg",
    "status":"Done",
    "table":plot_energy,
    "details":"Show the energy savings for recycling various commodities. The table shows energy (gigajoules per ton) to produce the commodity from virgin material and from recycled material.",
    "references":["warm15"],
    "source_file":"recycling.py"
}
#helper.save_image(plot_energy_im)

plot_ghg = [["<b>Commodity</b>","<b>GHG for Virgin Production (Tons COe2/ton)</b>","<b>GHG for Production from Recycling (Tons COe2/ton)</b>"]] + [ [ plot1commodities[i],virgin_co2[plot1commodities[i]],virgin_co2[plot1commodities[i]]-recycling_co2_savings[plot1commodities[i]] ] for i in range(len(plot1commodities))]
plot_ghg_im = {
    "filename":"recycling_ghg.jpg",
    "status":"Done",
    "table":plot_ghg,
    "details":"Show the greenhouse gas savings for recycling various commodities. The table shows GHG (tons CO<sub>2</sub>-equivalent per ton of material) to produce the commodity from virgin material and from recycled material.",
    "references":["warm15"],
    "source_file":"recycling.py"
}
#helper.save_image(plot_ghg_im)

################################
# From msw_stats15. In 2015, thousands of tons. Table 1
waste_generation = {
    "Paper":68050,
    "Glass":11470,
    "Steel":18170, # Ferrous
    "Aluminum":3610,
    "Other Nonferrous":2220,
    "PET":5100, # Table 8
    "HDPE":6040, # Table 8
    "Other Plastic":34500-6040-5100, # Want to break this down
    "Tires": 3750, # Table 9
    "Rubber and Leather":8480-3750,
    "Textiles":16030,
    "Wood":16300,
    "Other":5160,
    "Food":39730,
    "Yard Trimmings":34720,
    "Miscellaneous Inorganic Wastes":3990
}
# Table 2, 2015
recycled_composted = {
    "Paper":45320,
    "Glass":3030,
    "Steel":6060,
    "Aluminum":670,
    "Other Nonferrous":1500,
    "PET": 940, # Table 8
    "HDPE":620, # Table 8
#    "Plastic":3140,
    "Tires":1510, # Table 9
    "Rubber and Leather":1510-1510,
    "Textiles":2450,
    "Wood":2660,
    "Other":1430,
    "Food":2100,
    "Yard Trimmings":21290,
    "Miscellaneous Inorganic Wastes":0
}
# Table 3, 2015
combustion = {
    "Paper":4450,
    "Glass":1470,
    "Steel":2140,
    "Aluminum":500,
    "Other Nonferrous":60,
    # Figures by resin are not given, so I am guessing they are combusted in numbers proportional to total generation
    "PET": 5100./34500. * 5350., # Table 8
    "HDPE": 6040./34500. * 5350., # Table 8
    "Tires":1780, # Table 9
    "Rubber and Leather":2490-1780,
    "Textiles":3050,
    "Wood":2580,
    "Other":690,
    "Food":7380,
    "Yard Trimmings":2630,
    "Miscellaneous Inorganic Wastes":780
}
# Convert to metric tons
for key in waste_generation:
    waste_generation[key] *= 0.907185
for key in recycled_composted:
    recycled_composted[key] *= 0.907185
for key in combustion:
    combustion[key] *= 0.907185

recycling_rates = [["<b>Commodity</b>","<b>Share of material recycled or composted</b>"]] + [
    [ commodity, float(recycled_composted[commodity])/waste_generation[commodity] ]
    for commodity in recycled_composted if recycled_composted[commodity] > 0
]
recycling_rate_im = {
    "filename":"recycling_rates.jpg",
    "status":"Done",
    "details":"Recycling and composting rates by various commodities.",
    "table":recycling_rates,
    "references":["msw_stats15"],
    "source_file":"recycling.py"
}
#helper.save_image(recycling_rate_im)

# From Table 2 and Figure 2 of https://www.epa.gov/sites/production/files/2018-07/documents/2015_smm_msw_factsheet_07242018_fnl_508_002.pdf
recycling_time_series = [
    [1960,"6.4%"],[1965,"6.2%"],[1970,"6.6%"],[1975,"7.3%"],[1980,"9.6%"],[1985,"10.1%"],[1990,"16.0%"],[1995,"21.7%"],[2000,"28.5%"],[2005,"31.4%"],[2010,"34.0%"],[2014,"34.6%"],[2015,"34.7%"]
]
recycling_time_im = {
    "filename":"recycling_history.jpg",
    "status":"Done",
    "details":"History of recycling rates in the US. Figures are share of MSW (not C&D) that are recycled or composted, by weight.",
    "table":recycling_time_series,
    "references":["msw_stats15"],
    "source_file":"recycling.py"
}
#helper.save_image(recycling_time_im)

combustion_time_series = [
    [1960,0],[1970,0.5/121/1],[1980,2.8/151.6],[1990,29.8/208.3],[2000,33.7/243.5],[2005,31.7/251.1],[2010,29.3/251.1],[2014,33/259.0],[2015,33.5/262.4]
]
combustion_time_im = {
    "filename":"combustion_history.jpg",
    "status":"Done",
    "details":"History of combustion rates in the US. Share of MSW that is combusted, by weight.",
    "table":combustion_time_series,
    "references":["msw_stats15"],
    "source_file":"recycling.py"
}
#helper.save_image(combustion_time_im)

################################# Overall energy and GHG savings potential
# Link commodity names between the above data sets. No need to include if they are the same
commodity_map = {
    "Food":"Food Waste",
    "Other Nonferrous":"Copper Wire" # Could be risky
}
for key in waste_generation:
    if key in recycling_energy_savings and key not in commodity_map:
        commodity_map[key] = key
# Terajoules
potential_energy_savings = sum([
    recycling_energy_savings[commodity_map[key]]*(waste_generation[key]-recycled_composted[key]) - combustion_energy_savings[commodity_map[key]]*combustion[key]
    for key in commodity_map])
current_energy_savings = sum([recycling_energy_savings[commodity_map[key]]*(recycled_composted[key]) for key in commodity_map])

# Thousands of tons CO2e.
potential_ghg_savings = sum([
    recycling_co2_savings[commodity_map[key]]*(waste_generation[key]-recycled_composted[key]) - combustion_co2_savings[commodity_map[key]]*combustion[key]
    for key in commodity_map])
current_ghg_savings = sum([recycling_co2_savings[commodity_map[key]]*(recycled_composted[key]) for key in commodity_map])

savings_im = {
    "filename":"recycling_savings.jpg",
    "status":"Done",
    "table":[
        ["Current Energy Savings from Recycling",str(current_energy_savings/10**6) + " Exajoules"],
        ["Potential Energy Savings from Recycling",str(potential_energy_savings/10**6) + " Exajoules"],
        ["Current GHG Savings from Recycling",str(current_ghg_savings/10**3) + " Million Tons CO2e"],
        ["Potential GHG Savings from Recycling",str(potential_ghg_savings/10**3) + " Million Tons CO2e"]
    ],
    "details":"Current and potential additional energy and GHG savings from recycling or composting in the US. Potential savings are additional (i.e. on top of what is already being saved) by recycling or composting all material that is currently landfilled or combusted. At least all material that I can find data for, which includes the following: food waste, aluminum, steel, other nonferrous metals (which I am treating as copper), paper, PET plastic, HDPE plastic, yard waste, wood, tires, and paper. I am not included construction and demolition, as I do not have good recycling figures for those, but I would like to add that. Some other materials not included are leather, textiles, and other kinds of plastic.",
    "references":["msw_stats15","warm15"],
    "source_file":"recycling.py"
}
#helper.save_image(savings_im)

################################# Job creation figures
recycling_jobs = [["<b>Tool</b>","<b>Jobs per 1000 tons of waste per year</b>"],["Remanufacturing","2.5-17.3"],["Recycling",1.2],["Landfilling or Incineration",0.66]]

jobs_im = {
    "filename":"recycling_jobs.jpg",
    "status":"Done",
    "table":recycling_jobs,
    "details":"Jobs from waste management. The key message is that the big job creator is remanufacturing, though recycling is necessary so there is material to remanufacture from.",
    "references":["morejobs"],
    "source_file":"recycling.py"
}
#helper.save_image(jobs_im)

################################## Other stuff
# Translation from carbon price to price on MSW landfilling
total_msw = 262430000 * 0.907185 # https://www.epa.gov/sites/production/files/2018-07/documents/smm_2015_tables_and_figures_07252018_fnl_508_0.pdf, Table 1
total_ghg = sum([recycling_co2_savings[commodity_map[key]]*(waste_generation[key]) for key in commodity_map])
# Recycling price from $50/ton carbon price
print(1000* 50 *total_ghg/total_msw)
