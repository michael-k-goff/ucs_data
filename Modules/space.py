# Space

import helper
from primary_energy_factors import primary_factors # Source is 'energycode'
primary_factors["rp1"] = 1.05 # Assuming it is the same as some other petroleum-based fuels.

# Launch costs, monetary and energy. Based on Falcon Heavy.

falcon_heavy_cost = 90000000 # Dollars per launch
# From https://spaceflight101.com/spacerockets/falcon-heavy/
falcon_heavy_tonnage = { # kg, actually
    "Low Earth Orbit":54400,
    "Geosychronous Transfer Orbit":22200,
    "Mars":13600
}
# Based on GTO, less payload with a resuable launch (standard payment plan).
# For calculations I will assume this ratio applies to all launch scenarios, which is probably not exactly accurate.
reusable_adjustor = 8000. / 26700.

# I'm not sure if we should use the adjustor. For now I'm thinking not.
#for key in falcon_heavy_tonnage:
#    falcon_heavy_tonnage[key] *= reusable_adjustor
    
falcon_heavy_cost_per_ton = [["<b>Destination</b>","<b>Cost: dollars per kg payload (Falcon Heavy)</b>"]] + [
    [key,falcon_heavy_cost / falcon_heavy_tonnage[key]] for key in falcon_heavy_tonnage
]

# From falcon_heavy_energy. Also reviewed https://space.stackexchange.com/questions/32729/how-much-fuel-does-the-falcon-heavy-use-what-is-the-price-rp-1
# Figures in kilograms
falcon_heavy_energy = {
    "rp1":123570*3 + 32300, # A core, two boosters, and the second stage.
    "lox":287430*3 + 75200
}

falcon_heavy_energy["rp1"] = falcon_heavy_energy["rp1"] * 12.8*3.6*primary_factors["rp1"] # The 12.8 term is from 'hotair', converting a kg of fuel (kerosene) to kWh, then MJ, then primary energy
falcon_heavy_energy["lox"] = falcon_heavy_energy["lox"] * 0.8 * 3.6 * primary_factors["Electricity"] # lox_energy. This is to produce the liquid oxygen.

falcon_heavy_energy_total = sum([falcon_heavy_energy[key] for key in falcon_heavy_energy])

falcon_heavy_energy_perton = [["<b>Destination</b>","<b>Energy Consumption: MJ/kg payload (Falcon Heavy)</b>"]] + [ # Actually MJ/kg. Or GJ/ton. For J/mg if we want to be silly.
    [key,falcon_heavy_energy_total / falcon_heavy_tonnage[key]] for key in falcon_heavy_tonnage
]

rocket_cost_im = {
    "filename":"launch_cost.jpg",
    "status":"Done",
    "table":falcon_heavy_cost_per_ton,
    "details":"Launch cost for three destinations by the SpaceX Falcon Heavy rocket. Note that SpaceX (and nobody else either) does commercial Mars missions, but they report the payload capacity if they were to do a Mars mission. Figures are dollars per kilogram. I will mention in the text some historical and projected future cost points, but I am uncertain if I want to add anything more to the graphic.",
    "references":["spacex"],
    "source_file":"space.py"
}

rocket_energy_im = {
    "filename":"launch_energy.jpg",
    "status":"Done",
    "table":falcon_heavy_energy_perton,
    "details":"There were a couple errors here before which I've fixed. First, I only counted one booster toward total energy when I should have counted two. Second, the tonnage figures to LEO, GEO, and Mars were off.",
    "references":["spacex","energycode","falcon_heavy_energy","hotair","lox_energy"],
    "source_file":"space.py"
}

helper.save_image(rocket_cost_im)
helper.save_image(rocket_energy_im)

##########################################################
# Calculate total launch energy. Covers 2016, 2017, and 2018.
# Launch rates from spacelaunchreport.com. As are all vehicle parameters unless otherwise noted.
launch_figures = {
#    "CZ (DF-5)":{ # Break this down to subcategories
#        "2018":34,
#        "2017":13,
#        "2016":19
#    },
    "CZ-2C":{
        "2018":6,
        "2017":3,
        "Liftoff Mass":213
    },
    "CZ-2D":{
        "2018":8,
        "2017":3,
        "2016":6,
        "Liftoff Mass":232
    },
    "CZ-2F":{
        "2016":2,
        "Liftoff Mass":464
    },
    "CZ-3A":{
        "2018":2,
        "2016":1,
        "Liftoff Mass":242
    },
    "CZ-3B":{
        "2018":3,
        "2017":1,
        "Liftoff Mass":426
    },
    "CZ-3BE":{
        "2018":8,
        "2017":4,
        "2016":3,
        "Liftoff Mass":456
    },
    "CZ-3C":{
        "2016":1,
        "Liftoff Mass":345
    },
    "CZ-3CE":{
        "2018":1,
        "2016":2,
        "Liftoff Mass":366
    },
    "CZ-4B":{
        "2018":2,
        "2017":1,
        "2016":2,
        "Liftoff Mass":249
    },
    "CZ-4C":{
        "2018":4,
        "2017":1,
        "2016":2,
        "Liftoff Mass":249
    },
    "Falcon 9":{
        "2018":20,
        "2017":18,
        "2016":8,
        "Liftoff Mass":556
    },
#    "R-7":{ # Break down into subtypes
#        "2018":15,
#        "2017":14,
#        "2016":14
#    },
    "Soyuz-U":{
        "2017":1,
        "2016":2,
        "Liftoff Mass":310
    },
    "Soyuz-FG":{
        "2018":5,
        "2017":4,
        "2016":4,
        "Liftoff Mass":308
    },
    "Soyuz-2-1a":{
        "2018":5,
        "2017":4,
        "2016":4,
        "Liftoff Mass":308
    },
    "Soyuz-2-1b":{
        "2018":5,
        "2017":5,
        "2016":4,
        "Liftoff Mass":308
    },
#    "Ariane 5":{ # Break down into subcategories
#        "2018":6,
#        "2017":6,
#        "2016":7
#    },
    "Ariane 5ECA":{
        "2018":5,
        "2017":5,
        "2016":6,
        "Liftoff Mass":780
    },
    "Ariane 5ES":{
        "2018":1,
        "2017":1,
        "2016":1,
        "Liftoff Mass":760
    },
#    "Atlas 5": { # Break into subcategories
#        "2018":5,
#        "2017":6,
#        "2016":8
#    },
    "Atlas 5-401":{
        "2018":1,
        "2017":4,
        "2016":3,
        "Liftoff Mass":333.32
    },
    "Atlas 5-411":{
        "2018":1,
        "2016":1,
        "Liftoff Mass":374.12
    },
    "Atlas 5-421":{
        "2017":1,
        "2016":1,
        "Liftoff Mass":414.92
    },
    "Atlas 5-431":{
        "2016":1,
        "Liftoff Mass":461.18
    },
    "Atlas 5-541":{
        "2018":1,
        "2017":1,
        "2016":1,
        "Liftoff Mass":522.33
    },
    "Atlas 5-551":{
        "2018":2,
        "2016":1,
        "Liftoff Mass":568.59
    },
#    "PLSV":{ # Break down into subcategories
#        "2018":4,
#        "2017":3,
#        "2016":6
#    },
    "PLSV-G":{
        "2016":1,
        "Liftoff Mass":295
    },
    "PLSV-CA":{
        "2018":2,
        "Liftoff Mass":230
    },
    "PLSV-XL":{
        "2018":2,
        "2017":5,
        "Liftoff Mass":316
    },
    "H-2A-202":{
        "2018":3,
        "2017":4,
        "2016":2,
        "Liftoff Mass":290
    },
    "H-2A-204":{
        "2017":2,
        "Liftoff Mass":445
    },
    "CZ-11":{
        "2018":3,
        "2016":1,
        "Liftoff Mass":58
    },
    "Electron":{
        "2018":3,
        "2017":1,
        "Liftoff Mass":12.55
    },
    "Proton":{
        "2018":2,
        "2017":4,
        "2016":3,
        "Liftoff Mass":700 # All are Briz-M
    },
    "GSLV Mk1":{
        "2018":1,
        "Liftoff Mass":401
    },
    "GSLV Mk2":{
        "2018":1,
        "2017":1,
        "2016":1,
        "Liftoff Mass":415
    },
    "Antares 230":{
        "2018":2,
        "2017":1,
        "2016":1,
        "Liftoff Mass":286 # Antares 230
    },
    "Vega":{
        "2018":2,
        "2017":3,
        "2016":2,
        "Liftoff Mass":136.7 # Regular Vega, not Vega-C
    },
    "Rokot/Briz KM":{
        "2018":2,
        "2017":1,
        "2016":2,
        "Liftoff Mass":107
    },
    "Delta 4 Heavy":{
        "2018":1,
        "2016":4,
        "Liftoff Mass":732
    },
    "Falcon Heavy":{
        "2018":1,
        "Liftoff Mass":1420.788
    },
    "H-2B":{
        "2018":1,
        "2016":1,
        "Liftoff Mass":531
    },
    "Delta 4M":{
        "2018":1,
        "Liftoff Mass":332 # Delta IV-M+(5,2)
    },
    "GLSV Mk3":{
        "2018":1,
        "2017":1,
        "Liftoff Mass":640
    },
    "Soyuz 2-1v":{
        "2018":1,
        "Liftoff Mass":158.5 # 157-160
    },
    "Delta 2 7420":{
        "2018":1,
        "Liftoff Mass":162
    },
    "Delta 2 7920":{
        "2017":1,
        "Liftoff Mass":228
    },
    "Enhanced Epsilon":{
        "2018":1,
        "2016":1,
        "Liftoff Mass":95.4
    },
    "KZ-1A":{
        "2018":1,
        "2017":1,
        "Liftoff Mass":30
    },
    "SS-520":{
        "2018":1,
        "2017":1,
        "Liftoff Mass":2.6
    },
    "ZQ-1":{
        "2018":1,
        "Liftoff Mass":27
    },
    "Delta 4 (5,4)":{
        "2017":1,
        "Liftoff Mass":399
    },
    "CZ-7":{
        "2017":1,
        "2016":1,
        "Liftoff Mass":594 # Not sure which ones they are, so going with the 340.
    },
    "Zenit":{
        "2017":1,
        "Liftoff Mass":460 # 3F
    },
    "Soluz 2-1v/Volga":{
        "2017":1,
        "Liftoff Mass":158.5 # Not sure how this differs from the other 2-1v
    },
    "Minotaur 4":{
        "2017":1,
        "Liftoff Mass": 86 # Regular Minotaur
    },
    "Minotaur-C":{
        "2017":1,
        "Liftoff Mass":77 # 3210
    },
    "CZ-6":{
        "2017":1,
        "Liftoff Mass":103.217
    },
    "KT-2":{
        "2017":1,
        "Liftoff Mass":58
    },
    "CZ-5":{
        "2017":1,
        "2016":1,
        "Liftoff Mass":500 # I can't figure this one out and so am just guessing.
    },
    "Shavit 2": {
        "2016":1,
        "Liftoff Mass":30. * 0.3/0.16 # Missing figure, so I am doing some extrapolation.
    },
    "Pegasus-XL":{
        "2016":1,
        "Liftoff Mass":23.13
    },
    "Unha":{
        "2016":1,
        "Liftoff Mass": 91 # Unha 3
    }
}

# Calculation benchmarks for estimating energy for each rocket.
benchmarks = {
    "Liftoff Mass":1420.788
}

# Get total liftoff tonnage as a multiple of Falcon Heavy launches
tonnage = sum([launch_figures[key]["Liftoff Mass"] for key in launch_figures])
# Total energy, in TJ per year
# This is much lower than I expected.
tj_year = falcon_heavy_energy_total * tonnage / benchmarks["Liftoff Mass"] / 1000000. / 3

########################################## Statistics on launches
# Launches in 2018, 2017, 2016 (that order for summands) by destination

launch_target_dict = {
    "Low Earth Orbit, excluding International Space Station":67-12+50-13+44-11,
    "International Space Station":12+13+11,
    "Medium Earth Orbit":13+3+6,
    "Geosynchronous Transfer Orbit":26+32+32,
    "Earth Elliptical Orbit":4+4+2,
    "Earth Escape":4+0+2
}
target_by_energy_dict = {
    "Low Earth Orbit":launch_target_dict["Low Earth Orbit, excluding International Space Station"]+launch_target_dict["International Space Station"],
    "Geosychronous Transfer Orbit":launch_target_dict["Medium Earth Orbit"]+launch_target_dict["Geosynchronous Transfer Orbit"]+launch_target_dict["Earth Elliptical Orbit"],
    "Mars":launch_target_dict["Earth Escape"]
}
tonnage_launched = {
    "Low Earth Orbit":397,
    "Geosychronous Transfer Orbit":71,
    "Mars":20
}
#print([tonnage_launched[key] for key in tonnage_launched] )
#print([falcon_heavy_energy_total / falcon_heavy_tonnage[key] for key in falcon_heavy_tonnage])
#print(sum([tonnage_launched[key]*falcon_heavy_energy_total / falcon_heavy_tonnage[key] for key in target_by_energy_dict]))

launch_targets = [
    ["<b>Destination</b>","<b>Number of launches, 2016-18</b>"],
    ["Low Earth Orbit, excluding International Space Station",67-12+50-13+44-11 -2-3-3], # Final terms are failures
    ["International Space Station",12+13+11],
    ["Medium Earth Orbit",13+3+6], # MEO and MTO
    ["Geosynchronous Transfer Orbit",26+32+32 -1-2-1], # GTO and GEO. Not sure where to allocate failures, so putting them here.
    ["Earth Elliptical Orbit",4+4+2],
    ["Earth Escape",4+0+2],
    ["Failed Launches",3+6+3]
]
launch_target_im = {
    "filename":"launch_targets.jpg",
    "status":"Done",
    "table":launch_targets,
    "details":"Table showing where rockets go. This is based on all launches from 2016-18, including failed launches (where the rocket was intended to go).",
    "references":["spacelaunchreport"],
    "source_file":"space.py"
}
helper.save_image(launch_target_im)

###########################################
# Delta V table
delta_v = [
    ["<b>Trip</b>","<b>&Delta;v (km/s)</b>"],
    ["Earth surface to Earth orbit",8],
    ["Earth orbit to Earth-Moon Lagrange Point",3.5],
    ["Earth orbit to low-Moon orbit",4.1],
    ["Earth orbit to Lunar surface",6],
    ["Earth orbit to near-Earth asteroids","4+"],
    ["Earth orbit to Mars surface",8]
]
delta_v_im = {
    "filename":"delta_v.jpg",
    "status":"Done",
    "table":delta_v,
    "details":"Show &Delta;v values for common trips. This is not a very good source, and I want to find a better one. There is a common table that gets copied around, apparently originating from Wikipedia, but the source link is dead and I can't find where it came from; if I could, that would be much better. A remarkable fact is that, once you've gotten into orbit just a few hundred kilometers up, you are over half way from an energy expenditure standpoint to almost any destination in the inner solar system.",
    "references":["pettit"],
    "source_file":"space.py"
}
helper.save_image(delta_v_im)

##########################################
# Exhaust velocity. Mostly from pettit
exhaust = [
    ["<b>Reaction</b>","<b>Exhaust Velocity</b>"],
    ["Solid Fuel",3.0],
    ["Kerosene",3.1],
    ["Hypergols",3.2],
    ["Methane/Oxygen",4.5],
    ["Hydrogen/Oxygen",4.5], # hydrogen_propulsion
    ["Nuclear Thermal",8.3],
    ["Microwave Thermal (best case scenario)",11.9] # microwave_launch
]
exhaust_im = {
    "filename":"exhaust_velocity.jpg",
    "status":"Done",
    "table":exhaust,
    "details":"Show exhaust velocity for various rocket fuels. This graphic is meant only to cover propellant-based options for launching from Earth.",
    "references":["pettit","hydrogen_propulsion","microwave_launch"],
    "source_file":"space.py"
}
helper.save_image(exhaust_im)

############################################
# Power in space
space_power = [
    ["<b>Source</b>","<b>Purpose</b>","<b>Details</b>","<b>Power range</b>"],
    ["Solar","Most satellites","3-junction cells, 30% efficiency","Few watts to 10s of kW"],
    ["Radioisotope","Outer solar system, planetary landers","Pu-238, Am-241, Po-210","100 W to 100 kW"],
    ["Fission","Large robotic missions, crewed Mars mission","Various designs","45.5 kW to 2 MW (thermal) and 650 W to 100 kW (electric)"]
]
space_power_im = {
    "filename":"space_power.jpg",
    "status":"Done",
    "table":space_power,
    "details":"Summary of how power (not primarily for propulsion) is generated in space.",
    "references":["spacepower_solar","spacepower_rtg","spacepower_kilopower"],
    "source_file":"space.py"
}
helper.save_image(space_power_im)

###########################################
# In-space propulsion. Really, this could go on forever.
in_space_propulsion = [
    ["<b>Method</b>","<b>Energy Source</b>","<b>Use Case</b>","<b>Example Project</b>","<b>Exhaust Velocity (if applicable)</b>","<b>Rationale</b>","<b>Challenges</b>"],
    ["<b>Present Day</b>","","","","","",""],
    ["Chemical Rocket","Chemical Reaction","Launch, upper stages","Widely used","Up to 4.5 km/s","Established technology",""],
    ["Hydrazine","Chemical Reaction","Satellite Maneuvering","Widely used","2.3 km/s","Easily used as a monopropellant","Highly toxic"], # monopropellant and hydrazine
    ["Gravity Assist","Gravitational Potential Energy","Interplanetary Travel","Voyager, many other interplanetary missions","Depends on circumstances. Galileo gained 18.3 km/s from a Venus-Earth-Earth assist.","Save propellant","May require slow, indirect routes"], # gravity_assist
    ["Pulsed plasma thruster","Electricity (solar, radioisotope)","Small Satellite Maneuvering"," Earth Observing 1 satellite","5-60 km/s","Simple design","Less efficient than other electric options"], # ppt
    ["Ion Drive","Electricity","Satellites, low-mass robotic probes","Dawn","20-50 km/s","High impulse","Low thrust. Thrust may increase with next generation Hall thruster."], # dawn, new_dawn
    
    ["<b>Under Development</b>","","","","","",""],
    ["Nuclear Thermal Rocket","Nuclear Fission","Crewed Mission to Mars","NERVA","8.3 km/s","Most promising near-term option for large, high-impulse craft","Safety may preclude use as a booster stage"], # ntr
    ["Magnetoplasmadynamic Thruster","Electricity, most likely from fission","Large interplanetary spacecraft","Space Flyer Unit","15-60 km/s","High impulse and thrust","High power needed, likely necessitating a new reactor design, degradation of cathodes limits lifespan."], # new_dawn for exhaust velocity. magneto
    ["Variable Specific Impulse Magnetoplasma Rocket","Fission","Crewed interplanetary missions","Ad Astra Rocket Company","50 km/s","Balance between low thrust, high impulse and high thrust, low impulse designs","Required power system might not be feasible."], # vasimr, vasimr2
    ["Solar Sail","Solar Power","Interplanetary transport of goods, deorbiting satellites","IKAROS","c (propellantless)","Low cost, propellantless craft, faster travel to outer Solar System","Cannot operate in Earth orbit below 800 km."], # solar_sail
    ["Direct Fusion Drive","Nuclear Fusion","Interplanetary travel","Princeton Satellite Systems","100 km/s","High thrust and exhaust velocity","Much R&D required on the fusion generator"],
    
    ["<b>Speculative</b>","","","","","",""],
    ["Beamed Propulsion","Laser","Interstellar Probe","Breakthrough Starshot","c (Propellantless)","Nearest term possibility for interstellar mission","Keeping laser focused on the craft is extremely challenging."], # breakthrough_starshot
    ["Magnetic Sail","Stellar Wind","Low cost interplanetary travel, interstellar travel","---","---","Reduce need for propellant, onboard energy","---"], # magsail
    ["Nuclear Pulse Propulsion","Nuclear explosions or inertial confinement fusion","Interplanetary, Interstellar Travel","Project Orion, Project Daedalus","10000 km/s","Very high exhaust velocity and thrust","Safety, craft is necessarily very large"], # daedalus
    
    ["<b>Theoretical</b>","","","","","",""],
    ["Antimatter-catalyzed nuclear pulse propulsion","Primarily fusion","Interplanetary, interstellar travel","---","8000 km/s","More compact than nuclear pulse rocket","Difficulty in producing and storing antimatter"], # acnp
    ["Antimatter","Matter-Antimatter Reaction","Interstellar Travel","Project Valkyrie","100,000 km/s","Exhaust velocity and thrust near theoretical maximum","Difficulty in producing and storing antimatter"], # antimatter_rocket
    ["Black Hole","Hawking Radiation","Interstellar Travel","---","c","Pure mass to energy conversion","Physics are highly uncertain."], # black_hole, black_hole2
    ["Wormhole, Warp Field, Reactionless Drive, etc.","???","???","EmDrive","???","???","Not permitted under established physics."]
]
in_space_im = {
    "filename":"in_space_propulsion.jpg",
    "status":"Done",
    "table":in_space_propulsion,
    "details":"Methods for moving spacecraft when they are already in space. This is a big chart with a bunch of sources, plus--not listed before--sources indicated earlier in the Space section for chemical and nuclear thermal rockets. If this is too cumbersome for a single image, break it up into four. The categories criteria are as follows. Present Day: the method is in use for real missions. Under Development: prototypes have been built or major R&D activities are under way. Speculative: no major prototypes or R&D efforts, but we have plausible schematics of how they might work. Theoretical: a concept has been described, but it might contradict physics or there are otherwise major conceptual gaps. Don't try to compare the exhaust velocities numerically, as they are not all comparable and the scale would have too much variance. c is the speed of light.",
    "references":["monopropellant", "hydrazine","gravity_assist","ppt","nasa_ppt","dawn","new_dawn","ntr","magneto","vasimr","vasimr2","solar_sail","spacepower_fusion", "breakthrough_starshot","magsail","daedalus","acnp","antimatter_rocket","black_hole","black_hole2"],
    "source_file":"space.py"
}
helper.save_image(in_space_im)