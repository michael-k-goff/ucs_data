# Diets

import helper

# Get yields for various crops
def get_yields():
    # Yield data. From http://www.fao.org/faostat/en/#data/QC
    # Select World, 2017, all caterogies and subcategories (Aggregate), and Yield.
    filepath = "Modules/FAO/yield.csv"
    yields = {}
    with open(filepath) as fp:
        line = fp.readline()
        headers = line.split(',')
        while line:
            line = fp.readline()
            if line:
                fields = line.split('"')
                # Relevant fields
                # 13: yield (hg/ha)
                # 15: the crop
                yields[fields[15]] = 10./float(fields[23])

    # For translating from the food balance object below to the yield object above. In many cases I have to make educated guesses
    yield_keys = {
        "Olives (including preserved)":"Olives",
        "Ricebran Oil":"Oilseeds nes",
        "Plantains":"Plantains and others",
        "Millet and products":"Millet",
        "Coconuts - Incl Copra":"Coconuts",
        "Vegetables, Other":"Vegetables, fresh nes",
        "Maize and products":"Maize",
        "Apples and products":"Apples",
        "Rape and Mustard Oil":"Oilseeds nes",
        "Sweeteners, Other":"Sugar crops, nes",
        "Groundnuts (Shelled Eq)":"Groundnuts, with shell",
        "Barley and products":"Barley",
        "Maize Germ Oil":"Oilseeds nes",
        "Groundnut Oil":"Oilseeds nes",
        "Sugar non-centrifugal":"Sugar cane",
        "Pineapples and products":"Pineapples",
        "Pulses, Other and products":"Pulses, nes",
        "Sugar (Raw Equivalent)":"Sugar crops, nes",
        "Pimento":"Chillies and peppers, green",
        "Palm Oil":"Oil palm fruit",
        "Oilcrops, Other":"Oilseeds nes",
        "Soyabeans":"Soybeans",
        "Beans":"Beans, green", # It makes a big difference if they are dry or green beans. Guessing green. See also, Pimento above.
        "Sesameseed Oil":"Oilseeds nes",
        "Grapes and products (excl wine)":"Grapes",
        "Potatoes and products":"Potatoes",
        "Cottonseed Oil":"Oilseeds nes",
        "Palm kernels":"Oil palm fruit",
        "Onions":"Onions, shallots, green",
        "Coffee and products":"Coffee, green",
        "Roots, Other":"Roots and tubers, nes",
        "Sorghum and products":"Sorghum",
        "Oilcrops Oil, Other":"Oilseeds nes",
        "Cereals, Other":"Cereals, nes",
        "Pepper":"Pepper (piper spp.)", # Pepper the chili pepper or pepper the spice?
        "Peas":"Peas, green",
        "Nuts and products":"Nuts, nes",
        "Sunflowerseed Oil":"Oilseeds nes",
        "Cottonseed":"Seed cotton",
        "Wheat and products":"Wheat",
        "Cassava and products":"Cassava",
        "Cocoa Beans and products":"Cocoa, beans",
        "Palmkernel Oil":"Oilseeds nes",
        "Fruits, Other":"Fruit, fresh nes",
        "Citrus, Other":"Fruit, citrus nes",
        "Lemons, Limes and products":"Lemons and limes",
        "Tea (including mate)":"Tea",
        "Soyabean Oil":"Oilseeds nes",
        "Grapefruit and products":"Grapefruit (inc. pomelos)",
        "Rye and products":"Rye",
        "Olive Oil":"Oilseeds nes",
        "Coconut Oil":"Oilseeds nes",
        "Tomatoes and products":"Tomatoes",
        "Spices, Other":"Spices, nes",
        "Rape and Mustardseed":"Rapeseed",
        "Oranges, Mandarines":"Oranges",
        "Rice (Milled Equivalent)":"Rice, paddy"
    }

    # Add in more yield data from animals
    # Figures are taken from https://iopscience.iop.org/article/10.1088/1748-9326/aa6cd5, the supplementary data file.
    # For each product, take the median of all LCA land use figures (per gram) for that product. Numbers are converted from m^2/g to ha/kg by dividing by 10
    yields["Eggs"] = 0.00668 / 10
    yields["Pigmeat"] = 0.0182 / 10 # Pork
    yields["Bovine Meat"] = 0.0647 / 10
    yields["Milk - Excluding Butter"] = 0.00149 / 10
    yields["Poultry Meat"] = 0.0114 / 10
    yields["Mutton & Goat Meat"] = 0.0549 / 10 # Only three values

    # The following is the same as above, but using the mean instead of median. This may better capture outliers from low intensity systems.
    # This change increases total land use by over 50%.
    yields["Eggs"] = 0.00645 / 10
    yields["Pigmeat"] = 0.0246 / 10 # Pork
    yields["Bovine Meat"] = 0.194 / 10
    yields["Milk - Excluding Butter"] = 0.00167 / 10
    yields["Poultry Meat"] = 0.014 / 10
    yields["Mutton & Goat Meat"] = 0.184 / 10 # Only three values

    # Yields in aquaculture. Figures from https://www.pnas.org/content/pnas/suppl/2018/04/24/1801692115.DCSupplemental/pnas.1801692115.sapp.pdf
    # Table 1.5 for feed conversion ratios. Using freshwater values for crustaceans. Will also use that FCR for all non-fish aquaculture.
    aquaculture_fcr = {"Fish":(1.1+1.6)/2, "Crustaceans":(1.1+1.8)/2}
    aquaculture_biomass_ratio = {"Fish":0.7, "Crustacean":0.3, "Mollusk":0.2} # Edible biomass ratio
    # USA, freshwater aq. Names are converted to the most relevant categories for land-based crops above.
    aquaculture_feed = {"Wheat":0.47, "Maize":0.06, "Soybeans":0.22, "Rapeseed":0.03, "Pulses,Total":0.22}
    aquaculture_feed_yield = sum([aquaculture_feed[key]*yields[key] for key in aquaculture_feed])
    yields["Marine Fish, Other"] = aquaculture_feed_yield / aquaculture_fcr["Fish"] / aquaculture_biomass_ratio["Fish"]
    yields["Fish, Liver Oil"] = aquaculture_feed_yield / aquaculture_fcr["Fish"] / aquaculture_biomass_ratio["Fish"]
    yields["Fish, Body Oil"] = aquaculture_feed_yield / aquaculture_fcr["Fish"] / aquaculture_biomass_ratio["Fish"]
    yields["Demersal Fish"] = aquaculture_feed_yield / aquaculture_fcr["Fish"] / aquaculture_biomass_ratio["Fish"]
    yields["Freshwater Fish"] = aquaculture_feed_yield / aquaculture_fcr["Fish"] / aquaculture_biomass_ratio["Fish"]
    yields["Cephalopods"] = aquaculture_feed_yield / aquaculture_fcr["Crustaceans"] / aquaculture_biomass_ratio["Mollusk"]
    yields["Crustaceans"] = aquaculture_feed_yield / aquaculture_fcr["Crustaceans"] / aquaculture_biomass_ratio["Crustacean"]
    yields["Aquatic Animals, Others"] = aquaculture_feed_yield / aquaculture_fcr["Crustaceans"] / aquaculture_biomass_ratio["Crustacean"]
    yields["Molluscs, Other"] = aquaculture_feed_yield / aquaculture_fcr["Crustaceans"] / aquaculture_biomass_ratio["Mollusk"]
    yields["Pelagic Fish"] = aquaculture_feed_yield / aquaculture_fcr["Fish"] / aquaculture_biomass_ratio["Fish"]

    # There are a few more products not account for (yet).
    # I am guessing, perhaps incorrectly, that butter and cream can be treated as coproducts of other dairy products and should not be added separately.
    # Various kinds of unspecified meat are not included.
    # Alcoholic beverages are not counted
    return yields, yield_keys
    
# Return a dictionary of LCA GHG emissions by crop. The keys should match those in the diet CSV files used below.
# Unless otherwise noted, GHG figures are taken from the Clark and Tilman (2017) paper, with averages of all figures for which GHG are available.
# Units are gCO2e per g of product.
# For the world, these categories cover all but 89 calories per person per day (as of January 2, 2020).
def ghg_by_crop():
    ghg = {}
    # Grains
    ghg["Rice (Milled Equivalent)"] = 1.68
    ghg["Wheat and products"] = 0.712
    ghg["Barley and products"] = 0.697
    ghg["Oats"] = 0.77
    ghg["Maize and products"] = 0.416
    ghg["Rye and products"] = (0.712+0.697+0.77+0.416)/4. # Average of cereals above except rice
    ghg["Cereals, Other"] = (0.712+0.697+0.77+0.416)/4. # Average of cereals above except rice
    ghg["Sorghum and products"] = (0.712+0.697+0.77+0.416)/4. # Average of cereals above except rice
    ghg["Millet and products"] = (0.712+0.697+0.77+0.416)/4. # Average of cereals above except rice
    # For oil crops, unless they are explicitly present in the spreadsheet, take the average of all ___ Oil entries.
    ghg["Ricebran Oil"] = 5.19
    ghg["Oilcrops, Other"] = 5.19
    ghg["Sesameseed Oil"] = 5.19
    ghg["Groundnut Oil"] = 5.19
    ghg["Cottonseed Oil"] = 5.19
    ghg["Sunflowerseed Oil"] = 2.71
    ghg["Oilcrops Oil, Other"] = 2.71
    ghg["Palm Oil"] = 2.73
    ghg["Palmkernel Oil"] = 2.73 # Treat as palm oil
    ghg["Rape and Mustard Oil"] = 6.54 # Rapeseed Oil
    ghg["Olive Oil"] = 8.54
    ghg["Soyabean Oil"] = 5.19 # GHG for soybean oil is missing, so treat as average of other oils.
    ghg["Coconut Oil"] = 5.19
    ghg["Maize Germ Oil"] = 5.19
    # Fruit
    ghg["Olives (including preserved)"] = 8.54 / 10 # Divide Olive Oil by 10: https://www.quora.com/How-many-olives-does-it-take-to-make-one-liter-of-olive-oil
    ghg["Lemons, Limes and products"] = 0.0873
    ghg["Oranges, Mandarines"] = 0.161
    ghg["Citrus, Other"] = (0.0873+0.161)/2 # Average lemons and oranges
    ghg["Plantains"] = 0.237 # Banana
    ghg["Bananas"] = 0.237
    ghg["Grapes and products (excl wine)"] = 0.315
    ghg["Apples and products"] = 0.102
    ghg["Tomatoes and products"] = 0.4 # 19 non-contiguous studies. Lots of greenhouse values.
    ghg["Pineapples and products"] = 0.0976 # Seems low.
    ghg["Grapefruit and products"] = 0.161 # Using the Oranges and Mandarines figure.
    ghg["Dates"] = 0.0959 # Peaches
    ghg["Coconuts - Incl Copra"] = 0.0959 # Peaches. It's a stone fruit
    ghg["Andean blackberry"] = 0.17 # Not in the food balances data set, but will use for calculations
    ghg["Avocado"] = 0.166 # Not in FBS but used for calculations
    ghg["Blueberries"] = 0.113 # Not in FBS but used for calculations
    ghg["Chinese Pear"] = 0.156 # Not in FBS but used for calculations
    ghg["Golden berry"] = 0.241 # Not in FBS
    ghg["Kiwi"] = 0.819 # Not in FBS
    ghg["Mango"] = 0.052 # Not in FBS
    ghg["Passion Fruit"] = 0.107 # Not in FBS
    ghg["Pear"] = 0.376 # Not in FBS
    ghg["Raspberry"] = 0.337 # Not in FBS
    ghg["Strawberry"] = (0.614+0.695)/2 # Not in FBS. Two entries.
    ghg["Melon"] = 1.61 # Not in FBS
    ghg["Fruits, Other"] = (ghg["Olives (including preserved)"]+ghg["Lemons, Limes and products"]+ghg["Citrus, Other"]+ghg["Bananas"]+ghg["Grapes and products (excl wine)"]+ghg["Apples and products"]+ghg["Tomatoes and products"]+ghg["Pineapples and products"]+ghg["Grapefruit and products"]+ghg["Dates"]+ghg["Andean blackberry"]+ghg["Avocado"]+ghg["Blueberries"]+ghg["Chinese Pear"]+ghg["Pear"]+ghg["Golden berry"]+ghg["Kiwi"]+ghg["Mango"]+ghg["Passion Fruit"]+ghg["Raspberry"]+ghg["Strawberry"]+ghg["Melon"])/22.
    # Vegetable
    ghg["Pepper"] = 0.909
    ghg["Pimento"] = ghg["Pepper"]
    ghg["Asparagus"] = 0.676 # Not in FBS
    ghg["Leeks"] = 0.069 # Not in FBS
    ghg["Lettuce"] = (0.025+0.844+0.209)/(1.+3.+1.) # Not in FBS
    ghg["Spinach"] = 2.3 # Not in FBS
    ghg["Zucchini"] = 1.21 # Not in FBS
    ghg["Vegetables, Other"] = (ghg["Pepper"]+ghg["Asparagus"]+ghg["Leeks"]+ghg["Lettuce"]+ghg["Spinach"]+ghg["Zucchini"])/6.
    # Meat
    ghg["Poultry Meat"] = 5.9
    ghg["Bovine Meat"] = 40.5
    ghg["Pigmeat"] = 6.99
    ghg["Mutton & Goat Meat"] = 50.4
    # Seafood
    ghg["Demersal Fish"] = (52.7+21.9+3.61+186.+61.2+2.65+16.1)/(5.+1.+1.+46+4.+5.+1.) # In order, Turbot, Catfish, Eel, Cod, Sea bass, snapper, tilapia
    ghg["Pelagic Fish"] = (66.1+13.1+62.5+26.3+46.6)/(7.+10.+1.+10.+9.) # In order, Tuna, Herring, Angler Fish, Mackerel
    ghg["Cephalopods"] = (32.2)/(3.) # Squid,
    ghg["Freshwater Fish"] = (53.2+21.9)/(10.+1.) # Trout, Catfish
    ghg["Crustaceans"] = (141.+17.5)/(6.+2.) # Crab, shrimp
    ghg["Molluscs, Other"] = ghg["Cephalopods"] # Probably clams and oysters, but I don't see figures there, so I'm using this one instead.
    ghg["Marine Fish, Other"] = (ghg["Demersal Fish"]+ghg["Pelagic Fish"]+ghg["Freshwater Fish"])/3. # Average of other types of fish
    # Dairy
    ghg["Eggs"] = 3.03
    ghg["Milk - Excluding Butter"] = 1.12
    ghg["Butter, Ghee"] = 1.09
    ghg["Cream"] = ghg["Butter, Ghee"]
    # Pulses
    ghg["Cassava and products"] = 0.0711
    ghg["Onions"] = 0.0506
    ghg["Soyabeans"] = 0.211
    ghg["Potatoes and products"] = 0.153
    ghg["Sweet potatoes"] = 0.153 # Treat like regular potato
    ghg["Yams"] = 0.153 # Also like regular potato
    ghg["Roots, Other"] = 0.153 # Also like regular potato. Kind of guessing at this point.
    ghg["Pulses, Other and products"] = 0.211 # All pulses other than beans are treated as soybeans.
    ghg["Beans"] = 0.231 # All beans treated as Prespa beans, except soybeans
    ghg["Peas"] = 0.211 # Soybeans
    ghg["Cocoa Beans and products"] = 0.231 # It's a bean
    ghg["Coffee and products"] = 0.231 # Beans
    # Nuts and seeds
    # All nuts and seeds figures are taken as Almonds. Quite a stretch, I know.
    ghg["Groundnuts (Shelled Eq)"] = 0.00125
    ghg["Sunflower seed"] = 0.00125
    ghg["Nuts and products"] = 0.00125
    ghg["Cottonseed"] = 0.00125
    ghg["Rape and Mustardseed"] = 0.00125
    ghg["Sesame seed"] = 0.00125
    ghg["Palm kernels"] = 0.119 # Except this one
    # Other
    ghg["Beer"] = 0.145
    ghg["Beverages, Fermented"] = ghg["Beer"]
    ghg["Sugar (Raw Equivalent)"] = 0.818 # Table sugar
    ghg["Sweeteners, Other"] = 0.818 # Table sugar
    ghg["Sugar non-centrifugal"] = 0.818 # Table sugar
    ghg["Sugar beet"] = 0.818 # Table sugar again
    ghg["Sugar cane"] = 0.818 # Table sugar again
    ghg["Wine"] = 1.38
    
    return ghg
ghg = ghg_by_crop()
energy = {
    "Apples and products":0.72,
    "Aspagarus":1.2,
    "Bovine Meat":67,
    "Blueberries":1.29,
    "Chinese Pear":1.3,
    "Eggs":17,
    "Lemons, Limes and products":2.7,
    "Maize and products":2.7,
    "Milk - Excluding Butter":2.9,
    "Mutton & Goat Meat":32,
    "Onions":0.4,
    "Oranges, Mandarines":2.6,
    "Pineapples and products":1.67,
    "Pigmeat":40,
    "Poultry Meat":28,
    "Raspberry":6.6,
    "Rice (Milled Equivalent)":7.8,
    "Tomatoes and products":(5.3*4+12*5+3.1*8)/17., # 4 non-greenhouse and 5 greenhouse values.
    "Wheat and products":2.2,
    "Melon":2.71,
    "Pepper":1.788,
    "Potatoes and products":1.27,
    "Beans":1.8,
    "Soyabeans":2.9,
    "Wine":0.0000192,
    "Zucchini":2.24
}
energy["Fruits, Other"] = (energy["Lemons, Limes and products"]+energy["Apples and products"]+energy["Blueberries"]+energy["Chinese Pear"]+energy["Tomatoes and products"])/5.
energy["Vegetables, Other"] = (energy["Zucchini"]+energy["Pepper"]+energy["Aspagarus"])/3.

####################

# Download instructions for per_cap3.csv
# Food Balance Sheets from FAOSTAT: http://www.fao.org/faostat/en/#data/FBSH
# Select 
#     Year 2013
#     region World
#     For Items, select "Grand Total>List" under Items Aggregated
#     Under Elements, select Seed, Losses, Food, Food supply quantity (kg/capita/yr), Feed, Processed, Other uses
# usa_calories: same as per_cap3 except with the US instead of world

def get_caloric_intake(input_file):
    food_share = {}
    filepath = input_file
    with open(filepath) as fp:
        line = fp.readline()
        headers = line.split(',')
        while line:
            line = fp.readline()
            # Relevant field values
            # 11 is what is being measured. Values are Feed, Seed, Food supply quantity (kg/capita/yr), Losses
            # 15 is the food item
            # 23 is the amount. Thousands of tons for Seed, Food, Losses; kg per person per year for food supply.
            if line:
                fields = line.split('"')
                if fields[15] not in food_share:
                    food_share[fields[15]] = {}
                food_share[fields[15]][fields[11]] = float(fields[23])
    return food_share
            
# Some post-processing. Several things going on here
# 1) Calculate efficiency of food production to consumption. Only accounts for losses in transportation and storage; not wastage.
# 2) Load in yield information from the yields object.

def add_yields(food_share, yields, yield_keys):
    for key in food_share:
        if "Food" in food_share[key]:
            numer = food_share[key]["Food"]
            denom = food_share[key]["Food"]
            if "Losses" in food_share[key]:
                denom += food_share[key]["Losses"]
            if "Seed" in food_share[key]:
                numer += food_share[key]["Seed"]
                denom += food_share[key]["Seed"]
            if "Feed" in food_share[key]:
                numer += food_share[key]["Feed"]
                denom += food_share[key]["Feed"]
            if "Processing" in food_share[key]:
                numer += food_share[key]["Processing"]
                denom += food_share[key]["Processing"]
            if "Other uses" in food_share[key]:
                numer += food_share[key]["Other uses"]
                denom += food_share[key]["Other uses"]
            if denom == 0:
                pass
            else:
                food_share[key]["Efficiency"] = numer/denom
            # Check for matched keys
            if key in yields:
                food_share[key]["Yield"] = yields[key]
            elif key in yield_keys:
                food_share[key]["Yield"] = yields[yield_keys[key]]
            if key in ghg:
                food_share[key]["GHG"] = ghg[key]
            if key in energy:
                food_share[key]["Energy"] = energy[key]
            
# The following are a grouping of each of the food items that appear in the above data files into broader categories.
food_categories = {
    "Sugar":["Sweeteners, Other","Honey","Sugar non-centrifugal","Sugar (Raw Equivalent)","Sugar cane"],
    "Oil, Fat":["Ricebran Oil","Fats, Animals, Raw","Rape and Mustard Oil","Fish, Liver Oil","Fish, Body Oil","Maize Germ Oil","Groundnut Oil","Palm Oil","Oilcrops, Other","Sesameseed Oil","Cottonseed Oil","Oilcrops Oil, Other","Sunflowerseed Oil","Palmkernel Oil","Soyabean Oil","Olive Oil","Coconut Oil"],
    "Nuts, seeds":["Groundnuts (Shelled Eq)","Sesame seed","Palm kernels","Sunflower seed","Nuts and products","Cottonseed","Cocoa Beans and products","Rape and Mustardseed"],
    "Pulses":["Pulses, Other and products","Beans","Peas","Soyabeans"],
    "Fruit":["Plantains","Olives (including preserved)","Apples and products","Pineapples and products","Dates","Grapes and products (excl wine)","Fruits, Other","Citrus, Other","Lemons, Limes and products","Grapefruit and products","Tomatoes and products","Bananas","Oranges, Mandarines"],
    "Vegetables":["Cloves","Coconuts - Incl Copra","Vegetables, Other","Pimento","Pepper"],
    "Grain":["Millet and products","Maize and products","Barley and products","Oats","Sorghum and products","Cereals, Other","Wheat and products","Rye and products","Rice (Milled Equivalent)"],
    "Tuber":["Cassava and products","Potatoes and products","Yams","Sweet potatoes","Sugar beet","Onions","Roots, Other"],
    "Dairy and Eggs":["Eggs","Cream","Milk - Excluding Butter","Butter, Ghee"],
    "Meat (Terrestrial)":["Pigmeat","Mutton & Goat Meat","Bovine Meat","Offals, Edible","Meat, Other","Poultry Meat"],
    "Aquaculture Seafood":["Marine Fish, Other","Demersal Fish","Freshwater Fish","Cephalopods","Crustaceans","Aquatic Animals, Others","Molluscs, Other","Meat, Aquatic Mammals","Pelagic Fish"],
    "Alcohol":["Beverages, Alcoholic","Wine","Alcohol, Non-Food","Beer","Beverages, Fermented"],
    "Other":["Miscellaneous","Aquatic Plants","Coffee and products","Infant food","Tea (including mate)","Spices, Other"]
}

# Calories, land use, and GHG by food type
def calories_land_by_type(food_share):
    calories_by_category = {}
    land_use_by_category = {}
    ghg_by_category = {}
    energy_by_category = {}
    for key in food_categories:
        calories_by_category[key] = 0
        land_use_by_category[key] = 0
        ghg_by_category[key] = 0
        energy_by_category[key] = 0
        
        # Count number of GHG and energy food by calories so we can make an adjustment if necessary.
        ghg_count, energy_count = 0, 0
        
        for i in range(len(food_categories[key])):
            k = food_categories[key][i]
            if (k in food_share and "Yield" in food_share[k]):
                land_use_by_category[key] += food_share[k]["Food supply quantity (kg/capita/yr)"]*food_share[k]["Yield"]
            if (k in food_share and "Food supply (kcal/capita/day)" in food_share[k]):
                calories_by_category[key] += food_share[k]["Food supply (kcal/capita/day)"]
            if (k in food_share and "GHG" in food_share[k]):
                ghg_by_category[key] += food_share[k]["Food supply quantity (kg/capita/yr)"]*food_share[k]["GHG"]
                ghg_count += food_share[k]["Food supply quantity (kg/capita/yr)"]
            if (k in food_share and "Energy" in food_share[k]):
                energy_by_category[key] += food_share[k]["Food supply quantity (kg/capita/yr)"]*food_share[k]["Energy"]
                energy_count += food_share[k]["Food supply quantity (kg/capita/yr)"]
        # Multiply energy_by_category[key] by energy_count / ghg_count.
        multiplier = 0
        if energy_count > 0:
            multiplier = (ghg_count / energy_count)
        energy_by_category[key] *= multiplier
    return calories_by_category, land_use_by_category, ghg_by_category, energy_by_category
    
# Get overall land use for a given diet
def diet_land_use(food_share):
    total_land_use = 0
    for k in food_share:
        if "Yield" in food_share[k]:
            total_land_use += food_share[k]["Food supply quantity (kg/capita/yr)"]*food_share[k]["Yield"]
    return total_land_use

# Get overall GHG for a given diet
def diet_ghg(food_share):
    total_ghg = 0
    for k in food_share:
        if "GHG" in food_share[k]:
            total_ghg += food_share[k]["Food supply quantity (kg/capita/yr)"]*food_share[k]["GHG"]
    return total_ghg
    
###################################################

# Water by category
def get_water_by_category(calories_by_category, food_share):
    return { # Data is pulled from figures in ag_environment.py. For refactoring, would want to pull directly
        # Figures are liters of water per kcal.
        "Sugar":0.68*calories_by_category["Sugar"], # Sugar crops
        "Vegetables":1.34*calories_by_category["Vegetables"],
        "Oil, Fat":0.81*calories_by_category["Oil, Fat"],
        "Pulses":1.19*calories_by_category["Pulses"],
        "Fruit":2.1*calories_by_category["Fruit"],
        "Grain":0.51*calories_by_category["Grain"],
        "Tuber":0.47*calories_by_category["Tuber"],
        "Nuts, seeds":3.63*calories_by_category["Nuts, seeds"],
        "Dairy and Eggs":(food_share["Milk - Excluding Butter"]["Food supply (kcal/capita/day)"]*1.82+food_share["Eggs"]["Food supply (kcal/capita/day)"]*2.29),
        "Meat (Terrestrial)":(food_share["Pigmeat"]["Food supply (kcal/capita/day)"]*2.15+food_share["Bovine Meat"]["Food supply (kcal/capita/day)"]*10.19+food_share["Poultry Meat"]["Food supply (kcal/capita/day)"]*3.+food_share["Mutton & Goat Meat"]["Food supply (kcal/capita/day)"]*4.25),
        "Aquaculture Seafood":0,
        "Other":16.4*calories_by_category["Other"] # Based on stimulants
    }

def diet_land_use_chart(ghg=0):
    # Set two two baseline diets
    diets = {}
    yields, yield_keys = get_yields()
    food_share_us = get_caloric_intake("Modules/FAO/usa_calories.csv")
    food_share_world = get_caloric_intake("Modules/FAO/per_cap3.csv")
    food_share_euro = get_caloric_intake("Modules/FAO/euro_calories.csv")
    food_share_china = get_caloric_intake("Modules/FAO/china_calories.csv")
    add_yields(food_share_us, yields, yield_keys)
    add_yields(food_share_world, yields, yield_keys)
    add_yields(food_share_euro, yields, yield_keys)
    add_yields(food_share_china, yields, yield_keys)
    if ghg==1:
        diets["American"] = diet_ghg(food_share_us)
        diets["World"] = diet_ghg(food_share_world)
        diets["Euro"] = diet_ghg(food_share_euro)
        diets["China"] = diet_ghg(food_share_china)
    elif ghg==0:
        diets["American"] = diet_land_use(food_share_us)
        diets["World"] = diet_land_use(food_share_world)
        diets["Euro"] = diet_land_use(food_share_euro) # Comment out if this is not intended for the diet land use plot
        diets["China"] = diet_land_use(food_share_china) # Comment out if this is not intended for the diet land use plot
    
    # Diets are assessed relative to a baseline. Options for now are "US" and "World"
    
    ########## Parameter to set ############
    baseline = "US"
    ########## Parameter to set ############
    
    calories_by_category, land_use_by_category, ghg_by_category, energy_by_category = calories_land_by_type({"US":food_share_us,"World":food_share_world}[baseline])
    water_by_category = get_water_by_category(calories_by_category, {"US":food_share_us,"World":food_share_world}[baseline])
    if ghg==1:
        land_use_by_category = ghg_by_category
    if ghg==2:
        land_use_by_category = water_by_category
    if ghg==3:
        land_use_by_category = energy_by_category
        
    # Redoing US diet here
    if ghg==2:
        base_land = 0
        for key in land_use_by_category:
            base_land += land_use_by_category[key]
        calories_by_category_world, _, _, _ = calories_land_by_type(food_share_world)
        calories_by_category_china, _, _, _ = calories_land_by_type(food_share_china)
        calories_by_category_euro, _, _, _ = calories_land_by_type(food_share_euro)
        calories_by_category_us, _, _, _ = calories_land_by_type(food_share_us)
        water_by_category_world = get_water_by_category(calories_by_category_world, food_share_world)
        water_by_category_china = get_water_by_category(calories_by_category_china, food_share_china)
        water_by_category_euro = get_water_by_category(calories_by_category_euro, food_share_euro)
        water_by_category_us = get_water_by_category(calories_by_category_us, food_share_us)
        diets["World"] = 0
        for key in water_by_category_world:
            diets["World"] += water_by_category_world[key]
        diets["China"] = 0
        for key in water_by_category_china:
            diets["China"] += water_by_category_china[key]
        diets["Euro"] = 0
        for key in water_by_category_euro:
            diets["Euro"] += water_by_category_euro[key]
        diets["American"] = 0
        for key in water_by_category_us:
            diets["American"] += water_by_category_us[key]
            
    # Baseline diet (yes, this could be done in a simpler way but I am trying to set up a pattern for other diets)
    # American diet
    low_cal_land = 0
    for key in land_use_by_category:
        low_cal_land += land_use_by_category[key]
    diets["American Diet"] = low_cal_land
    
    # Low calorie (yes, this could be done in a simpler way but I am trying to set up a pattern for other diets)
    # Assume a 25% across-the-board reduction from the base diet.
    low_cal_land = 0
    for key in land_use_by_category:
        low_cal_land += land_use_by_category[key]*0.75
    diets["Low Calorie"] = low_cal_land

    # Pescetarian
    # Assume all terresterial meat is seafood instead.
    pesc_land = 0
    for key in land_use_by_category:
        if key != "Meat (Terrestrial)":
            pesc_land += land_use_by_category[key]
    pesc_land += land_use_by_category["Aquaculture Seafood"] * float(calories_by_category["Meat (Terrestrial)"]) / float(calories_by_category["Aquaculture Seafood"])
#    diets["Pescetarian"] = pesc_land
    
    # Vegetarian
    # Assume all meat is converted to the other categories and spread evenly
    veg_land = 0
    all_cal = 0
    for key in land_use_by_category:
        if key != "Meat (Terrestrial)" and key != "Aquaculture Seafood":
            veg_land += land_use_by_category[key]
        all_cal += calories_by_category[key]
    meat_share = (calories_by_category["Meat (Terrestrial)"] + calories_by_category["Aquaculture Seafood"]) / float(all_cal)
    veg_land /= (1-meat_share)
    diets["Vegetarian"] = veg_land
    
    # Vegan
    # Assume all meat and animal products are converted to the other categories and spread mostly evenly, but an extra 100 of those calories go to nuts/seeds.
    vegan_land = 0
    all_cal = 0
    for key in land_use_by_category:
        if key != "Meat (Terrestrial)" and key != "Aquaculture Seafood" and key != "Dairy and Eggs":
            vegan_land += land_use_by_category[key]
        all_cal += calories_by_category[key]
    meat_share = (calories_by_category["Meat (Terrestrial)"] + calories_by_category["Aquaculture Seafood"] + calories_by_category["Dairy and Eggs"]-100) / float(all_cal)
    vegan_land /= (1-meat_share)
    vegan_land += 100./calories_by_category["Nuts, seeds"]*land_use_by_category["Nuts, seeds"]
    diets["Vegan"] = vegan_land
        
    return diets
    
def diet_table():
    diets = diet_land_use_chart()
    table = [["<b>Diet</b>","<b>Land use (ha/person)</b>"]]
    for key in diets:
        table.append([key,diets[key]])
    return table

def diet_table_ghg():
    diets = diet_land_use_chart(1)
    table = [["<b>Diet</b>","<b>GHG emissions (kg CO<sub>2</sub>e/person/year)</b>"]]
    for key in diets:
        table.append([key,diets[key]])
    return table
    
def diet_table_energy():
    diets = diet_land_use_chart(3)
    table = [["<b>Diet</b>","<b>Energy (MJ/person/year)</b>"]]
    for key in diets:
        table.append([key,diets[key]])
    return table

def diet_table_water():
    diets = diet_land_use_chart(2)
    table = [["<b>Diet</b>","<b>Water consumption (m<sup>3</sup>/person/year)</b>"]]
    for key in diets:
        table.append([key,0.365*diets[key]])
    return table
    
def diet_image():
    table = diet_table()
    helper.save_image({
        "filename":"land_use_by_diet.jpg",
        "status":"Done",
        "table":table,
        "references":["faostat","meat_land_use","aq_land_use"],
        "details":"Show land use by type of diet. Land use per food item is the same as in diet_land_use.jpg. See the footnote on the Diet page for details on what the diets are. 'Euro' is the average European diet.",
        "source_file":"diet.py"
    })
#diet_image()

def diet_image_ghg():
    table = diet_table_ghg()
    helper.save_image({
        "filename":"ghg_by_diet.jpg",
        "status":"Done",
        "table":table,
        "references":["faostat","meat_land_use"],
        "details":"Show GHG emissions by type of diet. Land use per food item is the same as in diet_ghg.jpg. See the footnote on the Diet page for details on what the diets are.",
        "source_file":"diet.py"
    })
#diet_image_ghg()

def diet_image_energy():
    table = diet_table_energy()
    helper.save_image({
        "filename":"diet_energy.jpg",
        "status":"Done",
        "table":table,
        "references":["faostat","meat_land_use"],
        "details":"Energy usage by diet. Much of the data is missing. There are no seafood figures, for instances, so the pescatarian diet is left out. These figures also don't account for energy in sugar, nuts, and oil. But it's the best I could do with available data.",
        "source_file":"diet.py"
    })
diet_image_energy()

def diet_image_water():
    table = diet_table_water()
    helper.save_image({
        "filename":"water_by_diet.jpg",
        "status":"Done",
        "table":table,
        "references":["faostat","water_crops1","water_crops2","nutritive"],
        "details":"Double-check the numbers; some look like they are wrong.",
        "source_file":"diet.py"
    })
#diet_image_water()
                    
#################################################

# Make the table and data for an image on world average calorie and land use.
def world_food_image():
    # Prepare data
    yields, yield_keys = get_yields()
    food_share = get_caloric_intake("Modules/FAO/per_cap3.csv")
    add_yields(food_share, yields, yield_keys)
    calories_by_category, land_use_by_category, _, _ = calories_land_by_type(food_share)
    
    # Make table for display in the dashboard
    table = [["<b>Food category</b>","<b>Calories in World Average Diet (kcal/cap)</b>","<b>Land from world average diet (ha/cap)</b>"]]
    for key in food_categories:
        table = table + [[key,calories_by_category[key],land_use_by_category[key]]]
    
    # Full image data for display in the dashboard
    helper.save_image({
        "filename":"diet_land_use.jpg",
        "status":"Done",
        "table":table,
        "details":"A few changes here. 'Meat (Seafood)' has been renamed. Also change 'Pulses' to 'Beans and other Legumes'. Avoid acronyms here, e.g. 'hectares per person' rather than 'ha/cap'.",
        "references":["faostat","meat_land_use","aq_land_use"],
        "source_file":"diet.py"
    })
#world_food_image()

# Table and data for an image of world average calorie and GHG emissions.
def world_food_ghg_image():
    # Prepare data
    yields, yield_keys = get_yields()
    food_share = get_caloric_intake("Modules/FAO/per_cap3.csv")
    add_yields(food_share, yields, yield_keys)
    calories_by_category, _, ghg_by_category, _ = calories_land_by_type(food_share)
    
    # Make table for display in the dashboard
    table = [["<b>Food category</b>","<b>Calories in World Average Diet (kcal/cap)</b>","<b>Greehouse gas emissions (kg CO<sub>2</sub>e per year)</b>"]]
    for key in food_categories:
        table = table + [[key,calories_by_category[key],ghg_by_category[key]]]
    
    # Full image data for display in the dashboard
    helper.save_image({
        "filename":"diet_ghg.jpg",
        "status":"Done",
        "table":table,
        "details":"Same comments apply here as to the Diet and Land Use Plot. In addition, the bars on the upper side should be black and on the lower side be gray.",
        "references":["faostat","meat_land_use"],
        "source_file":"diet.py"
    })
#world_food_ghg_image()

