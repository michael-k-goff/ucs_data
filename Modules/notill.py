# Calculations related to no-till agriculture (and maybe other stuff)

import helper

##################### Yields

notill_yields = [
    ["<b>Study</b>","<b>Yield, relative to tilled farming</b>"],
    ["O'Connor","104%"],
    ["Derpsch et al., low estimate","120%"],
    ["Derpsch et al., high estimate","220%"],
    ["Zhao et al.","104.6%"]
]

helper.save_image({
    "filename":"notill_yield.jpg",
    "status":"Done",
    "details":"Show some estimates of yield from no-till agriculture, relatived to conventioned tilled farming. I'm not sure how representative these studies are; these are the ones that I found that readily spell out numbers. Additional results or insights would be appreciated.",
    "references":["notill_yield","notill_yield2","nrdc_notill"],
    "table":notill_yields,
    "source_file":"notill.py"
})

##################### Soil carbon sequestration

notill_carbon = [
    ["<b>Study</b>","<b>Potential soil carbon sequestration from no-till (tons C per ha per year)</b>"],
    ["Lal et al., low estimate","0.1"],
    ["Lal et al., high estimate","1.0"],
    ["Du et al.","0.3"],
    ["VandenBygaart","Negligible"]
]

helper.save_image({
    "filename":"notill_c_seq.jpg",
    "status":"Done",
    "details":"Show various estimates of how much carbon can be sequested through no till farming. These figures are highly disputed, and so the range of values is meant to capture this.",
    "table":notill_carbon,
    "references":["notill_carbon1","notill_carbon2","notill_carbon3"],
    "source_file":"notill.py"
})

################### Other benefits/drawbacks to no-till agriculture

notill_other = [
    ["<b>Study</b>","<b>Quantity</b>","<b>Impact of no-till relative to tilled farming</b>"],
    ["Lal et al.","Soil loss","20%"], # notill_carbon1
    ["Lal et al.","Fertilizer usage","Savings, unquantified"],
    ["Derpsch","Erosion","4%"], # notill_yield
    ["Derpsch","Fuel consumption","34%"],
    ["Zhao et al.","Methane emissions","70%"], # notill_ghg2
    ["Zhao et al.","Nitrous oxide emissions","120.8-182.1%"],
    ["Karayel","Water quality","Improved"], # karayel
    ["Elias et al.","Pesticide runoff","Increased"], # notill_pesticide
    ["Gattinger et al.","Herbicde applied","Increased"] # notill_drawback
]

helper.save_image({
    "filename":"notill_impacts.jpg",
    "status":"Done",
    "details":"Show various other impacts of no till farming. Some are available in qualitiative only. As with the other no till studies, I'm not sure how representative this sample of studies is of the general body of knowledge.",
    "table":notill_other,
    "references":["notill_yield","notill_carbon1","karayel","notill_pesticide","notill_drawback"],
    "source_file":"notill.py"
})