# World energy, based primary on IEA Sankey Diagrams
# This module should ultimately govern how world (and maybe some national) energy figures are reported.

# Main source here is 'iea_sankey'

import helper
from primary_energy_factors import primary_factors # Source is 'energycode'
from primary_energy_factors import emissions_factors # Various sources: see the file for details.

primary_factors["Oil"]=1
primary_factors["Oil Products"]=1.05
primary_factors["Natural Gas"]=1.05
primary_factors["Biofuel"]=1.05
primary_factors["Heat"]=1
primary_factors["Geothermal"]=1
primary_factors["Solar/Wind/Tide"]=1

def total(energy_input):
    return sum([energy_input[key]*primary_factors[key] for key in energy_input])
def ghg_total(energy_input):
    return sum([energy_input[key]*emissions_factors[key] for key in energy_input]) / 1000. # With PJ as energy input, outputs emissions in millions of tons CO2e.

# All values in PJ.

# Following are all top-level values

# Includes Industry and non-energy use in Industry
# When two values are added, the first is Industry and the second is non-energy use in Industry.
industry_world = total({
    "Oil":245+364,
    "Oil Products":13187+24631,
    "Coal":34232+2105,
    "Natural Gas":23764+7786,
    "Biofuel":8671,
    "Geothermal":24,
    "Electricity":32201,
    "Heat":5764
})

# Includes non-energy use in Transportation as the second value when there is a sum.
transportation_world = total({
    "Oil Products":108376+461,
    "Coal":3,
    "Natural Gas":4384,
    "Biofuel":3500,
    "Electricity":1309
})

residential_world = total({
    "Oil Products":8991,
    "Coal":3163,
    "Natural Gas":18446,
    "Biofuel":29422,
    "Geothermal":298,
    "Solar/Wind/Tide":1072,
    "Electricity":20791,
    "Heat":4244
})

commercial_world = total({
    "Oil Products":3544,
    "Coal":1394,
    "Natural Gas":7968,
    "Biofuel":1273,
    "Geothermal":150,
    "Solar/Wind/Tide":191,
    "Electricity":16694,
    "Heat":1633
})

# Includes Agriculture, Fishing, Forestry
# Fishing is the second term when there is a sum
agriculture_world = total({
    "Oil Products":4481+257,
    "Coal":688,
    "Natural Gas":414,
    "Biofuel":450,
    "Geothermal":91,
    "Electricity":2310+27,
    "Heat":145
})

# Other categories. When there is a sum, the second term is non-energy use
other_world = total({
    "Oil Products":863+1431,
    "Coal":1107+12,
    "Natural Gas":136,
    "Biofuel":133,
    "Geothermal":3,
    "Solar/Wind/Tide":48,
    "Electricity":3606,
    "Heat":332
})

##################################################################
# Transportation

transportation_road = total({
    "Oil Products":82077,
    "Natural Gas":1834,
    "Biofuel":3464,
    "Electricity":190
})
road_ghg = ghg_total({
    "Oil Products":82077,
    "Natural Gas":1834,
    "Biofuel":3464,
    "Electricity":190
})

# For the following, the 0.6 comes from iea_transport, the CO2 chart. I am assuming the following:
# - The fact that 60% of emissions are passenger vehicles can be translated to 60% of energy (2018 figure).
# - Cars, buses, and 2,3-wheelers are in passenger transportation

# The car, bus, 2/3-wheeler numbers come from eyeballing Figure 8.6 of https://www.eia.gov/outlooks/ieo/pdf/transportation.pdf, though the source is eia_outlook
transportation_bus = transportation_road*0.6*0.07
transportation_23wheeler = transportation_road*0.6*0.04
transportation_car = transportation_road*0.6*0.89
transportation_truck = transportation_road*0.4
bus_ghg = road_ghg*0.6*0.07
ghg_23wheeler = road_ghg*0.6*0.04
car_ghg = road_ghg*0.6*0.89
truck_ghg = road_ghg*0.4

transportation_aviation = total({
    "Oil Products":8180+5361 # First is bunkers, second is domestic
})
aviation_ghg = ghg_total({
     "Oil Products":8180+5361 # First is bunkers, second is domestic
})

transportation_rail = total({
    "Oil Products":1208,
    "Coal":2,
    "Electricity":926
})
rail_ghg = ghg_total({
    "Oil Products":1208,
    "Coal":2,
    "Electricity":926
})

transportation_pipeline = total({
    "Oil Products":10,
    "Natural Gas":2538,
    "Electricity":121
})
pipeline_ghg = ghg_total({
    "Oil Products":10,
    "Natural Gas":2538,
    "Electricity":121
})

transportation_marine = total({
    "Oil Products":9080+2281 # First is bunkers, second is domestic
})
marine_ghg = ghg_total({
    "Oil Products":9080+2281 # First is bunkers, second is domestic
})

# Including the non-energy use in Transportation here as the second term in the sum.
transportation_other = total({
    "Oil Products":180+461,
    "Electricity":72
})
other_transpo_ghg = ghg_total({
    "Oil Products":180+461,
    "Electricity":72
})

it_energy_mfg = total({
    "Electricity":1817*3.6*0.18 # greenpeace_data. See table on p. 16 for total, pie chart on p. 15 to break out components
})

it_energy_other = total({
    "Electricity":1817*3.6*0.82
})
it_ghg = ghg_total({
    "Electricity":1817*3.6
})

cycling_distance = (250+200) * 10**9 # passenger-km traveled. See reference 'cycling_scenario', p. 27 (add up OECD and non-OECD, estimate pixel thickness of the green bars representing bikes.)
cycling_energy = cycling_distance * 1322. / 10**12 # See the current (as of March 4, 2020) plot, img2019_05_23_active.jpg
ag_ghg = 2379470+1098395+7463342+604298+801404+626871+394203+1100000 # See world_food_ghg.jpg
# The 0.76... is the portion of food reported in FAOSTAT that is actually eaten. To estimate that, I took the overall food loss rates (see food_loss.py) but skipped agricultural production and postharvest, which I don't think are included in the 2917 calories. The 2917 is the number of kcal per day. The 365 converts to kcal per year. The 4.184 converts to kJ and 7.7B is world population.
energy_produced = 0.7647801856219506*2917*365*4.184*7.7*10**9
# Calories burnt. See https://www.choosemyplate.gov/resources/physical-activity-calories-burn
# For cycling, averaging the figures for <10 MPH and >10 MPH to get 10 MPH.
# The -86 is for sitting as the baseline. https://www.startstanding.org/calculate-calories-burned-sitting-vs-standing/
# For the above, settings are male, 5'10", 157 lb
# Final figure is kJ/kM, directly by person.
calories_cycling = ((290+590)/2 - 86) * 4.184 / 16.0934 # (290+590)/10 is kcal for one hour, or 10 miles. 4.184 to convert to kJ. 16.0934 converts from 10 miles to 1 km.
cycling_ghg = calories_cycling * cycling_distance / energy_produced * ag_ghg / 1000.

# Note: figures differ by about 50 PJ. I'm not sure why, but it seems to be inherent in the Sankey diagram.
#print(transportation_truck+transportation_car+transportation_bus+transportation_23wheeler+transportation_aviation+transportation_rail+transportation_pipeline+transportation_marine+transportation_other)
#print(transportation_world)

transport_chart = [
    ["<b>Mode</b>","<b>Energy (PJ)</b>"],
    ["Industry - Other",industry_world - it_energy_mfg - (0.59+0.64)/(0.59+0.64+3.38+0.43)*transportation_car - (0.83+0.35)/(0.83+0.35+6.44+0.84)*transportation_bus - (0.24+0.12)/(0.24+0.12+3.47+0.34)*transportation_aviation - (0.31+0.7)/(0.31+0.7+0.2+1.07)*transportation_rail],
    ["Residential",residential_world],
    ["Commercial - Other",commercial_world - it_energy_other],
    ["Agriculture",agriculture_world],
    ["Other",other_world],
    ["Transportation Overall",transportation_world],
    ["Road Transportation Overall",transportation_road],
    ["Cars",transportation_car + (0.59+0.64)/(0.59+0.64+3.38+0.43)*transportation_car], # For the embodied and infrastructure energy, using the Conventional Gas Sedan figure
    ["Buses",transportation_bus + (0.83+0.35)/(0.83+0.35+6.44+0.84)*transportation_bus], # Urban Diesel Bus, off peak
    ["2-, 3-Wheelers", transportation_23wheeler],
    ["Trucks",transportation_truck],
    ["Aviation",transportation_aviation + (0.24+0.12)/(0.24+0.12+3.47+0.34)*transportation_aviation], # Small Aircraft
    ["Rail",transportation_rail + (0.31+0.7)/(0.31+0.7+0.2+1.07)*transportation_rail], # Caltrain
    ["Shipping",transportation_marine],
    ["Pipeline",transportation_pipeline],
    ["Other and Unspecified",transportation_other],
    ["Information Technology",it_energy_mfg + it_energy_other],
    ["Space",0.09], # See Space page.
    ["Cycling",cycling_energy]
]
transport_im = {
    "filename":"world_transportation_energy.jpg",
    "status":"Done",
    "details":"Show world primary energy in transportation by mode, and also how it fits into the context of world overall energy. Note that Transportation Overall and Road Transportation Overall are aggregate categories. Most of the numbers come from the IEA Sankey diagram. I used the IEA Transport page to break down road transportation into passenger and freight, and then the EIA transportation scenario to break down passenger into car, bus, and 2/3-wheelers. Yes, there is a slight difference (about 50 PJ) between the figures for Transportation Overall and the sum of the individual pieces; I am not sure why but it's small enough to not worry about. These figures take a more expansive view of the transportation sytem than most. Information technology, for instance, would typically fall under the commercial and industrial (and a bit of residential) categories, and I compenstated that by subtracting out figures from Industry and Commercial. IT figures are from Cook et al. Space transportation energy is based on Kyle and estimates of the energy requirements of a Falcon Heavy launch (see Space page). Cycling energy is calculated from total cycling distance traveled (Mason et al.) and energy intensity of cycling (see Short Range Transportation page). I have also included estimates of energy that goes into manfacture of vehicles and infrastructure for cars, rail, air, and buses; see Chester and Horvath for that.",
    "table":transport_chart,
    "references":["iea_sankey","iea_transport","eia_outlook","greenpeace_data","spacelaunchreport","cycling_scenario","chester2"],
    "source_file":"world_energy.py"
}
helper.save_image(transport_im)

transport_ghg_table = [
    ["<b>Mode</b>","<b>World Emissions (millions of tons CO<sub>2</sub>e)</b>"],
    ["Aviation",aviation_ghg + (18.80+11.1)/(18.8+11.1+232.49+31.1)],
    ["Buses",bus_ghg + (66.54+30)/(490.6+66.54+30+76.63)*bus_ghg],
    ["2,3-wheelers",ghg_23wheeler],
    ["Cars",car_ghg + (47.89+58.51)/(47.89+58.81+231.99+38.9)*car_ghg],
    ["Trucks",truck_ghg],
    ["Rail",rail_ghg + (32.19+51.52)/(32.19+51.52+73.87+13.42)*rail_ghg],
    ["Pipelines",pipeline_ghg],
    ["Shipping",marine_ghg],
    ["Other Transportation",other_transpo_ghg],
    ["Information Technology",it_ghg],
    ["Space",ghg_total({"Oil Products":0.09})],
    ["Cycling",cycling_ghg],
    ["Total world emissions",33000/0.76]
]

helper.save_image({
    "filename":"world_transportation_ghg.jpg",
    "status":"Done",
    "details":"World greenhouse gas emissions in transportation. For complex reasons that I won't go into here, I do not (yet) have figures across the full range of categories portrayed in world_transportation_energy.jpg, but at least I have them for the transportation categories, which are the same across the two plots. The derivation of energy inputs into transportation modes is the same as in world_transportation_energy.jpg. Emissions intensity of energy are given by the EPA, Hanova and Dowlatabadi, Staffell, and Fridleifsson et al. Emissions intensity of the food that power cycling is determined from overall emissions in world agriculture and food distribution (see the Food Distribution page). Embodied emissions and emissions from infrastructure are included for cars, buses, rail, and air, all from Chester and Horvath. Total world emissions are shown for comparison.",
    "table":transport_ghg_table,
    "references":["epa_biofuel","hanova","staffell","coal_intensity","chester2"],
    "source_file":"world_energy.py"
})

# A few more values to export that are helpful

ghg_car_embodied = car_ghg + (47.89)/(47.89+58.81+231.99+38.9)*car_ghg # Based on the Chester and Horvath stuff, but not including infrastructure.
transportation_car_embodied = transportation_car + (0.59)/(0.59+0.64+3.38+0.43)*transportation_car
ghg_car_all = car_ghg + (47.89+58.81)/(47.89+58.81+231.99+38.9)*car_ghg # Based on the Chester and Horvath stuff, but not including infrastructure.
transportation_car_all = transportation_car + (0.59+0.64)/(0.59+0.64+3.38+0.43)*transportation_car
full_aviation_energy = transportation_aviation + (0.24+0.12)/(0.24+0.12+3.47+0.34)*transportation_aviation
full_aviation_ghg = aviation_ghg + (18.80+11.1)/(18.8+11.1+232.49+31.1)
full_rail_energy = transportation_rail + (0.31+0.7)/(0.31+0.7+0.2+1.07)*transportation_rail
full_rail_ghg = rail_ghg + (32.19+51.52)/(32.19+51.52+73.87+13.42)*rail_ghg
full_bus_energy = transportation_bus + (0.83+0.35)/(0.83+0.35+6.44+0.84)*transportation_bus
full_bus_ghg = bus_ghg + (66.54+30)/(490.6+66.54+30+76.63)*bus_ghg