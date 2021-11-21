#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Organic figures

import helper

##########################################
# Table of price premiums
# Aggregating categories, which are made explicit here: https://www.usda.gov/media/blog/2016/06/14/investigating-retail-price-premiums-organic-foods
organic_price_table = [
    ["<b>Product category</b>","<b>Price premium (percentage premium of organic product over conventional equivalent)</b>"],
    ["Fresh produce",(7+27+28+29+44+60)/6.],
    ["Processed products",(22+29+30+31+33+47+53+54)/8.],
    ["Dairy and eggs",(52+72+82)/3.]
]

helper.save_image({
    "filename":"organic_premium.jpg",
    "status":"Done",
    "table":organic_price_table,
    "details":"Show organic price premium in the US as of 2010 for three broad product categories. My understanding is that more recent premiums are lower, but I haven't found good information that isn't proprietary, so we'll stick with this source for now. The three categories are aggregates of more detailed data in the source. I used the same categorization as in the blog post.",
    "references":["org_premium","org_premium_blog"],
    "source_file":"organic.py"
})

###################################
# Yields
yield_table = [
    ["<b>Study</b>","<b>Ratio of organic to conventional yield</b>"],
    ["Seufert et al.","66%"],
    ["Seufert et al. -- rain-fed legumes and perennials","95%"],
    ["de Ponti, Rijk, van Ittersum","80%"],
    ["Tuomisto, Hodge, Riordan, Macdonald","54%"],
    ["Ponisio et al.","80.8%"],
    ["Ponisio et al. -- with multicropping","91%"],
    ["Ponisio et al. -- with crop rotation","92%"],
    ["Crowder and Reganold","82-90%"],
    ["Stanhill","91%"],
    ["Reganold and Wachter","75-92%"],
    ["Clark and Tilman","47.6-80%"],
    ["Ferro et al.","69%"]
]

helper.save_image({
    "filename":"organic_yield.jpg",
    "status":"Done",
    "table":yield_table,
    "details":"Present the results from several meta-analyses on the yields of organic farming, expressed relative to the conventional equivalents.",
    "references":["org_yield_nature","org_yield2","org_env","org_yield3","org_yield4","org_yield5","org_yield6","meat_land_use","org_yield7"],
    "source_file":"organic.py"
})

#######################################
# Energy
energy_table = [
    ["<b>Study</b>","<b>Crop(s)</b>","<b>Ratio of organic to conventional energy needs</b>"],
    ["Lynch et al.","General","80%"], # org_energy2
    ["Pimentel et al.","Corn","69%"], # organic_energy
    ["Pimentel et al.","Soybeans","83%"], # organic_energy
    ["University of Manitoba","Two rotation patterns","55.0-64.6%"], # 'glenlea', table near the bottom of the page. Comparing total energy for two rotation patterns
    ["Reganold et al.","Apples","93.5%"], # reganold
    ["Fließbach and Mäder","General","44-80%"], # org_switz
    ["ADAS Consulting Ltd.","Dairy","25.7%"], # ork_uk
    ["Ziesemer","General","50-70%"], # ziesemer
    ["Clark and Tilman","General","85%"], # meat_land_use
    ["Ferro et al.","General","94.5%"], # org_yield7
    ["Fess and Benedito","General","73.1%"], #fess
    ["Tuomisto et al.","General","79%"] # org_env
]

helper.save_image({
    "filename":"organic_energy.jpg",
    "status":"Done",
    "table":energy_table,
    "details":"Present the results from several studies and meta-analyses on the energy requirements of organic farming, expressed relative to conventional equivalents.",
    "references":["org_energy2","organic_energy","glenlea","reganold","org_switz","org_uk","ziesemer","meat_land_use","org_yield7","fess","org_env"],
    "source_file":"organic.py"
})

##################################
# Other organic impacts
# This file should review major impacts that are not energy or land use.

impact_table = [
    ["<b>Metric</b>","<b>Organic value, relative to conventional</b>","<b>Source</b>"],
    ["Soil organic matter","107%","Tuomisto et al."], # org_env
    ["Nitrogen leaching","149%","Tuomisto et al."],
    ["Nitrous oxide emissions","108%","Tuomisto et al."],
    ["Ammonia emissions","111%","Tuomisto et al."],
    ["Phosphorus loss","99%","Tuomisto et al."],
    ["Greenhouse gases","100%","Tuomisto et al."],
    ["Greenhouse gases","96%","Clark and Tilman"],
    ["Eutrophication","120%","Tuomisto et al."],
    ["Eutrophication","137%","Clark and Tilman"], # meat_land_use
    ["Acidification potential","117%","Clark and Tilman"],
    ["Labor","135%","Pimentel et al."],
    ["Species richness (per farm)","130%","Tuomisto et al."],
    ["Organism count (per farm)","150%","Tuomisto et al."]
]

helper.save_image({
    "filename":"organic_impact.jpg",
    "status":"Done",
    "table":impact_table,
    "details":"Show various metrics related to organic farming, each presented relative to the conventional equivalent. Since some categories are shown multiple times, with results from different studies, aggregate them in a manner similar to what we did with the LCOE plots (though do something simpler since there are fewer of them).",
    "references":["org_env","meat_land_use","pimentel05"],
    "source_file":"organic_py"
})