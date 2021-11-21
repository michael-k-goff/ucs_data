# Calculations and plots related to heat islands.

import helper

heat_table = [
    ["<b>City</b>","<b>Effect of heat island &deg;(C)</b>"],
    ["38 largest cities in the US, yearround average","2.9"], # heat_island1
    ["38 largest cities in the US, summer","4.3"], # heat_island1
    ["38 largest cities in the US, winter","1.3"], # heat_island1
    ["Top 5% of world cities","1.72"], # heat_island2
    ["Median world cities","0.70"], # heat_island2
    ["Cities in humid climates","3.0"], # heat_island3
    ["Cities in dry climates","-1.5"] # heat_island3
]

helper.save_image({
    "filename":"heat_island.jpg",
    "status":"Done",
    "details":"A plot showing the heat island effect for various cities or groups of cities. The US figures are from Imhoff et al., the world figures from Estrada et al, and Zhao et al. estimate figures for humid and dry cities. In the latter, they estimate the impact of climate change on UHI and give several estimates of warming; the 2015 figures are used here.",
    "table":heat_table,
    "references":["heat_island1","heat_island2","heat_island3"],
    "source_file":"heat_island.py"
})

########################################

# Fraction of heat wave deaths attributable to UHI

deaths_table = [
    ["<b>Fraction of heat wave deaths attributable to UHI</b>","<b>Source and Explanation</b>"],
    ["0.42%","Ho Chi Minh City, Dang et al."],
    ["52%","West Midlands, UK in the August 2003 heat wave, Heaviside et al."]
]

helper.save_image({
    "filename":"uhi_deaths.jpg",
    "status":"Done",
    "details":"Some estimates of what fraction of heat wave deaths are due to UHI. Estimates vary widely and I would like to have a few more eventually.",
    "table":deaths_table,
    "references":["uhi_hcmc","uhi_midlands"],
    "source_file":"heat_island.py"
})