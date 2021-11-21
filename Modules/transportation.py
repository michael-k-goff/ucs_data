# Transportation figures

import pandas as pd
import helper

# Parameters by transportation mode
# For speed for cars, walking, biking, see https://www.vtpi.org/tca/tca0502.pdf
# Speed for mass transit from https://www.apta.com/research-technical-resources/transit-statistics/public-transportation-fact-book/
# Assume transit vanpool has the same speed as regular cars
# Subway based on NYC system, reported here: https://ggwash.org/view/4524/average-schedule-speed-how-does-metro-compare
# BRT speed: average of North America values here: https://brtdata.org/indicators/corridors/operating_speed_corridor
# Speed in miles per hour for now.
# Space in square km per passenger
# For cost figures, see notes in transportation.txt. Figures are USD/passenger-mile.
general_parameters = {
    # Assumptions: 4 meter lanes, car needs three seconds of stopping space plus three meters for the car itself
    # 1.14 passengers per car for commute trips, as per https://www.vtpi.org/land.pdf
    # The 4 is the width in meters of a lane, rounded up to add shoulders and right of way.
    # For circuity, see https://conservancy.umn.edu/bitstream/handle/11299/180059/CircuityTrends.pdf?sequence=1&isAllowed=y
    "car":{"speed":32, "space":4*(3+(32 * 1.60934)*1000/1200.)*10**(-6)/1.14, "radius":0, "cost":0.3751820739549839, "circuity":1.339},
    # Space requirement based on 12 meters long (roughly) and 42 passengers, otherwise same formula as for car. See https://www.codot.gov/programs/commuterchoices/documents/trandir_transit.pdf
    # Circuity is a guesstimate based on the table at https://conservancy.umn.edu/bitstream/handle/11299/180057/TransitCircuity.pdf?sequence=1&isAllowed=y
    "bus":{"speed":12, "space":4*(12+(12 * 1.60934)*1000/1200.)*10**(-6)/42, "radius":0, "cost":1.5089555564442871, "circuity":2.5,"istransit":1},
    # Calculations for space based on https://www.theurbanist.org/2016/05/26/the-supply-and-demand-of-street-space/
    # Circuity figure is a guess
    "brt":{"speed":30.79166666666667*0.621371, "space":30.79166666666667*0.004/6000, "radius":0, "cost":2.295604470422855,"circuity":1.5,"istransit":1},
    # From https://www.theurbanist.org/2016/05/26/the-supply-and-demand-of-street-space/, assuming no grade separation.
    # Circuity figure is a guess
    "lightrail":{"speed":15.7, "space":0.00762*15.7*0.621371/9000, "radius":0, "cost":2.115912793855225,"circuity":1.5,"istransit":1},
    # From https://www.theurbanist.org/2016/05/26/the-supply-and-demand-of-street-space/. Using light rail with grade separation.
    # Circuity figure is a guess here too
    "subway":{"speed":17.4, "space":0.00762*17.4*0.621371/32000, "radius":0, "cost":0.8851407814178762,"circuity":1.5,"istransit":1}, # Cost based on heavy rail
    # Same formula as for a car, but using average passengers per vanpool as given in https://www.apta.com/wp-content/uploads/APTA_Fact-Book-2019_FINAL.pdf
    # Circuity guessed to be slightly higher than for cars
    "vanpool":{"speed":32, "space":4*(3+(32 * 1.60934)*1000/1200.)*10**(-6)/5.677349501948896, "radius":0, "cost":0.1524906552750019, "circuity":1.5,"istransit":1},
    # Based on 30 square feet, see https://www.vtpi.org/land.pdf
    # Guessing a low circuity for active transportation
    "bike":{"speed":12, "space":9.2903*10**-6, "radius":0, "cost":0.14, "circuity":1.2},
    # Based on 30 square feet, see https://www.vtpi.org/land.pdf
    # Low circuity guesstimated
    "walk":{"speed":3, "space":2.78709*10**-6, "radius":0, "cost":0.017, "circuity":1.2}
}
for key in general_parameters:
    general_parameters[key]["speed"] *= 1.60934 # Convert miles to km
    functional_radius = general_parameters[key]["speed"]/general_parameters[key]["circuity"]*0.75 # Using a 45 minute radius
    if "istransit" in general_parameters[key]:
        functional_radius = 35./45 * functional_radius + 0.3 # 20 minutes instead of 30, but allow 300 meters of walking
    general_parameters[key]["radius"] = 3.14159 * functional_radius**2
    general_parameters[key]["cost"] /= 1.60934
keys = general_parameters.keys()
df_transpo_params = pd.DataFrame()
df_transpo_params["Mode"] = keys
df_transpo_params["Average Speed (km/h)"] = [general_parameters[keys[i]]["speed"] for i in range(len(keys))]
df_transpo_params["Range (square km reachable in 45 minutes)"] = [general_parameters[keys[i]]["radius"] for i in range(len(keys))]
df_transpo_params["Cost (USD/passenger-km)"] = [general_parameters[keys[i]]["cost"] for i in range(len(keys))]
df_transpo_params["Space Required (square meters per passenger)"] = [10**6*general_parameters[keys[i]]["space"] for i in range(len(keys))]

# General notes on parameter sets
# "type" indicates how travel radius should be calculated. "free" is for modes like walking, biking, cars where one can travel mostly freely.
# "transit" is for buses and many other transit forms

car_parameters = {
    "name":"Car",
    "type":"free",
    "average_vehicle_speed": 32 * 1.60934,
    "circuity":1.339,
    "max_commute_time":0.5,
    "rush_hour_share":0.5,
    # Number of square kilometers taken up by each traveler on the road
    # Assumptions: 4 meter lanes, car needs three seconds of stopping space plus three meters for the car itself
    # 1.14 passengers per car for commute trips, as per https://www.vtpi.org/land.pdf
    "area_per_traveler":4*(3+(32 * 1.60934)*1000/1200.)*10**(-6)/1.14,
    # Proportion of city given to roads
    # See p. 7 of https://www.vtpi.org/land.pdf. 25% seems reasonable for large cities.
    "road_share":0.25,
    # Roughly 100 square meters per person for a single family home, as per https://www.census.gov/const/C25Ann/sftotalmedavgsqft.pdf
    # Note that there are about 2.5 people per SFH
    "personal_space":50*10**-6
}

pedestrian_parameters = {
    "name":"Pedestrian",
    "type":"free",
    "average_vehicle_speed":3*1.60934, # Walking speed of 3 MPH
    "circuity":1.2, # Look up a value to put here
    "max_commute_time":0.5,
    "rush_hour_share":0.5,
    "area_per_traveler":2.78709*10**-6, # Based on 30 square feet, see https://www.vtpi.org/land.pdf
    "road_share":0.15,
    # Calculations on building form
    # Desired personal living space, square km per person
    "personal_space":50*10**-6
}

bicycle_parameters = {
    "name":"Bicycle",
    "type":"free",
    "average_vehicle_speed":10*1.60934, # 10 MPH
    "circuity":1.2, # Look up a value to put here
    "max_commute_time":0.5,
    "rush_hour_share":0.5,
    "area_per_traveler":9.2903*10**-6, # Based on 30 square feet, see https://www.vtpi.org/land.pdf
    "road_share":0.15,
    # Calculations on building form
    # Desired personal living space, square km per person
    "personal_space":50*10**-6
}

# Unrealistic, as it does not account for headway between buses
bus_parameters = {
    "name":"Bus",
    "type":"transit",
    "average_vehicle_speed":15*1.60934, # 10 MPH
    # Guesstimate based on the table at https://conservancy.umn.edu/bitstream/handle/11299/180057/TransitCircuity.pdf?sequence=1&isAllowed=y
    "circuity":2.5,
    "max_commute_time":0.5, # Transit trips are typically longer than auto trips by time.
    "wait_time":1./12,
    "transfer_time":1./12,
    "rush_hour_share":0.5,
    "area_per_traveler":1.85806*10**-6, # Based on 20 square feet. Seems quite low, but oh well. See https://www.vtpi.org/land.pdf
    "road_share":0.15,
    "personal_space":50*10**-6
}

brt_parameters = {
    "name":"Bus Rapid Transit",
    "type":"transit",
    "average_vehicle_speed":30*1.60934, # See https://en.wikipedia.org/wiki/Bus_rapid_transit and look for a better source
    "circuity":1.5, # Wild guess
    "max_commute_time":0.5, # 10 minutes of walking and transfers
    "wait_time":1./12,
    "transfer_time":1./12,
    "catchment_radius":0.75, # Kilometers one is willing to walk to the bus stop
    "num_routes":2, # Number of routes available to a typical rider at nearest stop. Treat different directions as different routes.
    "rush_hour_share":0.5,
    "area_per_traveler":0.004*(30*1.60934)/6000,
    "road_share":0.15, # Seems unrealistically high
    "personal_space":50*10**-6
}

# Assuming grade separated rail, as described in https://www.theurbanist.org/2016/05/26/the-supply-and-demand-of-street-space/
light_rail_parameters = {
    "name":"Light Rail",
    "type":"transit",
    "average_vehicle_speed":25*1.60934, # Guesstimate based on https://www.lightrailnow.org/myths/m_lrt012.htm
    "circuity":1.5, # Wild guess
    "max_commute_time":0.5, # 10 minutes of walking and transfers
    "wait_time":1./12,
    "transfer_time":1./12,
    "catchment_radius":0.75, # Kilometers one is willing to walk to the bus stop
    "num_routes":2, # Number of routes available to a typical rider at nearest stop. Treat different directions as different routes.
    "rush_hour_share":0.5,
    # For right of way for a single direction at 7.5 m, see http://www.trolleycoalition.org/pdf/lrtreport.pdf, p. 29
    "area_per_traveler":0.0075*(25*1.60934)/32000,
    "road_share":0.15, # Seems unrealistically high
    "personal_space":50*10**-6
}

# Hybrid system with 75% driving, 20% light rail, 5% walking
# Urban physical characteristics determined by the car still.
car_rail_parameters = {
    key: car_parameters[key] for key in car_parameters
}
car_rail_parameters["area_per_traveler"] = 0.75*car_parameters["area_per_traveler"] + 0.2 * light_rail_parameters["area_per_traveler"] + 0.05 * pedestrian_parameters["area_per_traveler"]
car_rail_parameters["name"] = "70% car, 20% light rail, 5% walking"

def get_city_characteristics(parameters):
    # Define the commutershed
    # For now we are using the same formula for transit, until we have a better one
    if parameters["type"] == "free":
        max_commute_radius = parameters["max_commute_time"] * parameters["average_vehicle_speed"] / parameters["circuity"] # Max commuting radius, in km
        max_commute_area = 3.14159 * max_commute_radius**2
    if parameters["type"] == "transit":
        # Travel radius for a transfer.
        # Assume all territory within circuitious radius can be reached.
        max_commute_radius2 = (parameters["max_commute_time"]-parameters["wait_time"]-parameters["transfer_time"]) * parameters["average_vehicle_speed"] / parameters["circuity"]
        max_commute_area2 = 3.14159 * max_commute_radius2**2
        # For the extended radius, ignore circuity
        extended_radius = (parameters["max_commute_time"]-parameters["wait_time"]) * parameters["average_vehicle_speed"] - max_commute_radius2
        extended_area = extended_radius * parameters["catchment_radius"] * parameters["num_routes"]
        max_commute_area = max_commute_area2 + extended_area

    # Share of population on the road at peak commuting time.
    # Assume one hour (8 AM to 9 AM) of peak traffic, during which half the population travels.
    # Each person is out for 30 minutes, or half the rush hour.
    pop_share_on_road = parameters["rush_hour_share"]*parameters["max_commute_time"]
    # Calculate the population this hypothetical city can support
    population = max_commute_area / parameters["area_per_traveler"] * parameters["road_share"] / pop_share_on_road
    population_density = population/max_commute_area
    far = 0
    if "personal_space" in parameters:
        # The 68/40 term accounts for the fraction of non-road space that is residential
        far = population_density * parameters["personal_space"]/(1-parameters["road_share"])*(68./40.)

    #print "City Area: " + str(max_commute_area) + " square kilometers"
    #print "Population: " + str(population)
    #print "Population Density: " + str(population_density) + " people per square kilometer"
    #if "personal_space" in parameters:
    #    print "Required Floor-Area Ratio: " + str(far)
    #print ""
    return [parameters["name"], max_commute_area, population/float(10**6), population_density, far]
    
city_table = [
    ["<b>Transportation Mode</b>","<b>City Area (square km)</b>","<b>Population (millions)</b>","<b>Population Density (people per square km)</b>","<b>Residential floor-area ratio</b>"],
    get_city_characteristics(car_parameters),
    get_city_characteristics(car_rail_parameters),
    get_city_characteristics(light_rail_parameters),
    get_city_characteristics(brt_parameters),
    get_city_characteristics(bicycle_parameters),
    get_city_characteristics(pedestrian_parameters),
]

city_im = {
    "filename":"transport_urban_form.jpg",
    "status":"Done",
    "table":city_table,
    "details":"Express the maximum size and population density of a large metro in terms of its transportation infrastructure. This is a simplified model and assumes the following. Each city is a 30 minute commutershed around a central business district, using the predominant form of transportation; uniform population density; 25% of the city's surface area for the car and mostly car scenarios is for roads, and 15% is for roads or rail in the other scenarios (not including parking, vehicle maintenance facilities, etc.); the road network must accomodate 25% of the population traveling at peak; personal space is 50 square meters per person. There are various other simplifying assumptions, such as ignoring space requirements for freight and emergency vehicles. These figures may be revisited later as needed. These figures are calculated from the data portrayed in the speed and space plots, as well as the urban land use plot, and there are no additional references.",
    "references":[],
    "source_file":"transportation.py"
}
helper.save_image(city_im)

######################################### Transportation safety

# References put after names in the table if applicable

safety_table = [
    ["<b>Mode</b>","<b>Deaths per billion journeys</b>","<b>Deaths per billion hours</b>","<b>Deaths per billion km</b>","<b>Typical Occupancy</b>"],
    ["Air",117,30.8,0.05,134.4], # airplane_occupancy
    ["Bicycle",170,550,44.6,1], # ~
    ["Bus",4.3,11.1,0.4,20.29], # rail_occu
    ["Car",40,130,3.1,1.67], # car_occu
    ["Pedestrian",40,220,54.2,1], # ~
    ["Motorcycle",1640,4840,108.9,1], # ~
    ["Rail",20,30,0.6,24.], # Based on light rail, rail_occu2
    ["Space Shuttle",103703703,438019,16.2,7.], # ~
    ["Van",20,60,1.2,2.44], # car_occu
    ["Water",90,50,2.6,323/2.] # ferry_cap. I only have the capacity, so I'm assuming the actual number of passengers is half that.
]

for i in range(1,len(safety_table)):
    safety_table[i][1] /= safety_table[i][4]
    safety_table[i][2] /= safety_table[i][4]
    safety_table[i][3] /= safety_table[i][4]

helper.save_image({
    "filename":"transportation_deaths.jpg",
    "status":"Done",
    "details":"Estimates of the safety of various modes. The original paper (first source) reported metrics on a vehicle basis (deaths per billion vehicle-journeys, vehicle-hours, vehicle-km) as opposed to passengers. I converted it to a passenger basis, which I think is more useful information, based on guessed capacity factors. Capacity factors for air, bus, car, rail, and feries are taken from the second, third, fourth fifth, and sixth sources respectively, and the others were guessed from common sense. I didn't find actual load for ferries, just a capacity factor of 323, so I assumed the load was half that. The space shuttle numbers are a good comparision, but they are extreme so leave that off if it is necessary for visual presentation. For a graphic, don't show the occupancy; that is presented only for your information and as an intermediate calculation.",
    "table":safety_table,
    "references":["transpo_deaths","airplane_occupancy","rail_occu","car_occu","rail_occu2","ferry_cap"],
    "source_file":"transportation.py"
})

######################################### Some other plots

# Revised figure for the cost of driving is $2.08 per passenger-km for vehicles, based on the VTPI plot, and 1.67 passengers per car.

helper.save_image({
    "filename":"commuter_cost.jpg",
    "status":"Done",
    "details":"The cost of driving here, 23 cents per passenger-km, I think is much too small and also inconsistent with the figure from VTPI. I would like to revise it to $1.25/passenger-km, which is the same figure reported by VTPI except for the cost of travel time, which isn't assessed for the other modes, and assuming 1.67 passengers per car on average. I'm not 100% about the other figures either, but I am leaving them for now. While we're at it, put the numbers in an appropriate order and change BRT to Bus Rapid Transit. See Cities/Energy and Pollution/Transportation for source details.",
    "references":[],
    "source_file":"transportation.py"
})

######################################### Weight

# Average human body mass: https://www.livescience.com/36470-human-population-weight.html
average_human_weight = 62 # In kilograms
carry_weight = 20 # From https://www.thedoctorwillseeyounow.com/content/fitness/art4498.html. A rather generous value.
gasoline_weight = 2.72155 # Pounds per gallon, converted to kg. https://www.autoblog.com/2009/10/29/greenlings-how-does-weight-affect-a-vehicles-efficiency/
diesel_weight = 3.17515 # Pounds per gallon, converted to kg. https://www.autoblog.com/2009/10/29/greenlings-how-does-weight-affect-a-vehicles-efficiency/
kerosene_weight = 6.82*0.453592 # https://coolconversion.com/density-volume-mass/--1--gallon--of--kerosene--in--pound
teu_weight = 24000 # https://www.marineinsight.com/maritime-law/teu-in-shipping-everything-you-wanted-to-know/

# See transportation_deaths.jpg for occupancy figures.
weight_table = [
    ["<b>Vehicle</b>","<b>Typical Vehicle Weight</b>","<b>Number of passengers</b>","<b>Passenger Weight</b>","<b>Cargo Weight</b>","<b>Fuel Weight</b>","<b>Passenger Weight by Share (Percent)</b>","<b>Cargo Weight by Share</b>","<b>Fuel Weight by Share</b>","<b>Vehicle Weight by Share</b>"],
    ["Compact Car",1324,1.67,"","",12*gasoline_weight,"","","","","",""], # Weight: https://cars.lovetoknow.com/List_of_Car_Weights
    ["Midsize Car",1524,1.67,"","",16.25*gasoline_weight,"","","","","",""], # Weight: https://cars.lovetoknow.com/List_of_Car_Weights
    ["Large Car",1760,1.67,"","",18.5*gasoline_weight,"","","","","",""], # Weight: https://cars.lovetoknow.com/List_of_Car_Weights
    ["Compact SUV",1628,1.67,"","",16.5*gasoline_weight,"","","","","",""], # Weight: https://cars.lovetoknow.com/List_of_Car_Weights
    ["Midsize SUV",1997,1.67,"","",25.25*gasoline_weight,"","","","","",""], # Weight: https://cars.lovetoknow.com/List_of_Car_Weights
    ["Large SUV",2541,1.67,"","",34*gasoline_weight,"","","","","",""], # Weight: https://cars.lovetoknow.com/List_of_Car_Weights
    # Occupancy I believe is for municipal buses rather than charter buses, but oh well.
    # Fuel tank of 183 gallons is the media of five values reported here: https://gogocharters.com/charter-bus-comparison-chart
    ["Charter Bus",18144,20.29,"","",183*diesel_weight,"","","","","",""], # Weight: https://www.dot.state.pa.us/public/pdf/InfoBridge/Approximate%20vehicle%20weights.pdf
    # I'm assuming the figures here are per-car
    ["Light Rail",37415,24,"","","","","","","","",""], # Weight: the average on Table 2.1 of http://onlinepubs.trb.org/onlinepubs/tcrp/tcrp_rpt_57-a.pdf (single far)
    # For fuel weight, see https://modernairliners.com/boeing-747-jumbo/boeing-747-specs/
    ["Boeing 747-400ER",182840,134.4,"","",57285*kerosene_weight,"","","","","",""], # Weight: http://www.boeing.com/resources/boeingdotcom/company/about_bca/startup/pdf/historical/747-400-passenger.pdf
    ["Bicycle",8.16466,1,"","","","","","","","",""], # Weight: https://bicycleuniverse.com/how-much-does-bike-weigh/. Using the Road Bike value (18 pounds)
    ["Pedestrian",0,1,"","","","","","","","",""],
    # Vehicle Weight: https://www.dot.state.pa.us/public/pdf/InfoBridge/Approximate%20vehicle%20weights.pdf
    # Fully loaded weight of an extra 45000 lb (~20412 kg): https://www.tcsfuel.com/blog/truck-weight-classification/
    # Fuel tank, taking the median of the 120-150 gallons given. https://www.internationalusedtrucks.com/maintenance-tips/how-many-gallons-does-a-semi-truck-hold/
    ["<b>Primarily Freight Modes</b>"],
    ["Tractor Trailer",36287,"","",20412,135*diesel_weight,"","","","",""],
    ["Freight Train",27216,"","",99790,"","","","","",""], # Weight: https://web.engr.uky.edu/~jrose/papers/REES%202012%20Introduction.pdf (for a single car)
    ["Boeing 747-400ER Freighter",182840,"","",103419,57285*kerosene_weight,"","","","","",""] # Cargo capacity of a 747-400EF for cargo. http://www.boeing.com/commercial/aeromagazine/aero_21/747ER.pdf
    
    # For stats, see https://boatinggeeks.com/how-much-does-a-cargo-ship-weigh/
    #["Large Cargo Ship",220000*907.185-teu_weight*23756,"","",teu_weight*23756,"","","",""]
    # Neo-panamax ship: Deadweight is 165,517 tons, carrying capacity is 14,000 TEUs. https://www.ship-technology.com/features/feature-the-worlds-biggest-cargo-container-ships/
    # Some weight statistics here if we can't find anything better. https://boatinggeeks.com/how-much-does-a-cargo-ship-weigh/
]

for i in range(1,len(weight_table)):
    if len(weight_table[i])>2 and weight_table[i][2]:
        weight_table[i][3] = weight_table[i][2] * average_human_weight
        weight_table[i][4] = weight_table[i][2] * carry_weight
        
    total_weight = 0
    if len(weight_table[i])>1 and weight_table[i][1]:
        total_weight += weight_table[i][1]
    if len(weight_table[i])>3 and weight_table[i][3]:
        total_weight += weight_table[i][3]
    if len(weight_table[i])>4 and weight_table[i][4]:
        total_weight += weight_table[i][4]
    if len(weight_table[i])>5 and weight_table[i][5]:
        total_weight += weight_table[i][5]
    if len(weight_table[i])>3 and weight_table[i][3]:
        weight_table[i][6] = weight_table[i][3] / float(total_weight) * 100.
    elif len(weight_table[i])>3:
        weight_table[i][6] = 0
    if len(weight_table[i])>4 and weight_table[i][4]:
        weight_table[i][7] = weight_table[i][4] / float(total_weight) * 100.
    elif len(weight_table[i])>4:
        weight_table[i][7] = 0
    if len(weight_table[i])>5 and weight_table[i][5]:
        weight_table[i][8] = weight_table[i][5] / float(total_weight) * 100.
    elif len(weight_table[i])>5:
        weight_table[i][8] = 0
    if len(weight_table[i])>8:
        weight_table[i][9] = 100. - float(weight_table[i][6]) - float(weight_table[i][7]) - float(weight_table[i][8])

helper.save_image({
    "filename":"vehicle_weight.jpg",
    "status":"Done",
    "details":"This is an analysis that John requested. The sources used are shown where the image is shown, which for now is under Transportation Speed and Space under Mobility under Cities. I would like to have a cargo ship figure but haven't found anything yet that looks reliable. The weights of light rail and freight trains are on a per-car basis. All weights are in kilograms. The fuel weight assumes the vehicle has a full fuel tank and is not estimated where liquid fuels are not the main source of energy. Passenger weight and cargo weight is given both in absolute terms and as a percentage of total weight. We assume 62 kg of weight per passenger and that each person can comfortably carry 20 kg.",
    "reference":[],
    "table":weight_table,
    "source_file":"transportation.py"
})