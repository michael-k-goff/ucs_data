# Mass transit effectiveness

import helper

people_per_household = 2.62 # https://www.census.gov/quickfacts/fact/table/US/HCN010212
acres_per_hectare = 2.47105
housing_share = 0.4 # Portion of built up area that is housing. See the Value of High Density page.

density_threshold_table = [
    ["<b>Density figure</b>","<b>Value, people her hectare</b>","<b>Source</b>"],
    ["Municipal Buses","30","Holtzclaw"],
    ["Light Rail","35","Holtzclaw"],
    ["Metro Service","50","Holtzclaw"],
    ["Infrequent Bus Service","11.6","Kinder Institute"],
    ["Frequent Bus Service","38.6","Kinder Institute"],
    ["Heavy Rail","111","Guerra and Cervero"],
    ["Light Rail","74","Guerra and Cervero"],
    ["Frequent Buses",10*people_per_household*acres_per_hectare,"Twin Cities Metro Council"],
    ["Arterial BRT",15*people_per_household*acres_per_hectare,"Twin Cities Metro Council"],
    ["Highway BRT",str(8*people_per_household*acres_per_hectare)+"-"+str(25*people_per_household*acres_per_hectare),"Minneapolis Metro Council"],
    ["Light Rail, Commuter Rail, Dedicated BRT",str(15*people_per_household*acres_per_hectare)+"-"+str(50*people_per_household*acres_per_hectare),"Minneapolis Metro Council"],
    ["Buses (depending on level of services)",str(4*people_per_household*acres_per_hectare)+"-"+str(15*people_per_household*acres_per_hectare),"Pushkarev and Zupan"],
    ["Light Rail",str(9*people_per_household*acres_per_hectare),"Pushkarev and Zupan"],
    ["Rapid Transit",str(12*people_per_household*acres_per_hectare),"Pushkarev and Zupan"],
    ["Commuter Rail",str(1*people_per_household*acres_per_hectare)+"-"+str(2*people_per_household*acres_per_hectare),"Pushkarev and Zupan"],
    ["Median urban residential TOD project",str(36*people_per_household*acres_per_hectare),"Santasieri"],
    ["Median suburban residential TOD project",str(10.9*people_per_household*acres_per_hectare),"Santasieri"],
    ["Single family housing on median US lot",housing_share*1/290.86*10**4,""],
    ["Typical duplexes",housing_share*1/126.22*10**4,""],
    ["Typical walk-up apartments",housing_share*1/65.40*10**4,""],
    ["Typical midrise apartments",housing_share*1/18.28*10**4,""],
    ["Population-weighted average density in the U.S.","20.7","Bradford"]
]

helper.save_image({
    "filename":"density_treshold.jpg",
    "status":"Done",
    "table":density_threshold_table,
    "details":"Some estimates of the density thresholds needed for mass transit to be financially viable. The definition of 'financially viable' seems to vary a bit across papers, so these should be treated as rough values only. I don't know exactly what most authors mean, but Guerra and Cervo mean that it is more cost-effective to build new light/heavy rail than to reduce fares or expand service. A few other density figures are included for comparison. The numbers from Minneapolis are reported in dwelling units per acre rather than people, so I assume 2.62 (the national average) people per unit. They are recommended densities within 1/4 or 1/2 mile of stations. The Minnepolis numbers are minimum guidelines, and the target values given are higher.<br><br>Everything from the Santasieri figures downward should be in a different color, as these are some comparison density figures so that people will be able to understand the numbers.",
    "references":["holtzclaw","kinder","transit_density","transit_works","twin_cities","tod_density","bradford"],
    "source_file":"mass_transit.py"
})