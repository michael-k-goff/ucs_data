# Social well-being

import helper

freedom_table = [
    ["<b>Year</b>","<b>Percent of countries that are Free</b>","<b>Percent Partly Free</b>","<b>Percent Not Free</b>"],
    ["2019","42.56%","32.31%","25.13%"],
    ["2018","44.10%","30.26%","25.64%"],
    ["2017","45.13%","29.74%","25.13%"],
    ["2016","44.62%","30.26%","25.13%"],
    ["2015","44.10%","30.26%","25.64%"],
    ["2014","45.64%","28.21%","26.15%"],
    ["2013","45.13%","30.26%","24.62%"],
    ["2012","46.15%","29.74%","24.10%"],
    ["2011","44.62%","30.77%","24.62%"],
    ["2010","44.85%","30.93%","24.23%"],
    ["2009","45.88%","29.90%","24.23%"],
    ["2008","46.11%","32.12%","21.76%"],
    ["2007","46.63%","31.09%","22.28%"],
    ["2006","46.63%","30.05%","23.32%"],
    ["2005","46.35%","30.31%","23.44%"],
    ["2004","46.35%","28.13%","25.52%"],
    ["2003","45.83%","28.65%","25.52%"],
    ["2002","46.35%","28.65%","25.00%"],
    ["2001","44.27%","30.73%","25.00%"],
    ["2000","44.79%","30.21%","25.00%"],
    ["1999","44.27%","31.25%","24.48%"],
    ["1998","45.55%","28.27%","26.18%"],
    ["1997","42.41%","30.37%","27.23%"],
    ["1996","41.36%","30.89%","27.75%"],
    ["1995","39.79%","32.46%","27.75%"],
    ["1994","39.79%","31.94%","28.27%"],
    ["1993","37.89%","33.16%","28.95%"],
    ["1992","40.32%","39.25%","20.43%"],
    ["1991","41.21%","35.71%","23.08%"],
    ["1990","39.02%","30.49%","30.49%"],
    ["1989","36.14%","26.51%","37.35%"],
    ["1988","35.76%","26.67%","37.58%"],
    ["1987","34.55%","34.55%","30.91%"],
    ["1986","33.94%","33.94%","32.12%"],
    ["1985","33.94%","32.73%","33.33%"],
    ["1984","32.12%","34.55%","33.33%"],
    ["1983","31.71%","32.93%","35.37%"],
    ["1981-82","33.13%","27.61%","39.26%"],
    ["1980","31.68%","31.06%","37.27%"],
    ["1979","31.88%","33,13%","35.00%"],
    ["1978","29.94%","35.03%","35.03%"],
    ["1977","27.92%","31.17%","40.91%"],
    ["1976","26.58%","31.01%","42.41%"],
    ["1975","25.52%","33.54%","41.14%"],
    ["1974","26.97%","31.58%","41.45%"],
    ["1973","29.33%","27.33%","43.33%"],
    ["1972","29.73%","24.32%","45.95%"]
]

helper.save_image({
    "filename":"freedom.jpg",
    "status":"Done",
    "table":freedom_table,
    "details":"Freedom in the world. These are 'Free', 'Partly Free', and 'Not Free' categories as defined by Freedom House, in percent of countries by year. They aren't weighted by population or anything like that. Several years for which Freedom House reported data do not exactly line up with calendar years; I rounded as appropriate.",
    "references":["freedom_house"],
    "source_file":"social_well_being.py"
})

press_freedom_table = [
    ["<b>Year</b>","<b>Percent of Countries with a Free Press</b>","<b>Partly Free Press</b>","<b>Unfree Press</b>"],
    ["1986","24%","21%","55%"],
    ["1996","34%","34%","32%"],
    ["2006","38%","30%","32%"],
    ["2016","31%","36%","33%"]
]

helper.save_image({
    "filename":"freedom_press.jpg",
    "status":"Done",
    "table":press_freedom_table,
    "details":"Freedom of the Press in the world.",
    "references":["freedom_house_press"],
    "source_file":"social_well_being.py"
})

helper.save_image({
    "filename":"economic_freedom.jpg",
    "status":"Done",
    "details":"Simple graphic here. Show evolution in economic freedom, as determined by this index. 57.6 in 1995 to 61.6 in 2020. To get a more granular resolution of the data, go to the Downloads section of the site, Highlights, then the table on page 5.",
    "references":["economic_freedom"],
    "source_file":"social_well_being.py"
})

#################### Education

education_table = [
    ["<b>Year</b>","<b>Children not in primary school</b>","<b>Children not in lower secondary school</b>","<b>Children not in upper secondary school</b>"],
    ["1998",47.0+65.1, 44.7+52.5, 82.2+90.8],
    ["1999",44.5+60.6, 45.9+54.0, 83.1+91.8],
    ["2000",42.3+57.3, 45.7+53.7, 84.6+92.3],
    ["2001",40.7+54.8, 45.9+53.2, 86.2+92.6],
    ["2002",39.5+52.9, 44.5+50.5, 87.0+92.6],
    ["2003",37.3+45.0, 41.4+45.9, 87.9+91.8],
    ["2004",34.9+42.2, 39.7+43.4, 88.5+91.1],
    ["2005",32.2+39.1, 37.7+41.6, 89.4+90.4],
    ["2006",32.1+38.0, 36.9+39.9, 87.8+88.5],
    ["2007",27.6+34.0, 35.0+38.0, 84.5+85.2],
    ["2008",27.6+32.1, 34.7+36.6, 80.6+80.8],
    ["2009",28.9+31.8, 34.4+35.4, 78.8+78.2],
    ["2010",29.6+32.1, 33.5+33.6, 75.9+75.1],
    ["2011",30.2+31.3, 33.4+32.8, 74.4+72.7],
    ["2012",28.5+30.8, 32.9+31.7, 74.2+71.7],
    ["2013",27.8+30.4, 33.2+31.1, 73.1+70.4],
    ["2014",27.2+30.3, 33.5+31.0, 73.8+70.2],
    ["2015",27.4+31.4, 31.6+29.9, 72.6+69.0],
    ["2016",26.7+31.3, 31.3+29.7, 71.2+67.4],
    ["2017",26.8+31.6, 31.3+29.8, 70.6+67.1],
    ["2018",26.8+32.3, 31.6+29.8 ,70.8+67.0]
]

helper.save_image({
    "filename":"education_rates.jpg",
    "status":"Done",
    "details":"Number of children out of school, in millions. Definitions vary around the world, but typically primary school is from the start of school age to about 11, lower secondary school is ages 12-15, and upper secondary school is ages 15-18. They would correspond roughly to grade school, middle school, and high school in the United States.",
    "table":education_table,
    "references":["education_stats"],
    "source_file":"social_well_being.py"
})

#################### Some equality stuff

helper.save_image({
    "filename":"gender_equality.jpg",
    "status":"Done",
    "details":"A few plots in one for gender equality. The rate of child marriage (women now aged 20-24 who were married before age 18) was 29% in 1994, 28% in 2009, and 21% in 2019. The rate of female genital mutilization was 47% in 1994, 45% in 1999, 44% in 2004, 42% in 2009, 39% in 2014, and 34% in 2019.",
    "references":["education_stats"],
    "source_file":"social_well_being.py"
})

gini_table = [
    ["<b>Country</b>","<b>Gini Coefficient</b>","<b>Most Recent Year</b>"],
    ["United States","0.411","2016"],
    ["Canada","0.333","2017"],
    ["Mexico","0.454","2018"],
    ["Brazil","0.539","2018"],
    ["South Africa","0.63","2014"],
    ["Nigeria","0.351","2018"],
    ["United Kingdom","0.348","2016"],
    ["France","0.316","2017"],
    ["Germany","0.319","2016"],
    ["Switzerland","0.327","2017"],
    ["Russia","0.375","2018"],
    ["China","0.385","2016"],
    ["India","0.357","2011"],
    ["Indonesia","0.378","2018"],
    ["Japan","0.329","2013"],
    ["Australia","0.344","2014"]
]

helper.save_image({
    "filename":"gini.jpg",
    "status":"Done",
    "table":gini_table,
    "details":"Gini coefficient for select countries. See the World Bank source for more; most countries of the world have data.",
    "references":["wb_gini"],
    "source_file":"social_well_being.py"
})