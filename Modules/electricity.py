# A summary of the value of continuing deployment of existing electricity sources.
# Consider merging into research.py if appropriate.

# Sources to consider:

# Solar PV (existing, conventional)
# Onshore wind
# Offshore wind
# Current nuclear
# Natural gas maybe

# Similar to the other model, but without the R&D expense and time. I think?

# For each source, we need the following:
# - LCOE
# - Learning rate
# - Current deployment

# General information needed
# - Cost and externalities of natural gas, which will probably be the baseline power source
# - How much saved by the reduced LCOE of the source

import helper
import sys
sys.path.insert(1, '/Modules')
import data_lcoe

electricity = {
    "solar_pv":{
        "cost":data_lcoe.lcoe["electricity_cost"][11], # See research.py for costs
        "learning":0.32, # Median of endpoints
        "market":0.021*27004.7,
        "cap_factor":0.3,
        "direct":data_lcoe.lcoe["direct"][11],
        "name":"Solar PV"
    },
    "onshore_wind":{
        "cost":data_lcoe.lcoe["electricity_cost"][3],
        "learning":0.06, # Median of endpoints
        "market":0.048*27004.7,
        "cap_factor":0.3,
        "direct":data_lcoe.lcoe["direct"][3],
        "name":"Onshore Wind"
    },
    "offshore_wind":{
        "cost":data_lcoe.offshore_wind_lcoe+0.001575+0.0009, # Offshore wind looks like 12 c/kWh from the site. Assuming no visual disamenity externality
        "learning":0.06, # Same as onshore wind
        # About 19 GW of capacity according to the IEA: https://www.iea.org/reports/offshore-wind-outlook-2019
        # Assuming a capacity factor of 50%.
        "market":19*8760*0.5*0.001,
        "cap_factor":0.5,
        "direct":data_lcoe.offshore_wind_lcoe,
        "name":"Offshore Wind"
    },
    "gen_iii":{
        "cost":data_lcoe.lcoe["electricity_cost"][9],
        "learning":0, # Median of endpoints is negative. Assuming zero here.
        "market":0.101*27004.7,
        "cap_factor":0.9,
        "direct":data_lcoe.lcoe["direct"][9],
        "name":"Generation III Nuclear"
    }
}

market = {
	"shares2020":[
		"Geothermal",0.005,
		"Wind",0.048,
		"Hydro",0.162,
		"Natural Gas",0.23,
		"Nuclear",0.101,
		"Solar",0.021,
		"Biofuel",0.024,
		"Coal",0.38,
		"Oil",0.029
    ],
	"electricity_cost":[
		"Geothermal",0.046+0.002125+0.005, # Don't see Geothermal on the external cost plot, so guessing here
		"Wind",0.077+0.001575+0.0077,
		"Hydro",0.082+0.00125+0.0069, # Guessing 50 g/kWh CO2e for Hydro
		"Natural Gas",0.065+0.0265+0.0055,
		"Nuclear",0.095+0.00285+0.0085,
		"Solar",0.126+0.00495+0.0081,
		"Biofuel",0.101+0.0135+0.0273,
		"Coal",0.082+0.057475+0.0436,
		"Oil",0.17+0.042+0.0436 # Guessing the same external cost as coal
	],
    "electricity2020":27004.7, # In 2019 actually. In TWh, from BP
    "ng_price":0.065+0.0265+0.0055 # See above
}

electricity_table = [["<b>Source</b>","<b>Cost of plant</b>","<b>Cost of displaced gas</b>","<b>Value of future cost reductions</b>"]]
for key in electricity:
    # Determine how much will be deployed. k and n are in TWh
    k = electricity[key]["cap_factor"] * 8760*10**-3 # Billions of kWh the plant will produce per year (assuming 1 GW for now)
    n = electricity[key]["market"] # Total deployment
    lr = electricity[key]["learning"]
    price_reduction = electricity[key]["direct"] * (lr)*k/n
    electricity_table += [[electricity[key]["name"],
        (electricity[key]["cost"])*k*10**9 * (1/0.07) / 10**9,
        (data_lcoe.lcoe["electricity_cost"][7])*k*10**9 * (1/0.07) / 10**9,
        price_reduction * n * 10**9 * (1/0.07) / 10**9
    ]]
    
helper.save_image({
    "filename":"plant_value.jpg",
    "status":"Done",
    "table":electricity_table,
    "details":"Sorry to make you redo this one so soon after the previous version, but the numbers before were not correct. Also, proper names for the energy sources are included. As before, figures in billions of USD. This assesses the value of building certain plants at 1 GW scale, on the assumption that natural gas would be built otherwise. Capacity factors are different between the sources, so the amount of displaced gas differs. Make it clear in the title that the baseline scenario for these plants is natural gas.",
    "references":[],
    "source_file":"electricity.py"
})

################################## Estimating the proper subsidy

subsidy_table = [["<b>Source</b>","<b>Proper subsidy (USD/kWh) for learning effect</b>"]]
for key in electricity:
    # Determine how much will be deployed. k and n are in TWh
    k = electricity[key]["cap_factor"] * 8760*10**-3 # Billions of kWh the plant will produce per year (assuming 1 GW for now)
    n = electricity[key]["market"] # Total deployment
    lr = electricity[key]["learning"]
    price_reduction = electricity[key]["direct"] * (lr)*k/n
    subsidy_table += [[electricity[key]["name"],
        price_reduction * n * 10**3 * 1/(0.3*8760)
    ]]
    
helper.save_image({
    "filename":"clean_energy_subsidy.jpg",
    "status":"Done",
    "table":subsidy_table,
    "details":"An estimate of the proper subsidy for established clean energy technologies. Only the proper subsidy for the learning effect is estimate; subsidy for other effects, such as air pollution or climate change reduction, is not estimated. No source here because I am pulling figures from elsewhere. Nuclear energy has zero learning value because there is no established positive learning rate, but I am not assuming a negative learning rate because that's silly.",
    "references":[],
    "source_file":"electricity.py"
})