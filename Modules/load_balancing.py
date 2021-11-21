# Load balancing strategies

import helper

# Our goal here is to compare the cost of strategies that will enable high renewable penetration in the US.

# The three strategies are curtailment, HVDC supergrid, and storage. More may be added later.

us_electricity = 4.18 * 10** 12 # In kWh, from https://www.eia.gov/energyexplained/electricity/electricity-in-the-us.php

# Calculations for storage
storage_needs = 5.4 * 10**9 # In kWh, source: shaner
storage_lifetime_high = 20. # Years, from Lazard. lazard_lcos
storage_lifetime_low = 10 # Years, from storage_life
storage_cost = 380. # storage_life, including balance of system costs.
storage_annual_cost_low = storage_needs / storage_lifetime_high * storage_cost
storage_annual_cost_high = storage_needs / storage_lifetime_low * storage_cost
storage_cost_overall = storage_needs * storage_cost # Total investment over however many years to get the storage

# Calculations for HVDC
# For HVDC network parameters, see the last full page before the conclusion in 'shaner', which in turn cites this paper: https://www.nature.com/articles/nclimate2921
hvdc_network_length = 34000 # km, or 21,000 miles.
hvdc_capacity = 12000 # Line capacity required, in MW. Note that the paper says only "up to 12GW" needed.
# From hvdc_cost via eia_hvdc
hvdc_cost_range = [700/1.609344,4400/1.609344] # Dollars per mi-km, with conversion from miles.
hvdc_cost_range2 = [890, 3961] # $/mi-MW, from ETSAP via the EIA paper. For the moment, not using this figure.
hvdc_amortization = 20 # Number of years over which costs are amortized
hvdc_cost_low = hvdc_network_length * hvdc_capacity * hvdc_cost_range[0]
hvdc_cost_high = hvdc_network_length * hvdc_capacity * hvdc_cost_range[1]
hvdc_annual_cost_low = hvdc_network_length * hvdc_capacity * hvdc_cost_range[0] / 20
hvdc_annual_cost_high = hvdc_network_length * hvdc_capacity * hvdc_cost_range[1] / 20
hvdc_cost_average = hvdc_network_length * hvdc_capacity * (hvdc_cost_range[0]+hvdc_cost_range[1])/2.0 # For use in other modules

# Curtailment strategy
curtailment_lcoe = 0.06 # Cents per kWh. Guesstimate pulled from the LCOE page
# Curtailment rate estimates from 'solar_overbuild'
curtailment_rate_low = 0.2
curtailment_rate_high = 0.4
curtailment_excess_low = curtailment_rate_low/(1-curtailment_rate_low) * curtailment_lcoe * us_electricity
curtailment_excess_high = curtailment_rate_high/(1-curtailment_rate_high) * curtailment_lcoe * us_electricity

load_balancing_annual_cost = {
    "Storage Low":storage_annual_cost_low,
    "Storage High":storage_annual_cost_high,
    "HVDC Low":hvdc_annual_cost_low,
    "HVDC High":hvdc_annual_cost_high,
    "Curtailment Low":curtailment_excess_low,
    "Curtailment High":curtailment_excess_high
}
load_balancing_cost_lcoe = {key: load_balancing_annual_cost[key]/us_electricity for key in load_balancing_annual_cost}

for key in load_balancing_annual_cost:
    load_balancing_annual_cost[key] = "{0:.1f}".format(load_balancing_annual_cost[key] / 10**9)
    load_balancing_cost_lcoe[key] = "{0:.3f}".format(100*load_balancing_cost_lcoe[key])
base_keys = ["Curtailment","HVDC","Storage"]
annual_range = [["<b>Strategy</b>","<b>Low Estimate (Billions of dollars annually)</b>","<b>High Estimate (billions of dollars annually)</b>"]]
lcoe_range = []
for i in range(len(base_keys)):
    annual_range.append([base_keys[i],load_balancing_annual_cost[base_keys[i]+" Low"],load_balancing_annual_cost[base_keys[i]+" High"]])
annual_range.append(["<b>Strategy</b>","<b>Low Estimate (cents per kWh)</b>","<b>High Estimate (cents per kWh)</b>"])
for i in range(len(base_keys)):
    annual_range.append([base_keys[i],load_balancing_cost_lcoe[base_keys[i]+" Low"],load_balancing_cost_lcoe[base_keys[i]+" High"]])

int_strat_im = {
    "filename":"integration_strategies.jpg",
    "status":"Done",
    "details":"Compare cost ranges for three grid integration strategies for 80% renewables in the US. Show both in terms of annual expense and on a per-kWh basis.",
    "table":annual_range,
    "references":["electricity_us","solar_overbuild","hvdc_cost","shaner","storage_life","lazard_lcos"],
    "source_file":"load_balancing.py"
}
#helper.save_image(int_strat_im)


