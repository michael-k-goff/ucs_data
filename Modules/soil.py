# Calculations on soil health. Initially erosion; we'll see if there are more later.

import helper

erosion_table = [
    ["<b><Source/b>","<b>Mean Erosion Rate: millimeters/year</b>"],
    ["Conventional agriculture",3.939],
    ["Conservation agriculture",0.124],
    ["Native vegetation",0.053],
    ["Geological processes",0.173],
    ["Soil production",0.036]
]

helper.save_image({
    "filename":"erosion.jpg",
    "status":"Done",
    "table":erosion_table,
    "details":"Average rates of erosion worldwide from conventional and conservation agriculture, compared with natural processes. Distinguish the 'soil production' value because that's adding to the soil supply over time, while the others are taking away. The idea of adding some material on erosion is based on a conversation we had a while ago, and this is now to be seen on the environmental impacts of agriculture page under Soil Health. It occurs to me that erosion is only one aspect of soil health, and perhaps we will address the others at some point.",
    "references":["erosion"],
    "source_file":"soil.py"
})

carbon_table = [
    ["<b>Action</b>","<b>Gain or loss of soil carbon</b>","<b>Notes</b>"],
    ["Converting native to agricultural soils","-18% to -30%","Study conducted in Canada specifically"],
    ["Converting cropland to grassland","+13-16%",""],
    ["Afforesting former cropland","+19-53%",""]
]

helper.save_image({
    "filename":"soil_carbon.jpg",
    "status":"Done",
    "table":carbon_table,
    "details":"Some figures on the effect of various land conversions on soil carbon. Negative values indicate a loss of carbon and positive values are a gain. I would also like to have some figures on agricultural practices, such as crop rotation, but this is enough for starters.",
    "references":["c_cycle_report"],
    "source_file":"soil.py"
})