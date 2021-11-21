# Housing-related calculations

import helper

# See https://www.jchs.harvard.edu/state-nations-housing-2019, Table A2 on p. 40. Reference housing_state2019

rent_burden_table = [
    ["<b>Category</b>","<b>Share of Owners</b>"],
    ["<30% of income on housing costs",59472./76779],
    ["30-50% of income on housing costs",9837./76779],
    [">50% of income on housing costs",7469./76779],
    ["<b>Category</b>","<b>Share of Renters</b>"],
    ["<30% of income on housing costs",22784./43284],
    ["30-50% of income on housing costs",9720./43284],
    [">50% of income on housing costs",10780./43284],
    ["<b>Category</b>","<b>Overall share</b>"],
    ["<30% of income on housing costs",82257./120063],
    ["30-50% of income on housing costs",19557./120063],
    [">50% of income on housing costs",18250./120063]
]

helper.save_image({
    "filename":"housing_affordability.jpg",
    "status":"Done",
    "table":rent_burden_table,
    "details":"Some stats on housing affordability. These figures are share of households (owners, renters, and overall) who pay <30%, 30-50%, and 50+% of their (pre-tax) income on tax. The latter two categories are the definition of cost-burdened and severely cost-burdened respectively, as used by the Department of Housing and Urban Development.",
    "references":["housing_state2019"],
    "source_file":"housing.py"
})

#########################################

# Cost of housing by (OECD) country, as shown here: https://www.oecd.org/els/family/HC1-1-Housing-related-expenditure-of-households.pdf

country_table = [
    ["<b>Country</b>","<b>Share of housing cost</b>","<b>Notes</b>"],
    ["Finland","29%","Highest share in OECD"],
    ["Malta","12%","Lowest share in OECD"],
    ["United States","19%"],
    ["United Kingdom","26%"],
    ["Germany","24%"],
    ["OECD","22.5%","The OECD is the Organisation for Economic Co-operation and Development, a set of generally wealthy, democratic, and market-oriented countries. All countries in this exhibit are members of the OECD."],
    ["EU","22%"],
    ["Mexico","16.5%"],
    ["Canada","24%"]
]

helper.save_image({
    "filename":"housing_aff_by_country.jpg",
    "status":"Done",
    "details":"Housing affordabiity for select countries. The full list of OECD countries are availabe at the source. Data approximated from Figure HC 1.1.2 of <a href=\"https://www.oecd.org/els/family/HC1-1-Housing-related-expenditure-of-households.pdf\">this document</a>. Figures include housing costs (mortgage, property tax, rent, etc.) and utilities.",
    "table":country_table,
    "references":["oecd_housing"],
    "source_file":"housing.py"
})

#########################################

# Rooms per person, a decent proxy for house size

rooms_table = [
    ["<b>Country</b>","<b>Rooms per Person</b>"],
    ["Canada","2.6"],
    ["United States","2.4"],
    ["New Zealand","2.4"],
    ["Australia","2.3"],
    ["United Kingdom","1.9"],
    ["Japan","1.9"],
    ["Germany","1.8"],
    ["France","1.8"],
    ["Korea","1.5"],
    ["Italy","1.4"],
    ["Israel","1.2"],
    ["Mexico","1.0"],
    ["Brazil","1.0"],
    ["Turkey","1.0"],
    ["South Africa","1.0"],
    ["Russia","0.9"]
]

helper.save_image({
    "filename":"Personal Space by Income Level.jpg",
    "status":"Done",
    "details":"There is a graphic now using Kozhenova's data under Trends, under Socioeconomics in Cities. I'd like to add this figure from the OECD to it. I don't think the Kozhenova source is very good, and later on I hope to replace it completely, but for now we'll keep it. The result will be a 2-in-1 graphic.",
    "table":rooms_table,
    "references":["oecd_better_living"],
    "source_file":"housing.py"
})