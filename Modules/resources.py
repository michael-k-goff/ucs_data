# Plots for the Resource Availablility page

import helper

ag_chart = [
    ["<b>Year</b>","<b>Area Harvested</b>","<b>Crop Production</b>"],
    ["2012","4040288.991","62525416.919999994"],
    ["2030","4705084.874","80408019.26699995"],
    ["2035","4783421.784000001","83571927.24999991"],
    ["2040","4844947.210000004","86453499.42699994"],
    ["2050","4956033.844999999","91482593.62000011"]
]

helper.save_image({
    "filename":"ag_projections.jpg",
    "status":"Done",
    "table":ag_chart,
    "details":"Expected evolution by the FAO of area harvested and total crop production to 2050. These are the only years in the downloaded data set. Industrial crops (e.g. fiber crops and rubber) and cash crops (e.g. coffee, tea, tobacco) are included.",
    "references":["fao_projection"],
    "source_file":"resources.py"
})

helper.save_image({
    "filename":"climate_yields.jpg",
    "status":"Done",
    "details":"The impact of climate change on yields. The study says there will be a reduction of 7.1 percent for maize, 5.6 percent for rice, 10.6 percent for soybean and 2.9 percent for wheat.",
    "references":["climate_yields"],
    "source_file":"resources.py"
})

#####################################

# Peak oil predictions

oil_chart = [
    ["<b>Date of prediction</b>","<b>Region and Date of predicted oil peak</b>","<b>Predicted cause of peak</b>","<b>Source</b>"],
    ["1919","United States, perhaps by 1922","Supply constraint","White"],
    ["1953","United States, 1960-1970","Supply constraint","Ayers"],
    ["1953","World, 1985-2000","Supply constraint","Ayres"],
    ["1956","United States, 1965-1971","Supply constraint","Hubbert"],
    ["1974","World, 1995","Supply constraint","Hubbert, via Grove"],
    ["2001","World, 2003-2006","Supply constraint","Deffeyes"],
    ["2011","World, around 2050","Reduced demand","Yergin"],
    ["2020","World, by 2030","Reduced demand","IEA"]
]

helper.save_image({
    "filename":"peak_oil.jpg",
    "status":"Done",
    "details":"A chart of various predictions about the peak in oil production. There are too many to try to be comprehensive, but this list highlights some of the major predictions over the years.",
    "table":oil_chart,
    "references":["oil_peak_1919","oil_peak_1953","hubbert_peak","hubbert_peak2","deffeyes_peak","yergin_peak","energy_forecast"],
    "source_file":"resources.py"
})

#####################################

price2020 = (7.78+7.03)/2 # Median of high and low price in December 2020. Dollars per ton I presume
# https://finance.yahoo.com/quote/SAND/history?period1=1266796800&period2=1617580800&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true
cpi_by_year = [
    ["2020",258.811],
    ["2019",255.657],
    ["2018",251.107],
    ["2017",245.120],
    ["2016",240.007],
    ["2015",237.017],
    ["2014",236.736],
    ["2013",232.957],
    ["2012",229.594],
    ["2011",224.939],
    ["2010",218.056],
    ["2009",214.537],
    ["2008",215.303],
    ["2007",207.3],
    ["2006",201.6],
    ["2005",195.3],
    ["2004",188.9],
    ["2003",184.0],
    ["2002",179.9],
    ["2001",177.1],
    ["2000",172.2]
]

# Sand price from https://ycharts.com/indicators/us_producer_price_index_construction_sand_and_gravel_mining_primary_products_yearly
sand_price = [
    ["<b>Year</b>","<b>Sand price</b>"],
    ["2020",407.3],
    ["2019",387.8],
    ["2018",366.6],
    ["2017",351.7],
    ["2016",337.2],
    ["2015",323.3],
    ["2014",306.1],
    ["2013",289.4],
    ["2012",283.7],
    ["2011",277],
    ["2010",272.5],
    ["2009",272.8],
    ["2008",264.7],
    ["2007",249],
    ["2006",230.4],
    ["2005",211],
    ["2004",195.6],
    ["2003",189.5],
    ["2002",186.5],
    ["2001",182.4],
    ["2000",176.7]
]

sp11 = sand_price[1][1]
for i in range(1,len(sand_price)):
    sand_price[i][1] = price2020 * cpi_by_year[0][1] / cpi_by_year[i-1][1] * sand_price[i][1] / sp11

# Price of sand
helper.save_image({
    "filename":"sand_price.jpg",
    "status":"Done",
    "details":"New version with new sources. Monetary values are all adjusted to 2020 USD.",
    "table":sand_price,
    "references":["yahoo_sand","ycharts_sand"],
    "source_file":"resources.py"
})

#####################################

# Peak metals
helper.save_image({
    "filename":"peak_metals.jpg",
    "status":"Done",
    "details":"Hopefully an easy chart, show the estimated peak dates of three major metals: copper in 2030-2045, zinc in 2030-2050, and lead in 2025-2030.",
    "references":["peak_copper"],
    "source_file":"resources.py"
})

#####################################

# Simon Abundance Index
helper.save_image({
    "filename":"simon_abundance.jpg",
    "status":"Done",
    "details":"This is the Simon abundance index, which shows how the weight price of a basket of commodities has evolved over time. Replicate Figure 4 of the source as best you can. The SAI is defined as the product of the commodities earnable through one hour of work and world population.",
    "references":["simon_ab"],
    "source_file":"resources.py"
})