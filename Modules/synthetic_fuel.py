# Synthetic fuels plots

import helper

# In the following data, oil_ghg indicates whether the figure should be included in the oil_ghg.jpg file.
# GHG units: grams CO2e/MJ
synfuel_data = {
    "Gasoline": {
        "oil_ghg":1,
        "synfuel_ghg":1,
        "GHG": 103.6 # Source: epa_biofuel. Unit conversion not shown
    },
    "Diesel": {
        "oil_ghg":0,
        "synfuel_ghg":1,
        "GHG": 102.3 # Source: epa_biofuel. Unit conversion not shown
    },
    "Coal to Liquids": {
        "oil_ghg":1,
        "synfuel_ghg":1,
        "GHG": 164 # Source: crs_oil, Figure 4
    },
    "Gas to Liquids": {
        "oil_ghg":1,
        "synfuel_ghg":1,
        "GHG": 104 # Source: crs_oil, Figure 4
    },
    "Ethanol - Barley/Corn/Sorghum": {
        "oil_ghg":1,
        "synfuel_ghg":1,
        "GHG": [43.1, 109.7] # From epa_biofuel, unit conversion not shown
    },
    "Ethanol - Sugarcane": {
        "oil_ghg":1,
        "synfuel_ghg":1,
        "GHG": [9.5, 57.9] # From epa_biofuel, unit conversion not shown
    },
    "Biodiesel - Palm Oil": {
        "oil_ghg":0,
        "GHG": [85.1, 91.5] # From epa_biofuel, unit conversion not shown
    },
    "Biodiesel - Canola/Soybean Oil": {
        "oil_ghg":0,
        "GHG": [24.9, 50.7] # From epa_biofuel, unit conversion not shown
    },
    "Switchgrass/Corn Stover": {
        "oil_ghg":0,
        "GHG": [-10.7, 30.6] # From epa_biofuel, unit conversion not shown
    },
    "Biodiesel - Yellow Grease": {
        "oil_ghg":0,
        "GHG": 14.6 # From epa_biofuel, unit conversion not shown
    },
    "Biodiesel - Algae": {
        "oil_ghg":1,
        "synfuel_ghg":1,
        "GHG": [24.9, 72.8] # From algae_lca, unit conversion not shown
    },
    "Oil Shale": {
        "oil_ghg":1,
        "GHG": [189,189] # From crs_oil
    },
    "Oil Sands": {
        "oil_ghg":1,
        "GHG": [106,120] # From crs_oil
    },
    "Forest Pyrolysis":{
        "synfuel_ghg":1,
        "GHG":32.3 # lca_pyrolysis. Last paragraph before the conclusion.
    },
    # In the following, solar's GHG intensity is 48 gCO2e/kWh, from techco2
    # The multiplication by 2 for GHG is based on 50% conversion efficiency from electricity to fuel, given by electrofuel_overview
    "Electrofuel from Solar":{
        "synfuel_ghg":1,
        "GHG":[48 / 3.6 * 2, 48 / 3.6 * 2.5]
    }
}
# General data processing
for key in synfuel_data:
    if "GHG" in synfuel_data[key] and type(synfuel_data[key]["GHG"]) in [float, int]:
        synfuel_data[key]["GHG"] = [synfuel_data[key]["GHG"], synfuel_data[key]["GHG"]]

# Prepare data for oil_ghg.jpg
oil_ghg_keys = []
oil_ghg_values = []
for key in synfuel_data:
    if "oil_ghg" in synfuel_data[key] and synfuel_data[key]["oil_ghg"]:
        oil_ghg_keys.append(key)
        # The 0.045 term converts to kg CO2e/gallon of resulting fuel. No reference now for the conversion factor.
        oil_ghg_values.append( "{0:.2f}".format(0.045*synfuel_data[key]["GHG"][0])+"-"+"{0:.2f}".format(0.045*synfuel_data[key]["GHG"][1])+" kg CO<sub>2</sub>e/gallon" )
im = {
    "filename":"oil_ghg.jpg",
    "status":"Done",
    "details":"Show the greenhouse gas emissions from a gallon of gasoline, depending on the type of oil that the gasoline came from. (The same, or similar, information is being presented in multiple places: here, for overall environmental impact of energy, the synthetic fuels page, and maybe elsewhere. There may be some further reworking of the presentation.)",
    "table":[[oil_ghg_keys[i],oil_ghg_values[i]] for i in range(len(oil_ghg_keys))],
    "references":["crs_oil","algae_lca","epa_biofuel"],
    "source_file":"synthetic_fuel.py"
}
helper.save_image(im)

# Prepare data for synfuel_ghg.jpg
# Units are in gCO2e/MJ.
synfuel_ghg_keys = []
synfuel_ghg_values = []
for key in synfuel_data:
    if "synfuel_ghg" in synfuel_data[key] and synfuel_data[key]["synfuel_ghg"]:
        synfuel_ghg_keys.append(key)
        synfuel_ghg_values.append( "{0:.2f}".format(synfuel_data[key]["GHG"][0])+"-"+"{0:.2f}".format(synfuel_data[key]["GHG"][1])+" g CO<sub>2</sub>e/MJ" )
im = {
    "filename":"synfuel_ghg.jpg",
    "status":"Done",
    "details":"Show the greenhouse gas emissions for a megajoule of fuel, depending on how it is made.",
    "table":[[synfuel_ghg_keys[i],synfuel_ghg_values[i]] for i in range(len(synfuel_ghg_keys))],
    "references":["crs_oil","algae_lca","epa_biofuel","lca_pyrolysis","techco2","electrofuel_overview"],
    "source_file":"synthetic_fuel.py"
}
helper.save_image(im)

###### Conversion efficiency of primary energy into motive power from various fuels.
from primary_energy_factors import primary_factors # Source is 'energycode'

# Well-to-wheels efficiency (or equivalent) for various fuels. On hold for the moment
w2w_efficiency = {
    "Electrofuel":0.13 / primary_factors["Electricity"], # electrofuel_overview
    "Hydrogen from Electrolysis":0.22 / primary_factors["Electricity"], # electrofuel_overview
    "Electric Vehicle":0.73 / primary_factors["Electricity"], # electrofuel_overview
    "Gasoline":0.3 / primary_factors["Gasoline"] # 30% internal combustion engine efficiency from 'carfuel'.
}

# Efficiency in producing the fuel from primary energy
fuel_production_efficiency = {
    "Electrofuel":0.5 / primary_factors["Electricity"], # electrofuel_overview
    "Gasoline":1. / primary_factors["Gasoline"], 
    "Coal to Liquids":0.73 / primary_factors["Gasoline"], # ctl_efficiency and based on the fact that the output of CTL still needs to be refined.
    "Gas to Liquids":0.75 # gtl_efficiency
}

primary_energy_im = {
    "filename":"synfuel_primary.jpg",
    "status":"Done",
    "details":"Show the efficiency of production of various fuels from primary energy. The figures are ratios of energy in the fuel to primary energy required to make the fuel. Bio-based production is left out due to some gnarly accounting issues.",
    "table":[[key,"{0:.3f}".format(fuel_production_efficiency[key])] for key in fuel_production_efficiency],
    "references":["electrofuel_overview","ctl_efficiency","gtl_efficiency","energycode"],
    "source_file":"synthetic_fuel.py"
}
helper.save_image(primary_energy_im)

############################# Efficiency of electricity to vehicle propulsion

electricity_fuel_im = {
    "filename":"electricity_fuel_eff.jpg",
    "status":"Done",
    "details":"Show conversion efficiencies of electricity into useful work in a vehicle by three pathways. Direct use of electricity in an EV is 73%, hydrogen from electrolysis is 22%, and electrofuels are 13%.",
    "references":["electrofuel_overview"],
    "source_file":"synthetic_fuel.py"
}
helper.save_image(electricity_fuel_im)

############################### Land use comparison

# For solar, we use 3.4 acres/GWh/year, based on nrel_solar_land
# 3.4 acres/GWh/year =
# 3.4/3.6 acres/TJ/year =
# 3.4/3.6/50 acres/TJ (assuming 50 years) =
# 3400/3.6/50/2.47105 ha/PJ
solar_land_use = 1/(3400/3.6/50/2.47105)

# Calculations for Coal to Liquids. Based only on mining land use (I'm not sure what happens to waste in CTL). See top of p.3
# 111093 acres disturbed to produce 1,352,398,000 MWh. Unit conversions done.
# Dividing by 0.34 assumes an efficiency of 34%, and backing it to primary energy. See ge_coal, average efficiency for world coal plants.

# For gas, 1,333,482,000 MWh produced and we are counting 194,377.4 + 57,982.186 acres disturbed (mining + sand)
# For gas efficiency, I can't find where the 40.7% figure came from. I'm guessing it is wec_ee, which is a dead link now.

# When appropriate, multiply by conversion factors above from primary energy to liquid fuels.
land_use_by_fuel = {
    "Corn Ethanol":0.0038, # In PJ/ha Assumes 50 years of cultivation. From 'yeh'. See Table S10.,
    "Alberta Oil":0.33*fuel_production_efficiency["Gasoline"], # From yeh, Table S2.
    "California Oil":0.79*fuel_production_efficiency["Gasoline"], # From yeh, Table S1.
    "Electrofuel from Solar":solar_land_use/2, # Divide by 2 for 50% efficiency, as in electrofuel_overview
    "Algal Biodiesel":0.17, # See todo notes for algae. I haven't recently verified the figure from the sources, which is 'biodiesel_review'. Mean of endpoints of range of figures (PJ/ha).
    "Coal to Liquids":1/9.234169764867048/0.34 * fuel_production_efficiency["Coal to Liquids"], # From strata_landuse, see notes above
    "Gas to Liquids": 1/21.273959499348326/0.407 * fuel_production_efficiency["Gas to Liquids"] # Also from strata_land_use
}

# Convert land use to hectares per PJ.
for key in land_use_by_fuel:
    land_use_by_fuel[key] = 1/land_use_by_fuel[key]
    
landuse_im = {
    "filename":"synfuel_landuse.jpg",
    "status":"Done",
    "details":"Land use require for various methods of producing liquid fuels. Try to plot it so the Corn Ethanol bar doesn't obscure the differences between the other options.",
    "table":[[key,"{0:.1f}".format(land_use_by_fuel[key])+" hectares per PJ"] for key in land_use_by_fuel],
    "references":["strata_landuse","yeh","electrofuel_overview","nrel_solar_land","ge_coal","wec_ee","biodiesel_review","ctl_efficiency","gtl_efficiency","energycode"],
    "source_file":"synthetic_fuel.py"
}
helper.save_image(landuse_im)

####################### Synfuel prices
# Corn Ethanol, Sugarcane Ethanol, and Gasoline are lifted from biofuels.py, the biofuel_costs object.
# The first element in the array is the cost, the second is the multiplicative factor to get to USD/GJ.
prices = {
    "Corn Ethanol":[0.46,1000/19.8], # moyo
    "Sugarcane Ethanol":[0.18,1000/19.8], # moyo
    "Gasoline":[1.95,1000/33.4/3.78541], # wholesale_gasoline
    # The following price is given in $/barrel. Averaging the four non-CCS figures on p. 809, Table 3
    # The 1.11 is a CPI adjustment
    "Coal to Liquids":[83.9*1.11, 1000/33.4/3.78541/42], # ctl_cost
    # See p. 18. Averaging the two costs
    # The 1.093 is a CPI adjustment
    "Gas to Liquids":[91.995*1.093, 1000/33.4/3.78541/42], # gtl_cost
    # The 240 is the median of the 2015 cost range, and the 1.25 is the approximate Euro-USD coversion at the time.
    "Electrofuel":[240*1.25, 1/3.6]
}
adjusted_prices = {}
adjusted_prices_gal = {}
for key in prices:
    adjusted_prices[key] = prices[key][0]*prices[key][1]
    adjusted_prices_gal[key] = prices[key][0]*prices[key][1] / 7.909346612514639
    
synfuel_price_im = {
    "filename":"synfuel_price.jpg",
    "status":"Done",
    "details":"Price of several liquid fuel options. There is substantial duplication here with the biofuels price plot, so some revision on how this is presented might be needed.",
    "table":[[key,"{0:.2f}".format(adjusted_prices[key])+" $/GJ", "{0:.2f}".format(adjusted_prices_gal[key])+" USD/gallon of gasoline-equivalent"] for key in adjusted_prices],
    "references":["electrofuel_cost","moyo","wholesale_gasoline","ctl_cost","gtl_cost"],
    "source_file":"synfuel_price.py"
}
helper.save_image(synfuel_price_im)

####################################
# Methane from various sources
# 5600 Euros/ton for CNG methane. See p. 6, CNG, 2015. Only counting things up to the methanization phase. https://www.transportenvironment.org/sites/te/files/publications/2018_06_Cerulogy_What-role-electromethane-and-electroammonia_June2018.pdf
# Biomethane: about 50 cents/m^3 for production from waste and 80 cents for maize silage. https://www.irena.org/publications/2013/Jul/Road-Transport-The-Cost-of-Renewable-Solutions
# Biomethane: $10.80/GJ. See table on p. 8. https://www.nrel.gov/docs/fy11osti/49629.pdf (2010 figures).

# Methane price per GJ
methane_price = [
    ["Biomethane",12.5457], # CPI adjusting biomethane_cost from January 2010 to January 2019
    # 5600 is Euros per ton, from electromethane
    # 52.5 is median in range of GJ/ton, from https://www.world-nuclear.org/information-library/facts-and-figures/heat-values-of-various-fuels.aspx
    # 1.18 is a guestimate of exchange rate and CPI
    ["Electromethane", 5600 * 1.18 / 52.5], # https://www.world-nuclear.org/information-library/facts-and-figures/heat-values-of-various-fuels.aspx
    # 2.62 is price as reported from natgas_price. I assume it is USD/1000 cubic feet.
    ["Natural Gas",2.62 / 1.036 / 1.055] # Latter two terms convert from thousand cubic feet to MMBTU to GJ.
]
for i in range(len(methane_price)):
    methane_price[i][1] = "$"+"{0:.2f}".format(methane_price[i][1])+" / GJ"

methane_price_im = {
    "filename":"methane_price.jpg",
    "status":"Done",
    "details":"Price of methane from three sources, USD per GJ. Natural gas prices are for the US and were checked on September 13, 2019.",
    "table":methane_price,
    "references":["electromethane","biomethane_cost","natgas_price"],
    "source_file":"synthetic_fuel.py"
}
helper.save_image(methane_price_im)

# grams CO2e/MJ.
methane_emissions = [
    ["Natural Gas",95.], # electromethane
    # From electromethane, the fact that 2 units of electricity produce 1 unit of fuel, and very little emissions other than from electricity
    ["Electromethane from Solar",48*2/1.8], # Emissions from solar are 48 gCO2e/kWh, from techco2.
    ["Biomethane",95./2] # From ucs_biomethane, the fact that biomethane emissions are generally about half emissions from natural gas methane.
]
for i in range(len(methane_emissions)):
    methane_emissions[i][1] = "{0:.2f}".format(methane_emissions[i][1])+" kg CO<sub>2</sub>e / GJ"

methane_emissions_im = {
    "filename":"methane_emissions.jpg",
    "status":"Done",
    "details":"Emissions of methane from three sources, kg CO2e/GJ. Electromethane from solar power counts upstream emissions from the solar panels.",
    "table":methane_emissions,
    "references":["electromethane","ucs_biomethane"],
    "source_file":"synthetic_fuel.py"
}
helper.save_image(methane_emissions_im)

################################# Biomethane figures

# Production potential. Based on https://www.iea.org/data-and-statistics/charts/production-potential-for-biogas-or-biomethane-by-feedstock-source-2018
# In millions of tons of oil equivalent, converted to PJ. Regions are, in order, Asia Pacific, North America, Central & South America, Europe, Africa, Rest of World
# Conversion factor: 827004./19751.
biomethane_potential = [
    ["<b>Source</b>","<b>World biomethane production potential, PJ</b>"],
    ["Crop residues",(86+45+68+26+27+17)*827004./19751.],
    ["Animal manure",(57+40+30+32+11+9)*827004./19751.],
    ["Municipal solid waste",(35+30+15+19+8+5)*827004./19751.],
    ["Municipal wate water",(6+2+1+2+1+1)*827004./19751.],
    ["Woody biomass",(27+42+20+35+13+26)*827004./19751.],
    ["Current natural gas production",3309.4*827004./19751.]
]

helper.save_image({
    "filename":"biomethane_potential.jpg",
    "status":"Done",
    "details":"Biomethane production potential. Figures are from the IEA sources, except for the current natural gas production figure, which is from BP. Be sure to have a separate color to portray current natural gas production, and consider how best to scale things so we can emphasize two points simultaneously: first clearly show biomethane production potential, but also have an adequate comparison to current natural gas.",
    "table":biomethane_potential,
    "references":["bp2019","iea_biomethane"],
    "source_file":"synthetic_fuel.py"
})

#################################### Cost-benefit of electrofuels and carbon abatement costs

ef_table = [
    ["<b>Option</b>","<b>Cost</b>","<b>Baseline</b>","<b>Cost</b>","<b>Carbon abatement cost</b>"],
    ["Electrofuels from solar",252957862,"Gasoline",46809195,1000*(83.33-15.42)/(102.3-30)]
]

# Based on reference 'synfuel_size', 50,000 BPD assumed for typical plant size.

helper.save_image({
    "filename":"synfuel_cost.jpg",
    "status":"Done",
    "details":"Costs and carbon abatement costs of electrofuels. That's the only thing here for now. $50/ton carbon cost assumed under the Cost columns. A typical plant size of 50,000 barrels per day is assumed, as per the reference.",
    "table":ef_table,
    "references":["synfuel_size"],
    "source_file":"synthetic_fuel.py"
})

##################################### Cost-benefit of synthetic methane options

methane_price = { # See website. USD/GJ
    "biomethane":12.55,
    "electromethane":125.87,
    "natural_gas":2.4
}

methane_ghg = { # KG/GJ. See website
    "biomethane":47.5,
    "electromethane":53.3, # From Solar
    "natural_gas":95.0
}

def methane_abatement(key):
    return (methane_price[key]-methane_price["natural_gas"])/(methane_ghg["natural_gas"]-methane_ghg[key])*1000

scc = 50

# 152 million cubic feet of natural gas per day: https://www.gem.wiki/Great_Plains_Synfuels_Plant
# Convert cubic foot of natural gas to MJ: 1.06. https://www.traditionaloven.com/tutorials/energy/convert-cubic-foot-natural-gas-to-mega-joule-mj.html#:~:text=Equals%3A%201.06%20megajoules%20(MJ),in%20the%20energy%20units%20scale.
plant_size = 54*10**9 * 0.00106

cost_table = [
    ["<b>Method</b>","<b>Cost</b>","<b>Baseline</b>","<b>Cost</b>","<b>Carbon abatement cost</b>"],
    ["Biomethane",(methane_price["biomethane"]+scc/1000*methane_ghg["biomethane"])*plant_size,"Natural Gas",(methane_price["natural_gas"]+scc/1000*methane_ghg["natural_gas"])*plant_size,methane_abatement("biomethane")],
    ["Electrofuels",(methane_price["electromethane"]+scc/1000*methane_ghg["electromethane"])*plant_size,"Natural Gas",(methane_price["natural_gas"]+scc/1000*methane_ghg["natural_gas"])*plant_size,methane_abatement("electromethane")]
]

helper.save_image({
    "filename":"methane_cost.jpg",
    "status":"Done",
    "details":"Costs and carbon abatement costs of methane production. $50/ton carbon cost assumed under the Cost columns. Figures are based on a plant of size 54 billion cubic feet of natural gas, as per the reference.",
    "table":cost_table,
    "references":["doe_methane"],
    "source_file":"synthetic_fuel.py"
})

##################################### GHG for LNG

# Based on LPDF medium-speed, 4-stroke
lng_ghg_table = [
    ["<b>Fuel</b>","<b>Life cycle greenhouse gas emissions, g CO<sub>2</sub>e/kWh</b>"],
    ["Liquified Natural Gas",786],
    ["Marine Gas Oil",727],
    ["Very Low Sulphur Fuel Oil",740],
    ["Heavy Fuel Oil",769],
    ["LNG, high methane assumptions",846]
]

helper.save_image({
    "filename":"lng_emissions.jpg",
    "status":"Done",
    "details":"Emissions of liquified natural gas compared to common diesel-based shipping fuels. This study gives emissions of LNG has higher, while most studies are slightly lower, but I think this one is better because it better accounts for leakage than the others. Emissions are on a per-kWh basis. I would rather have a per-ton-mile basis, but efficiency of diesel and LNG are close enough that this will be OK.",
    "table":lng_ghg_table,
    "references":["lng_icct"],
    "source_file":"synthetic_fuel.py"
})