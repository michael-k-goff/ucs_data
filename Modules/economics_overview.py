# Economics overview

import helper
import policy

# Figures that are not pulled from other modules

# Clean electricity cost to use in general. It is the capital cost, per kWh annual demand, for a mix of 1/3 nuclear, 1/3 solar, 1/3 wind.
electricity_cost_kwh =  (1./ 8760. / policy.nuclear_capacity * policy.nuclear_capital + 1./8760. / policy.solar_capacity * policy.solar_capital + 1./8760. / policy.wind_capacity * policy.wind_capital)/3.

num_cars = [193672370,56880878] # Light duty vehicles, short and long wheel bases. From reference bts_car_count
car_cost = num_cars[0]*30315+num_cars[1]*38500 # Based on the ev_cost reference. Short wheel base replaced by Hyundai Ioniq, long wheel base by Kia Niro.
us_vkt = 3.23*1.60934*10**12 # See afdc reference: 3.23 trillion VMT in the US in 2019.
ev_kwh = us_vkt * 1206. / 3600. / 3.19 # Based on the Fuel Source image on the Automobiles page.
ev_electricity_cost =  electricity_cost_kwh * ev_kwh

# For synfuels
other_transport_energy = (1599+28+246+3791+402+307+261)/1.055/3.6*10**9 # bts_by_mode: all aviation, trucks, all watercraft. In kWh
other_transport_electricity = electricity_cost_kwh*other_transport_energy /0.5 # Assume 50% electricity -> synfuel conversion
# Capital cost for electrofuels: 400 Euros or ~$450/kW fuel. See Table 5, FT Diesel entry. Reference electrofuel_cost.
other_capital_cost = 450*other_transport_energy/8760

# For industrial heat
industrial_heat = (2353+4796)/1.055/3.6*10**9 # See Sankey diagram, steam and fuel (but not electricity) input into heat. Reference 'mecs'.
industrial_heat_electricity = electricity_cost_kwh*industrial_heat * 0.8

# Residential heat. Resume later
# From RECS, from this sheet can can get all residential heat. https://www.eia.gov/consumption/residential/data/2015/c&e/pdf/ce4.1.pdf
# Also from RECS, 57.7 million homes with gas, 5.8 with fuel oil, 5.0 with propane, 3.5 with wood.
heat_pumps_needed = 10**6*(57.7+5.8+5.0+3.3)
heat_pump_cost = heat_pumps_needed * 2000 # $2000 per heat pump, based on reference 'heatpump'.
res_heat_electricity_needed = (3965+361+464)/1.055/3.6*10**9 # From 'recs', specially p.5 of https://www.eia.gov/consumption/residential/data/2015/c&e/pdf/ce4.1.pdf . Units initially in trillions of BTU. Convert to kWh
res_heat_electricity = electricity_cost_kwh*res_heat_electricity_needed / 3 * 0.9 # Assume coefficient of performance of 3.0 for heat pumps and onsite heating efficiency of 0.9 for the alternative heating options.

# Apartments
apt_cost = (64575+86100)/2. # See reference 'apt_cost'
apt_cost_overall = apt_cost * 330000000/4/2 # Scenario: apartments for 1/4 of all Americans (in addition to current apartment dwellers), assume 2 per unit.

energy_investment = [
    ["<b>Technology</b>","<b>Investment Needed, United States (billions of dollars)</b>","<b>Scenario Notes</b>"],
    ["Solar Power",policy.us_solar_nogrid/10**9,"Replace fossil fuels on power grid."],
    ["Nuclear Power",policy.us_nuclear/10**9,"Replace fossil fuels on power grid."],
    ["Wind Power",policy.us_wind/10**9,"Replace fossil fuels on power grid."],
    ["Electric Cars",str(car_cost/10**9)+" (cars) + "+str(ev_electricity_cost/10**9) + " (electricity)","Replace all internal combustion cars. Include electricity."],
    ["Low Carbon Electricity",str(industrial_heat_electricity/10**9)+ " (electricity only)","Electrify industrial heat. Include cost of industrial upgrades if possible."],
    ["Synfuels for Aviation, Shipping, and Trucking",str(other_transport_electricity/10**9)+" (electricity) + " + str(other_capital_cost/10**9) + " (capital cost of fuel synthesis)","Capital cost and clean power for electricity."],
    ["Midrise Apartments",apt_cost_overall / 10**9,"Allow an additional 82.5 million Americans (25% of the population) to live in apartments."],
    ["Electric Heating",str(res_heat_electricity/10**9)+" (electricity) + "+str(heat_pump_cost/10**9)+" (heat pumps)","Replace natural gas heating with heat pumps. Include cost of electricity."],
    ["HVDC Grid",str(policy.load_balancing.hvdc_cost_low/10**9) + " to " + str(policy.load_balancing.hvdc_cost_high/10**9),"Estimated cost to support 80% wind and solar."],
    ["Grid Storage",policy.load_balancing.storage_cost_overall/10**9,"Estimated cost to support 80% wind and solar."]
]

helper.save_image({
    "filename":"investment_overview.jpg",
    "status":"Done",
    "table":energy_investment,
    "details":"An overview of how much investment is needed for various aspects of a clean energy transition. I described the technology and a simple scenario for each one and a back-of-the-envelope cost estimate. I intend for this to be a centerpiece of the Economics section. While the individual options are explored in greater detail in the other sections, the Economics section is more about the economic context in which these transition might occur. Be aware that these options are mostly but not complete additive (e.g. we might build an HDVC grid, or massive grid storage, or a bit of both, but would not build both to the extent listed).<br><br>For specifics on how the numbers are determined, see the caption on the Economics Overview page.",
    "references":["wind_capital","bts_car_count","ev_cost","electrofuel_cost","mecs","apt_cost","heatpump","nrel_atb_solar","nuclear_build2","bts_by_mode"],
    "source_file":"economics_overview.py"
})