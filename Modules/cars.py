# Cars

import helper

# Potential fuel economy from interal combustion

fuel_economy = [
    ["<b>Scenario</b>","<b>Fuel Economy (miles per gallon gasoline)</b>"],
    ["Average Model Year 2018",25.4], # auto_trends
    ["Average MY2018 if horsepower and torque remained at 1980 values",40], # knittel
    ["2012 CAFE standards for 2025",50], # lipman
    ["2025 Fuel Economy with Expected Improvements to Drivetrain and Fuel Cycle",48.8] # fuelecon2025
]

helper.save_image({
    "filename":"ice_fuel_econ.jpg",
    "status":"Done",
    "table":fuel_economy,
    "details":"Fuel economy under various scenarios. Key point is that major improvements are possible.",
    "references":["auto_trends","knittel","lipman","fuelecon2025"],
    "source_file":"cars.py"
})

############################################## External costs
# Main source: https://www.vtpi.org/tdm/tdm66.htm, Table 16, ref [tdm]
# For each cost center, the costs are [internal variable, internal fixed, external]
# Cost figures are 2000 USD per vehicle-year.
per_vehicle_costs = [
    ["<b>Cost Center</b>","<b>Variable Internal</b>","<b>Fixed Internal</b>","<b>External</b>"],
    ["Travel Time",3818,0,0],
    ["Vehicle Ownership",0,2727,0],
    ["Crash Damages",1045,455,773],
    ["Non-residential Off-street Parking",68,68,1228],
    ["Vehicle Operations",1136,0,0],
    ["Roadway Costs",360,0,185],
    ["Traffic Congestion",0,0,455],
    ["Environmental Costs",0,0,455],
    ["Roadway Land Value",0,0,295],
    ["Residential Parking",0,227,0],
    ["Fuel Externalities",0,0,182],
    ["Traffic Services",0,0,136], # e.g. traffic police, street lighting, planning, and emergency services
    ["Total",6427,3477,3709]
]
for i in range(1,len(per_vehicle_costs)):
    for j in range(1,4):
        per_vehicle_costs[i][j] *= (1.198/13618.) * 1.60934 * 1.4911848 # First term converts from vehicle-years to vehicle-miles, the second from mi to km, the third CPI adjustment to 2019
helper.save_image({
    "filename":"car_costs.jpg",
    "status":"Done",
    "details":"Detailed breakdown of internal and external costs of driving. All figures are 2019 USD, dollars per vehicle-km. I'm not 100% sure yet, but I think the best way to do this will be to do three bars, one for each column in the table, and for each bar show the major cost centers. We might also combine the variable and fixed internal costs into a single bar. Another option is to three (or two) separate bar plots, one for each column. Variable costs are those that are accumulated on a per-mile driven basis, and fixed costs are incurred regardless of the amount of driving done (though are divided by average total km). A portion of crash damage costs are internalized through insurance and liability, and a portion of roadway costs are internalized through gas taxes or tolls.",
    "table":per_vehicle_costs,
    "references":["tdm"],
    "source_file":"cars.py"
})

############################################## Roadway damage figures

road_damage_table = [
    ["<b>Vehicle</b>","<b>Road damage compared to a typical passenger car</b>"],
    ["Average car",1],
    ["Vans / Pickups",7],
    ["Large pickups / Delivery Vans",15],
    ["Large delivery trucks",163],
    ["Local delivery trucks",236],
    ["Residential recycling trucks",274],
    ["Buses",851],
    ["Residential trash trucks",1279],
    ["Long-haul semi trailers",1408],
    ["Toyota Prius",0.338],
    ["Smart car",0.0410],
    ["Bicycle, worst case scenario",0.00006],
    ["Hummer H2",21.3675],
    ["Chevy Tahoe",3.5745],
    ["Toyota RAV 4",0.6204]
]

helper.save_image({
    "filename":"road_damage.jpg",
    "status":"Done",
    "table":road_damage_table,
    "details":"Some estimates of road damage by type of vehicle. Semi trailers and all figures above it come from the Minnesota study. All figures below that are from Streets MN.",
    "references":["streets_mn","mn_road_damage"],
    "source_file":"cars.py"
})

dev_table = [
    ["<b>Development Type</b>","<b>Unit</b>","<b>Appropriate Fee (USD)</b>"],
    ["Single Family Home","1 unit",600],
    ["Multi-family Home","1 unit",400],
    ["Shopping Center","1000 sf floor space",6500],
    ["Office/Institutional","1000 sf floor space",1700],
    ["General Commercial","1000 sf floor space",1900],
    ["Mixed industrial","1000 sf floor space",1000],
    ["Warehousing","1000 sf floor space",800],
    ["Manufacturing","1000 sf floor space",600],
    ["Oil and gas wells","1 well",17700]
]

helper.save_image({
    "filename":"road_damage_dev.jpg",
    "status":"Done",
    "table":dev_table,
    "details":"An estimate on how much road damage costs should be assessed for a new development, based on how much traffic they will generate. Although I am citing the Minnesota Department of Transportation, they cite another study by RPI Consulting for Rio Blanco County. I'd cite that study directly but I can't find a good link for it now.",
    "references":["mn_road_damage"],
    "source_file":"cars.py"
})
