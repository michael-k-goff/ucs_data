# This is a data file. It is not meant to generate any images of its own, but to be used by others objects.
# It contains LCOE values for various mainstream or projected electricity source. It is meant to put all LCOE data in one place.

# Social cost of carbon, in dollars per ton.
scc = 50

# The weird formatting is to insure the results appear in a desired order
# Figures are from Reference eia_lcoe, Accessed December 8, 2020.
lcoe = {
    "direct":[ # Financial costs
        # See Table 1B, https://www.eia.gov/outlooks/aeo/pdf/electricity_generation.pdf
		"Geothermal",0.03747,
		"Wind",0.03995,
		"Hydro",0.05279,
		"Natural Gas",0.03807,
		"Nuclear",0.08165,
		"Solar",0.03574,
		"Biofuel",0.09483,
		"Coal",0.07644,
		"Oil",0.017 # See LCOE chart on the website
    ],
    "ghg":[ # In grams/kWh. See https://ourworldindata.org/cheap-renewables-growth (which pulls from IPCC I think).
		"Geothermal",4, # Assumed to be the same as wind
		"Wind",4,
		"Hydro",34,
		"Natural Gas",490,
		"Nuclear",3,
		"Solar",5,
		"Biofuel",(78+230)/2,
		"Coal",820,
		"Oil",720
    ],
    "externalities":[ # Other externalities besides greenhouse gases. See individual pages on website.
		"Geothermal",0.005,
		"Wind",0.0077, # Includes visual disamenity
		"Hydro",0.0069,
		"Natural Gas",0.0055,
		"Nuclear",0.0085, # Includes meltdown
		"Solar",0.0081,
		"Biofuel",0.0273,
		"Coal",0.0436,
		"Oil",0.0436
    ]
}

lcoe["electricity_cost"] = [0]*len(lcoe["ghg"])
for i in range(len(lcoe["direct"])):
    if ((i%2) == 0):
        lcoe["ghg"][i+1] = lcoe["ghg"][i+1] * scc / 10**6
        lcoe["electricity_cost"][i] = lcoe["direct"][i]
        lcoe["electricity_cost"][i+1] = lcoe["direct"][i+1] + lcoe["externalities"][i+1] + lcoe["ghg"][i+1]

# Some others included for good measure
offshore_wind_lcoe = 0.12225 