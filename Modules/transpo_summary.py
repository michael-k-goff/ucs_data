# Figures for the summary section in Transportation

import helper
import world_energy

# Fuel economy: see IEA report. Says current world fuel economy is 7.2 liters of gasoline per 100 km, target in 2030 is 4.4. https://www.iea.org/reports/fuel-economy-in-major-car-markets
# For energy savings in EVs, take life cycle energy comparison of EVs vs ICE as in ev_ice and apply to operating and embodied energy in cars.
# For GHG savings for EVs, take the US electricity figure in automobile_lca.jpg and apply the ratio between that and the ICE car to all car energy except infrastructure

vmt_work = (6259.+1326.)/33587. # Share of VMT that is for work, including commuting and work-related travel.

# The compact cities scenario is based on Creutzig et al. It would be good to replace it with something else. They say 190 EJ primary energy saved.
# For emissions, see ag_summary.py also for the emissions intensity of world energy.
emissions_from_energy = 33*0.72/0.76
world_primary = 13864.9 * 0.042 # EJ, from BP

transpo_savings_table = [
    ["<b>Method</b>","<b>Potential Energy Savings (PJ)</b>","<b>Potenial GHG Savings (million tons CO<sub>2</sub>e)</b>"],
    ["Reduce fuel consumption of cars 39%", world_energy.transportation_car*(1-4.4/7.2), world_energy.car_ghg*(1-4.4/7.2)],
    ["Convert all cars to electric",world_energy.transportation_car_embodied*(1-1.993/4.154),world_energy.ghg_car_embodied*(1-290.2955979333333/392.612)],
    ["Replace business air travel with electronic communication",world_energy.full_aviation_energy*0.29, world_energy.full_aviation_ghg*0.29],
    ["Improve efficiency in shipping, trucking, and aviation",10003,10003*world_energy.emissions_factors["Oil Products"]/1000.],
    ["Replace 25% of work travel with remote work.",world_energy.transportation_car_all*0.25*vmt_work, world_energy.ghg_car_all*0.25*vmt_work],
    ["Compact Cities","190000",190000*emissions_from_energy / world_primary],
    ["Projected growth in aviation, 2015-50",-18000, -18000*world_energy.full_aviation_ghg/world_energy.full_aviation_energy],
    ["Projected growth in driving, 2015-50",-(69000-50600),-(69000.-50600.)*world_energy.ghg_car_all/world_energy.transportation_car_all],
    ["Projected growth in trucking, 2015-50",-(35200-28600),-(35200.-28600.)*world_energy.truck_ghg/world_energy.transportation_truck],
    ["Projected growth in shipping, 2015-50",13600-20900,(13600-20900)*world_energy.marine_ghg/world_energy.transportation_marine],
    ["Projected growth in rail, 2015-50",-2000,-2000*world_energy.full_rail_ghg/world_energy.full_rail_energy],
    ["Projected growth in buses, 2015-50",-3000,-3000*world_energy.full_bus_ghg/world_energy.full_bus_energy]
]

helper.save_image({
    "filename":"transpo_savings.jpg",
    "status":"Done",
    "table":transpo_savings_table,
    "details":"A summary of potential energy and greenhouse gas savings from various strategy on transportation. The 39% reduction in fuel in cars is based on the target in the IEA report and represents what appears to be a realistic but aggressive movement toward efficiency. The electric vehicle assumes US average carbon intensity of electricity (which is close to the world average) and accounts for manufacturing of the cars. The air travel scenario assumes 29% of air travel is for business, which is true in the US based on the Statista figures cited. The energy savings potential in freight is based on achieving the efficiency gains portrayed in the freight_savings_potential.jpg plot for shipping, trucking, and aviation, but does not include modal shift. For the remote work scenario, the 25% conversion is just a wild guess on my part of what might be possible to get an order of magnitude estimate. That 25% is applied to the share of VMT that is for commuting and work-related travel, as reported by the Bureau of Transportation Statistics data. The number is a snapshot for the US, and it's probably not very representative it is for the world as a whole, but it was the best I could find on the fly. Overall the remote work energy savings is surprisingly low, to me at least. Be sure to note somewhere on the plot that none of these savings potential estimates take the rebound effect into account. See also, world_transportation_energy.jpg and world_transportation_ghg.jpg.<br><br>The compact scenario is from Creutzig et al. (see the Urban Density page) based on 190 EJ savings per year. Because this is such an important figure, I think it's important to study it more carefully and not just site this other paper. Unfortunately my more detailed work has been US-specific, and trying to do my own world estimate of the energy savings potential from urban density would be a major undertaking. Also, while that we will show that compact development is the best solution under any scenario, the extent of the savings reported in Creutzig et al. is probably too high, as I think they have an unrealistic densification scenario.<br><br>The negative values are based on growth projections, see the Energy and Emissions page.",
    "references":["business_travel","iea_fuel_econ","vmt_purpose"],
    "source_file":"transpo_summary.py"
})

#############################
# Model commute comparison

# When I get back: see figures in transport_urban_form.jpg for density comparisons.

baseline_density = 6207.022719881059
rail_density = 63628.56823294021
bike_density = 64583.4903070945
rail_energy = [23540,105120]
bike_energy = 1322
rail_density_dist = 20/(rail_density/baseline_density)**0.5
bike_density_dist = 20/(bike_density/baseline_density)**0.5

model_commute_table = [
    ["<b>Scenario</b>","<b>Energy Consumption, kJ</b>"],
    ["Gasoline Car, 20 km","19920-85700"],
    ["Electric Car, 20 km","18120-41000"],
    ["Rail, 20 km",str(rail_energy[0])+"-"+str(rail_energy[1])],
    ["Bus, 20 km","5020-185860"],
    ["Rail, "+str(round(rail_density_dist,1))+" km",str(rail_energy[0]*rail_density_dist/20)+"-"+str(rail_energy[1]*rail_density_dist/20)],
    ["Cycling, "+str(round(bike_density_dist,1))+" km",str(bike_energy*bike_density_dist/20)]
]

helper.save_image({
    "filename":"model_commute.jpg",
    "status":"Done",
    "table":model_commute_table,
    "details":"This plot shows a typical (on the long side) commute in an American city. Think of the gasoline car, 20 km as a sort of baseline. Comparing to the EV, rail, and bus options, all at 20 km, we see that there is wide variation but they all look reasonably comparable in terms of energy needs. There are shorter commuting ranges for rail and cycling. Those are based on the fact that, due to smaller space requirements, a large city that revolves around mass and active transport can support up to about 10 times the population density. See the figures in transport_urban_form.jpg for details. The 6.2 km commute range is based on the fact that, at the higher density, there are as many destinations in a 6.2 km circle in the higher density city as there are in a 20 km circle in the lower-density city. I think the key moral of the story is that rail and cycling can save energy, but not so much because they modes are so efficient on a per-km basis, but because they enable density. It is also important to convey that changing transportation modes, without changing density or commute distance, doesn't do much good.<br><br>Energy requirements per km for each mode are reported on the Automobile, Mass Transit, and Short Range Transportation pages already. The wide ranges for Rail and Bus figures come from the Bureau of Transportation Statistics. I would have to look more deeply into the numbers, but it would appear that it is denser cities that have lower per-passenger km energy figures due to being able to fill the vehicles better.",
    "references":[],
    "source_file":"transpo_summary.py"
})