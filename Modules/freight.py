# Freight

import helper

ton_km = {
    "Truck":108*0.18,
    "Ship":108*0.7,
    "Ship - Inland":108*0.02,
    "Rail":108*0.09,
    "Airplane":108*0.0025
}

freight_overall_im = {
    "filename":"freight_stats.jpg",
    "status":"Done",
    "details":"Estimates of world freight tonnage, by mode. Figures are {} for maritime shipping, {} for road, {} for rail, {} for inland water, and {} for air. All in trillions of ton-kilometers.".format(ton_km["Ship"], ton_km["Truck"], ton_km["Rail"], ton_km["Ship - Inland"], ton_km["Airplane"]),
    "references":["itf2019","itf2019writeup"],
    "source_file":"freight.py"
}

helper.save_image(freight_overall_im)

# From 'freight_energy' unless otherwise noted. (Note: this is not a good source I am an trying to phase it out)
# See section 5.1.2
# Unit conversions when necessary

# Selected values in a separate object
energy_tonkm = {
    "Truck":45963./2022649*34.92*3.78541/1.60934, # Calculated from reference 'bts_truck'. As of 2017
    "Airplane":261.43/1960.*42.7*3.78541/1.60934, # Source: 'bushnell'. Based on 42.7 MJ/liter density for aviation fuel.
    "Ship":0.214/1.60934, # From 'transpo_data_book', 2014
    "Rail":0.212 # See reference 'bts_rail', 2018
}
ghg_tonkm = {
    "Truck":161.3, # Pounds CO2 per million BTU fuel for diesel. Convert later. Source: https://www.eia.gov/tools/faqs/faq.php?id=73&t=11
    "Rail":161.3, # Diesel, like truck
    "Ship":161.3, # Assuming diesel again
    "Airplane": 156.3 # https://www.eia.gov/environment/emissions/co2_vol_mass.php
}
freight_energy = [
    ["<b>Mode</b>","<b>Energy intensity: MJ/ton-km</b>","<b>Reference</b>"],
    ["Truck",energy_tonkm["Truck"],"BTS (Truck Profile)"],
#    ["Family Car",1.4/1.60934,4.8/1.60934], # Upper end for an SUV. Probably separate this for a last-mile plot.
    ["Air",energy_tonkm["Airplane"],"Bushnell and Hughes"],
    ["Waterborne",energy_tonkm["Ship"],"ORNL"],
    ["Gas Pipeline","0.11-0.18","van Essen et al."],
    ["Oil Pipeline",0.185,"Gellings"],
    ["Rail",energy_tonkm["Rail"],"BTS (Rail)"],
    ["Airship",energy_tonkm["Rail"]*15.2,"NASA"] # nasa_airship, based on 15.2X more than train
]

freight_ghg = [
    ["<b>Mode</b>","<b>Emissions: g CO<sub>2</sub>e/ton-km</b>"],
    ["Truck",energy_tonkm["Truck"]*ghg_tonkm["Truck"]/1.05505585*2.20462],
#    ["Family Car",0.1, 0.31], # Upper end for an SUV. Probably separate this for a last-mile plot.
    ["Air",energy_tonkm["Airplane"]*ghg_tonkm["Airplane"]/1.05505585*2.20462],
    ["Container Ship","8.4-13.5"], 
    ["Barge","28-35"], 
    ["Gas Pipeline","5"],
    ["Oil Pipeline","5"],
    ["Rail",energy_tonkm["Rail"]*ghg_tonkm["Rail"]/1.05505585*2.20462],
    ["Airship",(energy_tonkm["Rail"]*ghg_tonkm["Rail"]/1.05505585*2.20462)*15.2*ghg_tonkm["Airplane"]/ghg_tonkm["Rail"]] # nasa_airship, Assuming the same energy intensity as the long haul flight.
]

freight_energy_im = {
    "filename":"freight_energy.jpg",
    "status":"Done",
    "details":"Revised version of the energy intensity of freight plot. One of the numbers was way off, the link to the main source is dead, and it doesn't seem like it was a good source anyway, so I am redoing it.",
    "table":freight_energy,
    "references":["nasa_airship","bts_truck","bushnell","transpo_data_book","bts_rail","gellings","gas_pipeline"],
    "source_file":"freight.py"
}

freight_ghg_im = {
    "filename":"freight_ghg.jpg",
    "status":"Done",
    "details":"As with the energy intensity of freight, emissions intensity of freight needs to be redone. Responsible Care et al. for Barge, Container Ship, and pipelines. Energy for air, truck, and rail as in the energy intensity of freight plot, with carbon intensity of the fuels from the EIA references. NASA for the airship study.",
    "table":freight_ghg,
    "references":["nasa_airship","freight_emissions","co2coef"],
    "source_file":"freight.py"
}

helper.save_image(freight_energy_im)
helper.save_image(freight_ghg_im)

# From airship_review
# I started with these figures, which are now in Euros/1000 ton-km. But now I don't believe them and will not proceed with the plot.
freight_external = [
    ["<b>Mode</b>","<b>External Cost</b>"],
    ["Truck",34.],
    ["Rail",7.9],
    ["Ship",11.2],
    ["Airplane",456.8],
    ["Airship",12.5]
]

# Savings potential

############################## Energy savings potential in freight
# Percentage savings potential for each mode.
# As a general reference, freight_savings
modal_savings = {
    "Truck":0.34, # iea_trucks
    "Ship":0.33, # ship_savings
    "Airplane":0.2 # air_savings
}

# In exajoules
# For now, we assume the mode shift is 20%. Put in a range, maybe 10-30%, later. See freight notes.
overall_savings = {
    "Truck":ton_km["Truck"]*modal_savings["Truck"]*energy_tonkm["Truck"],
    "Airplane":ton_km["Airplane"]*modal_savings["Airplane"]*energy_tonkm["Airplane"],
    "Ship":ton_km["Ship"]*modal_savings["Ship"]*energy_tonkm["Ship"],
    "Mode Shift":ton_km["Truck"]*0.2*(energy_tonkm["Truck"]-energy_tonkm["Rail"])
}
savings_chart = [
    ["<b>Method</b>","World Savings Potential (EJ)"],
    ["Ship Efficiency",overall_savings["Ship"]],
    ["Truck Efficiency",overall_savings["Truck"]],
    ["Airplane Efficiency",overall_savings["Airplane"]],
    ["Mode Shift (Truck to Rail)",overall_savings["Mode Shift"]]
]
savings_im = {
    "filename":"freight_savings_potential.jpg",
    "status":"Done",
    "details":"Show savings (exajoules) worldwide from several freight strategies. Three of them are making certain modes more efficient, and the last one is shifting 20% of truck freight to rail. There are no good figures that I know of on how much mode shifting is actually feasible, but 20% seems to be about the median of several country-specific studies. It might also be worth considering whether there is savings potential on the demand side (e.g. localized manufacturing), though that isn't considered yet.",
    "table":savings_chart,
    "references":["freight_savings","iea_trucks","ship_savings","air_savings"],
    "source_file":"freight.py"
}
helper.save_image(savings_im)

######################################################################
# Fuel switching
shipping_fuel = [
    ["<b>Fuel Option</b>","<b>Comment</b>"],
    ["Heavy Fuel Oil","Most commonly used today. High sulfer oxide emissions."],
    ["Liquified Natural Gas","In use today."],
    ["Synthetic Methane","A most promising low-carbon option."],
    ["Alcohol (e.g. Methanol, Ethanol)","A most promising low-carbon option."],
    ["Ammonia","A most promising low-carbon option."],
    ["Hydrogen","Major R&D needed and logistical challenges."],
    ["Wind Power (sails)","Can augment but not replace on-board fuel."],
    ["Battery","Insufficient energy density for transoceanic voyages."],
    ["Nuclear","Requires a low-cost, meltdown-proof small modular reactor."]
]
helper.save_image({
    "filename":"shipping_fuel.jpg",
    "status":"Done",
    "details":"A qualitative review of the practicality of various fuel options for shipping. We're not going to discuss emissions, primary energy, etc. for these fuels here because they are discussed elsewhere. For this plot we are only interested in what can work specifically for shipping.",
    "table":shipping_fuel,
    "references":["abs_shipping","maersk","battery_ship","nuclear_ship"],
    "source_file":"freight.py"
})

trucking_fuel = [
    ["<b>Fuel Option</b>","<b>Comment</b>"],
    ["Diesel","Widely used today"],
    ["Electric - Battery","Suitable for urban trucks, insufficient density for long range."],
    ["Electric - Catenary (overhead wires)","Major infrastructure investments needed."],
    ["Hydrogen Fuel Cell","Technology and infrastructure needed."],
    ["Dimethyl Ether","Existing diesel trucks can be retrofitted."]
]
helper.save_image({
    "filename":"trucking_fuel.jpg",
    "status":"Done",
    "details":"Qualitative review of various fuels for trucking. Similar approach as to shipping_fuel.jpg.",
    "table":trucking_fuel,
    "references":["truck_fuel","itf_truck"],
    "source_file":"freight.py"
})

######################################################################
# Last mile options. For delivering packages.

from primary_energy_factors import primary_factors # Source is 'energycode'
primary_factors["Oil"]=1
primary_factors["Oil Products"]=1.05
primary_factors["Natural Gas"]=1.05
primary_factors["Biofuel"]=1.05
primary_factors["Heat"]=1
primary_factors["Geothermal"]=1

# Primary Energy, MJ per package. Figures from 'drone2'
last_mile_energy = [
    ["Delivery Truck (Diesel)",7.8*primary_factors["Oil Products"]],
    ["Delivery Truck (CNG)",8.3*primary_factors["Natural Gas"]],
    ["Delivery Truck (Electric)",3.44*0.95*primary_factors["Electricity"]], # The 0.95 factor is from the fact that 5% transmission losses are already factored in.
    ["Van (Gasoline)",3.3*primary_factors["Oil Products"]],
    ["Van (Electric)",1.02*0.95*primary_factors["Electricity"]],
    ["Car (Gasoline)",50.5*primary_factors["Oil Products"]],
    ["Car (Electric)",15.9*0.95*primary_factors["Electricity"]],
    ["Drone (up to 0.5 kg cargo)",0.29*0.95*primary_factors["Electricity"]],
    ["Drone (up to 8 kg cargo)",2.9*0.95*primary_factors["Electricity"]],
    ["E-Bike",0.0512*primary_factors["Electricity"]*2.9/0.34]
]
# From ebike_delivery, p. 18, 0.0512 kWh/km energy.
# km/package metric seems to vary widely, so I will use the same figure as for Large Drone in 'drone2', which is 2.9/0.34.

last_mile_energy_im = {
    "filename":"last_mile_energy.jpg",
    "status":"Done",
    "details":"Energy required to deliver packages, given in MJ per package. This is only the energy for the delivery vehicle itself. The distance traveled varies by mode because the drone and e-bike scenarios require more warehouses and thus less distance from the warehouse to customer. The car scenarios are based on someone driving to a store to pick up an item. These figures are regarded as averages; obviously the value for a specific package depends on many factors, such as the details of the vehicle, distance traveled, number of packages being carried at a time, etc.",
    "table":last_mile_energy,
    "references":["drone2","ebike_delivery"],
    "source_file":"freight.py"
}
helper.save_image(last_mile_energy_im)



# GHG, from drone2. Figures are ranges, in grans CO2e/package.
# Most are from Supplementary Figure 8, Car (gasoline and electric) are read from Figure 5 in the main text.
# Ranges reflect difference emission intensity of electricity.
last_mile_ghg = [
    ["Drone (up to 0.5 kg cargo)",421,847],
    ["Drone (up to 8 kg cargo)",830,1654],
    ["Delivery Truck (Diesel)",1015, 1015],
    ["Delivery Truck (CNG)",871, 871],
    ["Delivery Truck (Electric)",572, 1276],
    ["Van (Gasoline)",872,872],
    ["Van (Electric)",489,1026],
    ["Car (Gasoline)",4600,4600],
    ["Car (Electric)",2000,4600],
    ["E-Bike",830-200,1654-500] # Rough guesstimate. Based on the fact that the e-bike is about 1/6 the energy as the large drone, cutting out about 5/6 of the transportation GHG as on Supplementary Figure 8, assuming that e-bike is otherwise the same as large drone.
]

last_mile_ghg_im = {
    "filename":"last_mile_ghg.jpg",
    "status":"Done",
    "details":"Emissions from delivering packages, given in grams CO<sub>2</sub>-equivalent per package. Unlike last_mile_energy.jpg, these are life cycle emissions, which include manufacture of the vehicle and energy require by the warehouse. Therefore, while drone delivery saves most of the energy on the vehicle side relative to truck delivery, those savings are offset somewhat by requiring more warehouses. The ranges for electricity-based modes reflect differing emissions intensity for electricity. The low values are for California and the high values are for Missouri, which have the least and most emissions-intensive grids. For liquid fuel based options, electricity is assumed to have the US average emissions intensity. Most of the figures come from the Stolaroff et al. paper; for e-bikes, I assumed the same distance traveled per package and warehouse density as the large drone scenario and took the e-bike's energy intensity from Gonzalez et al. The other caveats described in last_mile_energy.jpg apply here too.",
    "table":last_mile_ghg,
    "references":["drone2","ebike_delivery"],
    "source_file":"freight.py"
}
helper.save_image(last_mile_ghg_im)

##################################################

# Shipping fuel share

shipping_fuel_table = [
    ["<b>Fuel</b>","<b>Share of new ships as of 2018</b>"],
    ["Heavy Fuel Oil","93.95%"],
    ["Battery","3.07%"],
    ["Liquified Natural Gas","2.73%"],
    ["Liquified Petroleum Gas","0.13%"],
    ["Methanol","0.08%"],
    ["Hydrogen","0.04%"]
]

helper.save_image({
    "filename":"shipping_fuel_share.jpg",
    "status":"Done",
    "details":"The main fuel source intended for ships under construction as of 2018. By comparison, about 99.7% of existing ships used heavy fuel oil as of 2018, according to the report. Batteries are used primarily in ferries and other ships intended for short distances.",
    "table":shipping_fuel_table,
    "references":["shipping_paper"],
    "source_file":"freight.py"
})

##################################################

# Cost of shipping fuel

shipping_fuel_cost_table = [
    ["<b>Fuel</b>","<b>Cost, 2020 dollars per GJ (low)</b>","<b>(High)</b>"],
    # Extra $10/GJ added for liquid ammonia and hydrogen to be reasonably consistent with the other four.
    # See reference 'delft' for the following six.
    ["Liquid Ammonia",17*1.05506+10,105*1.05506+10],
    ["Liquid Hydrogen (from H2 electrolyzed from low-carbon sources)",19*1.05506+10,72*1.05506+10],
    ["Very Low Sulphur Fuel Oil",19*1.05506,25*1.05506],
    ["Liquified Natural Gas",14*1.05506,18*1.05506],
    ["Biomethane",29*1.05506,63*1.05506],
    ["Synthetic Methane",35*1.05506,145*1.05506],
    # Reference 'methanol_shipping' for the following two.
    ["Fossil Methanol",16.7*1.19052366+0.091*50, 23.1*1.19052366+0.091*50], # Assuming 91 kg/GJ emissions (for natural gas) valued at $50/ton.
    ["Low-Carbon Methanol",20*1.19052366,33*1.19052366],
    ["Electricity from Offshore Wind", 33/3.6 * 1.19], # From Korberg et al., but figures pulled from here: https://www.fastwater.eu/data/08%20E-fuels%20The%20big%20p%C3%BCicture%20-%20Maria%20Grahn.pdf. The 3.6 coverts MWh to GJ, and the 1.19 Euros to USD.
    ["Electrodiesel",158/3.6 * 1.19],
    ["Dimethyl Ether from Electrolysis",126/3.6 * 1.19],
    ["Electrolyzed Methanol",119/3.6 * 1.19],
    ["Biodiesel",95/3.6 * 1.19]
]

helper.save_image({
    "filename":"shipping_fuel_cost.jpg",
    "status":"Done",
    "details":"I'm adding a bit to this plot. Electricity and everything lower from from Korberg et al., and the other figures are already there.",
    "table":shipping_fuel_cost_table,
    "references":["delft","methanol_shipping","synfuel_price"],
    "source_file":"freight.py"
})