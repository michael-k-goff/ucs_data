# Storage calculations

import helper

storage_table = [
    ["<b>Study</b>","<b>Estimated Cost</b>","<b>Estimated Benefit</b>"],
    ["Minnesota, Now","$140/kW-yr","$205/kW-yr"],
    ["Minnesota, 2025","$160/kW-yr","$135/kW-yr"],
    ["Sidhu et al., low estimates","$8686531","$8349665"],
    ["Sidhu et al., high estimates","$11076087","$17631561"],
    ["Li et al.","$4558665","$4923358"]
]

helper.save_image({
    "filename":"storage_cba.jpg",
    "status":"Done",
    "details":"Some cost-benefit results of battery grid storage. These figures include externalities. Note that the Minnesota study assess costs and value of a per storage unit basis, and the other references are on a per-battery basis, albeit different size batteries, so these values are comparable only on the ratios, not absolute cost and benefit values.",
    "table":storage_table,
    "references":["battery_cba1","battery_cba2","battery_cba3"],
    "source_file":"storage.py"
})