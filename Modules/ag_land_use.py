# Land use in agriculture estimates
# These are general purpose projections

import land_use
import population
import diet
import helper

total_ag_land = land_use.total_ag_land
total_ag_land -= 360000 # 36 million hectares, or 360,000 km^2, cropland for biofuels in 2008. Update if more recent figures can be found.
total_ag_land -= (11739333+3528473+1531576+28061+42219)/100. # Subtract area for nonfood crops, in the following order: rubber, tobacco, jute, hempseed, hemp tow waste. Data for cotton is missing.

total_ag_land_2060 = total_ag_land * population.pop2060 / population.pop2020

# Conservative yield trend from the FAO.
annual_yield_improvement = 1/1.008
ag_land_2060_imp = total_ag_land_2060 * annual_yield_improvement**40.

diets = diet.diet_land_use_chart()
american_diet_mult = diets["American"] / diets["World"]
ag_land_2060_us = ag_land_2060_imp*american_diet_mult

euro_diet_mult = diets["Euro"] / diets["World"]
ag_land_2060_euro = ag_land_2060_imp*euro_diet_mult

china_diet_mult = diets["China"] / diets["World"]
ag_land_2060_china = ag_land_2060_imp*china_diet_mult

# Potential land: currently used + arable
# Arable as percentage of total: https://data.worldbank.org/indicator/AG.LND.ARBL.ZS
# Ag land: https://data.worldbank.org/indicator/AG.LND.AGRI.ZS
farmable_land = total_ag_land * (11.06+37.431)/(37.431)

ag_land_table = [
    ["<b>Scenario</b>","<b>Land area required (square km)</b>"],
    ["Current",total_ag_land],
    ["Current yields and diets, projected 2060 population",total_ag_land_2060],
    ["Current diets, projected yields and 2060 population",ag_land_2060_imp],
    ["Chinese diet, projected yield and 2060 population",ag_land_2060_china],
    ["European diet, projected yield and 2060 population",ag_land_2060_euro],
    ["American diet, projected yield and 2060 population",ag_land_2060_us],
    ["Total farmable land",farmable_land]
]

helper.save_image({
    "filename":"world_ag_land_projected.jpg",
    "status":"Done",
    "table":ag_land_table,
    "details":"Current and projected agricultural land use under various scenarios. Current land use is cropland + pasture and meadows, as reported in land_use.jpg. For future scenarios, population is forecast from World Population Prospects. Projected yields 0.8% to 2060, based on an FAO model (they only go to 2050, but it's a fairly conservative estimate and I think it's safe to push it to 2060). Chinese, European, and American diets are pulled from FAOSTAT, and the land use impacts of these diets are as shown in the diet land use plot, with land use by food estimated from Clark and Tilman and Froehlich et al. as before. Total farmable land adds current farmable land plus additional arable land, as estimated from the two World Bank sources.",
    "references":["faostat","worldpopprospects","wb_arable","wb_farmland","meat_land_use","aq_land_use","fao_yield_proj"],
    "source_file":"ag_land_use.py"
})