# Rebound effect stuff. Note: there is also a rebound.py in the parent folder, which is different stuff.

import helper

rebound_studies = [
    ["<b>Field</b>","<b>Observation</b>","<b>Source</b>"],
    ["Farming","Improved yields increase overall food production","Ewers et al."], # ag_rebound
    ["Water","Improved irrigation efficiency increases water usage","Li and Zhao"], # water_rebound2
    ["Water","Improved irrigation efficiency increases water usage","Loch and Adamson"], # water_rebound
    ["Raw Materials","Material efficiency increases demand for products","Pfaff and Satorious"], # pfaff
    ["Primary Metals","Efficiency in primary metal uses increases demand","Lifset and Eckelman"], # material_efficiency
    ["Recycling and Remanufacturing","Recycling and remanufacturing can increase demand for products","Zink and Geyer"], # recycling_rebound
    ["Aquaculture","Aquaculture has mostly supplemented, rather than replaced, wild catch","Longo et al."] # aquaculture_rebound
]

helper.save_image({
    "filename":"nonenergy_rebound.jpg",
    "status":"Done",
    "table":rebound_studies,
    "details":"Summary of rebound effects observed from non-energy sectors. More could be added over time as appropriate. This data was previously included in the site as a paragraph of text, but I think it will work better as an infographic.",
    "references":["ag_rebound","water_rebound2","water_rebound","pfaff","material_efficiency","recycling_rebound","aquaculture_rebound"],
    "source_file":"rebound.py"
})