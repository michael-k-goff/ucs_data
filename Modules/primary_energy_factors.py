# Primary energy factors
# Store primary energy factors for various common fuels.
# This is meant to be a single source that contains PEFs when needed.

# See ASHRAE notes: https://www.energycodes.gov/901-prototype-building-models-high-rise-apartment
# To find these figures, download the ASHRAE901_ApartmentHighRise.zip file, unzip it, open any of the HTML files, and scroll to "Site to Source Energy Conversion Factors"
# Reference id is 'energycode'
primary_factors = {
    "Electricity":3.167,
    "Natural Gas (Buildings)":1.084,
    "Natural Gas":1.084, # Is there a different to other kinds of gas?
    "Propane":1.05,
    "Fuel Oil":1.05,
    "Gasoline":1.05,
    "Oil Products":1,
    "Diesel":1.05,
    "Coal":1.05,
    "Heat":1,
    "Biofuels and waste":1.05, # I would like to have a better figure here too, but this will do for now.
    "Oil":1, # Assuming this because I think, in IEA statistics, it refers to unprocessed petroleum
    "Geothermal":1, # Another guess here
    
    "District Cooling":1.056,
    "District Heating":3.613
}

# Some standard world emissions factors
# Units are grams CO2e/MJ = million tons / EJ = tons / TJ
emissions_factors = {
    "Gasoline":103.6, # epa_biofuel
    "Oil Products":103.6, # For now, taking all oil products based on gasoline
    "Biofuel":59.05, # From epa_biofuel. I took the average of eight values: high and low estimates for 'Ethanol - Barley/Corn/Sorghum', 'Ethanol - Sugarcane', 'Biodiesel - Palm Oil', and 'Biodiesel - Canola/Soybean Oil'. See synthetic_fuel.py for more.
    "Coal":88, # coal_intensity. I'm assuming that the Wikipedia article reports it correctly. https://en.wikipedia.org/wiki/Emission_intensity
    "Natural Gas":51, # hanova, though I lifted the figure from the same Wikipedia article above.
    "Oil":73, # From hanova via Wikipedia again.
    "Electricity":450/3.6 # From staffell. World average. Converting kWh to MJ.
}