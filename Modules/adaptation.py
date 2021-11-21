# Adaptation

import helper

# See reference 'climate_fund'

funding_table = [
    ["<b>Purpose</b>","<b>World funding, billions of dollars. Average of 2017/18</b>"],
    ["<b>Adaptation</b>",""],
    ["Agriculture, Forestry, Land Use",7],
    ["Disaster risk management",7],
    ["Water, wastewater management",10],
    ["Infrastructure",2],
    ["Other adaptation",4],
    ["<b>Dual Benefits</b>",12],
    ["<b>Mitigation</b>",""],
    ["Renewable energy",336],
    ["Transportation",140],
    ["Energy efficiency",34],
    ["Agriculture, Forestry, Land Use",11],
    ["Transmission and distribution",3],
    ["Waste and wastewater",2],
    ["Other mitigation",11]
]

helper.save_image({
    "filename":"climate_funding.jpg",
    "status":"Done",
    "table":funding_table,
    "details":"Show major destinations of funding. The numbers are the average of 2017 and 2018, the most recent years I have. They include government, business, and non-profit funding. Not all climate-related funding is shown, but the source thinks they have most of it. I am using this plot to highlight how much more is spent on mitigation compared to adaptation, though it clearly has other use cases too. You will see ag, forestry, land use and waste and wastewater cross-listed because these areas have both adaptation and mitigation components. The dual benefits category refers to spending that can be classified both as adaptation and mitigation.",
    "references":["climate_fund"],
    "source_file":"adaptation.py"
})