# Oil-related plots

import helper

helper.save_image({
    "filename":"oil_type_ghg.jpg",
    "status":"Done",
    "details":"Simple bar plot showing the greenhouse gas emissions of types of oil production. These are upstream GHG only; they do not include the larger amounts from combustion of the oil. The figures are 18-19 kg CO<sub>2</sub>e/barrel for oil overall, 17 kg for offshore oil, 12 kg for shale, and 21 kg for onshore (non-shale) oil.",
    "references":["oil_ghg"],
    "source_file":"oil.py"
})