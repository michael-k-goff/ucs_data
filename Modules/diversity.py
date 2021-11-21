# Calculations related to the diversity section of the website.

import helper

# City size figures
city_size_table = [
    ["<b>Size class</b>","<b>Number of Cities</b>","<b>Number of people (millions)</b>"],
    ["10 million+","33","529"],
    ["5-10 million","48","325"],
    ["1-5 million","467","926"],
    ["0.5-1 million","598","415"],
    ["500 thousand or fewer","Many","2025"],
    ["Rural","---","3413"]
]

helper.save_image({
    "filename":"city_size.py",
    "status":"Done",
    "table":city_size_table,
    "details":"This report gives the number and population of cities by size class. These figures are as of 2018. There are also some 2030 projections. I could probably dig up something more detailed from another source, but I think this will be good enough for our purposes. I think it will be more important to visually portray the number of people metric rather than the number of cities metric.",
    "references":["city_size"],
    "source_file":"diversity.py"
})

#####################################

# Some figures on spare bedrooms in the US
# See https://www.brookings.edu/essay/trend-2-americas-demographics-are-transforming-but-our-housing-supply-is-not/

# The 'br' figure is the capacity reported of bedrooms, in order, 1br, 2br, 3br, 4+br
# Metro population figures are from Wikipedia and are the 2019 values. https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas
metro_figures = [
    {
        "name":"NY",
        "br":[102,77,60,56],
        "pop":19216182
    },
    {
        "name":"LA",
        "br":[122,88,69,58],
        "pop":13214799
    },
    {
        "name":"Chicago",
        "br":[94,63,59,60],
        "pop":9458539
    },
    {
        "name":"Dallas",
        "br":[92,78,60,55],
        "pop":7573136
    },
    {
        "name":"Houston",
        "br":[97,83,59,55],
        "pop":7066141
    },
    {
        "name":"Philadelphia",
        "br":[78,69,59,50],
        "pop":6102434
    },
    {
        "name":"Washington",
        "br":[99,74,60,54],
        "pop":6280487
    },
    {
        "name":"Miami",
        "br":[93,69,61,55],
        "pop":6166488
    },
    {
        "name":"Atlanta",
        "br":[81,68,58,57],
        "pop":6020364
    },
    {
        "name":"Boston",
        "br":[90,65,59,53],
        "pop":4873019
    },
    {
        "name":"SF",
        "br":[113,75,65,57],
        "pop":4731803
    },
    {
        "name":"Phoenix",
        "br":[98,69,56,58],
        "pop":4948203
    },
    {
        "name":"Riverside",
        "br":[107,79,64,59],
        "pop":4650631
    },
    {
        "name":"Detroit",
        "br":[82,62,56,56],
        "pop":4319629
    },
    {
        "name":"Seattle",
        "br":[96,71,59,54],
        "pop":3979845
    }
]

# Get the weighted average of bedroom occupancy
results = [0,0,0,0]
total_pop = sum([metro_figures[i]["pop"] for i in range(len(metro_figures))])
for j in range(4):
    results[j] = sum([metro_figures[i]["pop"]*metro_figures[i]["br"][j] for i in range(len(metro_figures))]) / float(total_pop)

br_table = [
    ["<b>Number of Bedrooms</b>","<b>Occupancy Rate</b>"],
    ["1",results[0]],
    ["2",results[1]],
    ["3",results[2]],
    ["4+",results[3]]
]

helper.save_image({
    "filename":"br_occupancy.jpg",
    "status":"Done",
    "details":"The average occupancy by number of bedrooms. Occupancy is based on HUD's definition, which is 1.5 people per bedroom. Some metros have figures higher than 100% for 1 bedroom units, indicating overcrowding. The Brookings link gives figures for the top 15 metros, and I averaged them and weighted them by population (based on the Wikipedia page, 2019 values). The point to illustrate here is that there is a shortage of small housing units, particularly 1 bedroom, relative to larger units.",
    "table":br_table,
    "references":["brookings_bedroom"],
    "source_file":"diversity.py"
})

########################################################

# Household size

helper.save_image({
    "filename":"household_size.jpg",
    "status":"Done",
    "details":"The goal here is to show how household size have been decreasing in the US for many years. Replicate the first figure at the reference as best you can.",
    "references":["pew_household"],
    "source_file":"diversity.py"
})

########################################################

# House size

helper.save_image({
    "filename":"house_size.jpg",
    "status":"Done",
    "details":"Here we want to show how house sizes have generally been getting bigger over time, in contrast with shrinking household sizes. Replicate Figure 3 here. To keep the plot readable, only do two of the time series: share of houses under 1400 sqft, and houses bigger than 3000 sqft.",
    "references":["rclco"],
    "source_file":"diversity.py"
})

########################################################

# Some housing preference stats

preference_table = [
    ["<b>Metric</b>","<b>Share of Market</b>"],
    ["Single Family Detached Construction","85%"],
    ["Single Family Attached Construction","12%"],
    ["Multifamily Construction","3%"],
    ["Separate Suites Construction","Negligible"],
    ["Single Family Detached Preference","60%"],
    ["Single Family Attached Preference","15%"],
    ["Multifamily Preference","16%"],
    ["Separate Suites Preference","9%"]
]

helper.save_image({
    "filename":"house_preference.jpg",
    "status":"Done",
    "table":preference_table,
    "details":"Housing preference (2018 survey) versus what is actually built (in 2017). Here the goal is to illustrate that there is demand, as expressed through surveys, for alternatives to the single family detached home that is not being met. In portraying the figures here, display the actual construction with stated preference side by side. 'Separate suites' here refer to ADU, or granny flats, or whatever else you want to call them.",
    "references":["rclco"],
    "source_file":"diversity.py"
})