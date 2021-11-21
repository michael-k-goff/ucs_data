# Electrification

import helper

# Goal for this module, figure out how much electricity is needed worldwide in a fully electrified energy system.

# Calculations should include the following.

# - Current electricity
# - EVs for all cars
# - Electrofuels for the rest of road transportation (trucks)
# - Electrofuels for aviation
# - Diesel in rail, replace with H2?
# - For shipping, ammonia or methanol
# - For industry, assume it is all heat, except for ...
# - For chemicals, including heat and feedstock, derive figures from this paper: https://www.pnas.org/content/116/23/11187
# - For commercial and residential, assume fossil fuels are for heat and replace with heat pumps.
# - For agriculture, forestry, and fishing, it's probably for machinery, as fertilizers are already covered. Replace with hydrogen?
# - Alternately for agriculture, look at a scenario of replacing staple crops with power-to-food, all meat with cultured meat, and possibly greenhouses for fruits and vegetables.

# For cars, see world_energy.py. The transportation_car value, not including embodied energy, is 49312.48632.
# Reverse-engineering some of the calculations in transpo_energy.py in the parent folder.
car_electricity = 49312.48632 * 1205.86345961/1852.84857457 * 1.05/3.16 / 3.6 # The first multiplier is based on primary energy efficiency, and the second converts to in-car efficiency. Last divider converts to TWh.
truck_bus_electricity = [(36938.192+3878.51016) / 1.05 / 0.8 / 3.6, (36938.192+3878.51016) / 1.05 / 0.668 / 3.6] # See hydrogen.py for 66.8% electroylzed H2 efficiency. Low value is 80% efficient.
aviation_electricity = 14218.05 / 1.05 / 0.5 / 3.6 # Electrolyzed jet fuel. The 14218 PJ for aviation from world_energy.py.
rail_electricity = [1268.4 / 1.05 / 0.8 / 3.6, 1268.4 / 1.05 / 0.668 / 3.6] # See world_energy.py again. Only considering the portion of rail provided by oil products, replacing with H2.
shipping_electricity = 11929.05 / 1.05 * (0.008+0.008+0.071+1.43) / 3.6 # Supplying shipping energy (see world_energy.py) with ammonia. For conversion efficiency to ammonia, see figures in ammonia_electrolysis_energy.jpg.
chemicals_electricity = [32000 * 0.8, 18100 * 0.8] # The 0.8 is a rough guess as to how to adjust it to 2017 or so to be in line with other numbers. The 32 PWh comes from industry projection in 2030. See https://www.pnas.org/content/116/23/11187. Using the high-TRL scenario, which requires more than the 18.1 PWh in the low-TRL scenario.
industrial_heat = (245+13187+34232+23764+8671)-(2+2624+4541+5721+90) # Input for oil, oil products, coal, natural gas, biofuels respectively. Subtract the corresponding values for chemicals since that industry is covered separately.
industrial_heat_electricity = industrial_heat * 0.8 / 3.6 # Rough guess of 20% onsite savings, based on the bze reference.
res_comm_heat = (8991+3163+18446+29422)+(3544+1394+7968+1273) # Energy demand for residential and commercial from IEA Sankey: oil products, coal, gas, biomass respectively.
res_comm_electricity = [res_comm_heat*0.8/4.0 / 3.6, res_comm_heat*0.8/2.5 / 3.6] # Assuming primary energy factor of 0.8 for heating options (ignoring energy to produce fuel), coefficient of performance of 2.5 for heat pump, and 3.6 to convert to TWh
# Based on this plot, perhaps I can justify treating all thermal residential and commercial energy as heat. https://www.iea.org/data-and-statistics/charts/shares-of-residential-energy-consumption-by-end-use-in-selected-iea-countries-2017
ag_fuel = (4481+688+414+450)+257 # Oil products + coal + gas + biofuel. Plus for oil products in fishing.
ag_electricity = [ag_fuel / 0.8 / 3.6, ag_fuel / 0.668 / 3.6] # Assume hydrogen
meat_electricity = [371571 * (290.7)/2 / 3.167 / 3600, 371571 * (373)/2 / 3.167 / 3600] # Energy for cultured meat from the Smetana paper. Assume it is primary energy, converting to electricity by dividing by 3.167.
crop_production = (3006166-1009102-84248-143138-303299)+(355087-27293-10812-4613-3988) # All cereal crops and soybeans, as of 2017, from FAOSTAT. Taking total production and subtracting out feed, seed, losses, and other non-food uses. Losses are only up to harvest I think.
crops_electricity = [11.208 * crop_production / 10**3, 25.320512820512818 * crop_production / 10**3]
# For greenhouses, there are 13 tomato entries. I will use figures for the fourth smallest and fourth largest. They vary quite a bit.
greenhouse_electricity_low = 0.38/3.167/3.6 * 181015. / 1000. # 3.14 kJ/gram primary energy, the median for all tomato values in the big LCA spreadsheet. 181015 thousand tons per FAOSTAT production per year. Tomatoes provided 11 kcal/person/day, a bit under half a percent of the total, again from FAOSTAT.
greenhouse_electricity_high = 6.16/3.167/3.6 * 181015. / 1000.
dac_electricity_low = (35+219)/3.167/0.0036 # From https://www.nature.com/articles/s41467-019-10842-5#Tab2, Supplementary Table 3. Assumes 30 GtCO2e/year captured. Taking the heat as an electricity-equivalent value.
dac_electricity_high = (54+243)/3.167/0.0036
desal_electricity = [4028*3.5, 4028*5.0]

# ee for Electrify Everything. We'll see how far we can go with that.
ee = [
    ["<b>Usage (to replace fossil fuels or bioenergy)</b>","<b>Electricity Required, TWh, low</b>","<b>Electricity Required, TWh, high</b>"],
    ["Current Electricity",76938/3.6], # See iea_sankey, world, 2017. Converting from PJ to TWh.
    ["Electrify Passenger Cars",car_electricity],
    ["Electrolyzed Hydrogen for all Trucks and Buses",truck_bus_electricity[0], truck_bus_electricity[1]],
    ["Electrofuel for Aviation",aviation_electricity],
    ["Electrolyzed Hydrogen for all Diesel Rail",rail_electricity[0], rail_electricity[1]],
    ["Electrolyzed Ammonia for all Shipping",shipping_electricity],
    ["Carbon Capture and Utilization in Chemicals",chemicals_electricity[1],chemicals_electricity[0]],
    ["Electrification of Industrial Heat",industrial_heat_electricity],
    ["Heat pumps for residential and commercial heat",res_comm_electricity[0], res_comm_electricity[1]],
    ["Electrolyzed Hydrogen for Farming and Fishing Equipment",ag_electricity[0], ag_electricity[1]],
    ["<b>Usage (for other purposes)</b>","",""],
    ["Replace all Meat with Cultured Meat",meat_electricity[0], meat_electricity[1]],
    ["Replace Staple Crops and Soy with Electrolyzed Protein",crops_electricity[0], crops_electricity[1]],
    ["All Tomatoes from Greenhouses",greenhouse_electricity_low, greenhouse_electricity_high],
    ["Direct Air Capture and Carbon Sequestration, 30 billion tons CO<sub>2</sub>e/yr",dac_electricity_low, dac_electricity_high],
    ["Desalinate All Water Withdrawal",desal_electricity[0], desal_electricity[1]]
]

helper.save_image({
    "filename":"electrification.jpg",
    "status":"Done",
    "details":"The purpose of this plot is to illustrate how much electricity would be required for a clean energy system. I also review several scenarios for agricultural intensification and other concepts reviewed on the site. Bottom line is that a lot of electricity is needed to do this stuff. I give a low and high estimate for some things, or just a single estimate if I have only that. The numbers are based on current demand, not projected future demand.<br><br>For CCU in chemicals, see the new plot in Major Commodities. Since that was crafted with 2030 numbers in mind, I multiplied by 0.8 as a rough guess to get today's numbers. For the transportation figures, all transportation demand figures are in the Energy and Emissions in Transportation page. The scenarios are direct electricity for passenger cars (see the Automobiles page for electricity required for that); hydrogen for trucks, buses, rail, and agricultural equipment, for which I am assuming a production efficiency of 66.8% (high energy estimate) and 80% (low estimate); ammonia for shipping, and synthetic jet fuel for aviation. See the ammonia and synfuels pages for electrolysis efficiency. For industrial heat, I am assuming onsite energy with electricity is 80% what it is with fossil fuels. That's just a ballpark guess. For electrifying residential and commercial heat, I am assuming that all direct usage of fossil fuels and biomass in those sectors is for heat, which isn't quite accurate because some of it is for cooking, but I think that assumption is close enough. Both heating scenarios assume that fossil/biomass heating has an efficiency of 80%. The high energy scenario assumes this is replaced by heat pumps with a coefficient of performance of 2.5, which is fairly conservative, and the low energy scenario assumes a coefficient of performance of 4.0, which could be achieved by a combination of very efficient air-source heat pumps and geothermal heat pumps.<br><br>For cultured meat, I am taking all meat and replacing it with cultured options, and the energy intensities are from the Smetana et al. paper, and I assume it is all electricity. I know there are some lower numbers from the other papers, but I don't trust them very much. For the power-to-food scenarios, I am assuming that cereal and soy crops are replaced with the options described in the Bogdahn (lower energy) and Linder (higher energy) studies. I am considering only the portion of cereal and soy crops that are for human food, not counting feed, seed, losses, and other non-food uses. For the tomato greenhouse scenario, see the new plot in Intensive Farming. These numbers are the same, except I assume the energy all comes from electricity. The Direct Air Capture scenario is outlined in Realmonte et al. For desalination, see the Water Usage and Provision pages.",
    "table":ee,
    "references":["realmonte"],
    "source_file":"electrification.py"
})