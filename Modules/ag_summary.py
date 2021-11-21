# coding=utf-8
# Summary stats for the Food and water section

import land_use
import food_dist
import energy_in_ag
import ag_environment
import water
import primary_energy_factors
import helper

######################################### Overall impacts

# Land use
ag_land_use = land_use.herbaceous_crops + land_use.woody_crops + land_use.nonfood_crops + land_use.permanent_meadow_pasture
human_land_use = ag_land_use + land_use.urban_land_2018 + land_use.rural_land_2018 + land_use.rural_highway + land_use.reservoir + land_use.railway + land_use.mining + land_use.planted_forest

# Energy
ag_energy = energy_in_ag.direct_energy + energy_in_ag.machine_energy + energy_in_ag.irrigation_energy + energy_in_ag.fertilizer_energy + energy_in_ag.pesticide_energy + energy_in_ag.animal_energy
# To get energy from other parts of the supply chain, which I don't have directly, I will pull the greenhouse gas figures and convert them to primary energy by assuming that they are all from energy and the energy mix behind them is the same as the world mix.
extra_ghg = food_dist.ghg_table[4][1] + food_dist.ghg_table[5][1] + food_dist.ghg_table[6][1] + food_dist.ghg_table[7][1] # Thousands of tons
# We're going to cheat a bit. World emissions from energy are here: https://www.c2es.org/content/international-emissions/
# Starting with CO2, adjusting to the energy share, then adjusting to all GHGs.
emissions_from_energy = 33*0.72/0.76
world_primary = 13864.9 * 0.042 # EJ, from BP
ag_energy += world_primary* (extra_ghg/1000000./emissions_from_energy)
# Another way to look at it: convert from emissions to primary energy by multiplying by world_primary/emissions_from_energy/1000000.

# Greenhouse gases
ag_ghg = sum([ag_environment.ghg_dict[key] for key in ag_environment.ghg_dict]) + extra_ghg + food_dist.ghg_table[8][1]

# Water. Don't think any calculations are needed here.

ag_impact_table = [
    ["<b>Metric</b>","<b>Total Impact</b>","<b>Share of total human impact</b>"],
    ["Land Use",str(ag_land_use)+" km<sup>2</sup>",float(ag_land_use)/(human_land_use)],
    ["Energy",str(ag_energy)+" exajoules",float(ag_energy)/world_primary],
    ["Greenhouse Gases",str(ag_ghg/1000000.) + " billions of tons CO<sub>2</sub>e",ag_ghg/1000000./(33/0.76)],
    ["Water",str(water.ag_water)+" km<sup>3</sup>",water.ag_water/(water.ag_water+water.industry_water+water.municipal_water)]
]

helper.save_image({
    "filename":"ag_impacts.jpg",
    "status":"Done",
    "table":ag_impact_table,
    "details":"This is a graphic for the Food and Water summary section. Show the overall impacts on four key metrics, both in absolute terms and as a share of all human impacts. Right now I'm thinking that for summary material, we probably won't cite external sources but rather refer to 'Urban Cruise Ship analysis'. Energy figures are computed straight off the land use plot we have. The energy figures include processing, packaging, retail, and transportation, but not cooking or disposal I took the energy figures from the energy_in_ag plot for energy in growing crops or animals, and to get the other aspects of the food system, I took the greenhouse gas figures in world_food_ghg.jpg (processing, packaging, retail, transportation) and assumed they are all from energy at the same emissions intensity of the full world energy system. Total world energy is from BP. Greenhouse gases are taken from food_ghg.jpg figure, and include cookstoves as well. Water is pulled from water_by_sector.jpg.",
    "source_file":"ag_summary.py"
})

#####################################################

# The star attraction of the Food and Water section: impacts of various ag options.

# Vegetarian diet
# To get the 0.28... ha/person saved, go into diet.py, set baseline = "World", run diet_land_use_chart() and subtract the Vegetarian key from the World key
# Assuming world population 7.7 billion, then converting to km^2
# Similar for GHG, but use diet_land_use_chart(1)
# For water, use diet_land_use_chart(2)
# Dividing all by 2 to reflect switching only half of meat to vegetarian
veg_diet = {"Land":0.2892838067709273*7.7*10**9/2 / 100.,"GHG":777.1723058696232*7.7*10**9 / 10**12/2, "Water":365*644.5468215833002*7.7*10**9 / 10**12/2, "Energy":"NA"}

# No till.
# Assumptions: 80% of ag land is converted from conventional to no till.
# For land use, only herbacious crops are counted.
notill_ghgmin = 0 + 0.8*882589.2226*0.66/10**6 + 533245.4818*0.8*0.3/10**6 - 0.8*0.821*(223915.1636+127889.6925)/10**6 # Assuming no soil sequestration. Second term is (direct) energy savings of 66%. Third is methane reduction of 30%, applied only to rice. Last term is an increase of emissions from N2O, applied to crop residues and organic soils
notill_ghgmax = 0.8*1647931300*(1./1.04)*22./6./10**9 + 0.8*882589.2226*0.66/10**6 + 533245.4818*0.8*0.3/10**6 - 0.8*0.2*(223915.1636+127889.6925)/10**6 # 1 ton C per ha per year.
# Energy is based on direct usage and 66% savings.
notill = {"Land":str(0.8*16479313*(0.04/1.04))+"-"+str(0.8*16479313*(12./22.)), "GHG":str(notill_ghgmin)+"-"+str(notill_ghgmax), "Water":"NA","Energy":0.8*0.66*13.030061141210002}

# Organic. Based on the organic_scale reference, I will assume 30% conversion of conventional to organic
# For organic yields, I am using the figures in organic_yield.jpg, throwing out the higher and lowest values. 54-92%
# For organic energy, using the range of values for general crops in organic_energy.jpg: 50-94.5% and applying to energy in crops.
conv = 0.3*(16479313.236693999+1482340.7840000002+1393432.909306)
energy_in_ag = 13.030061141210002+3.4724374896800003+1.1362163181126999+7.728798146790001+1.5220287625+0.707447307
organic = {"Land":str(-conv*(1/0.54))+" to "+str(-conv*(1/0.92)),"Energy":str(energy_in_ag*0.3*0.055)+"-"+str(energy_in_ag*0.3*0.5),
    "GHG":"0-"+str(0.3*0.04*sum([ag_environment.ghg_dict[key] for key in ag_environment.ghg_dict])/10**6),"Water":"NA"}
    
# Expanding GMOs
current_gmo = 191.7 * 10000 # square km, based on the isaaa reference.
potential_gmo = (193743247+17580072+37579575+124922025+4821573)/100. # From FAOSTAT, production for Maize, Potatoes, Rapeseed, Soybeans, Sugarbeet (in that order).
gmo_yield_low = 1.056 # Low estimate from the gmo_yield plot, as a share of yields for conventional crops
gmo_yield_high = 1.245
gmo={"Land":str((potential_gmo-current_gmo)*(1.-1./gmo_yield_low))+"-"+str((potential_gmo-current_gmo)*(1.-1./gmo_yield_high))}

# Precision ag
# I don't readily see good numbers, so I'm going to assume 75% of cropland is non-precision and can be made precision. Will apply to all crops.
precision_land = 0.75*(land_use.herbaceous_crops + land_use.woody_crops + land_use.nonfood_crops)
# For land use, assuming the 15-20% yield gain from precision weeding, which is the best listed. Won't try to stack benefits of different technologies.
# For energy, based on precision_ag plot, assuming 25-33% savings in direct energy, 11-90% on pesticides, and 10-15% on fertilizer.
precision_energy_low = 0.75*(0.25*13.030061141210002+0.11*1.5220287625+0.1*7.728798146790001)
precision_energy_high = 0.75*(0.33*13.030061141210002+0.9*1.5220287625+0.15*7.728798146790001)
precision={"Land":str(precision_land*(1.-1./1.15))+"-"+str(precision_land*(1.-1./1.20)), "Water":str(0.75*water.ag_water*(-0.14))+" to "+str(0.75*water.ag_water*(0.35)), "Energy":str(precision_energy_low)+"-"+str(precision_energy_high), "GHG":str(precision_energy_low/(world_primary/emissions_from_energy))+"-"+str(precision_energy_high/(world_primary/emissions_from_energy))}

# Cultured meat
# Meat production, in tons
beef = 67362625
poultry = 114281475
pork = 120881269 # Really pig meat in general, but whatevs
# Using the figures in alt_meat.jpg for ranges
cultured_meat = {
    "Land":str( ( beef*(194-0.39)+poultry*(14-0.39)+pork*(24.6-0.39) )/1000. )+"-"+str( ( beef*(194-8.3)+poultry*(14-0.83)+pork*(24.6-0.39) )/1000. ),
    "Energy":str( ( beef*(67.1-373)+poultry*(27.9-373)+pork*(39.8-373) )/10**9 )+" to "+str( ( beef*(67.1-34.5)+poultry*(27.9-34.5)+pork*(39.8-34.5) )/10**9 ),
    "GHG":str( ( beef*(40.5-25)+poultry*(5.9-25)+pork*(6.9-25) )/10**9 )+" to "+str( ( beef*(40.5-2.268)+poultry*(5.9-2.268)+pork*(6.9-2.268) )/10**9 ),
    "Water":"NA"
}

# Greenhouses. Plan: get impact of current fruit and vegetable production, then shift it all to greenhouses by mulitplying by appropriate scaling factors.
gh_land = (0.008445565934541363+0.008551921615134543)*7.7*10**9/100 # In km^2
gh_ghg = (98.42622399999999+26.43954825) *7.7*10**9 / 10**12 # In billions of tons CO2e.
gh_water = (1.34*1088901183. + 2.1*868085435) / 10**9 # km^3 of water that goes into vegetables overall. 1.34 liter/kg from ag_environment.py.
# Energy for fruits and vegetables will be tricker.
# Fruits and vegetables account for 15.8% of the world fertilizer market as of 2014/15. Will extrapolate that to all energy https://www.fertilizer.org/images/Library_Downloads/2017_IFA_AgCom_17_134%20rev_FUBC%20assessment%202014.pdf
gh_energy = ag_energy * 0.158 # EJ
# Will assume conversion of 50% of all fruits and vegetables to greenhouses. I'm not finding the actual share but I expect it is well under 50%.
# Greenhouse stats relative to conventional, based on greenhouse.jpg: land: 11-25%, water: 10-50%, energy: 106-164% (ignoring figures for individual crops),
# GHG: 84-132%. I don't trust the Clark and Tilman figure here.
greenhouse = {
    "Land":str(gh_land*0.5*(0.75))+"-"+str(gh_land*0.5*0.89), "Water":str(gh_water*0.5*(0.5))+"-"+str(gh_water*0.5*0.9),
    "Energy":str(-gh_energy*0.5*0.64)+" to "+str(-gh_energy*0.5*0.06), "GHG":str(-gh_ghg*0.5*0.32)+" to "+str(gh_ghg*0.5*0.16)
}

# Power to food. Scenario: replace all cereal crops and soybeans with power-to-food.
p2fcrops = 3313106745 # Tons of crops that are being covered by these calculations
# For energy, taking the primary energy behind electricity, assuming natural gas, and subtracting the figure for wheat.
p2fen_low = -p2fcrops*(primary_energy_factors.primary_factors["Electricity"]*25.320512820512818 - 0.6111111111111112)*3.6 / 10**9
p2fen_high = -p2fcrops*(primary_energy_factors.primary_factors["Electricity"]*11.208 - 0.6111111111111112)*3.6 / 10**9
# Greenhouse gases: going with natural gas
p2fghg_low = -p2fcrops*(11.394230769230768-0.712) / 10**9
p2fghg_high = -p2fcrops*(5.0436000000000005-0.712) / 10**9
# Land
p2fland_low = (728642625+124922025)/100. - p2fcrops*0.006089904250087811 / 1000
p2fland_high = (728642625+124922025)/100. - p2fcrops*0.003673378082191781 / 1000
p2f = {
    "Energy":str(p2fen_low)+" to "+str(p2fen_high), "GHG":str(p2fghg_low)+" to "+str(p2fghg_high),
    "Land":str(p2fland_low)+"-"+str(p2fland_high), "Water":"NA"
}

# Cut food loss in half.
loss_rate = 0.341667111892575
adjustor = 1-(1-loss_rate)/(1-loss_rate/2)

# Cut food miles by 75%.
food_miles = {"GHG":0.75*0.801404, "Energy":0.75*0.801404*(world_primary/emissions_from_energy),"Land":"NA","Water":"NA"}

# Cut overeating by 75%.
overeat = {"GHG":0.75*0.239408, "Land":0.75*3784918, "Water":0.75*343.316,"Energy":"NA"}

# Convert half cattle meat and goat meat to poultry
cattle_kcal = 67362625 * 233 * 10000 # See ESS nutritive factors and FAOSTAT
cattle_tons = 67362625
poultry_kcal = 114281475 * 185 * 10000
poultry_tons = 114281475
goat_kcal = 5978156 * 263 * 10000
goat_tons = 5978156
poultry = {
    "Land":0.5*(cattle_kcal/365.*(45.2-3.56)/10**6+goat_kcal/365.*(31.95-3.56)/10**6),
    "GHG":0.5*(cattle_tons*(40.5-5.9)/10**9 + goat_tons*(50.4-5.9)/10**9),
    "Water":0.5*(cattle_kcal*(10.2-3.)/10**12 + goat_kcal*(4.3-3.0)/10**12),
    "Energy":"NA"
}

ag_options_table = [
    ["<b>Strategy</b>","<b>Land Use Savings, km<sup>2</sup><b>","<b>GHG savings, billions tons CO<sub>2</sub>e</b>","<b>Water Savings, km<sup>3</sup></b>","<b>Energy Savings (EJ)<b>"],
    ["Replace half of meat consumption with plant-based options",veg_diet["Land"],veg_diet["GHG"],veg_diet["Water"],veg_diet["Energy"]],
    ["Convert all cropland to no till",notill["Land"], notill["GHG"], notill["Water"], notill["Energy"]],
    ["Convert 30% of cropland from conventional to organic",organic["Land"], organic["GHG"], organic["Water"], organic["Energy"]],
    ["Convert all Maize, Potatoes, Rapeseed, Soybeans, Sugarbeet to GM",gmo["Land"],"NA","NA","NA"],
    ["Widespread adoption of precision agriculture",precision["Land"],precision["GHG"],precision["Water"],precision["Energy"]],
    ["Replace all beef, poultry, pig meat with cultured meat",cultured_meat["Land"],cultured_meat["GHG"],cultured_meat["Water"],cultured_meat["Energy"]],
    ["Grow half of fruits and vegetables in greenhouses",greenhouse["Land"],greenhouse["GHG"],greenhouse["Water"],greenhouse["Energy"]],
    ["Replace all cereal crops and soybeans with power-to-food",p2f["Land"],p2f["GHG"],p2f["Water"],p2f["Energy"]],
    ["Cut food loss and waste in half",ag_land_use*adjustor, ag_ghg*adjustor/10**6, water.ag_water*adjustor, ag_energy*adjustor],
    ["Cut food-miles by 75%",food_miles["Land"],food_miles["GHG"],food_miles["Water"],food_miles["Energy"]],
    ["Cut overeating by 75%",overeat["Land"],overeat["GHG"],overeat["Water"],overeat["Energy"]],
    ["Replace half of cattle and goat meat with poultry",poultry["Land"],poultry["GHG"],poultry["Water"],poultry["Energy"]]
]

helper.save_image({
    "filename":"ag_options.jpg",
    "status":"Done",
    "table":ag_options_table,
    "details":"This will probably be the most important plot in the Food and Water section, showing overall savings (or cost) of various agricultural measures. I am currently assessing them on land use, greenhouse gases, water, and energy, though data for all categories might not be available for all options. Negative values means that the impact would go up.<br><br>The replacing half of meat with plant-based products is adopted from the Diet analysis. For no-till, land savings are based on yield estimates, energy savings based on fuel savings, and greenhouse gas savings are a sum of soil carbon sequestration, fuel savings, methane reduction, and an increase in nitrous oxide which offsets some of the benefits. For organic farming, I'm not sure what the maximum feasible level is, but I am using a 30% rate (on top of current rates) here. Estimates on the savings/cost of organic farming for land use, energy, and greenhouse gases are taken from the figures in organic_yield.jpg, organic_energy.jpg, and organic_impact.jpg respectively. The figures for GM crops are based on converting all of the five crops listed to GM, assuming current technology and none of the technologies under development. As you can see, I only have land use estimates based on yield changes reported in gmo_yield.jpg. For precision farming, I don't know how widely these techniques are used already, so I made a guess that 75% of cropland is converted from non-precision to precision. All impacts are pulled from precision_ag.jpg. See alt_meat.jpg for estimates of savings/costs for cultured meat. The numbers for greenhouses are relatively small because only fruits and vegetables (and some crops like flowers that we're not really talking about here) are practically grown in greenhouses and they are a small portion of all crops. See greenhouse.jpg for range of impacts. Power-to-food impacts are shown in the power_to_food.jpg graphic. The food loss figure is based on the ~34% loss rate worldwide as shown in food_loss.jpg (I could make the numbers more precise by doing the calculations by crop family, but the numbers are so unreliable to begin with that I'm not bothering). Cutting food miles by 75% does not take into account any impacts that result from growing crops in different climates; see world_food_ghg.jpg for the figure there. For overeating figures, see overeat.jpg.<br><br>A few specific comments here. The power-to-food scenario assumes natural gas electricity, and as you can see both the energy and GHG figures are rather extreme. I'm not sure that's the right assumption to make. Generally speaking, all of these figures should be treated as fuzzy and approximate. The point is to portray the significance of various scenarios on an order of magnitude basis.",
    "source_file":"ag_summary.py"
})

####################################################

# Water savings potential

# US water withdrawal per capita. Adding up the figures in us_water.jpg and dividing by US population.
us_water_per_cap = (53.88531135+4.504259359+163.03760870000002+2.7633493000000002+10.4316436075+20.448784820000004+5.5266986000000005+183.76272845000003)/0.3272
irr = 163.03760870000002/0.3272
# For the vegetarian scenario, run diet_land_use_chart(2) and observe the ~27% water reduction.
# For power system, assuming a 75% savings is possible.
# For wastewater recycling, using treatment figure of 34B gallons/day here. https://www.epa.gov/nutrientpollution/sources-and-solutions-wastewater
wastewater = 34 * 10**9 * 3.78 / 1000. * 365 / 327200000.
water_savings_table = [
    ["<b>Strategy</b>","<b>Savings potential in the US, m<sup>3</sup> per capita</b>"],
    ["Drip Irrigation",str(irr*0.3)+"-"+str(irr*0.5)],
    ["Half of Americans switch to vegetarian diet",irr*0.27426906935/2],
    ["Savings in Power System",183.76272845000003/0.3272 * 0.75],
    ["Industrial Efficiency",6.7384548],
    ["Residential Appliances and Plumbing",13.2251616],
    ["Landscaping",6.20865],
    ["Recycle 75% of municipal wastewater",0.75*wastewater],
    ["Total US water withdrawal",us_water_per_cap]
]

helper.save_image({
    "filename":"water_summary.jpg",
    "status":"Done",
    "details":"Summary of water savings potential. Drip irrigation is based on the 30-50% reduction reported in the Water Usage section, but does not take into account any reduction from the percolation effect. For the vegetarian scenario, I am observing that the average American diet could cut water usage ~27 by going vegetarian. I am applying that to the USGS irrigation water figure rather than reporting the savings directly due to the significantly different manner in which Mekonnen and Hoekstra account for water. For the power system, I am assuming a 75% reduction through widespread use of nonthermal power or dry cooling, though it should be acknowledged that this would be a major undertaking. The industrial efficiency, appliances and plumbing, and landscaping figures are right out of water_savings.jpg. The water treatment figure is based on how much wastewater is currently collected in the US. Somehow or another, put these figures in the context of total US water withdrawal.",
    "table":water_savings_table,
    "references":[],
    "source_file":"ag_summary.py"    
})