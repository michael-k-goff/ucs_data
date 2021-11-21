# coding=utf-8
# Land use

import helper

# TO BE DONE: Incorporate non-food crops
# Plan: Go to FAOSTAT food production and add up land area for all fiber crops. Make sure they really are not for food individually.
# Add in FAOSTAT's rubber figures too, and tobacco
# Add in biofuels

# From FAOSTAT, select world, production area, 2018, add up all fiber crops. In hectares.
fiber_crops_area = (57551+143292+390482+240293+41587+1546953+213224+172870+52844+32420353+227637)/100.
other_crops_area = (11800491+3368929)/100. # Rubber, tobacco
# For each crop, I am taking the portion of non-loss crop that is going to nonfood use and multiplying it by total number of planted hectares.
# All figures from FAOSTAT.
nonfood_area = 88666784.9306/100 # See nonfood.py

# Convert everything to square km.

# https://ourworldindata.org/land-use
total_area = 510000000 # Square km

ocean_share = 361000000.
land_share = 149000000.

# http://www.fao.org/faostat/en/#data/LC
# See the following for explanation of categories: http://fenixservices.fao.org/faostat/static/documents/LC/LC_e.pdf

#glacier_share = 1446758.883*10/total_area # 2015 is the most recent. Covered in ice more than 10 months per year.
#barren_share = 1923001.731*10/total_area # 2015, CCI_LC. <2% plant cover.
#artificial_surfaces_share = 79183.4846*10/total_area # 2017 (MODIS 2015 days 55248.2573 kha). Should include mines, waste disposal, urban parks
#herbaceous_crops_share = 1239896.7675*10/total_area # 2017 MODIS
#woody_crops_share = 130190.5188*10/total_area # 2017 MODIS
#grassland_share = 3065710.6232*10/total_area # 2017 MODIS. May or may not involved grazing and have <10% of some other crop.
#tree_covered_area_share = 4906039.0511*10/total_area # 2017 MODIS. Includes afforested area and forest plantations.
#mangroves = 18834.309*10/total_area # 2015 CCI_LC
#shrub_covered_area = 1357741.4408*10/total_area # 2017 MODIS
#sparsely_naturally_vegetated = 887544.891*10/total_area # 2015 CCI_LC. 2-10% plant cover.
#inland_water = 249159.1519*10/total_area # 2017 MODIS

# Same as above, but all 2015 CCI_LC data and in absolute numbers, 1000 ha -> km^2
glaciers = 1446758.883*10
barren = 1923001.731*10
artificial_surface = 55248.2573*10
herbaceous_crops = (1736598.1086*10) - nonfood_area # See nonfood.py for subtracting out biofuels
woody_crops = 198910.5844*10 - fiber_crops_area - other_crops_area
nonfood_crops = fiber_crops_area + other_crops_area + nonfood_area
grassland = 1822226.6488*10
tree_covered = 4357669.9037*10
mangroves = 18834.309*10
shrub_covered = 1676600.7372*10
shrubs_herbacious_aquatic_flooded = 189196.398*10
sparse_natural_vegetation = 887544.891*10
inland_water = 377119.863*10

# From this page: http://www.fao.org/faostat/en/#data/RL. All in 1000 ha.
permanent_meadow_pasture = 3266422.8335*10
forestry = 3999133.622*10 # Same number as Forest Land, which seems odd
primary_forest = 1277217.221*10
naturally_regenerated_forest = 2428530.3198*10
planted_forest = 293426.0812*10
# Figures on aquaculture and farm buildings appear to be too spotty to extract to the world. If we can get production in those countries, we could estimate yields and maybe extrapolate.

# Some figures from https://www.geosociety.org/gsatoday/archive/22/12/article/i1052-5173-22-12-4.htm. In km^2.
urban = 3700000 # I think this is too high
rural = 4200000 # I think this is too high too
rural_highway = 400000
reservoir = 200000
railway = 30000
mining = 400000
# Ration based on https://data.worldbank.org/indicator/SP.URB.TOTL. 6.675 and 3.346 are total and urban population (in billions) in 2007.
urban_rural_pop_density_ratio = float(rural)/float(urban)*3.346/(6.675-3.346)

# From https://www.newgeography.com/content/001689-how-much-world-covered-cities
urban_land_2010 = 1200000 # Square km. Averaging the two estimates given.
urban_land_2018 = urban_land_2010 * 4.196/3.574 # Adjusting for growth in urban population
rural_land_2018 = (7.594-4.196)/4.196 * urban_land_2018 * urban_rural_pop_density_ratio # Estimate rural population density the urban/rural density ratio as of 2007 as in the geosociety source.

# From http://www.fao.org/3/a-i4793e.pdf
managed_forest = 11870000 # Millions of hectares -> km^2. As of 2015.

land_use_table = [
    ["<b>Category</b>","<b>Value (square km)</b>"],
    ["Total",total_area],
    ["Ocean",ocean_share],
    ["Land",land_share],
    ["Glacier",glaciers],
    ["Barren",barren],
    ["Grass, Shrub, Light Vegetation (not for pasture)",grassland+shrub_covered+sparse_natural_vegetation - permanent_meadow_pasture],
    ["Inland Water",inland_water],
    ["Aquatic/Flooded Plants",mangroves+shrubs_herbacious_aquatic_flooded],
    ["Forest - Unmanaged",tree_covered-managed_forest],
    ["Permanent Meadow and Pasture",permanent_meadow_pasture],
    ["Herbacious Crops",herbaceous_crops],
    ["Woody Crops",woody_crops],
    ["Nonfood Crops",nonfood_crops],
    ["Forest - Managed",managed_forest],
    ["Urban",urban_land_2018],
    ["Rural",rural_land_2018],
    ["Rural Highway and Railway",rural_highway+railway],
    ["Reservoirs",reservoir],
    ["Mining and Quarrying",mining]
]

helper.save_image({
    "filename":"land_use.jpg",
    "status":"Done",
    "details":"World land use be category, in square km. 'Total' and 'Land' are aggregate categories. The subcategories under Land don't add up exactly to total land area. There's no reasonable way to make them add up because I am pulling from different sources. The Urban, Rural, Highway and Rail, Reservoir, and Mining categories add up to significantly more than the built up area in the FAO, which I think is correct, but I'm not going to try to deduct that difference from other categories to make the numbers be exact. We'll just have to note that numbers don't add up exactly due to measurement uncertainties. At any rate, don't report Total and Land values in the graphic; those are for reference.<br><br>I would like to have a number here on waste management (mostly landfills), and there are probably other categories we can think of.<br><br>See the caption in the Land Use section for details on how these calculations were done.<br><br>Edit on February 23, 2020. I estimated area nonfood crops (fiber, biofuels, rubber, tobacco) and subtracted them out from the woody and herbacious crop figures. All those estimates came from FAOSTAT too.",
    "table":land_use_table,
    "references":["wb_pop","wb_pop_urban","gsa_land","fao_fra","faostat","owid_landuse","newgeography"],
    "source_file":"land_use.py"
})

total_ag_land = permanent_meadow_pasture+herbaceous_crops+woody_crops

# Road ecology stuff

infra_table = [
    ["<b>Impact</b>","<b>Infrastructure</b>","<b>Distance from Infrastructure</b>"],
    ["Habitat directly disturbed","US Federal Highways","67.5 meters"],
    ["Frogs","Highways","50 m"],
    ["Egg and seed predation","Highways","100m"],
    ["Birds","Highways","50m"],
    ["Small mammals","Highways","60m"],
    ["Bats","Highways","3000 m"],
    ["Soil pollution","Highways","10 m"],
    ["Runoff pollution","Highways","200 m"],
    ["Headlight disturbance","Highways","50 m"],
    ["Noise pollution","Highways",">200 m"],
    ["Reduced bird population","Infrastructure","1000 m"],
    ["Reduced mammal population","Infrastructure","5000 m"]
]

helper.save_image({
    "filename":"infrastructure_radius.jpg",
    "status":"Done",
    "details":"Infrastructure can have an ecological disturbance well in excess of its physical area. This table shows the radius at which infrastructure works effects. All road stuff is from Goosem, general infrastructure stuff from Benítez-López et al.",
    "table":infra_table,
    "references":["road_radius","infra_radius"],
    "source_file":"land_use.py"
})