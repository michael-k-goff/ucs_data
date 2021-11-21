# Cooking

import helper

cookstove_table = [
    ["<b>Fuel Source</b>","<b>Total Energy (MJ/household/year)</b>","<b>Climate Change (kg CO<sub>2</sub>e/household/year)</b>","<b>Particular Matter (kg PM10-eq/household/year)</b>","<b>Water (m<sup>3</sup>/household/year)</b>","<b>Acidification (kg SO<sub>2</sub>-eq/household/year)</b>","<b>Eutrophication (kg P-eq/household/year)</b>","<b>Smog (kg-NMVOC/household/year)</b>"],
    ["Firewood","16742-114855","1390-12929","6.84-37.4","0.093-0.82","1.43-8.81","0.3-2.65","8.96-399"],
    ["Crop Residue","9670-39159","271-530","16.9-45.4","0.23-0.58","1.49-2.47","0.75-1.88","12.5-35.1"],
    ["Dung","51628","765","94.9","4.76","3.01","15.3","74.9"],
    ["Charcoal from Wood","23441-322267","2279-24512","2.69-305","0.2-5.88","0.59-3.93","0.31-2.36","42.3-455"],
    ["Charcoal from Bamboo","23441-314079","470-5616","2.69-305","0.2-5.7","0.59-4.0","0.31-2.36","61.4-455"],
    ["Briquettes from Sawdust","16965-122583","204-1428","4.92-29.6","0.061-74.9","1.44-7.01","0.2-1.48","5.61-280"],
    ["Briquettes from Crop Residue","6733-58145","103-737","3.25-23.3","0.046-103","0.48-3.45","0.082-1.05","5.49-48.9"],
    ["Wood Pellets","5150-43160","683-6010","0.31-2.49","15.8-1304","0.29-2.61","0.0073-0.064","0.5-3.43"],
    ["Wood Chips","7338-52543","644-5851","2.99-17.0","0.63-13.4","0.58-4.2","0.1-1.2","9.77-180"],
    ["Sugarcane Ethanol","13532-43912","72.9-540","0.23-0.98","80.6-411","1.01-3.39","0.04-0.21","0.64-13.8"],
    ["Wood Ethanol","4787-34080","18.5-126","0.15-1.04","0.63-23.3","0.19-1.3","0.0000074-0.023","0.46-3.25"],
    ["Dung Biogas","4111-28483","13.6-164","0.17-1.21","2.36-51.5","0.07-1.66","0","0.37-1.78"],
    ["Liquified Petroleum Gas","4702-111077","671-6412","0.26-1.92","44.7-379","0.66-4.13","0.0056-0.047","1.48-34.9"],
    ["Kerosene","10373-14577","728-1027","1.15-1.24","146-358","1.6-4.3","0.013-0.051","2.1-4.65"],
    ["Natural Gas","10150","1056","0.28","28.6","0.84","0.0034","1.12"],
    ["Dimethyl Ether","31681","1711","3.73","136","5.86","0.31","9.97"],
    ["Coal","44249-55317","3865-3885","3.37-77.5","66.7-368","7.51-7.92","0.0086-0.44","5.94-31.6"],
    ["Electricity","21853-30023","1665-2458","6.61-6.77","2066-2598","16.1-21.2","0.014-0.31","8.08-9.26"]
]

helper.save_image({
    "filename":"cookstove_impact.jpg",
    "status":"Done",
    "details":"Evaluation of various metrics across different kinds of stoves.",
    "table":cookstove_table,
    "references":["cookstoves3"],
    "source_file":"cooking.py"
})

cooking_method_table = [
    ["<b>Strategy</b>","<b>Energy Savings, per unit food</b>"],
    ["Simmering (90 &deg;C) instead of boiling (100 &deg;C)","69-95%"],
    ["Steaming instead of boiling","9-56%"],
    ["Passive cooking (using residual heat to finish cooking after turning off heat source)","17-23%"],
    ["Simmering with a pot lid","50-85%"],
    ["Baking at a lower temperature","4-13%"],
    ["Using a pan with diameter larger than heat source","31-40%"],
    ["Non-distorted, flat pans","42-68%"],
    ["Larger pot size","42-63%"],
    ["Filling pot to capacity","20-49%"],
    ["Cooking larger quantities","78-83%"],
    ["Baking multiple portions simultaneously","43-75%"],
    ["Monitoring interal temperature","19-50%"],
    ["Stirring","3-14%"],
    ["Soaking before cooking, for certain foods","3-19%"]
]

helper.save_image({
    "filename":"cooking_method.jpg",
    "status":"Done",
    "details":"Energy savings for various strategies of cooking.",
    "table":cooking_method_table,
    "references":["modern_cooking"],
    "source_file":"cooking.py"
})

fuel_time_table = [
    ["<b>Study</b>","<b>Time estimated gathering fuel, hours per head of household per year</b>"],
    ["Das et al., 2019","40"],
    ["Clean Cooking Alliance","374"],
    ["Anderman et al.","438"],
    ["Lewis et al.","1059"],
    ["Das et al., 2017","1716"]
]

helper.save_image({
    "filename":"cooking_time.jpg",
    "status":"Done",
    "details":"Various studies on time spent cooking.",
    "table":fuel_time_table,
    "references":["cookstove_time1","cookstove_time2","cookstove_time3","cookstove_time4","cookstove_time5"],
    "source_file":"cooking.py"
})

###############################

helper.save_image({
    "filename":"cooking_electric.jpg",
    "status":"Done",
    "details":"Results of an LCA of gas versus electric cooking in South Korea. Emissions are 227.4 kg CO<sub>2</sub>/year for gas and 87.0 kg CO<sub>2</sub>/year for electric. Primary energy is 4.05 gigajoules for gas and 1.81 GJ for electric. The functional until is cooking for the average Korean household for a year.",
    "references":["korea_cooking"],
    "source_file":"cooking.py"
})