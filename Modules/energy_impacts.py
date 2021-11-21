# Environmental impacts of energy

import helper

impact_table = [
    ["<b>Type of car</b>","<b>kg minerals per vehicle</b>"],
    ["Internal combustion engine",35],
    ["Electric car",205],
    ["<b>Power Source</b>","<b>kg minerals per MW</b>"],
    ["Natural Gas",1200],
    ["Coal",2500],
    ["Nuclear",5200],
    ["Solar PV",6800],
    ["Onshore Wind",10000],
    ["Offshore Wind",15500]
]

helper.save_image({
    "filename":"energy_car_material.jpg",
    "status":"Done",
    "table":impact_table,
    "details":"For power sources, this is similar to the existing plot on material usage, but this one excludes some bulk, low-impact (per ton) materials including steel, aluminum, and glass, focusing on more expensive and higher impact materials. Specifically, the list of materials assessed include copper, lithium, nickel, manganese, cobalt, graphite, chromium, molybdenum, zinc, rare earths, silicon, and 'other' (which makes a negligible contribution in all cases).",
    "references":["iea_mining"],
    "source_file":"energy_impacts.py"
})