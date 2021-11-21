#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Calculations related to GM crops.

import helper

#################################
# GMO yields

yield_table = [
    ["<b>Trait and Crop</b>","<b>Yield Gain</b>","<b>Source</b>"],
    ["Overall","22%","Klümper and Qaim"], # gmo_yield1
    # Some figures from gmo_yield2
    ["Insect-resistant corn","13.1%","Brookes and Barfoot"],
    ["Insect-resistant cotton","15%","Brookes and Barfoot"],
    ["Insect-resistant soybeans","9.6%","Brookes and Barfoot"],
    ["Herbicide-tolerant soybeans","15%","Brookes and Barfoot"],
    ["GE Corn","5.6-24.5%","Pellegrino et al."]
]

helper.save_image({
    "filename":"gmo_yield.jpg",
    "status":"Done",
    "details":"Selected results on yield gains from various GM crops and traits.",
    "table":yield_table,
    "references":["gmo_yield1","gmo_yield2","gmo_yield3"],
    "source_file":"gmo.py"
})

###################################
# GMO projects

project_table = [
    ["<b>Project</b>","<b>Description</b>","<b>Rationale</b>","<b>Risks</b>"],
    ["C<sub>4</sub> Rice","Alternative photosynthetic biochemistry","Increase yields 30-50%","--"],
    ["Nitrogen-fixing cereals","Allow cereal crops to fix hydrogen via bacteria, as legumes naturally do.","Reduce fertilizer consumption and runoff.","May decrease yields."],
    ["Golden Rice","Rice that contains β-Carotene","Reduce vitamin-A deficiency","--"]
]

helper.save_image({
    "filename":"gmo_projects.jpg",
    "status":"Done",
    "details":"Infographic showing a brief description and rationale for some major GMO projects. This is not an attempt to be comprehensive about projects, but to cover what appear to me to be the most promising or notable projects. Info on C4 rice comes from the C4 Rice Project. Beatty and Good describe potential benefits of nitrogen-fixing cereals. Rogers and Oldroyd describe potential risk. See the Golden Rice reference for data on that topic.",
    "table":project_table,
    "references":["c4","nfc","nfc_biotech","golden_rice"],
    "source_file":"gmo.py"
})