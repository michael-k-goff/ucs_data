# Outline of Research solutions

# We need the following data for each technology:
# - Current Price
# - Learning Rate
#		(Possibly work backwards with a final price and learning rate)
# - Market potential (number of kWh/year)
# - Cost of doing R&D
# - Probability of success
# - External value of electricity depending on what is displaced

# Data that is needed:
# - US and world electricity generation, and at what prices. Probably use BP data for current data.
#	. This only goes to 2018 but is a bit more detailed. https://www.iea.org/data-and-statistics/charts/world-gross-electricity-production-by-source-2018
#	. International Energy Outlook. Electricity generation by source (crudely) can be derived from this figure. https://www.eia.gov/outlooks/ieo/pdf/ieo2020.pdf
#	. My guess is that we'll use LCOE for price. It's imperfect but at least readily available.
# - External costs of electricity generation and in what year. Might fill that in with generic numbers and the US/world electricity mix.
# - What portion of US and world electricity is on the coast
#	. Generation by state in the US. A crude approximation of coastal markets would be possible from this. https://www.eia.gov/electricity/state/
# - Estimates of probability of success of R&D programs, if any is to be used

# R&D time (rd_time). A subjective estimate of how long it will take to get things to market. Using the following values:
# 5 years for technologies that are already commercialized but not a full potential
# 10 years for technologies that appear to be near ready but are not commercialized
# 25 years for technologies that are not nearly ready
# 40 years for fusion and space solar

# For each technology, adding the midpoint of greeenhouse gas emissions (valued at $50/ton) and non-GHG externalities. Both future and existing.
# For future technologies, choose whatever mainstream technology is closest, but not adding the visual disamenity or meltdown risk.

import helper
import sys
sys.path.insert(1, '/Modules')
import data_lcoe

technologies = {
	"Advanced Reactor":{
        "base_price":0.06,
		"final_price":0.06+0.00285+0.0031, # 6 cents per kWh forecast,
        "ghg_price":0.00285,
        "other_price":0.0031,
		"share":1.,
		"rd_time":25,
		"rd_cost":11.5, # $11.5 billion of R&D money and 25 years.
	},
	"Small Modular Reactor":{
        "base_price":0.09,
		"final_price":0.09+0.00285+0.0031, # From the LCOE chart
        "ghg_price":0.00285,
        "other_price":0.0031,
		"share":1.,
		"rd_time":10,
		"rd_cost":11.5*10/25 # Haven't found figures for the cost, so assuming the same per-year as advanced reactors
	},
	"Wave Energy":{
        "base_price":0.06,
		"final_price":0.06+0.001+0.002, # From the consultant report. Check to see if other sources corroborate this number
        "ghg_price":0.001,
        "other_price":0.002,
		"share":0.2, # Coastal is 0.4, assuming half is suitable for wave.
		"rd_time":10,
		"rd_cost":8.3
	},
	"Concentrated Solar":{
        "base_price":0.05,
		"final_price":0.05+0.0018+0.0081, # I had 14 cents before, but changed to 5 cents from this source: https://www.energy.gov/eere/solar/concentrating-solar-thermal-power
        "ghg_price":0.0018,
        "other_price":0.0081,
		"share":0.6, # Hard to say how much of the world is suitable for CSP. This seems optimistic
		"rd_time":10, # Changed from 5 to 10 years from this source: https://www.energy.gov/eere/solar/concentrating-solar-thermal-power
		"rd_cost":8.3 # Same cost per year as wave energy
	},
	"High Altitude Wind":{
        "base_price":0.09,
		"final_price":0.09+0.001575+0.0009,
        "ghg_price":0.001575,
        "other_price":0.0009,
		"share":1., # Might be lower if access to the gulf stream is needed. There is also ultimate potential
		"rd_time":25,
		"rd_cost":8.3*25/10 # Assuming case cost per year as wave
	},
	"Enhanced Geothermal":{
        "base_price":0.06,
		"final_price":0.06+0.002125+0.005, # For electricity cost, see http://www2.itif.org/2019-budget-geothermal.pdf. Geothermal isn't on the plot for external costs so I'm guessing
        "ghg_price":0.002125,
        "other_price":0.005,
		"share":0.5, # A wild guess, based on Western US being good territory.
		"rd_time":10,
		"rd_cost":8.3 # Same cost as wave
	},
	"Hydrothermal Sea Vents":{
        "base_price":(7.7+11.1)/200,
		"final_price":(7.7+11.1)/200 +0.002125+0.005, # Based on the notes. Not a very good figure but that's what I have.
        "ghg_price":0.002125,
        "other_price":0.005,
		"share":0.2, # 0.4 for coast times 0.5 for share accessible by sea vents
		"rd_time":25,
		"rd_cost":8.3*25/10 # Same annual cost as wave energy
	},
	"Tidal Power":{
        "base_price":0.10556,
		"final_price":0.10556+0.001+0.002, # See notes for cost
        "ghg_price":0.001,
        "other_price":0.002,
		"share":0.04, # Based on 1200 TWh potential. See https://energypost.eu/unlocking-the-potential-of-ocean-energy-from-megawatts-to-gigawatts/
		"rd_time":10,
		"rd_cost":8.3 # Same annual cost as wave energy
	},
	"OTEC":{
        "base_price":0.13,
		"final_price":0.13+0.001+0.002,
        "ghg_price":0.001,
        "other_price":0.002,
		"share":0.2, # Guessing 50% of coast is suitable for OTEC
		"rd_time":25,
		"rd_cost":8.3*25/10 # Same annual cost as wave energy
	},
	"Fusion":{
        "base_price":0.13,
		"final_price":0.13+0.00285+0.0031,
        "ghg_price":0.00285,
        "other_price":0.0031,
		"share":1.,
		"rd_time":40,
		"rd_cost":65 # https://physicstoday.scitation.org/do/10.1063/PT.6.2.20180416a/full/#:~:text=The%20US%20Department%20of%20Energy,its%20figure%20of%20%2422%20billion.
	},
	"Space Solar":{
        "base_price":0.07,
		"final_price":0.07+0.0018+0.0081,
        "ghg_price":0.0018,
        "other_price":0.0081,
		"share":1.,
		"rd_time":40,
		"rd_cost":65 # Same as fusion
	},
	"Advanced Solar Cells":{
        "base_price":0.04,
		"final_price":0.04+0.00495+0.0081, # Based on Perovskite from the LCOE plot
        "ghg_price":0.00495,
        "other_price":0.0081,
		"share":1., # Price may vary by location
		"rd_time":10,
		"rd_cost":8.3 # Same annual cost as wave energy
	},
	"Concentrated PV":{
        "base_price":0.07,
		"final_price":0.07+0.00495+0.0081,
        "ghg_price":0.00495,
        "other_price":0.0081,
		"share":0.5, # Wild guess, based on the fact that CPV is a bit fussy about location
		"rd_time":5,
		"rd_cost":8.3 * 5 / 10 # Same annual cost as wave energy
	},
	"Building Integrated Solar":{
        "base_price":0.0372,
		"final_price":0.0372+0.00495+0.0081, # See notes for LSC. Consider a different value
        "ghg_price":0.00495,
        "other_price":0.0081,
		"share":1., # Price may vary by location
		"rd_time":25,
		"rd_cost":8.3*25/10 # Same annual cost as wave energy
	}
}

# Information about the market, both now and in the future being assessed
electricity_market = {
	# See https://www.iea.org/data-and-statistics/charts/world-gross-electricity-production-by-source-2018
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
	"electricity2020":27004.7, # In 2019 actually. In TWh, from BP
	"base_price":[
		"Geothermal",0.046,
		"Wind",0.077,
		"Hydro",0.082,
		"Natural Gas",0.065,
		"Nuclear",0.095,
		"Solar",0.126,
		"Biofuel",0.101,
		"Coal",0.082,
		"Oil",0.17
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
	"electricity2050":27004.7 * 42./26., # Adjusting it up based on the IEO data. Seems to be confusion in converting Quads to TWh. https://www.eia.gov/outlooks/ieo/pdf/ieo2020.pdf
	"coastal_share":0.4, # 40% of population within 100 km of coast. Will use this if nothing better. https://sedac.ciesin.columbia.edu/es/papers/Coastal_Zone_Pop_Method.pdf
	"discount_rate":0.07,
	"success_probability":0.049 # See https://www.knowledgeportalia.org/r-d-time-success
}

electricity_market["electricity_cost"] = data_lcoe.lcoe["electricity_cost"]
electricity_market["base_price"] = data_lcoe.lcoe["direct"]
electricity_market["ghg_price"] = data_lcoe.lcoe["ghg"] # Should be monetized at $50/ton.
electricity_market["other_price"] = data_lcoe.lcoe["externalities"] 

# By key
electricity_table = [["<b>Technology</b>","<b>Benefit</b>","<b>Cost<b>"]]
for key in technologies:
    cumulative_share = 0
    base_price_share = 0
    ghg_share = 0
    other_share = 0
    for share in range(0, len(electricity_market["electricity_cost"]), 2):
        if technologies[key]["base_price"] < electricity_market["base_price"][share+1]:
            # Following, add up the product of displaced electricity sources * financial benefit of doing so
            cumulative_share += electricity_market["shares2020"][share+1]*electricity_market["electricity2020"]*10**9*(electricity_market["electricity_cost"][share+1]-technologies[key]["final_price"])
            base_price_share += electricity_market["shares2020"][share+1]*electricity_market["electricity2020"]*10**9*(electricity_market["base_price"][share+1]-technologies[key]["base_price"])
            ghg_share += electricity_market["shares2020"][share+1]*electricity_market["electricity2020"]*10**9*(electricity_market["ghg_price"][share+1]-technologies[key]["ghg_price"])
            other_share += electricity_market["shares2020"][share+1]*electricity_market["electricity2020"]*10**9*(electricity_market["other_price"][share+1]-technologies[key]["other_price"])
            
	# To start total_value calculation, we assume a technology deploys over 50 years when ready, adding 2% of the potential per year
	# The following assumes deployment begins immediately. Accounting for R&D time comes later.
    deployment_time = 50
    total_value = (deployment_time+1) * [0] # Taking 50 years for a technology to reach full deployment
    base_value = (deployment_time+1) * [0]
    ghg_value = (deployment_time+1) * [0]
    other_value = (deployment_time+1) * [0]
    for i in range(deployment_time):
        total_value[i] = cumulative_share*(1-electricity_market["discount_rate"])**i*i*(1/deployment_time)
        base_value[i] = base_price_share*(1-electricity_market["discount_rate"])**i*i*(1/deployment_time)
        ghg_value[i] = ghg_share*(1-electricity_market["discount_rate"])**i*i*(1/deployment_time)
        other_value[i] = other_share*(1-electricity_market["discount_rate"])**i*i*(1/deployment_time)
    total_value[deployment_time] = cumulative_share*(1-electricity_market["discount_rate"])**deployment_time / electricity_market["discount_rate"]
    base_value[deployment_time] = base_price_share*(1-electricity_market["discount_rate"])**deployment_time / electricity_market["discount_rate"]
    ghg_value[deployment_time] = ghg_share*(1-electricity_market["discount_rate"])**deployment_time / electricity_market["discount_rate"]
    other_value[deployment_time] = other_share*(1-electricity_market["discount_rate"])**deployment_time / electricity_market["discount_rate"]
    # Discount total value by the time it takes to to R&D, share of electricity the technology will cover, and probability of success
    total_value = sum(total_value) * (1-electricity_market["discount_rate"])**(technologies[key]["rd_time"]) * electricity_market["success_probability"] * technologies[key]["share"]
    base_value = sum(base_value) * (1-electricity_market["discount_rate"])**(technologies[key]["rd_time"]) * electricity_market["success_probability"] * technologies[key]["share"]
    ghg_value = sum(ghg_value) * (1-electricity_market["discount_rate"])**(technologies[key]["rd_time"]) * electricity_market["success_probability"] * technologies[key]["share"]
    other_value = sum(other_value) * (1-electricity_market["discount_rate"])**(technologies[key]["rd_time"]) * electricity_market["success_probability"] * technologies[key]["share"]
    print(key + ": " + str(total_value))
    print(key + ": " + str(base_value))
    print(key + ": " + str(ghg_value))
    print(key + ": " + str(other_value))
    
    #print(key + (30-len(key))*[" "] + str(total_value / 10**9) + "   " + str(technologies[key].rd_cost))
    electricity_table += [[ key, str(total_value / 10**9), str(technologies[key]["rd_cost"]) ]]
    
helper.save_image({
    "filename":"electricity_rd.jpg",
    "status":"Done",
    "details":"Costs and benefits for electricity R&D. Benefits are based on a model where, after the R&D period, an electricity source gains 2% of its potential market share every year for 50 years. Benefits are based on financial savings of displacing more expensive electricity, as well as greenhouse gas benefits (valued at $50/ton) and non-GHG external benefits of electricity. See the individual production pages for information on potential cost, and the Environmental Impacts of Energy page for information about GHG and non-GHG impacts. For R&D time, we assume 5 years for technologies that are deployed but not at full potential, 10 years for those near but not at commercialization, 25 years for those not near commercialization, and 40 years for fusion and space-based solar. For R&D cost, we assume $460 million per year for nuclear technologies (based on the advanced reactor analysis), $830 million per year for renewables (based on the wave energy analysis), and $65 billion total for fusion and space-based solar. We assume a 4.9% of any given R&D program of achieving its desired effect, based on a similar study (Schuhmacher et al.) in the pharmaceutical industry. All figures are in billions of dollars.",
    "table":electricity_table,
    "references":["rd_success"],
    "source_file":"research.py"
})
