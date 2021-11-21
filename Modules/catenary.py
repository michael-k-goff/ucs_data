# Solution: trucks and catenary wires

# Concept: if WSDOT were to build catenary wires between Seattle and the Columbia River, what would be the costs and benefits?

# This corridor was chosen because
# 1) Seattle is a major port, so I think there should be a lot of truck traffic coming in and out.
# 2) Washington has fairly cheap and low-carbon electricity thanks mainly to hydropower.
# 3) The state governor, Jay Inslee, has addressing climate change a high priority.

# Costs:
# - Building infrastructure
#       # Cost per lane-km
#       # How many lane-km's on this corridor
# - Additional cost of the trucks

# Benefits
# - Financial savings on electricity (assuming there is a savings)
# - Greenhouse gas reduction
# - Other pollution reduction

# General parameters
discount_rate = 0.05 # Annual amount of devaluation of money. I think somewhere from 5-7% is typical.
infrastructure_life = 50 # Number of years that the infrastructure will last
carbon_price = 50 # Dollars per ton. Set to 0 to avoid climate change analysis.

# Length of the corridor in question
corridor_length = 266.01 # In km. Based on the 266.01 km mark being where express lanes in Seattle start. https://en.wikipedia.org/wiki/Interstate_5_in_Washington
total_interstate = (445.18+213.35+478.81+24.45+17.01+48.76+2.41) # https://en.wikipedia.org/wiki/List_of_Interstate_Highways_in_Washington

# Total VKT (vehicle-kilometers traveled) by trucks on the corridor
total_vkt = 17435 * 1.60934 # From https://wsdot.wa.gov/mapsdata/travel/hpms/annualmileage.htm, converting miles to km. In millions
truck_proportion = 0.032+0.0551 # From the above link, see "Travel Activity by Vehicle Type". Note: this is state total and does not differentiate by type of road.
corridor_vkt = total_vkt * truck_proportion * corridor_length / total_interstate # In millions of km.

# Truck upgrade cost
# According to http://www.csrf.ac.uk/2020/07/white-paper-long-haul-freight-electrification/, about half of all VKT in the UK will be from hybrids after the upgrades. That's where the 0.5 comes from.
corridor_vkt = corridor_vkt * 0.5
# According to the same report, 100,000 km/year per truck is driven.
num_trucks = corridor_vkt / 0.1
cost_per_truck = (105692-92200) # Based on the report above. The additional cost, including charger, for the hybrid truck. In pounds
cost_per_truck_usd = cost_per_truck * 1.39 # Approximate exchange rate now
total_truck_cost = num_trucks * cost_per_truck_usd

# Cost of building the wires
wire_per_km_cost = 2000000 # Based on the pilot project of the UK report noted above
wire_per_km_cost_usd = wire_per_km_cost * 1.39 # Convert pounds to USD
wire_cost = corridor_length * wire_per_km_cost_usd * 2 # The factor of 2 is to account for one land on the northbound and southbound sides.
maintenance_cost = wire_cost * 0.02 # Annual cost in dollars. The UK report estimates 2% of capital costs are the annual maintenance costs.
total_maintanence_cost = maintenance_cost * (sum([ (1-discount_rate)**i for i in range(infrastructure_life) ]))

# Total energy consumption
# Electricity in the catenary wire scenario
electricity_per_km = 1.68 # See https://www.mdpi.com/1996-1073/11/12/3446/htm, Figure 8. Using the larger battery and continuous catenary, which I think is what the UK study models. In kWh/km.
#electricity_cost = 0.03838 # Average wholesale electricity ($/kWh) (price at the Mid-Columbia hub in 2019 (using 2019 instead of 2020 because 2020 was unusual).
electricity_carbon_intensity = 35.2 # From Table 7, kg/mmbtu, https://www.eia.gov/environment/emissions/state/
electricity_carbon_intensity_converted = electricity_carbon_intensity / 293.07107 / 1000 # Tons ker kWh
electricity_base_cost = 0.0979 # Dollars per KWh in June 2018. From https://www.electricchoice.com/electricity-prices-by-state/
electricity_carbon_cost = electricity_carbon_intensity_converted*carbon_price
electricity_cost = electricity_base_cost + electricity_carbon_cost
total_electricity_cost = electricity_cost * electricity_per_km * corridor_vkt * 10**6 # Annual electricity cost
total_electricity_cost_no_c = electricity_base_cost * electricity_per_km * corridor_vkt * 10**6 # Annual electricity cost
total_electricity_cost_c = electricity_carbon_cost * electricity_per_km * corridor_vkt * 10**6 # Annual electricity cost
# Diesel in the business-as-usual scenario
diesel_direct_price = 3.211 # Dollars per gallon for Washington, accessed March 10, 2021, https://gasprices.aaa.com/state-gas-price-averages/
diesel_carbon_content = 10.21 # kg per gallon released. See Table 2, https://www.epa.gov/sites/production/files/2015-07/documents/emission-factors_2014.pdf
diesel_carbon_price = diesel_carbon_content / 1000 * carbon_price
diesel_price = diesel_direct_price + diesel_carbon_price
diesel_energy_price = diesel_price / 3.78 / 34.9 * 3.6 # Dollars per kWh. See the Transportation Fuels page to get the energy content (pre-combustion).
diesel_energy_price_no_c = diesel_direct_price / 3.78 / 34.9 * 3.6 
diesel_energy_price_c = diesel_carbon_price / 3.78 / 34.9 * 3.6 
diesel_per_km = 3.84 # Same chart as the electricity per km price. In kWh/km.
total_diesel_cost = diesel_energy_price * diesel_per_km * corridor_vkt * 10**6
total_diesel_cost_no_c = diesel_energy_price_no_c * diesel_per_km * corridor_vkt * 10**6
total_diesel_cost_c = diesel_energy_price_c * diesel_per_km * corridor_vkt * 10**6
# Savings
energy_savings = total_diesel_cost - total_electricity_cost # Energy savings, in dollars, for catenary wires.

# Cost and benefit
total_cost = wire_cost + total_truck_cost + maintenance_cost*(sum([ (1-discount_rate)**i for i in range(infrastructure_life) ])) 
total_benefit = energy_savings * (sum([ (1-discount_rate)**i for i in range(infrastructure_life) ]))
benefit_no_c = (total_diesel_cost_no_c - total_electricity_cost_no_c) * (sum([ (1-discount_rate)**i for i in range(infrastructure_life) ]))
benefit_c = (total_diesel_cost_c - total_electricity_cost_c) * (sum([ (1-discount_rate)**i for i in range(infrastructure_life) ]))
# Total costs and benefits in millions of dollars.
print("Costs: $" + str(total_cost / 10**6) + " million")
print("Benefits: $"+str(total_benefit / 10**6) + " million")
# This turns out to be a good investment, albeit barely, at a fairly generous 5% discount rate and 50 year infrastructure life, and the standard $50/ton carbon price. 
# If the discount rate is raised to 6%, or only 40 year life is assumed, it is not a good investment at $50/ton.
# Accounting for non-GHG externalities might help catenary wires look better.
# This looked much better in the UK report I cited. I think the main difference is that the UK heavily taxes diesel, so the energy savings is much greater there.
# I am also using the pilot program cost in the UK report. The full buildout costs are lower, so the CBA would be more favorable in that scenario.

#################################
# Everything beyond this point makes the image
import helper

cba_table = [
    ["<b>Factor</b>","<b>Cost</b>"],
    ["Infrastructure",wire_cost / 10**6],
    ["Maintenance",total_maintanence_cost/ 10**6],
    ["More expensive trucks",total_truck_cost / 10**6],
    ["Total cost",total_cost / 10**6],
    ["<b>Factor</b>","<b>Benefit</b>"],
    ["Energy savings, financial",benefit_no_c / 10**6],
    ["Climate change",benefit_c / 10**6],
    ["Total benefit",total_benefit / 10**6]
]

helper.save_image({
    "filename":"catenary_wires.jpg",
    "status":"Done",
    "details":"Cost-benefit analysis for building catenary wires for trucks, all figures in millions of dollars CPI-adjusted to 2020. This goes in one of the solutions boxes. See the Freight section for more details on how these numbers were derived. Some key figures: I used a 5% discount rate, assumed a 50 year infrastructure life, and applied the usual $50/ton carbon price. I use Wikipedia, which I'm not citing, to determine the length of the I-5 corridor to be assessed and full Washington state Interstate network. WSDOT is used for total travel information. The UK study (Ainalis et al.) gives per-km infrastructure, maintenance, and truck costs, and I am taking the pilot estimate to be representative. Mareev and Sauer give energy consumption estimates for the wire scenario and diesel baseline. Carbon intensity figures are from the EIA. Diesel prices are from the AAA. Electricity prices from Electric Choice. Diesel emissions are from the EPA. The Transportation Fuels page of the site is also used to get an per-kWh cost for diesel. An exchange rate of 1.39 USD per pound is used.",
    "references":["catenary_uk","catenary_energy","wsdot_vkt","emissions_by_state","electricity_price","aaa_state","epa_emissions_factors"],
    "table":cba_table,
    "source_file":"catenary.py"
})