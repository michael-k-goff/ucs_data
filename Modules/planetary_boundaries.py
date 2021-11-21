# Planetary boundaries. These are graphics for the Environmental Challenges (or whatever I rename it to) page. Other things on the main Environment page will go here for now.

import helper

planetary_boundaries_table = [
    ["<b>Environmental Challenge</b>","<b>Status</b>"],
    ["Biosphere Integrity","Critical"],
    ["Biogeochemical Flows","Critical"],
    ["Climate Change","Approaching Critical"],
    ["Land-system Change","Approaching Critical"],
    ["Novel Entities","Not Critical"],
    ["Ozone Depletion","Not Critical"],
    ["Ocean Acidification","Not Critical"],
    ["Freshwater Usage","Not Critical"],
    ["Aerosol Loading","Not Critical"]
]

helper.save_image({
    "filename":"planetary_boundaries.jpg",
    "status":"Done",
    "table":planetary_boundaries_table,
    "details":"Produce an infographic showing the nine planetary boundaries, as characterized by the Stockholm Resilience Center, and what they assess to be their current status. This table was already on the site, but it is one that I think should be in a graphical form. This is likely to be one of the first things a reader sees if they go through the sections in order, and keep in mind that one of the things we want to do is to invite the reader to review the rest of the site as we go into more detail on some of these topics. I don't yet know if we will have dedicated material on all of them, though.",
    "references":["planetary_boundaries"],
    "source_file":"planetary_boundaries.py"
})

####################################################

# Sources of nitrogen. See reference fowler

import helper

n_table = [
    ["<b>Source of reactive nitrogen</b>","<b>Millions of tons per year</b>","<b>Artificial or natural?</b>"],
    ["Fixed by natural terrestrial ecosystems",58,"Natural"],
    ["Fixed by oceans",140,"Natural"],
    ["Lightning",5,"Natural"],
    ["Fixed by agricultural crops",60,"Artificial"],
    ["Combustion of fossil fuels",40,"Artificial"],
    ["Industrial Production (mostly fertilizer)",120,"Artificial"]
]

helper.save_image({
    "filename":"nr_sources.jpg",
    "status":"Done",
    "table":n_table,
    "details":"Show creation of reactive nitrogen. This chart is only showing creation, not transfer of N<sub>r</sub> from one part of the environment to another. The numbers are all from Fowler et al. Note, via Galloway et al., that natural N<sub>2</sub> fixing has decreased somewhat since the start of the Industrial Revolution, but this offsets only a small portion of artificial sources.",
    "references":["fowler","galloway"],
    "source_file":"planetary_boundaries.py"
})

##########################################

# Monetized damages from nitrogen.

nr_damage_table = [
    ["<b>Source of damages</b>","<b>Low estimate, dollars per kilogram N</b>","<b>high estimate</b>"],
    ["Health impacts",10,30],
    ["Health impacts, secondary particles",2,20],
    ["Greenhouse gas effect from N<sub>2</sub>O",5,15],
    ["Ecosystem impact, N-runoff",5,20],
    ["Ecosystem impact, N-deposition",2,10],
    ["Health from NO<sub>3</sub> in drinking water",0,4],
    ["Stratospheric ozone depletion",1,3],
    ["Total",25,102]
]

exchange_rate = 1.39 * 1.17141 # Convert 2011 Euros to 2020 USD.

for i in range(1,len(nr_damage_table)):
    nr_damage_table[i][1] *= exchange_rate
    nr_damage_table[i][2] *= exchange_rate
    
helper.save_image({
    "filename":"nitrogen_damages.jpg",
    "status":"Done",
    "table":nr_damage_table,
    "details":"Monetized damages of nitrogen pollution, as measured in the EU. I converted the figures to 2020 US Dollars. They are assessed per kilogram of N that is released into the environment. Note, via Keeler et al., that damages depend very much on the site the pollutant is released.",
    "references":["nr_damages","minn_n"],
    "source_file":"planetary_boundaries.py"
})

# Estimating total world damages. The report says 70-320 billion Euros for the EU
# The latter terms are the ratios of world to EU N application, which I am crudely assuming are proportional to all damages.

damages_low = 70*exchange_rate * 109137240.84 / 11343786.1
damages_high = 320*exchange_rate * 109137240.84 / 11343786.1
#print(damages_low)
#print(damages_high)

####################################

# Sources of eutrophication. See Poore and Nemecek, Table S17
eutrophication_table = [
    ["<b>Source</b>","<b>Eutrophication, millions of tons of PO<sub>4</sub><sup>3</sup>-equivalent</b>"],
    ["Savannah burning",0.2],
    ["Crop production for food, including land use change",25.1+0.2],
    ["Crop production for feed, including land use change",20.3+0.3],
    ["Livestock/aquaculture/fisheries",15.9+0.3],
    ["Food processing and distribution",3.0],
    ["Non-food",84.2-65.3]
]

helper.save_image({
    "filename":"eutrophication.jpg",
    "status":"Done",
    "details":"Show main sources of eutrophication-driving pollution. It's not just nitrogen; the units themselves are given in terms of phosphorous. It's based on Table S17 in Poore and Nemecek, though I consolidated some of their categories for simplicity.",
    "table":eutrophication_table,
    "references":["poore"],
    "source_file":"planetary_boundaries.py"
})