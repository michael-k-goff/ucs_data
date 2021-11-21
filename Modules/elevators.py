# Elevators

import helper
from primary_energy_factors import primary_factors # Source is 'energycode'

#################################
# Figure from elevators_escalators. See Table 3, Figure 8, Figure 9.
# cycle is in Wh per elevator cycle
# running: share of energy that is used is active operation (as opposed to standby)
scenarios = {
    "A":{
        "type":"Gearless Traction",
        "stories":3,
        "cycle":6.04,
        "running":0.303
    },
    "B":{
        "type":"Traction with VSD",
        "stories":9,
        "cycle":30.73,
        "running":0.317
    },
    "C":{
        "type":"Gearless Traction",
        "stories":13,
        "cycle":58.71,
        "running":0.282
    },
    "D":{
        "type":"Geared Traction",
        "stories":9,
        "cycle":58.75,
        "running":0.754
    },
    "E":{
        "type":"Geared Traction",
        "stories":3,
        "cycle":15.93,
        "running":0.582
    },
    "F":{
        "type":"Geared Traction",
        "stories":4,
        "cycle":18.48,
        "running":0.204
    },
    "G":{
        "type":"Hydraulic",
        "stories":5,
        "cycle":143.77,
        "running":0.822
    },
    "H":{
        "type":"Hydraulic",
        "stories":6,
        "cycle":153.8,
        "running":0.870
    }
}

elevator_types = ["Gearless Traction","Traction with VSD","Geared Traction","Hydraulic"]
for key in scenarios:
    scenarios[key]["energy_per_cycle"] = scenarios[key]["cycle"] / scenarios[key]["running"]
    
scenario_table = [["<b>Type</b>","Primary Energy per Visitor (kJ, low estimate)","Primary Energy per Visitor (kJ, high estimate)","Primary Energy per Visitor (kJ/km, low estimate)","Primary Energy per Visitor (kJ/km, high estimate)"]]
for i in range(len(elevator_types)):
    # Energy per elevator cycle
    energies = [primary_factors["Electricity"] * 3.6 * scenarios[key]["energy_per_cycle"] for key in scenarios if scenarios[key]["type"]==elevator_types[i]]
    # Energy per km traveled. Assuming 4 meters per story and, on average, the elevators go half way to the top.
    # I am also assuming that the story count in the source does not include the ground floor.
    energies_dist = [primary_factors["Electricity"] * 3.6 * scenarios[key]["energy_per_cycle"] / scenarios[key]["stories"] / 0.004 for key in scenarios if scenarios[key]["type"]==elevator_types[i]]
    scenario_table.append([ elevator_types[i], min(energies), max(energies), min(energies_dist), max(energies_dist) ])
    
# Some stair figures for good measure. Four flights, round trip. 2.5-5 calories per flight. PEF of 15 for food; see ag - environmental.txt.
# The 4.184 term converts kcal to kJ.
# For longer distance, going with 4 meters per storey as before.
energy_stairs_low = 2.5*4*15*4.184
energy_stairs_high = 5.0*4*15*4.184
energy_stairs_km_low = 2.5*250*15*4.184
energy_stairs_km_high = 5.0*250*15*4.184
scenario_table.append(["Stairs: 4 stories round trip",energy_stairs_low, energy_stairs_high, energy_stairs_km_low, energy_stairs_km_high])

scenario_im = {
    "filename":"elevator.jpg",
    "status":"Done",
    "details":"Show how much primary energy is used for elevators. These figures are based on a study of eight buildings with different types of elevators. I am assuming that each elevator cycle carries two people and each person requires two cycles (an up and a down) per building visit, so that's one cycle per visitor. These figures include standby energy that the elevator uses while waiting to be summoned. For the energy per unit distance (kJ/km is an awkward unit for elevators, as there are no kilometer-tall buildings today, but I use it to be consistent with other plots), I assume that the elevators on average go half way to the top of the building and that each storey is 4 meters.",
    "table":scenario_table,
    "references":["energycode","elevators_escalators","stairs_energy"],
    "source_file":"elevators.py"
}
helper.save_image(scenario_im)

#################################
# Escalators

# Energy is annual, in kWh. Taken from escalator1.
# Passengers is taken from escalator2. First term is my guess on number per hour to use for full capacity, second is number of horus per day of operation
# Note that passengers are daily while energy is yearly.
# Alternative escalator2 document: https://www.kone.us/Images/KONE-Escalator-AutoWalk-Planning-Guide_tcm25-18783.pdf
scenarios = {
    "Shopping Mall":{
        "energy":4000., # High end: 10000
        "energy_high":10000.,
        "passengers":4800.*14.*0.2 # The 0.2 comes from
    },
    "Hotel / Convention Center":{
        "energy":31000.,
        "energy_high":31000.,
        "passengers":4800.*14.
    },
    "Metro / Airport":{
        "energy":60000.,
        "energy_high":60000.,
        "passengers":7300.*20.
    }
}
# Based on escalator2 and my own wild guessing, I will take load factors ranging from 1/3 to 2/3.
# Get primary energy per passenger in kJ.
for key in scenarios:
    scenarios[key]["energy_passenger_low"] = scenarios[key]["energy"] * 1.5 / scenarios[key]["passengers"] * primary_factors["Electricity"] * 3600. / 365.
    scenarios[key]["energy_passenger_high"] = scenarios[key]["energy_high"] * 3.0 / scenarios[key]["passengers"] * primary_factors["Electricity"] * 3600. / 365.
scenarios_chart = [["<b>Escalator Class</b>","<b>Primary Energy per Passenger, Low Estimate, kJ</b>","<b>Primary Energy per Passenger, High Estimate, kJ</b>"]]
for key in scenarios:
    scenarios_chart.append([key,scenarios[key]["energy_passenger_low"], scenarios[key]["energy_passenger_high"] ])

escalator_im = {
    "filename":"escalator.jpg",
    "status":"Done",
    "details":"Low and high end estimate of energy per passenger for various escalator scenarios. They assume 33-67% load factors, an additional 80% load factor reduction for the mall scenario, capacities of 4800 passengers per hour for the mall and hotel scenarios, 7300 passengers per hour for the metro scenario. Figures on total energy consumption for the escalators are from the E3T source, primary energy conversion from Building Energy Codes Program, and all other escalator parameter data from the KONE source. This plot felt like a lot of work for such small numbers.",
    "table":scenarios_chart,
    "references":["energycode","escalator1","escalator2"],
    "source_file":"elevators.py"
}
helper.save_image(escalator_im)

#################################
# The following is from elevator_energy. The figures don't feel right, and so I am not going to use them.

# Three elevator scenarios from elevator_energy
# Energy in kWh, per year.
scenarios = {
    "Gearless Traction":{
        "Number of Elevators":3,
        "Employees":460,
        "Stories":7,
        "Energy": 145130
    },
    "Geared Traction":{
        "Number of Elevators":3,
        "Employees":460,
        "Stories":7,
        "Energy": 98852
    },
    "Hydraulic":{
        "Number of Elevators":2,
        "Employees":410,
        "Stories":2,
        "Energy": 19862
    }
}

# Calculate energy per person for the three scenarios.
# Assumptions: Each person is there for 200 days pey year.
# Everyone who does not work on the ground floor makes, on average, two elevator trips per day.
# If there are more trips, then there will be less energy per trip.
# The same number of people work on every floor.
def energy_per_person(scenario):
    trips = scenario["Employees"]*200*2 * float(scenario["Stories"]) / float(scenario["Stories"]+1)
    energy_per_trip = scenario["Energy"] / trips # kWh per trip
    energy_per_trip = energy_per_trip * primary_factors["Electricity"] * 3.6 # Convert to primary energy and MJ
    return round(1000*energy_per_trip,-2)
    
elevator_table = [
    ["<b>Elevator Type</b>","<b>Primary Energy Consumption per Trip (kilojoules)</b>"],
    ["Hydraulic",energy_per_person(scenarios["Hydraulic"])],
    ["Geared Traction",energy_per_person(scenarios["Geared Traction"])],
    ["Gearless Traction",energy_per_person(scenarios["Gearless Traction"])]
]
