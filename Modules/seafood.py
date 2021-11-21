import helper

# aquaculture_land
aq_land_table = [
    ["<b>Product</b>","<b>Land use, m<sup>2</sup>/kg/year</b>"],
    ["Farmed Salmon",6.0],
    ["Chicken",12.5],
    ["Beef",33],
    ["Pig","5.4-15"],
    ["Bread",1.5],
    ["Tilapia (Extensive)",1.193],
    ["Tilapia (Intensive)",10.711],
    ["Bivalves",0],
    ["Catfish",10.5],
    ["Milkfish",18.5],
    ["Carp","8-11.5"],
    ["Diadromous fish, miscellaneous (migrate between fresh and salt water)",9.5],
    ["Marine fish, misc.",11],
    ["Shrimp",13],
    ["Tilapia (Gephart)",15.5],
    ["Salmons, Trouts, Smelts (Gephart)","3.6-5"]
]

helper.save_image({
    "filename":"aquaculture_land_use.jpg",
    "status":"Not Done",
    "details":"A basic comparison of land use for aquaculture (farmed salmon in particular) and some other foods. Everything from Farmed Salmon to Bread is from Mungkung and Sheewala, the tilapia figures are from Guzmán-Luna et al., and everything from bivalvues down are from Gephart. Bivalves (clams, oysters, cockles, mussels, scallops, etc.) do not require terrestrial feed and so that is why land use is zero.",
    "table":aq_land_table,
    "references":["aquaculture_land","aq_land","seafood_impact2"],
    "source_file":"seafood.py"
})

#####################################

# Fishing methods

method_table = [
    ["<b>Method</b>","<b>Millions of tons of fish caught</b>","<b>Notes</b>"],
    ["Bottom Trawl",29.74281,"Large nets to scoop the seafloor. Of greatest environmental concern."],
    ["Pelagic Trawl",11.66973,"Uses large nets, but unlike bottom floor, scoops midwaters instead of the seafloor."],
    ["Purse Seine",22.9359,"Uses a vertical net, rather than the horizontal net of trawling."],
    ["Small Scale",26.81864,"Small scale operations shown here, with additional type of gear not reported"],
    ["Gillnet",3.18773,"Net is a wall or curtain in the water without seafloor contact."],
    ["Longline",3.08408,"A long line with baited hooks is hung behind the fishing vessel."],
    ["Other Gear",4.02083],
    ["Unknown Gear",7.87628]
]

helper.save_image({
    "filename":"fishing_gear.jpg",
    "status":"Not Done",
    "table":method_table,
    "details":"Total amount of wild catch fishing (not aquaculture) as reported from Sea Around Us, by type of gear used, as of 2018. They in turn pull official data from FishStat from FAO, and some unreported data. I'm not sure the details; they have a <a href=\"https://www.seaaroundus.org/catch-reconstruction-and-allocation-methods/\">methodology paper</a> which I only skimmed. Notes on types of fishing gear are mostly shown in an illustration from Our World in Data. The sum differs a bit from the wild catch figures from the FAO source, I presume because of different methodology.",
    "references":["seaaroundus","owid_fishing"],
    "source_file":"seafood.py"
})

#####################################

# Overall production

seafood_production = [
    ["<b>Product</b>","<b>Quantity, millions of tons</b>","<b>Notes</b>"],
    ["Freshwater Fish",62.39232],
    ["Demersal Fish",23.25347,"Near the bottom of lakes or seas"],
    ["Pelagic Fish",34.78956,"In the midwaters of oceans or seas"],
    ["Other Marine Fish",9.63334],
    ["Crustaceans",15.185],
    ["Cephalopods",3.7406],
    ["Other Molluscs",19.94241],
    ["Other Aquatic Animals",1.37814],
    ["Aquatic Plants",32.92435]
]

helper.save_image({
    "filename":"seafood_production.jpg",
    "status":"Not Done",
    "table":seafood_production,
    "details":"Overall seafood production as of 2019, the most recent year for which FAOSTAT reports data. Figures include aquaculture and wild catch.",
    "references":["faostat"],
    "source_file":"seafood.py"
})

####################################

# Overfishing

helper.save_image({
    "filename":"overfish.jpg",
    "status":"Not Done",
    "table":[
        ["<b>Status</b>","<b>By fishery</b>","<b>By ton of seafood</b>"],
        ["Overfished","34.2%","21.3%"],
        ["Maximally Fished","61.6%","78.7%"],
        ["Underfished","6.2%","---"]
    ],
    "details":"According to the UW Fisheries explainer, a fishery is 'overfished' for the purpose of these statistics if it has less than 80% of the fish biomass for optimum yields. I'm not sure the definition of 'underfished'. I also don't have in the FAO report a separate statistic for the share of seafood by tonnage that comes from underfished fisheries, so the 78.7% figure is the sum of maximally fished and underfished.",
    "references":["uw_overfishing","fisheries2020"],
    "source_file":"seafood.py"
})