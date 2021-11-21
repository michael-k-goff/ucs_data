# Electrofuel summary

import helper

# Some stats.

# Natural gas price: taking the average industrial price from 2014-19 from https://www.eia.gov/dnav/ng/ng_pri_sum_dcu_nus_a.htm
# 1,027,000 BTU per thousand cubic feet of natural gas, as in here: http://www.crmu.net/Files/PDF%20files/Natural%20Gas%20pdfs/How%20to%20Measure%20Natural%20Gas.pdf
gas_price_range = [3.91, (5.62+3.93+3.51+4.08+4.21+3.91)/6., 5.62]
for i in range(len(gas_price_range)):
    gas_price_range[i] = gas_price_range[i] / 1027000. * 1055.06
# Average oil price from 2014-19, using the inflation-adjusted values. https://inflationdata.com/articles/inflation-adjusted-prices/historical-crude-oil-prices-table/
# Convert to GJ based on https://en.wikipedia.org/wiki/Barrel_of_oil_equivalent
oil_price_range = [39.02, (93.24+45.55+39.02+43.97+57.77+50.01)/6., 93.24]
for i in range(len(oil_price_range)):
    oil_price_range[i] = oil_price_range[i] / 6117.8632

# This paper gives hydrogen SMR efficiency of 70-85%. https://www.hindawi.com/journals/cpis/2013/690627/
smr_efficiency = [0.7, (0.7+0.85)/2, 0.85]
# Hydrogen electrolysis: 60-80% efficient. https://hydrogeneurope.eu/electrolysers
h2_electrolysis_efficiency = [0.6, 0.7, 0.8]
h2_breakeven = [
    gas_price_range[0] / smr_efficiency[2] * h2_electrolysis_efficiency[0] * 3.6,
    gas_price_range[1] / smr_efficiency[1] * h2_electrolysis_efficiency[1] * 3.6,
    gas_price_range[2] / smr_efficiency[0] * h2_electrolysis_efficiency[2] * 3.6
]

ammonia_efficiency = [18.6/28, 18.6/28, 18.6/28] # Assuming the new plant figure. See ammonia_energy.jpg
ammonia_electrolysis_efficiency = [18.6/31, 18.6/31, 18.6/31]
ammonia_ghg = 3.03226 / 0.0186 # Based on SMR. kg CO2e/kg => kg/GJ
ammonia_elec_ghg = 1.27745 / 0.0186
ammonia_breakeven = [
    gas_price_range[0] / ammonia_efficiency[2] * ammonia_electrolysis_efficiency[0] * 3.6,
    gas_price_range[1] / ammonia_efficiency[1] * ammonia_electrolysis_efficiency[1] * 3.6,
    gas_price_range[2] / ammonia_efficiency[0] * ammonia_electrolysis_efficiency[2] * 3.6
]

# Methanol. For GHG figures, see methanol_ghg.jpg
methanol_ghg = 90.99999999999999 # kg CO2e/GJ. The gas scenario
methanol_elec_ghg = 26.666666666666664
methanol_efficiency = [0.64, (.64+.72)/2, 0.72] # See methanol_efficiency.jpg
methanol_elec_efficiency = [0.5, 0.5, 0.5] # See methanol_efficiency.jpg
methanol_breakeven = [
    gas_price_range[0] / methanol_efficiency[2] * methanol_elec_efficiency[0] * 3.6,
    gas_price_range[1] / methanol_efficiency[1] * methanol_elec_efficiency[1] * 3.6,
    gas_price_range[2] / methanol_efficiency[0] * methanol_elec_efficiency[2] * 3.6
]

# Synfuels. Treating as gasoline
synfuel_efficiency = [0.95, 0.95, 0.95] # From crude oil. See synfuel_primary.jpg
synfuel_elec_efficiency = [0.5, 0.5, 0.5]
synfuel_breakeven = [
    oil_price_range[0] / synfuel_efficiency[2] * synfuel_elec_efficiency[0] * 3.6,
    oil_price_range[1] / synfuel_efficiency[1] * synfuel_elec_efficiency[1] * 3.6,
    oil_price_range[2] / synfuel_efficiency[0] * synfuel_elec_efficiency[2] * 3.6
]

# Methane
methane_efficiency = [1., 1., 1.] # Assuming trivial conversion from natural gas because it is natural gas
methane_elec_efficiency = [0.54, 0.54, 0.54] # https://phys.org/news/2018-03-power-to-gas-facility-high-efficiency.html
methane_breakeven = [
    gas_price_range[0] / methane_efficiency[2] * methane_elec_efficiency[0] * 3.6,
    gas_price_range[1] / methane_efficiency[1] * methane_elec_efficiency[1] * 3.6,
    gas_price_range[2] / methane_efficiency[0] * methane_elec_efficiency[2] * 3.6
]

def s(triple):
    return str(triple[0])+", "+str(triple[1])+", "+str(triple[2])

# Food. Based on the Soybean scenario on the Intensive Farming page
food_breakeven = 0.38 / 25.320512820512818

electrofuel_table = [
    ["<b>Product</b>","<b>Emissions, conventional option</b>","<b>Emissions, electric option (from solar)</b>","<b>Efficiency (conventional, low, median, high estimates)</b>","<b>Efficiency (electric, low, median, high estimates)</b>","<b>Electricity price for breakeven, USD/kWh (low, median, high)</b>"],
    ["Hydrogen","101.846153846 kg CO2e/GJ","17.0 kg CO2e/GJ",s(smr_efficiency), s(h2_electrolysis_efficiency), s(h2_breakeven)], # For SMR, see reference 'lcoh'.
    ["Ammonia",str(ammonia_ghg)+" kg CO2e/GJ", str(ammonia_elec_ghg)+" kg CO2e/GJ",s(ammonia_efficiency), s(ammonia_electrolysis_efficiency), s(ammonia_breakeven)],
    ["Methanol",str(methanol_ghg)+" kg CO2e/GJ", str(methanol_elec_ghg)+" kg CO2e/GJ",s(methanol_efficiency), s(methanol_elec_efficiency), s(methanol_breakeven)],
    ["Hydrocarbon Fuel","103.6 kg CO2e/GJ", "30 kg CO2e/GJ",s(synfuel_efficiency), s(synfuel_elec_efficiency), s(synfuel_breakeven)], # See synfuel_ghg.jpg for GHG figures.
    ["Methane","95 kg CO2e/GJ","53.333 kg CO2e/GJ",1.0, 0.54, s(methane_breakeven)] # See methane_emissions.jpg for emissions
#    ["Food","","","","",food_breakeven],
#    ["Plastic"]
]

helper.save_image({
    "filename":"electrofuel.jpg",
    "status":"Done",
    "table":electrofuel_table,
    "details":"For the five major classes of fuel described in the Energy Distribution section, I've estimated the greenhouse gas emissions from the most conventional method of production (based on natural gas in all cases except for hydrocarbon fuels, which are based on oil) and the electrolysis version. I've also shown the conversion efficiency of the two pathways (in the case of electricity, the electricty to fuel efficiency, disregarding the efficiency of electricity generation), and an estimate breakeven cost, which is how cheap electricity would have to be for electrolysis to be profitable. Three values are presented, based on high, median, and low estimates of the price of fossil fuel feedstock and conversion efficiency. The cost comparision is based only on the cost of energy feedstock; consideration of capital and maintenance cost of equipment would alter the numbers, though I'm guessing not too much.<br><br>Natural gas and crude ol prices are from the EIA and InflationData references respectively. I took the average of annual prices from 2014-2019 for the median prices, and the yearly low and high over those years for the low and high estimate. It is too early to say how ongoing economic and geopolitical concerns will affect the analysis, so I will not attempt to do so. For efficiency estimates, hydrogen SMR is from Kalamaras and Efstathiou and hydrogen electrolysis from the Hydrogen Europe reference. Efficiency of power-to-gas (methane from electricity) is from the phys.org reference. All GHG and all other efficiency figures are discussed on the respective pages for the given fuel.",
    "references":["eia_natgas","crude_inflation","kalamaras","h2euro","emethane"],
    "source_file":"electrofuel.py"
})