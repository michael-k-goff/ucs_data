# Transportation of fossil fuels

import helper

gas_efficiency_im = {
    "filename":"gas_transport_efficiency.py",
    "status":"Done",
    "details":"Compare energy consumed by modes of transporting natural gas. Figures, as a share of the energy content of the gas being transported, are 2.5% for pipelines and 13% for LNG.",
    "references":["pipeline_efficiency","lng_efficiency"],
    "source_file":"transportation_of_fuel.py"
}
helper.save_image(gas_efficiency_im)

oil_externality_im = {
    "filename":"oil_transport_externality.jpg",
    "status":"Done",
    "details":"Compare external costs of transporting oil by train and by pipeline, in terms of dollars per million-barrel miles. Figures for pipelines are $531 for air pollution and greenhouse gases and $62 for spills and accidents; for trains they are $1015 for pollution and greenhouse gases and $381 for spills and accidents.",
    "references":["oil_transport"],
    "source_file":"transportation_of_fuel.py"
}
helper.save_image(oil_externality_im)

oil_spill_im = {
    "filename":"oil_spill.jpg",
    "status":"Done",
    "details":"Barrels of crude oil spilled in the United States from 2002 to 2007 for every billion ton-miles by transportation mode.",
    "table":[["Pipeline",115],["Barge",17],["Truck",228],["Rail",30]],
    "references":["oil_spill"],
    "source_file":"transportation_of_fuel.py"
}
helper.save_image(oil_spill_im)

