# Kaya analysis stuff

import helper

# World, four factor Kaya plot

# World population, in thousands, from 1950 to 2019 (inclusive). Pulled from World Population Prospects.
# Cite reference wpp2019
world_pop = ("2,536,431	2,584,034	2,630,862	2,677,609	2,724,847	2,773,020	2,822,443	2,873,306	2,925,687	2,979,576	3,034,950	3,091,844	3,150,421	3,211,001	3,273,978	3,339,584	3,407,923	3,478,770	3,551,599	3,625,681	3,700,437	3,775,760	3,851,651	3,927,781	4,003,794	4,079,480	4,154,667	4,229,506	4,304,534	4,380,506	4,458,003	4,536,997	4,617,387	4,699,569	4,784,012"+"4,870,922	4,960,568	5,052,522	5,145,426	5,237,441	5,327,231	5,414,289	5,498,920	5,581,598	5,663,150	5,744,213	5,824,892	5,905,046	5,984,794	6,064,239	6,143,494	6,222,627	6,301,773	6,381,185	6,461,159	6,541,907	6,623,518	6,705,947	6,789,089	6,872,767	6,956,824	7,041,194	7,125,828	7,210,582	7,295,291	7,379,797	7,464,022	7,547,859	7,631,091	7,713,468").replace(',','').split('\t')
world_pop = [float(world_pop[i]) for i in range(len(world_pop))]

# World GDP
# Reference: world_bank_ppp2019 (same URL as the old PPP, but updated reference because there is new data)
# In trillions of USD, 2017, PPP. Years 1990 to 2018
world_gdp = [50.955, 51.615, 52.431, 53.306, 54.819, 56.557, 58.666, 60.935, 62.444, 64.627, 67.648, 69.205, 71.089, 73.744, 77.479, 81.025, 85.205, 89.614, 92., 91.363, 95.964, 99.67, 102.804, 106.169, 109.787, 113.421, 117.074, 121.415, 125.773]

# World primary energy. From BP, 2020, EJ. Reference: bp2020. Years: 1965-2019
world_energy = "155.69	164.10	170.27	180.65	192.86	205.01	213.36	224.93	237.88	239.16	240.46	253.45	262.75	271.95	281.45	279.46	278.16	276.46	280.94	294.42	302.23	308.88	319.66	331.88	338.31	342.23	344.63	347.22	349.63	354.11	361.52	372.13	375.67	378.02	384.85	394.50	398.45	407.18	421.74	442.23	457.08	470.14	484.67	490.23	482.82	506.02	518.31	524.98	534.91	539.25	543.17	550.60	560.42	576.23	583.90".split('\t')
world_energy = [float(world_energy[i]) for i in range(len(world_energy))]

# World GHG from energy, from BP, 2020. Millions of tons. Years: 1965-2019
world_ghg = "11207.7	11725.3	12084.7	12743.1	13530.9	14312.9	14788.4	15495.5	16345.1	16255.8	16281.7	17173.1	17739.3	18016.1	18596.5	18433.6	18202.3	18022.4	18185.1	18852.4	19249.9	19579.1	20186.5	20863.0	21242.6	21331.5	21338.6	21433.7	21488.9	21709.9	21982.9	22598.7	22749.9	22819.7	23127.8	23676.4	24010.3	24544.5	25767.5	27077.5	28186.5	29074.0	30095.9	30378.4	29745.2	31085.5	31973.4	32273.5	32795.6	32804.7	32787.2	32936.1	33279.5	34007.9	34169.0".split('\t')
world_ghg = [float(world_ghg[i]) for i in range(len(world_ghg))]

# Assemble Kaya metrics, 1990 to 2018
kaya_pop = world_pop[40:69]
kaya_gdpcap = [world_gdp[i]/kaya_pop[i] for i in range(29)]
kaya_enint = [world_energy[i+25]/world_gdp[i] for i in range(29)]
kaya_ghgint = [world_ghg[i+25]/world_energy[i+25] for i in range(29)]
kaya_ghg = [world_ghg[i+25] for i in range(29)]

def one_scale(seq):
    init_val = seq[0]
    for i in range(len(seq)):
        seq[i] /= init_val

one_scale(kaya_pop)
one_scale(kaya_gdpcap)
one_scale(kaya_enint)
one_scale(kaya_ghgint)
one_scale(kaya_ghg)

kaya_chart = [
    ["<b>Year</i>","<b>Population</b>","<b>Wealth (GDP per capita)</b>","<b>Energy Intensity (Energy/GDP)</b>","<b>Emissions Intensity (emissons/energy)</b>","<b>Emissions from Energy Total</b>"]
]

kaya_chart = kaya_chart + [
    [1990+i,kaya_pop[i],kaya_gdpcap[i],kaya_enint[i],kaya_ghgint[i],kaya_ghg[i]]
for i in range(29)]

helper.save_image({
    "filename":"kaya.jpg",
    "status":"Done",
    "table":kaya_chart,
    "details":"Show the evolution of four Kaya metrics worldwide over time. See the Drivers of Environmental Impacts section for details. Present as a time series plot, with the five series on a single plot. Units are dimensionless because all quantities are scaled so that the 1990 value is 1. Overall emissions are the product of the other three terms. Make that time series thicker than the others.",
    "references":["bp2019","wpp2019","world_bank_ppp2019"],
    "source_file":"kaya.py"
})


##############################################

# Kaya identity for the US. Same data sources and methodology.

# Thousands of people, 1990 to 2020 or so.
us_pop = "252,120	254,539	256,991	259,532	262,241	265,164	268,335	271,714	275,175	278,548	281,711	284,608	287,279	289,816	292,355	294,994	297,759	300,608	303,486	306,308	309,011	311,584	314,044	316,401	318,673	320,878	323,016	325,085	327,096	329,065	331,003".replace(',','').split('\t')
us_pop = [float(us_pop[i]) for i in range(len(us_pop))]

# Trillions of dollars, 1990-2018
us_gdp = [10.22, 10.202, 10.558, 10.846, 11.267, 11.576, 12.014, 12.535, 13.086, 13.718, 14.295, 14.455, 14.7, 15.135, 15.73, 16.276, 16.702, 17.08, 17.105, 16.662, 17.143, 17.445, 17.822, 18.141, 18.586, 19.097, 19.384, 19.83, 20.422]

# US primary energy
us_energy = "52.43	55.38	57.31	60.80	64.05	66.22	67.59	71.06	73.98	72.12	70.36	74.19	76.14	76.49	77.39	74.58	72.40	69.38	69.07	72.74	72.56	73.00	75.48	78.93	80.81	80.99	80.88	82.09	83.81	85.37	87.20	90.13	90.81	91.41	93.03	95.14	92.89	94.24	94.54	96.40	96.44	95.66	97.00	94.60	89.92	92.97	92.09	89.69	92.10	93.05	92.15	92.02	92.33	95.60	94.65".split('\t')
us_energy = [float(us_energy[i]) for i in range(len(us_energy))]

us_ghg = "3480.1	3675.5	3772.6	3994.2	4170.1	4298.2	4340.7	4564.7	4764.4	4596.4	4466.3	4741.9	4900.3	4863.2	4958.3	4785.7	4638.1	4398.0	4372.5	4574.2	4585.5	4597.7	4748.9	4968.4	5056.9	4969.6	4922.0	5004.1	5116.9	5195.3	5228.0	5407.9	5483.2	5524.2	5574.1	5740.8	5650.7	5672.4	5737.9	5839.0	5873.1	5795.1	5884.2	5699.1	5289.1	5485.7	5336.4	5090.0	5249.6	5254.6	5141.4	5042.4	4983.9	5116.8	4964.7".split('\t')
us_ghg = [float(us_ghg[i]) for i in range(len(us_ghg))]

# Assemble Kaya metrics, 1990 to 2018
us_kaya_pop = us_pop[:29]
us_kaya_gdpcap = [us_gdp[i]/us_kaya_pop[i] for i in range(29)]
us_kaya_enint = [us_energy[i+25]/us_gdp[i] for i in range(29)]
us_kaya_ghgint = [us_ghg[i+25]/us_energy[i+25] for i in range(29)]
us_kaya_ghg = [us_ghg[i+25] for i in range(29)]

one_scale(us_kaya_pop)
one_scale(us_kaya_gdpcap)
one_scale(us_kaya_enint)
one_scale(us_kaya_ghgint)
one_scale(us_kaya_ghg)

us_kaya_chart = [
    ["<b>Year</i>","<b>Population</b>","<b>Wealth (GDP per capita)</b>","<b>Energy Intensity (Energy/GDP)</b>","<b>Emissions Intensity (emissons/energy)</b>","<b>Emissions from Energy Total</b>"]
]

us_kaya_chart = us_kaya_chart + [
    [1990+i,us_kaya_pop[i],us_kaya_gdpcap[i],us_kaya_enint[i],us_kaya_ghgint[i],us_kaya_ghg[i]]
for i in range(29)]

helper.save_image({
    "filename":"us_kaya.jpg",
    "status":"Done",
    "table":us_kaya_chart,
    "details":"Similar to the Kaya identity plot above, but these figures are for the United States. Same sources as the world plot.",
    "references":["bp2019","wpp2019","world_bank_ppp2019"],
    "source_file":"kaya.py"
})

###########################################

# Report decomposition figures from reference 'decomp'
# From Table D.1
# I'm not sure what the difference is between demand structure and destination. I might combined them.
# Also might combine Leontief structure into energy intensity.
d1 = [
    "Dq -52067 -4805 -163667 -188352 -51066 -3727 -153191 -178535 -52067 -4805 -163667 -188352", # Energy intensity
    "DL -13668 10633 1099 13929 -12698 10435 666 14929 -13668 10633 1099 13929", # Leontief structure
    "Du 18 -5765 3117 7035 25 -5582 3103 7135 18 -5765 3117 7035", # Final demand structure
    "Dv -39603 7056 27141 48583 -33001 7032 24727 44895 -39603 7056 27141 48583", # Final demand destination
    "DY 124345 24798 156684 150931 117038 24326 150231 144876 124345 24798 156684 150931", # GDP/cap
    "DP 24754 24556 26237 28187 23480 23989 25076 27013 24754 24556 26237 28187", # Pop
    "DQ 43778 56474 50611 60313 43778 56474 50611 60313 43778 56474 50611 60313" # Total energy
]

decomp = {}
for i in range(len(d1)):
    cells = d1[i].split(' ')
    name = cells[0]
    values = [float(cells[1])+float(cells[2])+float(cells[3])+float(cells[4]), float(cells[5])+float(cells[6])+float(cells[7])+float(cells[8]), float(cells[9])+float(cells[10])+float(cells[11])+float(cells[12])]
    decomp[name] = [min(values), max(values)]

decomp_mod = [
    ["<b>Factor</b>","<b>Contribution to Energy Consumption, low estimate</b>","<b>Contribution to Energy Consumption, high estimate</b>"],
    ["Population",decomp["DP"][0], decomp["DP"][1]],
    ["Economic Growth",decomp["DY"][0], decomp["DY"][1]],
    ["Industrial Energy Intensity",decomp["Dq"][0]+decomp["DL"][0], decomp["Dq"][1]+decomp["DL"][1]],
    ["Demand Structure",decomp["Du"][0]+decomp["Dv"][0], decomp["Du"][1]+decomp["Dv"][1]]
]

helper.save_image({
    "filename":"decomp.jpg",
    "status":"Done",
    "table":decomp_mod,
    "details":"Show how four factors contribute to overall energy consumption (PJ) worldwide from 1990 to 2018. There are six factors in the paper, but I combined two of them into 'Industrial Energy Intensity' and two into 'Demand Structure' for clarity. Figures are from Appendix D of the paper. There are ranages because the authors use several formulas that give slightly different results.",
    "references":["decomp"],
    "source_file":"kaya.py"
})

###############################################

# Emissions embodied in trade go here, because why not.

trade_table = [
    ["<b>Country</b>","<b>Emissions in 2015, Based on Consumption</b>","<b>Emissions in 2015, Based on Production</b>"],
    ["United States",5794.5,5020.0],
    ["China",7977.9,9280.8],
    ["India",1918.8,2043.4],
    ["Russia",1167.5,1487.6],
    ["Europian Union (including UK)",3964.1,3458.3],
    ["Japan",1361.0,1202.3]
]

helper.save_image({
    "filename":"trade_emissions.jpg",
    "status":"Done",
    "table":trade_table,
    "details":"CO<sub>2</sub> emissions (millions of tons) by country, based on consumption and production accounting. Production accounting is typically what we are referring to when we talk about a country's emissions. Consumption accounting adds the emissions embodied in products that a country imports and subtracts emissions embodied in products that a country exports.",
    "references":["oecd_trade"],
    "source_file":"kaya.py"
})
