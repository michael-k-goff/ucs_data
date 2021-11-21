# Precision agriculture figures

import helper

table = [
    ["<b>Technique</b>","<b>Metric</b>","<b>Effect</b>"],
    ["Variable rate nutrient application","Nitrogen applied","4-46% savings"],
    ["Variable rate nutrient application","Yield gain","1-10%"],
    ["Precision irrigation systems","Water used","35% decrease to 14% increase"],
    ["Machine guidance","Fuel savings","6.3-10.4%"],
    ["Controlled traffic farming","Fuel savings","25-35%"],
    ["Controlled traffic farming","Fertilizer savings","10-15%"],
    ["Controlled traffic farming","Pesticide savings","25%"],
    ["Controlled traffic farming","Yield gain","5-15%"],
    ["Variable rate pesticide application","Pesticide savings","11-90%"],
    ["Variable rate seeding","Yield gain","3-6.5%"],
    ["Precision weeding","Yield gain","15-20%"]
]

helper.save_image({
    "filename":"precision_ag.jpg",
    "status":"Done",
    "table":table,
    "details":"This is a sampling of benefits from various precision agriculture techniques. They all are cited in the meta-analysis below, but dozens of studies were incorporated into the numbers above. Emphasize in the graphic that the numbers are the result of a fairly limited number of demonstration projects.",
    "references":["precision_ag"],
    "source_file":"precision_ag.py"
})