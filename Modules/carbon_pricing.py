# Carbon pricing calculations

import helper

# See https://www.rff.org/publications/data-tools/carbon-pricing-calculator/
# Using $52/ton carbon price

plans = {
    "Coons-Feinstein":{
        "Costs":-10.79,
        "Climate":7.6,
        "Health":10.87,
        "Net":7.68
    },
    "Deutch et al.":{
        "Costs":-7.54,
        "Climate":6.8,
        "Health":9.38,
        "Net":8.64
    },
    "Van Hollen-Beyer":{
        "Costs":-3.45,
        "Climate":5.31,
        "Health":7.24,
        "Net":9.11
    },
    "Fitzpatrick":{
        "Costs":-3.27,
        "Climate":5.2,
        "Health":6.91,
        "Net":8.84
    },
    "Rooney":{
        "Costs":-2.35,
        "Climate":4.9,
        "Health":6.29,
        "Net":8.84
    },
    "Larson":{
        "Costs":-6.87,
        "Climate":6.65,
        "Health":9.16,
        "Net":8.95
    },
    "Durbin":{
        "Costs":-8.48,
        "Climate":7.04,
        "Health":9.58,
        "Net":8.14
    },
    "Lipinski":{
        "Costs":-1.82,
        "Climate":4.56,
        "Health":5.98,
        "Net":8.73
    }
}

carbon_price_table = [["<b>Policy</b>","<b>Economic Costs</b>","<b>Climate Benefit ($valued at 52/ton CO<sub>2</sub> in 2020)</b>","<b>Health Benefit</b>","<b>Net Benefit</b>","<b>Return on Investment</b>"]]
for key in plans:
    carbon_price_table += [[key,plans[key]["Costs"],plans[key]["Climate"],plans[key]["Health"],plans[key]["Net"],-1*(plans[key]["Climate"]+plans[key]["Health"])/plans[key]["Costs"]]]
    
helper.save_image({
    "filename":"carbon_plan.jpg",
    "status":"Done",
    "details":"Evaluation of net benefits of various carbon pricing plans.",
    "table":carbon_price_table,
    "references":["rff_calc"],
    "source_file":"carbon_pricing.py"
})

######################
# Earlier calculations that are not the right way to do it I don't think.

# The following are based on the Coons-Feinstein proposal.

# GDP figures, 2020-35. Billions of USD, 2020.
gdp_baseline = [22513.07, 22884.52, 23262.31, 23640.88, 24051.07, 24496.94, 24958.73, 25443.60, 25956.68, 26457.60, 26982.24, 27511.76, 28026.29, 28568.26, 29116.75, 29650.59]
gdp_c_price = [22460.45, 22787.44, 23116.86, 23443.90, 23799.49, 24187.74, 24589.19, 25010.98, 25458.16, 25891.20, 26345.36, 26802.28, 27242.72, 27708.05, 28177.96, 28632.07]

# Cumulative emissions to 2035, billions of tons
emissions_baseline = 79.10
emissions_c_price = 46.55

################################ Some other energy pricing stuff

pricing_table = [
    ["<b>Metric</b>","<b>Value (trillions of USD)</b>"],
    ["Coal",2.1],
    ["Oil",1.9],
    ["Natural Gas",0.4],
    ["Electricity",0.3],
    ["<b>By type of subsidy</b>"],
    ["Direct",0.7],
    ["Global Warming",1.1],
    ["Local Air Pollution",2.2],
    ["Other Externalities",0.7],
    ["Total",4.7]
]

helper.save_image({
    "filename":"energy_subsidies.jpg",
    "status":"Done",
    "details":"This plot illustrates an IMF report on energy subsidies. As shown, 'subsidies' are really primarily in the form of unpriced externalities, and a smaller portion is what we would think of as proper subsidies. Most of the direct, in turn, is to consumers, such as gasoline or heating oil subsidies.",
    "table":pricing_table,
    "references":["imf_subsidy"],
    "source_file":"carbon_pricing.py"
})

############################### Carbon offsets

offset_table = [
    ["<b>Type of project</b>","<b>Emissions pledged, Q1 2018 (kilotons)</b>"],
    ["Agriculture",12],
    ["Chemical Processes / Industrial Manufacturing",620.9],
    ["Energy Efficiency / Fuel Switching",1758.4],
    ["Forestry and Land Use",9287],
    ["Household Devices",1472.9],
    ["Renewable Energy",2162.8],
    ["Transportation",8.9],
    ["Waste Disposal",444.4]
]

helper.save_image({
    "filename":"carbon_offsets.jpg",
    "status":"Done",
    "details":"Carbon offsets in Q1, 2018 (January, February, March) by type of project. This is the most recent period for which I have data. This is Figure 3 in the cited report, looking at new issuances, as opposed to traded or retired projects. I believe this is more representative of the current state of the market than the other figures.",
    "table":offset_table,
    "references":["carbon_offsets1"],
    "source_file":"carbon_pricing.py"
})