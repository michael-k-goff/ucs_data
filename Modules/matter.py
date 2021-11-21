# Plots and data related to matter on the space page.

import helper

helper.save_image({
    "filename":"dark_comp.jpg",
    "status":"Done",
    "details":"Basic composition of the universe.",
    "table":[
        ["<b>Substance</b>","<b>Share of Mass-Energy in the Universe</b>"],
        ["Dark Energy","71.4%"],
        ["Dark Matter","24%"],
        ["Ordinary (Baryonic) Matter","4.6%"]
    ],
    "references":["dark"],
    "source_file":"matter.py"
})

helper.save_image({
    "filename":"baryonic_comp.jpg",
    "status":"Done",
    "details":"Baryonic matter by element, at least that of baryonic matter that is atomic, which I believe is most of it.",
    "table":[
        ["<b>Element</b>","<b>Share of Baryonic Matter</b>"],
        ["Hydrogen","75%"],
        ["Helium","23%"],
        ["Oxygen","1%"],
        ["Carbon","0.5%"],
        ["Other Elements","0.5%"]
    ],
    "references":["element_composition"],
    "source_file":"matter.py"
})

helper.save_image({
    "filename":"baryonic_comp2.jpg",
    "status":"Done",
    "details":"A second plot showing the composition of baryonic matter, this time by macroscopic type of substance. I'm not sure why the second is intracluster (within galaxy clusters) as opposed to intragalactic, but it is.",
    "table":[
        ["<b>Substance</b>","<b>Share of Baryonic Matter</b>"],
        ["Intergalactic Plasma","89%"],
        ["Intracluster Plasma","4%"],
        ["Main-sequence Stars (such as the Sun)","4.6%"],
        ["White Dwarfs","0.8%"],
        ["Neutron Stars","0.11%"],
        ["Black Holes","0.16%"],
        ["Substellar Objects, such as Brown Drawfs","0.31%"],
        ["Planets","0.0022%"],
        ["Other","Small quantities"]
    ],
    "references":["fukugita"],
    "source_file":"matter.py"
})