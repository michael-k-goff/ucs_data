# Plots relating to automobiles

import helper

# Greenhouse gas emissions, gCO2e/mile
# Unless otherwise noted, figures are from 'greet'. Download the WTW Calculator spreadsheet, dated 2018.
vehicle_ghg = {
    "Gasoline (E10), Internal Combustion":414,
    "Gasoline (E10), Hybrid Electric":296,
    "Gasoline (E10), Plug-in Hybrid":274,
    "Gasoline, Pyrolysis from Corn Stover":83,
    "Corn Ethanol (E85)": 292,
    "Compressed Natural Gas":354, # First CNG Column
    "Liquified Petroleum Gas":361, # First LPG column
    "Hydrogen (SMR)":247,
    "Diesel (Internal Combustion Engine)":350,
    "Diesel, Pyrolysis from Corn Stover":60,
    "Renewable Diesel (Soybean)":85,
    "Electricity (US Mix)":176,
    "Direct Methanol Fuel Cell (from Natural Gas)":295 # methanol_car, Figure 1.
}

# Methanol values. 308 g/km (found an image). https://www.sciencedirect.com/science/article/abs/pii/S0360319916323060
# Direct Methanol Fuel Cell: 295 g/km. https://www.hydrogen.energy.gov/pdfs/16001_wtw_ghg_methanol_h2_pathways.pdf, Figure 1.

vehicle_ghg_chart = [
    [key, vehicle_ghg[key]/1.60934] # Convert to km
for key in vehicle_ghg]

vehicle_ghg_im = {
    "filename":"ghg_by_fuel.jpg",
    "status":"Done",
    "details":"Show greenhouse gases, in grams CO<sub>2</sub>e per kilometer, for various fuels. They are for the average light-duty vehicle in the US. Most of the numbers come from the GREET model, except the methanol number comes from the other source (which ultimately derives from GREET anyway). I only chose a subset of the fuel options from the GREET model, as listing all of them would be too many.",
    "table":vehicle_ghg_chart,
    "references":["methanol_car","greet"],
    "source_file":"automobiles.py"
}
helper.save_image(vehicle_ghg_im)

#####################################################
# Vehicle LCA. From ev_ice
ev_efficiency = 0.76/3.6 # kWh/km, converted from MJ/km
# First value is Vancouver, BC carbon intensity from ev_ice (mostly hydro), second is US carbon intensity from https://emissionsindex.org/
carbon_intensity = [10.7, (917+890+997+943)/4.*0.453592, 820] # gCO2e/kWh
ev_op = [ev_efficiency*carbon_intensity[i] for i in range(len(carbon_intensity))]
lca = [
    ["<b>Life cycle component</b>","<b>Ford Focus</b>","<b>Mitsubishi i-MiEV (Vancouver, BC)</b>","<b>Mitsubishi i-MiEV (US average)</b>","<b>Mitsubishi i-MiEV (Coal power)</b>"],
    ["Raw Material Production",100.9,163.7,163.7,163.7],
    ["Manufacturing",37.3,34.1,34.1,34.1],
    ["Transportation",1.4, 2.6, 2.6, 2.6],
    ["Operation",253,ev_op[0],ev_op[1],ev_op[2]],
    ["Decommissioning",0.012,0.194,0.194,0.194],
    ["Total",100.9+37.3+1.4+253+0.012, 163.7+34.1+2.6+0.194+ev_op[0],163.7+34.1+2.6+0.194+ev_op[1],163.7+34.1+2.6+0.194+ev_op[2]]
]
helper.save_image({
    "filename":"automobile_lca.jpg",
    "status":"Done",
    "details":"Life cycle greenhouse gas comparison of internal combustion and electric vehicles, presented on a per-km driven basis. The study cited compares a Ford Focus and a Mitsubishi i-MiEV, which aside from the power source, are similar cars and a good comparison. The paper only presents a single scenario for the EV, which is based on BC's low carbon grid (mostly hydro); I redid the numbers with electricity coming from the US average and from an all-coal grid for comparison. This is based on the 150,000 km scenario.",
    "table":lca,
    "references":["ev_ice","emissions_index"],
    "source_file":"automobiles.py"
})

#####################################################

# Plot on the cost of electric vehicles
social_cost_carbon = 50

# From Figure 12 of https://www.sciencedirect.com/science/article/pii/S1364032120304755. Not sure what this means exactly.
ice_cost = 28600
ev_cost = 33400

# Some figures from https://advocacy.consumerreports.org/wp-content/uploads/2020/10/EV-Ownership-Cost-Final-Report-1.pdf
ice_maint = 50000*(0.028+0.06+0.079) # Assuming 150,000 miles. See Table 2.1. Not discounted.
ev_maint = 50000*(0.012+0.028+0.043)
ice_fuel = 14200 # See Figure 3.1. Assuming 150,000 miles.
ev_fuel = 6200

# Already on the site
ice_emissions = 150000*392.6*10**(-6)
ev_emissions = 150000*290.3*10**(-6)
carbon_mitigation_cost = (ev_cost-ice_cost)/(ice_emissions-ev_emissions) # Not using this because EVs save money over the lifetime even without CO2 mitigation.

vehicle_table = [
    ["<b>Scenario</b>","<b>Cost</b>"],
    ["Internal Combustion Engine, car cost",ice_cost],
#    ["Diesel, direct cost",29300],
#    ["Hybrid gasoline",30000],
#    ["Plug-in hybrid",32400],
    ["Battery electric, car cost",ev_cost],
#    ["Hydrogen fuel cell",60000],
    ["ICE, maintenance cost",ice_maint],
    ["EV, maintenance cost",ev_maint],
    ["ICE, fuel cost",ice_fuel],
    ["EV, fuel cost",ev_fuel],
    ["ICE, emissions cost",150000*392.6*10**(-6)*social_cost_carbon],
    ["EV, emissions cost",150000*290.3*10**(-6)*social_cost_carbon],
    ["Cost of an EV, relative to ICE",ev_cost-ice_cost],
    ["Benefit of an EV, relative to ICE",ice_maint+ice_fuel+ice_emissions - ev_maint-ev_fuel-ev_emissions]
]

print(150000*392.6*10**(-6) - 150000*290.3*10**(-6))

helper.save_image({
    "filename":"bev.jpg",
    "status":"On Hold",
    "details":"Car purchase costs are from Balali and Stegen. Maintenance and fuel costs from Consumer Reports. Greenhouse gas figures are already on the website. I would classify this endeavor on the basis of total costs of a single EV purchase, as opposed to ICE. The cost is given by the cost of the vehicle and the benefit is everything else. No discount rate is used. I'm also not monetizing here other factors like battery range, vehicle size and power, etc.",
    "table":vehicle_table,
    "references":["consumer_reports_ev","car_cost"],
    "source_file":"automobiles.py"
})