# Material use in cities and related plots

import helper

helper.save_image({
    "filename":"density_embodied.jpg",
    "status":"Done",
    "details":"A simple plot that shows how energy and emissions embodied in materials varies by density. By 'embodied' I mean how much energy or emissions were required to make the building materials. Emissions figures are 597 kg CO<sub>2</sub>e/capita for low density construction (assumes 50 year life) and 391 in high density. Energy figures are 7365 MJ/year/cap for low density and 4678 for high density. Both energy and emissions figures are on an annual basis, even though the costs of construction are incurred up-front, so we can better compare then to other quantities. In this context, high density refers to a 15 story apartment building near downtown Toronto, and low density refers to an average detached house in a Toronto suburb.",
    "references":["toronto"],
    "source_file":"cities_material.py"
})

######################################################

# Embodied energy, but this time I think in everything instead of just construction

embodied_table = [
    ["<b>Scenario</b>","<b>Embodied Energy, GJ</b>"],
    ["Passive House, Suburban",2211],
    ["Low Energy House, Suburban",1904],
    ["Normal House, Suburban",1720],
    ["Passive House, Urban",1531],
    ["Low Energy House, Urban",1318],
    ["Normal House, Urban",1191]
]

helper.save_image({
    "filename":"density_embodied2.jpg",
    "status":"Done",
    "details":"A comparison of embodied energy. The suburban house is a 130 m^2 detached house in a suburb of Brussels, and the urban house is a 90 m^2 apartment near downtown Brussels. Unlike the first embodied energy plot, this one counts lifetime energy, not per year. I think it assessed embodied energy in construction and consumer goods, though I'm not 100% sure what all is counted here. The 'Normal House' is based on standard construction techniques for that type of house, based on the Energy Performance of Buildings Directive of the EU. The key message here is to compare the urban and suburban versions equivalents and show that this distinction has a bigger impact than the Passive/Low Energy/Normal distinction.",
    "table":embodied_table,
    "references":["density_embodied"],
    "source_file":"cities_material.py"
})