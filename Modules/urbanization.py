# Urbanization rate

import helper

# Urban population first

urban_pop = [
    750903, # 1950
    775068,
    799283,
    824290,
    850170,
    877009,
    904685,
    933113,
    962537,
    992821,
    1023846, # 1960
    1055436,
    1088377,
    1122562,
    1157813,
    1188469,
    1219993,
    1252567,
    1285933,
    1319833,
    1354215, # 1970
    1388834,
    1424735,
    1462178,
    1501135,
    1538625,
    1577376,
    1616419,
    1659306,
    1706022,
    1754201, # 1980
    1804215,
    1854134,
    1903822,
    1955106,
    2007939,
    2062604,
    2118883,
    2176127,
    2233141,
    2290228, # 1990
    2347462,
    2404337,
    2461224,
    2518254,
    2575505,
    2632942,
    2690814,
    2749214,
    2808232,
    2868308, # 2000
    2933079,
    3001808,
    3071744,
    3143045,
    3215906,
    3289446,
    3363610,
    3439719,
    3516830,
    3594868, # 2010
    3671424,
    3747843,
    3824990,
    3902832,
    3981498,
    4060653,
    4140189,
    4219817,
    4299439,
    4378994, # 2020
    4458417,
    4537671,
    4616770,
    4695753,
    4774646,
    4853440,
    4932106,
    5010637,
    5089024,
    5167258, # 2030
    5245334,
    5323245,
    5400980,
    5478519,
    5555833,
    5632878,
    5709649,
    5786163,
    5862368,
    5938249, # 2040
    6013773,
    6088941,
    6163655,
    6238212,
    6312545,
    6386625,
    6460428,
    6533912,
    6607034,
    6679756 # 2050
]

urban_table = [
    ["<b>Years</b>","<b>Growth in Urban Population (thousands of people)</b>"]
]

for i in range(len(urban_pop)-1):
    year_range = str(1950+i)+"-"+str(1951+i)
    growth_rate = urban_pop[i+1]-urban_pop[i]
    urban_table.append([year_range, growth_rate])
    
helper.save_image({
    "filename":"urban_pop.jpg",
    "status":"Done",
    "table":urban_table,
    "details":"Urbanization growth, in thousands of people per year. The peak rate of urbanization may have been 2017-18. The source gives total urbanized population in thousands, but I decided to go with growth rate because that's what I want to illustrate here. If you feel this would be too much to show, choose a later starting date (1980-2050 or 2000-2050 or whatever) but keep the ending date at 2050.",
    "references":["wup"],
    "source_file":"urbanization.py"
})

#######################################

# Expansion indices

expansion_table = [
    ["<b>City</b>","<b>Annual Outward Expansion Rate, 2001-2014</b>","<b>Annual Upward Expansion Rate, 2001-2009</b>"],
    ["Seattle",1.17,0.32],
    ["San Francisco",0.19,0.16],
    ["New York City",6.62,2.83],
    ["Washington, D.C.",6.68,0.49],
    ["Atlanta",4.49,0.58],
    ["Dallas",5.5,1.07],
    ["Houston",6.9,0.45],
    ["Mexico City",2.82,1.18],
    ["Toronto",3.63, 0.95],
    ["London",1.7, 2.59],
    ["Paris", 1.28, 0.71],
    ["Madris",3.65, 1.63],
    ["Berlin",0.34, 0.02],
    ["Rome",2.26, 0.61],
    ["Prague",1.12, 0.3],
    ["Budapest",1.55, 0.33],
    ["Warsaw",1.2, 0.59],
    ["Instanbul", 1.65, 0.87],
    ["Moscow",4.64,3.8],
    ["Tokyo",2.74, 3.59],
    ["Seoul",1.55, 3.4],
    ["Shanghai",15.21, 15.98],
    ["Chongqing",5.81, 2.08],
    ["Shenzhen",3.04, 3.35],
    ["Hong Kong",0.19, 0.68],
    ["Ho Chi Minh City",4.1, 1.34],
    ["Kuala Lumpur",2.57, 0.6],
    ["Singapore",0.81, 0.95],
    ["Jakarta",2.82, 1.19],
    ["Sydney",1.2, 0.8],
    ["Buenos Aires",0.91, 0.33],
    ["Santiago",1.12, 0.57],
    ["Bogota",2.15, 0.31],
    ["Dehli",3.57, 0.73],
    ["Dhaka",3.92,0.74],
    ["Riyadh",5.59, 1.98],
    ["Karachi",1.55, 0.5],
    ["Baghdad",1.87,0.71],
    ["Jerusalem",0.54, 0.03],
    ["Cairo",5.81, 0.5],
    ["Addis Ababa",2.11, 0.19],
    ["Lagos",3.74,0.23],
    ["Kinshasa",6.22, 0.09],
    ["Nairobi",0.26, 0.01],
    ["Cape Town",2.22, 0.42]
]

for i in range(1,len(expansion_table)):
    expansion_table[i][1] = expansion_table[i][1] / 14
    expansion_table[i][2] = expansion_table[i][2] / 8

helper.save_image({
    "filename":"expansion_index.jpg",
    "status":"Not Done",
    "details":"Here we show some upward and outward expansion rates for a few major cities. Almost every large city in the world is in this database, so there is a lot we could add. The figures are based on satellite observation, so precision is limited. You can see more cities at <a href=\"https://resourcewatch.org/data/explore/40ffc305-609a-4367-a24f-816d9d43e508?hash=further_information&section=Discover&selectedCollection=&zoom=0.7270060154092359&lat=25.927466075387613&lng=-100.35003478952213&pitch=0&bearing=0&basemap=dark&labels=light&layers=%255B%257B%2522dataset%2522%253A%252240ffc305-609a-4367-a24f-816d9d43e508%2522%252C%2522opacity%2522%253A1%252C%2522layer%2522%253A%25221856044a-9d63-4b57-a582-ac316f1d93a6%2522%257D%255D&aoi=&page=1&sort=most-viewed&sortDirection=-1\">this interactive map</a>. Feel free to drop some cities from this list or request new ones be added as you see fit. The OGI and UGI have been divided by 14 and 8 respectively to get annual values.",
    "table":expansion_table,
    "references":["city_expansion_index"],
    "source_file":"urbanization.py"
})