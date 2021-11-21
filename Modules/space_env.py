# Impact of space activities on terrestrial environment

import helper

warming_table = [
    ["<b>Substance</b>","<b>Contribution to warming</b>"],
    ["Black Carbon","70%"],
    ["Alumina","28%"],
    ["Water Vapor","2%"]
]

helper.save_image({
    "filename":"rocket_warming.jpg",
    "status":"Done",
    "table":warming_table,
    "details":"An estimate of what stratospheric rocket fuel emissions contribute to global warming. These figures are very uncertain.",
    "references":["radiative_rocket"],
    "source_file":"space_env.py"
})