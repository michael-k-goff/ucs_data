# -*- coding: utf-8 -*-
# Greenhouse gases by source

# This is the first modeul after the August 2019 Energy Model revamp. As of its creation, it does not yet meet the standards desired for modules.
# - Should clearly show where each figure comes from
# - Should export figures or at least keep them internally as actually numbers, not embedded in strings
# - Should refer to sources by reference

import helper
reload(helper)

# From ipcc_synthesis
# Figures are percentages of total anthropogenic emissions
# Do not add to 100% due to rounding
overall_emissions = {
    "CO2_energy":65,
    "CO2 from Forestry and Land Use":11,
    "CH4":16,
    "N2O":6.2,
    "F":2
}

# From carbon_budget, download the first spreadsheet. On the second tab, take the relevant column (2017 value) and divide by 11260 (sum of carbon emissions from industry+FOLU)
overall_emissions["CO2 from Coal"] = 3978/9867. * overall_emissions["CO2_energy"]
overall_emissions["CO2 from Gas"] = 1969/9867. * overall_emissions["CO2_energy"]
overall_emissions["CO2 from Oil"] = 3450/9867. * overall_emissions["CO2_energy"]
overall_emissions["CO2 from Cement"] = 403/9867. * overall_emissions["CO2_energy"]
overall_emissions["CO2 from Flaring"] = 68/9867. * overall_emissions["CO2_energy"]

# From 'methane', applying percentages in the fact sheet to overall methane percentages
overall_emissions["CH4 from Oil and Gas"] = overall_emissions["CH4"] * 0.24
overall_emissions["CH4 from Wastewater"] = overall_emissions["CH4"] * 0.07
overall_emissions["CH4 from Other Ag Source"] = overall_emissions["CH4"] * 0.05
overall_emissions["CH4 from Biomass"] = overall_emissions["CH4"] * 0.03
overall_emissions["CH4 from Other"] = overall_emissions["CH4"] * 0.04
overall_emissions["CH4 from Rice Cultivation"] = overall_emissions["CH4"] * 0.07
overall_emissions["CH4 from Enteric Fermentation"] = overall_emissions["CH4"] * 0.27
overall_emissions["CH4 from Manure Management"] = overall_emissions["CH4"] * 0.03
overall_emissions["CH4 from Coal Mining"] = overall_emissions["CH4"] * 0.09
overall_emissions["CH4 from Municipal Solid Waste"] = overall_emissions["CH4"] * 0.11

# Nitrogen. From n2o1. In TG N2O-N/yr (whatever that unit is)
# Most of the figures come from table on p. 2
nitrogen_from_n2o1 = {
    "Anthropogenic":5.3, # Aggregate category
    "Agriculture":4.1, # Aggregate category
    "Biomass Burning":0.7,
    "Industry, energy, transport":0.9, # An aggregate category, see below
    "Wastewater":0.2,
    "Other":0.3 # Ocean + Solvent and Other + Aquaculture
}

# Subcategories from agriculture. See table on p. 5., FAO column.
nitrogen_from_n2o1_ag_subcategories = {
    "Fertilizer":1.4,
    "Manure":2.1, # Manure Direct + Manure Indirect + Manure Management
    "Other Agriculture":0.5 # Organic Soils + Crop Residues
}
sum_ag_subcat = sum([nitrogen_from_n2o1_ag_subcategories[key] for key in nitrogen_from_n2o1_ag_subcategories])

# Figures from n2o2. Based on visual inspection of the plot on p. 4. Figures are smaller categories as shares of larger categories from nitrogen_from_n2o1
# The numbers of shares of "Industry, energy, transport" from above, NOT absolute figures.
nitrogen_from_n2o2 = {
    "Energy":0.45,
    "Transportation":0.35,
    "Industrial Processes":0.2
}

# Aggregate the N2O figures
overall_nitrogen = {key: nitrogen_from_n2o1[key] for key in nitrogen_from_n2o1 if key not in ["Anthropogenic","Agriculture","Industry, energy, transport"]}
for key in nitrogen_from_n2o1_ag_subcategories:
    overall_nitrogen[key] = nitrogen_from_n2o1_ag_subcategories[key] * nitrogen_from_n2o1["Agriculture"] / sum_ag_subcat
for key in nitrogen_from_n2o2:
    overall_nitrogen[key] = nitrogen_from_n2o2[key] * nitrogen_from_n2o1["Industry, energy, transport"]
    
# N2O into the overall list of figures
for key in overall_nitrogen:
    overall_emissions["N2O from " + key] = overall_nitrogen[key]

# From the table in fgas, eyeballing the table, it looks like about 65% of the F-gas emissions are from cooling and refrigeration and the rest I assume are from industry.
overall_emissions["F-Gases from Cooling"] = 0.65 * overall_emissions["F"]
overall_emissions["F-Gases from Industry"] = 0.35 * overall_emissions["F"]

# Keys for non-aggregate categories for plotting
overall_keys = ['N2O from Industrial Processes',
 'CH4 from Other',
 'CO2 from Coal',
 'CH4 from Other Ag Source',
 'F-Gases from Industry',
 'CH4 from Wastewater',
 'N2O from Fertilizer',
 'CH4 from Municipal Solid Waste',
 'N2O from Transportation',
 'N2O from Other Agriculture',
 'CH4 from Coal Mining',
 'CO2 from Flaring',
 'CH4 from Enteric Fermentation',
 'N2O from Biomass Burning',
 'F-Gases from Cooling',
 'CH4 from Rice Cultivation',
 'CO2 from Forestry and Land Use',
 'CH4 from Biomass',
 'N2O from Energy',
 'N2O from Other',
 'CO2 from Gas',
 'CO2 from Cement',
 'CH4 from Manure Management',
 'CO2 from Oil',
 'CH4 from Oil and Gas',
 'N2O from Wastewater',
 'N2O from Manure']
overall_keys.sort()

im = {
    "filename":"Global Warming Potential.jpg",
    "status":"Done",
    "details":"The November 18, 2019 version is a big improvement over what we had before. Try to avoid break words over multiple lines whereever possible (e.g. Wastewater in a couple of the small boxes), and if it is absolutely necessary, use a hyphen and break between syllables. If feasible, find a way to make it more visually explicit that the CO2, N2O, F-gas, and CH4 boxes are breakouts from the main GHG plot.",
    "table":[[overall_keys[i],"{0:.1f}".format(overall_emissions[overall_keys[i]])+"%"] for i in range(len(overall_keys))],
    "references":["ipcc_synthesis","carbon_budget","methane","n2o1","n2o2","fgas"],
    "source_file":"ghg_by_source.py"
}
helper.save_image(im)

