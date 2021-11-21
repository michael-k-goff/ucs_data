# Plots on biodiversity

import helper

# Species threats. See IUCN. https://www.iucnredlist.org/search
# Done on April 16, 2020. Instructions:
# Select EX, EW, CR, EN, VU in the Red List Category item on the left menu
# Go to Threats and count how many there are of each threat
# Note that some species are affected by multiple threats
# Threats not prefaced by "---" are main ones, with "---" are subcategories of the preceding main one.

species_threats_table = [
    ["<b>Threat</b>","<b>Number of species threatened</b>","<b>Notes</b>"],
    ["Residential & Commercial Development",6887],
    ["---Housing and urban areas",5636],
    ["---Commercial and industrial areas",1326],
    ["---Tourism and recreation areas",2189],
    ["Agriculture and aquaculture",14316],
    ["---Annual and perennial crops (non-timber)",11345],
    ["---Wood and pulp plantations",1880],
    ["---Livestock farming and ranching",6422,"Does not include farming of feed or forage for stall-fed animals."],
    ["---Marine and freshwater aquaculture",156],
    ["Energy production and mining",3656],
    ["---Oil and gas drilling",179,"Does not include pipelines, oil spills, and pollution or emissions from combustion."],
    ["---Mining and quarrying",3423,"Pollution may be classified as Industrial Effluent."],
    ["---Renewable energy",150,"Does not include hydropower."],
    ["Transportation and service corridtors",2164],
    ["---Roads and railroads",1717,"Service roads for other utilities are considered under Utility and Service Lines."],
    ["---Utility and service lines",169],
    ["---Shipping lanes",369],
    ["---Flight paths",7],
    ["Biological resource use",13210],
    ["---Hunting and trapping, terrestrial",1885],
    ["---Gathering terrestrial plants",1630],
    ["---Logging and wood harvesting",9826,"Clearing of trees for farming goes under Agriculture and Aquaculture, not here."],
    ["---Fishing and harvesting aquatic resources",1649],
    ["Human intrusion and disturbance",2545],
    ["---Recreational activities",1896],
    ["---Military",224],
    ["---Work and other activities",657,"Does not include military or recreation. Examples are law enforcement, drug smugglers, illegal immigrants, species research, vandalism, etc."],
    ["Natural system modifications",7774],
    ["---Fire and fire suppression",4773,"Includes fires from human activity, including wildfires in excess of what would be expected absent human modification to the land."],
    ["---Dams and water management//use",2552],
    ["---Other ecosystem modification",980,"Examples include land reclamation projects, abandonment of managed lands, rip- rap along shoreline, mowing grass, tree thinning in parks, beach construction, removal of snags from streams, etc."],
    ["Invasive and other problematic species, genes, diseases",6064],
    ["---Invasive species/diseases",5372],
    ["---Problematic native species/diseases",1265,"Refers to native species/diseases that cause problems as a result of human activites. Does not include predation, disease, etc. that cannot be attributed to human activity."],
    ["---Introduced genetic material",59,"Examples include pesticide resistant crops, hatchery salmon, restoration projects using non-local seed stock, genetically modified insects for biocontrol, genetically modified trees, genetically modified salmon, etc."],
    ["---Problematic species/diseases of unknown origin",194],
    ["---Viral/prion-induced diseases",94,"Prions are misfolded proteins that cause additional proteins to misfold and lead to disease. Not necessarily resulting from human activity."],
    ["---Diseases of unknown origin",25],
    ["Pollution",4222],
    ["---Domestic and urban waste water",1805],
    ["---Industrial and military effluent",1270],
    ["---Agricultural and forestry effluents",3244],
    ["---Garbage and solid waste",251],
    ["---Air-borne pollutants",343],
    ["---Excess energy",68,"Light, thermal, or noise pollution."],
    ["Geological events",595],
    ["---Volcanoes",231],
    ["---Earthquake and tsunami",67],
    ["---Avalanches/landslides",350],
    ["Climate change and severe weather",3922,"This and all subcategories refer specifically to what can be attributed to anthropogenic climate change."],
    ["---Habitat shifting and alteration",1751],
    ["---Drought",1676],
    ["---Temperature extremes",768],
    ["---Storms and flooding",1043],
    ["---Other climate impacts",254],
    ["Other",234]
]

helper.save_image({
    "filename":"species_threat.jpg",
    "status":"Done",
    "details":"List of threats to species and number of species affected by each one. There are a lot, so feel free to consolidate if appropriate. Note that many species are threatened by more than one factor, so typically the sum of values in a category is less than the sum in its subcategories. The main purpose is to illustrate what are the most important issues from a biodiversity standpoint.",
    "table":species_threats_table,
    "references":["iucn"],
    "source_file":"biodiversity.py"
})

############################

# Current species loss

species_loss_table = [
    ["<b>Class</b>","<b>Loss rate from 1900 to 2014</b>"],
    ["Background rate",0.0002*1.14],
    ["Vertebrates overall",477./39223],
    ["Mammals",69./5513],
    ["Birds",80./10425],
    ["Reptiles",24./4414],
    ["Amphibians",146./6414],
    ["Fishes",158./12457]
]

helper.save_image({
    "filename":"species_loss.jpg",
    "status":"Done",
    "details":"Show portion of species lost from 1900 to 2014, as documented by IUCN. Also for comparison is the background rate, or the portion that would 'naturally' have gone extinct.",
    "table":species_loss_table,
    "references":["extinction_rate"],
    "source_file":"biodiversity.py"
})

#######################################

# Monetized damages from ecosystems

damages_table = [
    ["<b>Area</b>","<b>Annual Cost</b>","<b>Source</b>"],
    ["Loss of coral reefs","Gain of $765 billion to loss of $13.9 trillion","Costanza et al."],
    ["Loss of forests","$2.3 to $4.2 trillion","Costanza et al."],
    ["Loss of wetlands","$4.2 to $12.6 trillion","Costanza et al."],
#    ["Loss of ecosystem services from land use change","$5.5 to $25.7 trillion","Costanza et al."], # Base values were $4.3T to $20.2T, 2007 USD. I CPI-adjusted to 2020.
    ["Land degradation","$7.0 to $11.7 trillion","ELD Initiative"], # Base was $6.3-10.6T, adjusted from 2015.
    ["Poor management of oceans","$230 billion","UNDP and GEF"] # Base $200B, CPI adjusted from 2012.
]

helper.save_image({
    "filename":"ecosystem_damages.jpg",
    "status":"Done",
    "table":damages_table,
    "details":"I think this should be done more graphically, as there are monetary values to compare. I broke up the ecosystem services piece into multiple components, as I think it was too broad before. There are loss of coral reefs, forests, and wetlands. Among forests and wetlands, they are generally being converted into grassland, cropland, and cities, and the loss of ecosystem service value is offset by a gain of $255 billion to $4.8 trillion from the new biomes.",
    "references":["costanza","eld","ocean_finance","oecd_biodiversity"],
    "source_file":"biodiversity.py"
})

####################################

# Biomass figures.

# Based on https://www.pnas.org/content/115/25/6506, reference biomass_earth

# For most values, see Figures 1 and 2. Crops are stated about half way down
biomass_table = [
    ["<b>Lifeform</b>","<b>Estimated mass on Earth by carbon, billions of tons</b>","<b>Notes</b>"],
    ["Plants (non-crop)",440,"I don't have a detailed breakdown, but the paper says the majority of this is trees."],
    ["Crops",10],
    ["Bacteria",70],
    ["Fungi",12],
    ["Archaea",7,"Single-celled organisms that live most deep underground or underwater"],
    ["Protists",4,"Protists are single-celled eukaryotic (meaning that the cell nucleus is enclosed in a membrane) organisms, which excludes bacteria and archaea"],
    ["Animals",2],
    ["Viruses",0.2],
    ["<b>More detailed breakdown of animal biomass</b>","<b>Estimated mass on Earth by carbon, billions of tons</b>","<b>Notes</b>"],
    ["Arthropods",1,"Includes insects, spiders, crustaceans, millipedes, centipedes, mites, scorpions, among other animals."],
    ["Fish",0.7],
    ["Molluscs",0.2,"Includes snails, slugs, clams, oysters, squids, octopi, and other animals."],
    ["Annelids",0.2,"Includes earthworms, leeches, and other animals."],
    ["Cnidarians",0.1,"Includes jellyfish, sea anenomes, and other mostly aquatic animals."],
    ["Livestock",0.1],
    ["Humans",0.06],
    ["Nematodes",0.02,"Includes roundworms and related animals."],
    ["Wild Mammals",0.007,"Both land and sea."],
    ["Wild Birds",0.002]
]

helper.save_image({
    "filename":"earth_biomass.jpg",
    "status":"Done",
    "details":"World biomass by tons of carbon. Take a look at Figure 1 in the reference to see how they visualized the data with Voronoi diagrams (I made a slight change here by separating out crops from other plants).",
    "table":biomass_table,
    "references":["biomass_earth"],
    "source_file":"biodiversity.py"
})

####################################

# Changes in biomass over the last 50,000 years

biomass_change_table = [
    ["<b>Lifeform</b>","<b>Estimated mass on Earth by carbon, billions of tons, 50,000 years ago</b>","<b>Estimated mass on Earth today</b>"],
    ["Wild mammals, land",0.02, 0.003],
    ["Wild mammals, marine",0.02, 0.004],
    ["All mammals",0.04, 0.17],
    ["Fish",1.7, 0.7],
    ["Plants",900,450]
]

helper.save_image({
    "filename":"biomass_change.jpg",
    "status":"Done",
    "details":"Show how some kinds of biomass measures have changed over the last 50,000. The Quaternary extinction event began around that time, which roughly marks the beginning of major human transformation of the biosphere. Therefore, these figures give a full, albeit quite crude, view of aggregate human impact.",
    "table":biomass_change_table,
    "references":["biomass_earth"],
    "source_file":"biodiversity.py"
})

####################################

# Biome change from 1994 to 2014, from Costanza et al.

biome_table = [
    ["<b>Biome</b>","<b>Millions of hectares, 1997</b>","<b>Millions of hectares, 2011</b>","<b>Monetary Value, 2011, USD/ha/yr (2007)</b>","<b>Value change, low (trillions 2007 USD/year)</b>","<b>Value change, high</b>"],
    ["<b>Marine</b>",36302,36302,1368,0.6,-10.9],
    ["Open Ocean",33200,33200,660,0,0],
    ["<b>Coastal</b>",3102,3102,8944,0.6,-10.9],
    ["Estuaries",180,180,28916,0,0],
    ["Seagrass/Algae Beds",200,234,28916,0.9,1.0],
    ["Coral Reefs",62,28,352249,-0.3,-11.9],
    ["Shelf",2660,2660,2222,0,0],
    ["<b>Terrestrial</b>",15323,15323,4901,-4.9,-9.9],
    ["<b>Forest</b>",4855,4261,3800,-1.8,-3.3],
    ["Tropical Forest",1900,1258,5382,-1.8,-3.5],
    ["Temperate/Boreal Forest",2955,3003,3137,0,0.2],
    ["Grass/Rangelands",3898,4418,4166,0.2,2.2],
    ["<b>Wetlands</b>",330,188,140174,-2.8,-2.7],
    ["Tidal Marsh/Mangroves",165,128,193843,-0.5,-7.2],
    ["Swamps/Floodplains",165,60,25681,-2.8,-2.7],
    ["Lakes/Rivers",200,200,12512,0,0],
    ["Desert",1925,2159,0,0,0],
    ["Tundra",743,433,0,0,0],
    ["Ice/Rock",1640,1640,0,0,0],
    ["Cropland",1400,1672,5567,0,1.5],
    ["Urban",332,352,6661,0,0.1]
]

helper.save_image({
    "filename":"biome_change.jpg",
    "status":"Done",
    "table":biome_table,
    "details":"Show how major classes of biomes have changed in area from 1997 to 2011. The bold categories are aggregate categories, which entail two or more of the following subcategories. Put some thought into how best to present this one. There should be heavy emphasis on the amount of change of each biome, not just the absolute size (e.g. the fact that the open ocean hasn't changed in size isn't very interesting here). You may note that the urban area is different from the overall land use plot, as it comes from a different source. For the moment, ignore the monetary value column and value change columns; we might use it later for some other purpose.",
    "references":["costanza"],
    "source_file":"biodiversity.py"
})

####################################

# Mass extinction table.
# Figures are from Wikipedia; want more legitimate sources.

mass_extinction_table = [
    ["<b>Event</b>","<b>Proportion of species lost</b>","<b>Date, millions of years ago</b>","<b>Main cause</b>"],
    ["Ordovician-Silurian extinction events","85% (Holland)","450-440","Debated; possibly volcanism, gamma ray burst, asteroid impact (Gong et al.)"],
    ["Late Devonian extinction","70-80% (House)","375-360","Multiple asteroid impacts and volcanism (Barash)"],
    ["Permian-Triassic extinction event","80-96% (Nowak et al.)","252","Methane release, volcanism, asteroids (Sheldon)"],
    ["Triassic-Jurassic extinction event","76% (Britannica)","201.3","Volcanism (Blackburn et al.)"],
    ["Cretaceous-Paleogene extinction event","75%, including non-avian dinosaurs (Raup and Sepkoski)","66","Chicxulub impact (asteroid) (Schulte et al.)"],
    ["Holocene/Anthropocene","Threatened: 12.5% (IPBES), 16-30% (Roman-Palacios and Wiens)","0","Human activity"]
]

helper.save_image({
    "filename":"mass_extinction.jpg",
    "status":"Done",
    "table":mass_extinction_table,
    "details":"Some basic information about historical mass extinctions to put ongoing extinction in the long term context. I think it would be best to do this as a timeline, a horizontal bar with the six events broken out. The two studies cited for number of threatened species in modern times are based on two major recent reports; I don't know how reliable they are, nor do I have an estimate I am confident in of how many species have already been lost.",
    "references":["ordavician","ordavician_cause","devonian","barash","sheldon","nowak","triassic","triassic2","kpg","chicxulub","ipbes_assessment","pnas_extinction"],
    "source_file":"biodiversity.py"
})

#################################################

# Ecosystem service valuation by biome and service

# Using values in the 2014 Costanza paper and translating them into de Groot's biome presentation. Millions of ha
# Woodlands missing
# Other listed in Costanza but for which values are not available in de Groot: desert, tundra, ice/rock, cropland, urban.
biome_area = {
    "Marine":33200+2660, # Open ocean and shelf
    "Coral reefs":28,
    "Coastal systems":180+234, # Estuaries and seagrass/algae beds
    "Coastal wetlands":128, # Tidal Marsh/Mangroves
    "Inland wetlands":60, # Swamps/Floodplains
    "Fresh water (rivers/lakes)":200,
    "Tropical forest":1258,
    "Temperate forest":3003,
    "Grasslands":4418,
    "Woodlands":0
}

# Figures are in international dollars (2007)/ha/yr
value_by_service = {
    "Food":{
        "Marine":93,
        "Coral reefs":677,
        "Coastal systems":2384,
        "Coastal wetlands":1111,
        "Inland wetlands":614,
        "Fresh water (rivers/lakes)":106,
        "Tropical forest":200,
        "Temperate forest":299,
        "Woodlands":52,
        "Grasslands":1192
    },
    "Water":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":1217,
        "Inland wetlands":408,
        "Fresh water (rivers/lakes)":1808,
        "Tropical forest":27,
        "Temperate forest":198,
        "Woodlands":0,
        "Grasslands":60
    },
    "Raw Materials": {
        "Marine":8,
        "Coral reefs":21528,
        "Coastal systems":12,
        "Coastal wetlands":358,
        "Inland wetlands":425,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":84,
        "Temperate forest":181,
        "Woodlands":170,
        "Grasslands":53
    },
    "Genetic Resources":{
        "Marine":0,
        "Coral reefs":33048,
        "Coastal systems":0,
        "Coastal wetlands":10,
        "Inland wetlands":0,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":13,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":0
    },
    "Medicinal Resources":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":301,
        "Inland wetlands":99,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":1504,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":1
    },
    "Ornamental Resources":{
        "Marine":0,
        "Coral reefs":472,
        "Coastal systems":0,
        "Coastal wetlands":0,
        "Inland wetlands":114,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":0,
        "Temperate forest":0,
        "Woodlands":32,
        "Grasslands":0
    },
    "Air Quality Regulation":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":0,
        "Inland wetlands":0,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":12,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":0
    },
    "Climate Regulation":{
        "Marine":65,
        "Coral reefs":1188,
        "Coastal systems":479,
        "Coastal wetlands":65,
        "Inland wetlands":488,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":2044,
        "Temperate forest":152,
        "Woodlands":7,
        "Grasslands":40
    },
    "Disturbance Moderation":{
        "Marine":0,
        "Coral reefs":16991,
        "Coastal systems":0,
        "Coastal wetlands":5351,
        "Inland wetlands":2896,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":66,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":0
    },
    "Regulation of Water Flows":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":0,
        "Inland wetlands":5606,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":342,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":0
    },
    "Waste Treatment":{
        "Marine":0,
        "Coral reefs":85,
        "Coastal systems":0,
        "Coastal wetlands":162125,
        "Inland wetlands":3105,
        "Fresh water (rivers/lakes)":187,
        "Tropical forest":6,
        "Temperate forest":7,
        "Woodlands":0,
        "Grasslands":75
    },
    "Erosion Prevention":{
        "Marine":0,
        "Coral reefs":153214,
        "Coastal systems":25368,
        "Coastal wetlands":3929,
        "Inland wetlands":2607,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":15,
        "Temperate forest":5,
        "Woodlands":13,
        "Grasslands":44
    },
    "Nutrient Cycling":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":45,
        "Inland wetlands":1713,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":3,
        "Temperate forest":93,
        "Woodlands":0,
        "Grasslands":0
    },
    "Pollination":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":0,
        "Inland wetlands":0,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":30,
        "Temperate forest":0,
        "Woodlands":31,
        "Grasslands":0
    },
    "Biological Control":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":0,
        "Inland wetlands":948,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":11,
        "Temperate forest":235,
        "Woodlands":0,
        "Grasslands":0
    },
    "Nursery service":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":194,
        "Coastal wetlands":10648,
        "Inland wetlands":1287,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":16,
        "Temperate forest":0,
        "Woodlands":1273,
        "Grasslands":0
    },
    "Genetic Diversity":{
        "Marine":5,
        "Coral reefs":16210,
        "Coastal systems":180,
        "Coastal wetlands":6490,
        "Inland wetlands":1168,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":23,
        "Temperate forest":862,
        "Woodlands":3,
        "Grasslands":1214
    },
    "Esthetic Information":{
        "Marine":0,
        "Coral reefs":11390,
        "Coastal systems":0,
        "Coastal wetlands":0,
        "Inland wetlands":1292,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":0,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":167
    },
    "Recreation":{
        "Marine":319,
        "Coral reefs":96302,
        "Coastal systems":256,
        "Coastal wetlands":2193,
        "Inland wetlands":2211,
        "Fresh water (rivers/lakes)":2166,
        "Tropical forest":867,
        "Temperate forest":989,
        "Woodlands":7,
        "Grasslands":26
    },
    "Inspiration":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":0,
        "Coastal wetlands":0,
        "Inland wetlands":700,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":0,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":0
    },
    "Spiritual Experience":{
        "Marine":0,
        "Coral reefs":0,
        "Coastal systems":21,
        "Coastal wetlands":0,
        "Inland wetlands":0,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":0,
        "Temperate forest":0,
        "Woodlands":0,
        "Grasslands":0
    },
    "Cognitive Development":{
        "Marine":0,
        "Coral reefs":1145,
        "Coastal systems":22,
        "Coastal wetlands":0,
        "Inland wetlands":0,
        "Fresh water (rivers/lakes)":0,
        "Tropical forest":0,
        "Temperate forest":1,
        "Woodlands":0,
        "Grasslands":0
    }
}

service_table = [
    ["<b>Biome</b>","<b>Monetized value of ecosystem services, USD (2020)/hectare/year</b>"],
    ["Open ocean",660],
    ["Seagrass/Algae Beds/Estuaries",28916],
    ["Coral reefs",362249],
    ["Ocean shelf",2222],
    ["Tropical forest",5382],
    ["Temperate/boreal forest",3137],
    ["Grass/rangelands",4166],
    ["Tidal marsh/mangroves",193843],
    ["Swamps/floodplains",25681],
    ["Lakes/rivers",12512],
    ["Cropland",5567],
    ["Urban",6661],
    ["<b>Service</b>","<b>Monetized value (billions USD, 2020)</b>"]
]

for i in range(1,len(service_table)-1):
    service_table[i][1] *= 1.27445953

for key in value_by_service:
    total_value = 0
    for k in value_by_service[key]:
        total_value += value_by_service[key][k]*biome_area[k]/1000*1.27445953 # In billions of dollars, CPI-adjusted to 2020
    service_table = service_table + [[key,total_value]]
    
helper.save_image({
    "filename":"ecosystem_services",
    "status":"Done",
    "details":"Two in one here: value of ecosystem services by biome and by service. The biome figures are from Costanza et al. They lack valuations for desert, tundra, and rock/ice. By service, figures are reported in billions of dollars annually, CPI-adjusted to 2020. The per-hectare valuations are from de Groot et al, while I got total area from Costanza et al. Nursery services refer to the value of ecosystems for growing fish for commercial fisheries and other wildlife of economic value. Cognitive development refers to the value of nature in education. Inspiration means inspiration for art, culture, design, etc. Biological control is stuff like seed disperal, pest control, etc. Waste treatment includes water and soil treatment and noise control. Disturbance moderation includes storm and fire protection, etc. The rest should be self-explanatory I hope. The two sources have somewhat different valuations in some cases, so numbers won't line up perfectly.",
    "table":service_table,
    "references":["costanza","degroot"],
    "source_file":"biodiversity.py"
})

######################## Bird deaths

bird_death_chart = [
    ["<b>Cause</b>","<b>Number of birds in the US (millions)</b>"],
    ["Buildings",550],
    ["Power Lines",130],
    ["Cats",100],
    ["Cars",80],
    ["Pesticides",67],
    ["Communication Towers",4.5],
    ["Wind Turbines",0.0285],
    ["Airplanes",0.025],
    ["Other","Not Estimated"]
]

helper.save_image({
    "filename":"bird_deaths.jpg",
    "status":"Done",
    "details":"Cause of bird deaths in the US. Only anthropogenic (human-caused) deaths are assessed.",
    "table":bird_death_chart,
    "references":["bird_deaths"],
    "source_file":"biodiversity.py"
})

###################### Effectiveness of conservation

cons_eff_table = [
    ["<b>Birds</b>","<b></b>Value"],
    ["Extinct in the Wild",368],
    ["Conserved",48],
    ["Species Saved","21-32"],
    ["<b>Mammals</b>","<b></b>Value"],
    ["Extinct in the Wild",263],
    ["Conserved",25],
    ["Species Saved","7-16"]
]

helper.save_image({
    "filename":"cons_eff.jpg",
    "status":"Done",
    "details":"Effectiveness of conservation measures, in this case measured by number of species saved. For birds and mammals, I am showing the number of threatened species identified, defined by extinction in the wild and endangered or critically endangered by the IUCN; the number of species that have had conservation programs; and the number of species saved, which the authors determine by subtracting out those that would have likely survived without a program.",
    "table":cons_eff_table,
    "references":["conservation_effectiveness"],
    "source_file":"biodiversity.py"
})

###################### Population of taxa

pop_table = [
    ["<b>Taxon</b>","<b>Population</b>"],
    ["Marine Prokaryrote","1.2 X 10^29"],
    ["Soil Prokyraote","4 X 10^29"],
    ["Marine Subsurface Prokaryrote","4 X 10^29"],
    ["Terrestrial Subsurface Prokaryrote","2 X 10^30"],
    ["Fungal Cells","10^27"],
    ["Molluscs","5 X 10^17"],
    ["Fish","10^15"],
    ["Terrestrial Arthropods","10^18"],
    ["Copepods (Marine Arthropods)","10^20"],
    ["Cnideria","2 X 10^16"],
    ["Terrestrial Protists","3 X 10^25"],
    ["Marine Protists","10^27"],
    ["Wild Birds","3 X 10^11"],
    ["Livestock","10^10"],
    ["Humans","8 X 10^9"],
    ["Wild Mammals","2.5 X 10^13"],
    ["Annelids","10^18"],
    ["Nematodes","3.8 X 10^20"],
    ["Viruses","10^31"],
    ["Trees","3 X 10^12"]
]

helper.save_image({
    "filename":"earth_pop.jpg",
    "status":"Done",
    "details":"Population of major taxa. Note that I am using scientific notation and these figures differ by orders of magnitude, which could present a challenge in displaying it well. John wanted to avoid a logarithmic plot and use blowouts if possible, but go ahead with a logarithmic plot if that is the only feasible method. The tree figure comes from Crowther and the rest come from Bar-On et al.",
    "table":pop_table,
    "references":["biomass_earth","tree_census"],
    "source_file":"biodiversity.py"
})

####################### Required spending in conservation programs.

needed_spending_table = [
    ["<b>Outcome</b>","<b>Spending required</b>"],
    ["Conserve Birds","$0.875 to $1.23 billion"],
    ["Conserve All Endangered Species","$3.41 to $4.76 billion"],
    ["Actual Spending, 2001-08","21.5 billion"],
    ["Protect All Bird Habitat","$65.1 billion"],
    ["Protect All Endangered Species Habitat","76.1 billion"],
    ["Ecosystem Service Benefit of Conservation","2-6 trillion"]
]

helper.save_image({
    "filename":"conservation_spending.jpg",
    "status":"Done",
    "details":"Spending required for conservation programs, as well as possible benefits. These are annual spending figures. Actual spending figures are from Barbosa and Tella, and the others are from McCarthy et al.",
    "table":needed_spending_table,
    "references":["conservation_spending","lears_macaw"],
    "source_file":"biodiversity.py"
})

########################### Summary of willingness to pay studies

wtp_table = [
    ["<b>Species</b>","<b>Annual Willingness to Pay</b>"],
    ["Bald Eagle",39],
    ["Bighorn Sheep",17],
    ["Dolphin",36],
    ["Gray Whale",35],
    ["Owl",65],
    ["Salmon/Steelhead",81],
    ["Sea Lion",71],
    ["Sea Otter",40],
    ["Sea Turtle",19],
    ["Seal",35],
    ["Silvery Minnow",38],
    ["Squawfish",12],
    ["Stiped Shiner (type of fish)",8],
    ["Turkey",13],
    ["Whooping Crane",56],
    ["Wookpecker",16],
    ["<b>Species</b>","<b>One-Time Willingness to Pay</b>"],
    ["Arctic Grayling (type of fish)",23],
    ["Bald Eagle",297],
    ["Falcon",32],
    ["Humpback Whale",240],
    ["Monk Seal",166],
    ["Wolf",61]
]

helper.save_image({
    "filename":"wtp_conservation.jpg",
    "status":"Done",
    "details":"Results of some willingness to pay studies for Americans. They are divded into annual payments and one-time payments.",
    "table":wtp_table,
    "references":["wtp_cons"],
    "source_file":"biodiversity.py"
})

#################### De-extinction graphic

deext_table = [
    ["<b>Scenario</b>","<b>Species Saved</b>"],
    ["Externally sponsored de-extinction",1.5],
    ["Conventional Conservation",6]
]

helper.save_image({
    "filename":"deextinct.jpg",
    "status":"Done",
    "details":"Number of species saved in New Zealand and New South Wales by two methods, using the same amount of money.",
    "table":deext_table,
    "references":["deextinct2"],
    "source_file":"biodiversity.py"
})