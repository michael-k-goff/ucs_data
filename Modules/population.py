# Population figures
# May do something more details here later.

import helper
tfr_table = [
    ["<b>Country/Region</b>","<b>TFR as of 2018</b>"],
    ["World",2.415],
    ["<b>By Income Bracket</b>",""],
    ["Low Income",4.506],
    ["Lower Middle Income",2.711],
    ["Middle Income",2.322],
    ["Upper Middle Income",1.874],
    ["High Income",1.598],
    ["<b>By Region</b>",""],
#    ["Central Europe and the Baltics",1.574],
    ["East Asia and Pacific",1.823],
#    ["Euro Area",1.523],
    ["Europe and Central Asia",1.711],
    ["Latin America and Caribbean",2.029],
    ["Middle East and North Africa",2.809],
    ["North America",1.706],
    ["South Asia",2.385],
    ["Subsaharan Africa",4.693],
    ["<b>By Country</b>",""],
    ["China",1.69],
    ["India",2.222],
    ["United States",1.73],
    ["Indonesia",2.311],
    ["Pakistan",3.51],
    ["Brazil",1.73],
    ["Nigeria",5.387],
    ["Bangladesh",2.036],
    ["Russia",1.57],
    ["Mexico",2.129],
    ["Niger (highest TFR)",6.913],
    ["South Korea (lowest TFR)",0.977]
]

helper.save_image({
    "filename":"tfr.jpg",
    "status":"Done",
    "details":"Total fertility rate for select regions and countries. See the Population page under Habitat/Well-Being for an explanation of the TFR metric. For the individual countries, I listed the top 10 countries by population, in order from highest to lowest, followed by Niger and South Korea because they have the highest and lowest TFRs respectively. I imagine presenting this as four separate sets of bar plots: the World figure (by itself), by income group, by region, and by country. As far as ordering, do whatever makes most sense. Keep in mind that I am trying my best to structure the population section with a neutral tone, so as not to take a clear pronatalist or antinatalist point of view, so the ordering should not imply 'best to worst' in any way.",
    "table":tfr_table,
    "references":["tfr"],
    "source_file":"population.py"
})

helper.save_image({
    "filename":"tfr_trend.jpg",
    "status":"Done",
    "details":"World total fertility trend from 1960 to 2018. Replicate the plot that is in the linked source. I could give you the numbers here, but you can just as easily get them from the source directly. (When you move the mouse over the plot, you can get the exact number for the year.)",
    "references":["tfr"],
    "source_file":"population.py"
})

######################################################################

# A plot showing factors that influence fertility.

fertility_table = [
    ["<b>Factor</b>","<b>Effect</b>","<b>Source</b>"],
    ["Education","10% increase in primary education causes 3-4% fertility decrease in OECD countries","Madsen and Strulik"],
    ["Religion","Across countries, Christians have higher fertility than nonbelievers","Herzer"],
    ["Baby Bonus","One induced birth for every $30,000 to $300,000 spent in Australia","Stone"],
    ["Subsidized Childcare","10% increase in public childcare coverage increases fertility 3.2%","Bauernschuster et al."],
    ["Family Planning","Access to contraception reduces births in high fertility countries, reduces abortion in all countries.","Stover and Winfrey"],
    ["Legalized Abortion","Fertility in the US is 11% lower than it would be with completely outlawed abortion","Levine et al."],
    ["Zoning","Restrictive zoning correlated with lower fertility in the US","Shoag and Russell"],
    ["Urbanization","Fertility lower in urban than rural areas in developing countries","Lerch"],
    ["Suburbanization","Fertility higher in suburbs than urban cores in Northern Europe","Kulu et al."],
    ["City Size","Fertility higher in smaller cities relative to big cities","Kulu and Washbrook"]
]

helper.save_image({
    "filename":"tfr_factors.jpg",
    "status":"Done",
    "table":fertility_table,
    "details":"A collection of factors that influence birth rates. I try to put in quantitative results wherever possible, but use qualitative results if that's all that is available. It is also not clear in general whether the factors in question <i>cause</i> changes in birth rates, which must be kept in mind in considering the relevance of this data in a pro- or anti-natalist policy.",
    "references":["ed_fert", "babybonus","zoning_fert","lerch","suburban_fertility","citysize_fert","family_planning","abortion_fertility","childcare_fertility","herzer"],
    "source_file":"population.py"
})

# From https://population.un.org/wpp/Download/Standard/CSV/
# Not sure what this is for
pop2020 = 7794798729.
pop2060 = 10151469683.
pop2060high = 11529222442.
pop2060low = 8882879799.