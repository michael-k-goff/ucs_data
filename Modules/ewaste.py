# Calculations related to e-waste

import helper

helper.save_image({
    "filename":"ewaste_rate.jpg",
    "status":"Done",
    "details":"Some figures about recycling rates for e-waste. The 2014 figure is calculated by dividing the amount of material properly recycled (7.6 million tons) by the total amount of e-waste (44.4 million tons). Doing the same for 2019 gives just over 17.5%, but the frequently quoted figure of 17.4%, so we're using that. I presume this is due to rounding. I am also including some historical and projected generation figures. Thus even if the recycling rate continues to creep up like in 2014-19, unrecycled e-waste will continue to be a growing problem.",
    "table":[
        ["<b>Year</b>","<b>Recycling Rate (percentage)</b>"],
        ["2019",17.4], # 9.4/53.6
        ["2014",100*7.6/44.4],
        ["<b>Generation, Year</b>","<b>Generation (million tons)"],
        ["2014",44.4],
        ["2015",46.4],
        ["2016",48.2],
        ["2017",50.0],
        ["2018",51.8],
        ["2019",53.6],
        ["2020",55.5],
        ["2021",57.4],
        ["2022",59.4],
        ["2023",61.3],
        ["2024",63.3],
        ["2025",65.3],
        ["2026",67.2],
        ["2027",69.2],
        ["2028",71.1],
        ["2029",72.9],
        ["2030",74.7]
    ],
    "references":["ewaste2021"],
    "source_file":"ewaste.py"
})

#################################################

# Costs of improper e-waste disposal

costs_table = [
    ["<b>Cost</b>","<b>Dollars per tonne</b>"],
    ["Refrigerants released",98/(53.6*0.826) * 50], # 98 million tons CO2e stated in the report (p. 15). Valuing at $50/ton.
    ["Greenhouse gas savings by recycling Fe, Al, Cu",15/(53.6*0.826) * 50],
    ["Damage to human health for informal recycling in Southern China",423]
]

helper.save_image({
    "filename":"ewaste_cost.jpg",
    "status":"Done",
    "details":"Damages from improper e-waste disposal. The values are per-tonne, averaged over all e-waste. So, for instance, the greenhouse gas potential of CFCs and HCFCs released are the average per tonne of e-waste, not per tonne of refrigerators. These costs are not generally additive. For example, the value of raw materials and GHG savings will be realized if the e-waste is informally recycled, but the health damage will be realized too. I am using a social cost of carbon of $50/ton. The health damages figures are from Boardman et al. and the others are from the E-waste monitor. Make this graphic a lower priority for now because I will revise it if I can find more figures. I especially want some monetized (non-GHG) environmental damages.",
    "table":costs_table,
    "references":["ewaste2021","china_ewaste"],
    "source_file":"ewaste.py"
})

#################################################

# Material value

material_table = [
    ["<b>Scenario</b>","<b>Estimated value of recovered material</b>"],
    ["Value of raw materials (mostly Fe, Cu, Au)",57000/53.6], # $57B of raw materials stated on p. 15.
    ["Value of raw materials",4412484/2829.1], # See Table 15 in the Egypt study. Using 2829.1 tons of waste by the facility.
    ["Minerals in car recycling",218.93/0.8*1.16], # In Denčić-Mihajlov et al. See Table 2. Note 8000 tons total, or 0.8 tons per vehicle. Using 1 Euro = $1.16
    ["Minerals in refrigerators",1022335/8000*1.16] # In Denčić-Mihajlov et al. See Table 3.
]

helper.save_image({
    "filename":"ewaste_material.jpg",
    "status":"Done",
    "details":"This was part of the cost plot, but I am spinning it off to something separate. This table is meant to be a collection of results on the per-ton mineral value in e-waste. It will expand as I find more figures. The first figures comes from the E-waste Monitor, the second from the Egypt report, and the car and refrigerator values from the Serbia report.",
    "table":material_table,
    "references":["ewaste2021","egypt_ewaste","serbia_ewaste"],
    "source_file":"ewaste.py"
})

helper.save_image({
    "filename":"ewaste_material.jog",
    "status":"Done",
    "details":"",
    "references":[],
    "source_file":""
})

#################################################

# A table of recycling costs

recycling_cost_table = [
    ["<b>Estimate</b>","<b>Cost, dollars per tonne</b>","<b>Source</b>"],
    ["E-waste, recycling and metal recovery","1000-9000","Yang et al."],
    ["Collection costs in Denmark","55-377, avg. 202","Clemente et al."], # Taking an exchange rate of 0.16 DKK per USD, then CPI-adjusting from 2012 to 2020.
    ["Recycling CRT TVs in China","1226-1601","Zeng et al."], # See Table S3 of the paper. Taking 13.83 kg for a weight of a CRT TV.
    ["Modeled material recovery facility in Egypt","1309","Mostafa and Sarhan"], # Based on 2829.1 tons in year 5. All expenses are included.
    ["Solar PV recycling cost in China","334.80","Liu et al."]
]

helper.save_image({
    "filename":"ewaste_recycling_cost.jpg",
    "status":"Not Done",
    "details":"A list of estimates of e-waste processing. They are measuring different things (countries, phases of recycling, etc.), which will have to be kept in mind when comparing them. Also keep this one a lower priority for now, because I hope to find more estimates.",
    "table":recycling_cost_table,
    "references":["ewaste10009000","denmark_ewaste","china_ewaste2","egypt_ewaste","solar_ewaste2"],
    "source_file":"ewaste.py"
})

#################################################

# Egypt e-waste study

egypt_table = [
    ["<b>Cost or Revenue</b>","<b>Thousand dollars per year in Year 5</b>"],
    ["Waste purchases",-3106],
    ["Revenue from selling recovered material",4412],
    ["Staff",-200],
    ["Infrastructure",-347],
    ["Equipment",-29],
    ["Other Expenses",-22],
    ["Total profit",709]
]

helper.save_image({
    "filename":"egypt_ewaste.jpg",
    "status":"Done",
    "details":"The purpose of this graphic is to show that an e-waste recycling facility can be profitable. A simplified profit and loss model is shown. The paper costs this out and reports five years; I am only showing year 5. I am also rounding everything to the nearest $1000, so that's why profit is not exactly equal to the sum of the others. A positive value represents revenue and a negative value is expense.",
    "table":egypt_table,
    "references":["egypt_ewaste"],
    "source_file":"ewaste.py"
})