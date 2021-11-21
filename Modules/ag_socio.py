# Socioeconomics of agriculture

import helper

helper.save_image({
    "filename":"urbanization_rate.jpg",
    "status":"Done",
    "details":"The reference is to a World Bank plot. Let's duplicate that one.",
    "references":["wb_urbanization"],
    "source_file":"ag_socio.py"
})

urban_ag_table = [
    ["<b>Production System</b>","<b>Yields, kg/m<sup>2</sup></b>","<b>Description</b>"],
    ["Conventional system","2.96"],
    ["Biointensive system","4.94+","An organic practice that aims to maximize yield."],
    ["Compost-only","2.22","Compost is the only source of nutrients."],
    ["Precision organic","2.87","Solid organic fertilizers are used."],
    ["Urban cap-and-fill","2.61","Similar to compost-only, but a plastic liner to prevent soil contamination is added."]
]

helper.save_image({
    "filename":"urban_ag.jpg",
    "status":"Done",
    "details":"Urban agriculture.",
    "table":urban_ag_table,
    "references":["urban_ag1"],
    "source_file":"ag_socio.py"
})