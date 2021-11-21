# Infrastructure

import helper

interstate_table = [
    ["<b>Year Range</b>","<b>Spending per mile (2016 dollars)</b>"],
    ["1958-1963",8.50],
    ["1964-1969",8.91],
    ["1970-1975",11.68],
    ["1976-1981",16.18],
    ["1982-1987",24.57],
    ["1988-1993",34.25]
]

helper.save_image({
    "filename":"interstate_cost.jpg",
    "status":"Done",
    "details":"This is for a section of the website that discusses drivers of infrastructure cost. For that we illustrate the cost per mile of the Interstate highway system in the US. These figures are averaged over year ranges, since looking at individual years would give much more stochastic results.",
    "table":interstate_table,
    "references":["brookings_inf_cost"],
    "source_file":"infrastructure.py"
})

helper.save_image({
    "filename":"interstate-cost.jpg",
    "status":"Done",
    "details":"",
    "table":interstate_table,
    "references":[],
    "source_file":"infrastructure.py"
})