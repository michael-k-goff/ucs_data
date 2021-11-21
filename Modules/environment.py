# Monetized damage from environmental problems

import helper

# This image is for the Society Overview page. See the other pages throughout the site for details on where the numbers come from.
env_table = [
    ["<b>Environmental challenge</b>","<b>World monetized damages, billions of dollars per year</b>"],
    ["Climate Change","2000"],
    ["Loss of Coral Reefs","-765 to 13900"],
    ["Loss of Forests","2300-4200"],
    ["Loss of Wetlands","4200-12600"],
    ["Land Degradation","7000-11700"],
    ["Ecosystem Services Gain from Grassland, Crops, Cities","-4800 to -255"],
    ["Poor Management of Oceans","230"],
    ["Ozone Depletion","86-199"],
    ["Lead Exposure","1155"], # This comes from the plot on the chemical exposure page and contradicts the one on the air pollution page
    ["Organophosphate Pesticide Exposure (US and EU only)","249"],
    ["PDBE Exposure (US and EU only)","279"],
    ["Endocrine Disruptor Exposure (US and EU only)","557"],
    ["Air Pollution (ambient and indoor)","3767"],
    ["Water Pollution and Poor Sanitation","404"],
    ["Nitrogen Pollution","1000-5000"],
    ["World GDP in 2018","85910"]
]

helper.save_image({
    "filename":"monetized_env.jpg",
    "status":"Done",
    "table":env_table,
    "details":"This is an overall comparison of monetized costs of various environmental problems discussed throughout the site. These are all very rough estimates to begin with, so it should really be taken as more of an order of magnitude kind of estimate. World GDP is from the reference. All other figures are from the various other pages that discuss the issue in greater detail. One idea I've had is to compare this to monetized costs from other social issues, like crime, disease, maybe overall damages from COVID-19 once the dust settles, military spending, warfare, etc.; we'll revisit that later. If you go ahead with a bar plot here, be careful that the World GDP figure doesn't cause the others to be dwarfed. Also be sure to visually distinguish GDP from the others. The ecosystem services gain from grassland, crops, cities is negative because that those land uses are growing, but they are coming at the expense of larger losses from forests and wetlands.",
    "references":["world_bank_gdp"],
    "source_file":"environment.py"
})