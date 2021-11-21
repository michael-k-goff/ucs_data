# Plots and calculations related to orbital debris

import helper

helper.save_image({
    "filename":"num_orbital_debris.jpg",
    "status":"Done",
    "details":"Some estimates of how much orbital debris there is.",
    "table":[
        ["<b>Size Range</b>","<b>Number of Pieces in Earth Orbit</b>"],
        ["10+ cm",23000],
        ["1-10 cm",500000],
        ["1 mm to 1 cm",100000000]
    ],
    "references":["num_debris"],
    "source_file":"orbital_debris.py"
})