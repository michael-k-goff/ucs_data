import helper

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
    "source_file":"transportation2.py"
})