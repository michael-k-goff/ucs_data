# Biomass plots

import helper

helper.save_image({
    "filename":"biofuel_prices.jpg",
    "status":"Done",
    "details":"I just noticed the figures are off and these are prices per megajoule, not gigajoule. To get prices per GJ, multiply all cost figures by 1000. So for instance it would be $9/GJ for sugarcane ethanol all the way to $45/GJ for microalgae.",
    "references":[],
    "source_file":"biomass.py"
})

helper.save_image({
    "filename":"img2019_06_11_liquid_land.jpg",
    "status":"Done",
    "details":"Where the upper and lower bar are the same value, just use one bar.",
    "references":[],
    "source_file":"biomass.py"
})

helper.save_image({
    "filename":"biofuel_potential.jpg",
    "status":"Done",
    "details":"Some information about the production potential of bioenergy.",
    "table":[
        ["<b>Source of Bioenergy</b>","<b>Annual production potential, exajoules, low estimate</b>","<b>Annual production potential, exajoules, high estimate</b>"],
        ["Agricultural residues, food waste",37,65],
        ["Forest biomass",27,43],
        ["Bioenergy crops",33,39],
        ["Total",97,147]
    ],
    "references":["iea_biofuel"],
    "source_file":"biomass.py"
})