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