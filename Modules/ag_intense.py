# Calculations related to greenhouses, hydroponics, vertical farming, cellular agriculture.

import helper

#########################

# Impact of greenhouse agriculture relative to conventional

greenhouse_table = [
    ["<b>Metric</b>","<b>Impact, relative to conventional</b>","<b><Source/b>"],
    ["Water","10-50%","Czyzyk et al."], # greenhouse_water
    ["Land use","11%","Smith"], # greenhouse_yield
    ["Energy (grapes)","171%","Ozkan et al."], # grape_energy
    ["Energy (lettuce)","200+%","Kuswardhani et al."], # greenhouse_energy
    ["Energy (tomato)","63%","Kuswardhani et al."],
    ["Energy (pepper)","<50%","Kuswardhani et al."],
    ["Greenhouse gases","300%","Clark and Tilman"], # meat_land_use
    ["Land use","25%","Clark and Tilman"],
    ["Eutrophication","80%","Clark and Tilman"],
    ["Acidification","90%","Clark and Tilman"],
    ["Energy","130%","Clark and Tilman"],
    ["Acidification","80-170%","Bartzas et al."], # bartzas
    ["Eutrophication","78-180%","Bartzas et al."],
    ["Greenhouse gases","84-132%","Bartzas et al."], # Some ozone figures skipped
    ["Energy","106-164%","Bartzas et al."]
]

helper.save_image({
    "filename":"greenhouse.jpg",
    "status":"Done",
    "details":"Show impact of greenhouses relative to conventional growing methods. I think the best approach will be to present ranges of all results for each major impact category: water, land use, energy (all commodities on a single bar), eutrophication, acidification.",
    "table":greenhouse_table,
    "references":["greenhouse_water","greenhouse_yield","grape_energy","meat_land_use","bartzas"],
    "source_file":"ag_intense.py"
})

#########################
# Scenario for all tomato production from greenhouses.
# For greenhouses, there are 13 tomato entries. I will use figures for the fourth smallest and fourth largest in Clark and Tilman. They vary quite a bit.
greenhouse_energy_low = 0.38 * 181015. / 1000. # 0.38 kJ/gram. 181015 thousand tons per FAOSTAT production per year. Tomatoes provided 11 kcal/person/day, a bit under half a percent of the total, again from FAOSTAT.
greenhouse_energy_high = 6.16 * 181015. / 1000.
tomato_intake = 11./2917

greenhouse_scenario_table = [
    ["<b>Energy Scenario</b>","<b>Energy to grow all tomatoes in greenhouses, PJ</b>","<b>Share of caloric intake</b>","<b>Share of world energy</b>"],
    ["Low energy",greenhouse_energy_low,tomato_intake,greenhouse_energy_low/566000],
    ["High energy",greenhouse_energy_high,tomato_intake,greenhouse_energy_high/566000]
]
helper.save_image({
    "filename":"greenhouse_scenario.jpg",
    "status":"Done",
    "table":greenhouse_scenario_table,
    "details":"It is difficult to get price figures on energy requirements of greenhouses, so I crafted this scenario just for tomatoes. Even then, it is a little dicey because there is such wide variation in the energy requirements, as reported in Clark and Tilman. There are 13 tomato studies in their database, and for the scenarios I picked the energy values closest to the 25th and 75th percentiles. FAOSTAT is used for total tomato and food production.",
    "references":["meat_land_use","faostat"],
    "source_file":"ag_intense.py"
})

#########################################

# Impact of hydroponics

hydroponic_table = [
    ["<b>Metric</b>","<b>Impact, relative to conventional</b>","<b>Source</b>"],
    ["Land use","9%","Barbosa et al."], # hydroponic_energy
    ["Water","8%","Barbosa et al."],
    ["Energy","8200%","Barbosa et al."],
    ["Land use (tomatoes)","3.3-8.3%","Biksa"], # hydro_yields
    ["Land use (cucumbers)","25%","Biksa"],
    ["Energy", "117%","Martinez-Mate et al."], # hydroponic_lca
    ["Greenhouse gases", "48%","Martinez-Mate et al."],
    ["Labor", "141%","Martinez-Mate et al."], # See Table 1 in the full text
    ["Water", "38%","Martinez-Mate et al."], # Table 1
    ["Greenhouse gases","225%","Khandelwal"], # khandelwal
    ["Eutrophication","258%","Khandelwal"],
    ["Acidification","261%","Khandelwal"],
    ["Land use","23%","Romeo et al."], # romeo, Table 2
    ["Water","26%","Romeo et al."], # Table 2
    ["Greenhouse gases","134%","Romeo et al."], # Table 3
    ["Eutrophication","12%","Romeo et al."], # Table 3
    ["Water (from irrigation)","10-20%","AlShrouf"], # ponics_comp
    ["Fertilizer","15-45%","AlShrouf"],
    ["Land use","29-50%","AlShrouf"]
]

helper.save_image({
    "filename":"hydroponics.jpg",
    "status":"Done",
    "details":"A summary of impacts of hydroponics, relative to conventional growing methods. All studies cited did a side-by-side comparison of a hydroponic and open field system. Similar in nature to greenhouse.jpg.",
    "table":hydroponic_table,
    "references":["ponics_comp","hydroponic_energy","hydro_yields","hydroponic_lca","khandelwal","romeo"],
    "source_file":"ag_intense.py"
})

###########################

# Comparison of some other --ponics systems.
# The hydroponics figures.

ponics_table = [
    ["<b>Production System</b>","<b>Irrigation water</b>","<b>Fertilizer</b>","<b>Land use</b>"],
    ["Hydroponics","10-20%","15-45%","29-50%"],
    ["Aeroponics","5%","15%","25%"],
    ["Aquaponics","15-20%","1-15%","20-25%"]
]

helper.save_image({
    "filename":"ponics_comp.jpg",
    "status":"Done",
    "details":"Comparison of hydroponics, aquaponics, and aeroponics system. The for hydroponics reflect several variations that are considered. I'm not sure about the ranges for aquaponics, but that's what they find. All impact figures are given relative to conventional growing. The hydroponics figures are also showin in hydroponics.jpg. The main purpose of this is to compare the various -ponics methods.",
    "table":ponics_table,
    "references":["ponics_comp"],
    "source_file":"ag_intense.py"
})

###########################

# Vertical farming.
# This plot compares vertical farming and grennhouses. All from 'hallikainen'

vertical_farm_table = [
    ["<b>Metric</b>","<b>Vertical Farm impact</b>","<b>Greenhouse impact</b>"],
    ["Electricity (kWh/kg greens)","294-770","70-209"], # See Table 7. For vertical farms, skipping the 100% efficient LED scenario.
    ["Water (kg/kg greens)","20","28-280"], # Tables 5 and 6
    ["Land use (m^2/ton greens/year)","2.3-5","17-34"] # Tables 5 and 6
]

helper.save_image({
    "filename":"vertical_farm.jpg",
    "status":"Done",
    "table":vertical_farm_table,
    "details":"Comparison of three impacts between vertical farms (really more of a plant factory in an artificially lit warehouse) vs. greenhouses. Scale it so all the greenhouse bars are the same length. It will illustrate how vertical farms save land and water relative to greenhouses at the cost of energy, as greenhouses do relative to open field farming.",
    "references":["hallikainen"],
    "source_file":"ag_intense.py"
})

######################################################

# Single-celled animal feed comparison.
# All from scp_feed.
# See the attached spreadsheet for figures. Taking FA2 figures. Functional unit is 1 kg, with equal amounts of proteins and lipids across scenarios.
# Standard meal is soy-based.
# There are two sets of FA2 columns for each meal type and impact. I am added all elements from both of them. I'm not sure why.

scp_feed_table = [
    ["<b>Impact</b>","<b>Soy-based (standard meal)</b>","<b>Yeast-based</b>","<b>Bacteria-based</b>"],
    ["Land use, m^2*yr",2.678+3.190, 2.571+1.923, 2.229+1.9],
    ["Climate change, kg CO<sub>2</sub>e",3.038,1.036,2.991],
    ["Freshwater consumption, liters",55.0,63.6,39.4]
]

helper.save_image({
    "filename":"scp_feed.jpg",
    "status":"Done",
    "table":scp_feed_table,
    "details":"This is a comparison of three kinds of fish feed for salmon aquaculture: soy-based feed that is commonly used, yeast-based, and bacteria-based. Ideally I would be quoting a study that is comparing single-celled proteins with conventoinal crops intended directly for human consumption, but since I didn't find that, I am using this insteady. All impacts are for one kilogram of feed, with ingredients chosen so that protein and lipid quantities are the same for all three. The SCPs are assumed to be cultivated from agricultural residue; the case of electrolyzed ingredients is the next plot. There are also acidification and eutrophication figures, but I decided to skip them for the sake of simplicity.",
    "references":["scp_feed"],
    "source_file":"ag_intense.py"
})

###############################################

# Wheat: comparison of energy, land use, and GHG for conventional and bioreactor using different energy sources.

# From the ever-trusty meat_land_use, average impacts (per kg) of wheat are as follows
# GHG: 0.712 kg CO2e/kg
# Land use: 5.45 m^2/kg/yr
# Energy: 2.2 MJ/kg.
# Soy figures from meat_land_use too.
# I don't see explicitly where the paper says that they are refering to dry weight, but my guess is that it is. The yield figures here are a bit better than for
# the FAOSTAT world average, which would make sense if the studies skew toward richer countries, and FAOSTAT uses dry weight.

# From https://peerj.com/preprints/1279/, table 2: 11.208 kWh/kg wheat (the equivalent thereof).

energy_cr=11.208 # From bogdahn. kWh/kg dry mass. Assumes the "common" scenario.
energy_mm = 23.7/0.5 /3.6 / 0.52 # From linder. The 23.7 is the energy density of methanol ('dana', fuels.py), 
    # the 0.5 is the electricity->methanol efficiency ('data', methanol.py),
    # The 3.6 is MJ->kWh conversion
    # The 0.52 is from 0.52 g dry mass of protein for 1 g methanol input.
# Emissions factors: assuming 50 gCO2e/kWh for solar and nuclear, 450 for gas; see 'ipcc_ghg'
# Land use factors from 'vanzalk'. Taking midpoints.

power_to_food = [
    ["<b>Food</b>","<b>Energy Source</b>","<b>Energy (kWh/kg dry mass)</b>","<b>Greenhouse Gas Emissions (kg CO<sub>2</sub>e/kg dry mass)","<b>Land Use (m<sup>2</sup>yr/kg dry mass)</b>"],
    ["Conventional Wheat","Fossil Fuels",2.2/3.6,0.712,5.45],
    ["<i>Chlamydomonas reinhardtii</i>","Solar Electricity",energy_cr, energy_cr*0.05, energy_cr*139./8760+0.0017542], # bogdahn
    ["<i>Chlamydomonas reinhardtii</i>","Nuclear Electricity",energy_cr, energy_cr*0.05, energy_cr*4./8760+0.0017542],
    ["<i>Chlamydomonas reinhardtii</i>","Natural Gas Electricity",energy_cr, energy_cr*0.45, energy_cr*1.5/8760+0.0017542],
    ["Conventional Soybeans","Fossil Fuels",2.94/3.6,0.211,3.79],
    ["<i>Methylophilus methylotrophus</i>","Solar Electricity",energy_mm, energy_mm*0.05, energy_mm*139./8760+0.0017542], # linder
    ["<i>Methylophilus methylotrophus</i>","Nuclear Electricity",energy_mm, energy_mm*0.05, energy_mm*4./8760+0.0017542],
    ["<i>Methylophilus methylotrophus</i>","Natural Gas Electricity",energy_mm, energy_mm*0.45, energy_mm*1.5/8760+0.0017542]
]

helper.save_image({
    "filename":"power_to_food.jpg",
    "status":"Done",
    "table":power_to_food,
    "details":"OK, lots going on here. There are not very many studies out there quantifying energy requirements of power to food schemes. The Bogdahn and Linder studies were the best I could find, so we're going to make the most of them. The Bogdahn study describes a process involving the bacterium <i>Chlamydomonas reinhardtii</i> and compares it to wheat. The Linder study describes a process involving <i>Methylophilus methylotrophus</i> (that's a methanol eating bacterium if you're up on your Latin) and compares it to soy, so wheat and soy from conventional farming are included for illustration. The Bogdahn study gives the energy estimate explicity. The Linder study does not, but they do say that 1 gram of methanol can be used to produce 0.52 grams of the bacteria by dry weight. So to get an energy estimate we are using the fact that methanol has a energy density of 23.7 MJ/kg (Dana et al.) and that we can convert electricity to methanol at 50% efficiency (Dana et al. again). The Bogdahn study only gives energy to produce hydrogen, but this species of bacteria evidently fixes its own nitrogen and carbon. In the Linder study, they say that ammonia needs to be supply as a nitrogen source, but I would guess the ammonia needs would be comparable to how much is used in fertilizer for conventional farming, which as you can see has much lower energy needs. The figures also don't account for embodied energy in all the equipment, which again I would have to guess is a small fraction the electricity use reported. Note also that in conventional, the energy source is fossil fuels (primary energy) and electricity for the bacteria options, and I'm not dong any sort of primary energy conversion, just noting different sources. Clark and Tilman are used to get the impacts of conventional wheat and soybeans. The IPCC is used to get greenhouse gas impact of energy; I am using figures of 50 gCO2e for solar and nuclear and 450 for gas. Land use is the land use of energy production (see van Zalk and Behrens for land use by source; I am taking midpoints of the ranges), plus an additional 0.0018 m^2/kg for the facilities themselves, which is given by Linder but I am applying it to the Bogdahn study too.",
    "references":["bogdahn","linder","meat_land_use","ipcc_ghg","dana","vanzalk"],
    "source_file":"ag_intense.py"
})

########################################################

# Algaculture statistics

# Comparison of protein yields between algae and staple crops.
# Yields in tons per hectare per year
# Wheat, Soy, Rice, Maize from meat_land_use, taking the high protein yield for each crop and making unit conversions.
yield_comp = [
    ["<b>Crop</b>","<b>Protein yield: tons protein per year per hectare</b>"],
    ["Wheat",1/0.666],
    ["Soy",1/1.02],
    ["Rice",1/2.29],
    ["Maize",1/1.12],
    ["Algae, open system","12-35"], # Yields are based on 100 tons per hectare ('algae_feed') and protein share of 12-35%, as from http://www.fao.org/3/W3732E/w3732e07.htm
    ["Algae, closed system","18-52.5."]
]

helper.save_image({
    "filename":"algaculture_yield.jpg",
    "status":"Done",
    "table":yield_comp,
    "details":"Yields, per unit protein, of open and close algae systems (as reported by Walsh et al.) compared to some staple crops. For the staple crops, I took the highest figures from Clark and Tilman, since I think the Walsh et al. study is also considering ideal algaculture systems. Protein density of algae is given by Lavens and Sorgeloos.",
    "references":["algae_protein","meat_land_use","algae_feed"],
    "source_file":"ag_intense.py"
})

#############################################################

# Cultured meat LCA and comparison to other meats and meat alternatives.
# Beef, poultry, pork from meat_land_use.
cultured_table = [
    ["<b>Product</b>","<b>Energy use, MJ/kg</b>","<b>Land use, m<sup>2</sup>-year/kg</b>","<b>Greenhouse gases, kg CO<sub>2</sub>e/kg</b>"],
    ["Beef","67.1","194","40.5"],
    ["Poultry","27.9","14","5.9"],
    ["Pork","39.8","24.6","6.9"],
    ["Cultured Meat, Mattick et al.","34.5-60.9","0.46-2.82","2.268-4.379"], # ivm_energy2
    ["Cultured Meat, Tuomisto et al.","48-360","2.5-8.3","3.4-25"], # tuomisto_cm. See supplementary material.
    ["Cultured Meat, Smetana et al.","290.7-373","0.39-0.77","23.9-24.64"], # smetana, Table 2
    ["Insects","32-40.4","1.5-1.52","2.84-3.02"],
    ["Gluten-based substitute","39.7-49.2","5.5-5.82","3.59-4.03"],
    ["Soymeal-based substitute","27.78-36.9","1.06-1.44","2.65-2.78"],
    ["Mycoprotein","60.07-76.8","0.79-0.84","5.55-6.15"]
]

helper.save_image({
    "filename":"alt_meat.jpg",
    "status":"Done",
    "table":cultured_table,
    "references":["meat_land_use","ivm_energy2","tuomisto_cm","smetana"],
    "details":"A comparison of energy use, land use, and greenhouse gases of various meats and meat alternatives. The main goal here is to show how cultured meat in particular compares to other options.",
    "source_file":"ag_intense.py"
})