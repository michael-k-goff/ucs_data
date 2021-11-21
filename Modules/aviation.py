# Aviation plots

import helper

fuel_table = [
    ["<b>Feedstock</b>","<b>Conversion Method</b>","<b>Greenhouse gas emissions, grams CO<sub>2</sub>e/MJ</b>","<b>Share of conventional jet fuel</b>"],
    ["Conventional","","87.5","100%"],
    ["Cooking Oil","Hydroprocessed esters and fatty acids","27","(You can calculate all these)"],
    ["Jatropha","Hydroprocessed esters and fatty acids","55"],
    ["Camelina","Hydroprocessed esters and fatty acids","47"],
    ["Willow","Fischer–Tropsch","9"],
    ["Poplar","Fischer–Tropsch","9"],
    ["Corn Stover","Fischer–Tropsch","13"],
    ["Forestry Residue","Fischer–Tropsch","6"],
    ["Forestry Residue (in situ)","Hydrothermal liquefaction","18"],
    ["Forestry Residue (ex situ)","Hydrothermal liquefaction","20"],
    ["Forestry Residue (in situ)","Pyrolysis","22"],
    ["Forestry Residue (ex situ)","Pyrolysis","40"],
    ["Corn","Alcohol to jet","55"],
    ["Corn Stover","Alcohol to jet","35"],
    ["Sugar Cane","Alcohol to jet","26"],
    ["Sugar Cane (increased blend)","Direct sugars to hydrocarbons","72"],
    ["Sugar Cane (10% blend)","Direct sugars to hydrocarbons","44"],
    ["Electrofuels (Sweden)","Electrolysis","17.1"]
]

helper.save_image({
    "filename":"aviation_fuel.jpg",
    "status":"Done",
    "details":"The electrofuels option is assessed in Katebi and Carlsson; the rest are in the other source. I think the most important data to highlight in the absolute emissions. There is also the share of conventional jet fuel, which I think is necessary for comparison, but the reader will be able to see that fairly well even if it is not explicitly shown. This plot might be extended later to show hydrogen fuel cells or liquid hydrogen.",
    "references":["aviation_fuel_ghg","electrofuel_ghg"],
    "table":fuel_table,
    "source_file":"aviation.py"
})