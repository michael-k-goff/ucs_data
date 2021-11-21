# Calculations related to energy geopolitics, military, etc.

import helper

# Energy used by Department of Defense.
# Figures from Appendix H from annual energy management report, 2018. https://www.acq.osd.mil/eie/Downloads/IE/FY%202018%20AEMR.pdf
# Figures were copied from the PDF into dod_energy.txt. Following code reads them out.

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
results = {}

filepath = 'Modules/dod_energy.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        if (len(line)>1):
            blocks = line.split(' ')
            head = blocks[0]
            tail = blocks[-1].strip()
            nocomma_tail = ''.join(tail.split(','))
            if (not (is_number(nocomma_tail))):
                line = fp.readline()
                cnt += 1
                
                blocks = line.split(' ')
                tail = blocks[-1].strip()
                nocomma_tail = ''.join(tail.split(','))
            if head not in results:
                results[head] = 0
            results[head] += float(nocomma_tail)
        line = fp.readline()
        cnt += 1
        
# Get operational energy
operational_energy = 690615.1
for key in results:
    operational_energy -= results[key]
        
dod_table = [
    ["<b>Branch</b>","<b>Energy Consumption in 2018 (PJ)</b>"],
    ["Federal government excluding Department of Defense",896788.7-690615.1],
    ["Operational - Army",9.2*6.1179],
    ["Operational - Navy",26*6.1179],
    ["Operational - Air Force",51.9*6.1179],
    ["Operational - Marine Corps",0.5*6.1179],
    ["Operational - Other DoD",0.9*6.1179],
    ["Installation - Army",results["ARMY"]],
    ["Installation - Navy",results["NAVY"]],
    ["Installation - Air Force",results["AIR"]],
    ["Installation - Marine Corps",results["MARINE"]],
    ["Installation - Logistics, intelligence, administration",results["NSA"]+results["DLA"]+results["NRO"]+results["DCMA"]+results["DFAS"]+results["DECA"]+results["WHS"]+results["NGA"]]
]

dod_table[1][1] *= 0.001055
for i in range(7,len(dod_table)):
    dod_table[i][1] *= 0.001055

helper.save_image({
    "filename":"dod_energy.jpg",
    "status":"Done",
    "details":"Energy used by the US Department of Defense in 2018. Operational energy refers to that which is used for powering military vehicles and used in field operations and comes from the second DoD report. Installation energy is what is used at permanent bases and offices and comes from the first DoD source. Overall federal energy is from the EERE source.",
    "table":dod_table,
    "references":["dod_energy","federal_energy","dod_operational"],
    "source_file":"geopolitics.py"
})

# Get crude estimate for world military energy
us_military_energy = sum(dod_table[i][1] for i in range(2,len(dod_table)))
#print(us_military_energy)
us_military_spending = 682491. # Millions of dollars as of 2018. See reference 'sipri'
world_military_spending = 1849 * 1000.
#print(us_military_energy * world_military_spending / us_military_spending)

#####################################################

# Historical energy for military. Reference 'smil_war'
war_energy_table = [
    ["<b>War</b>","<b>Years</b>","<b>Energy consumption as share of US total</b>"],
    ["World War I","1917-18","15%"],
    ["World War II","1941-45","40%"],
    ["Vietnam War","1964-72","4%"],
    ["Current","2018","1%"]
]

helper.save_image({
    "filename":"war_energy.jpg",
    "status":"Done",
    "table":war_energy_table,
    "details":"Above we saw how the US military takes up about 1% of national energy consumption. Here we compare that to periods of major war. These figures assess US military energy consumption as a share of total US energy that went to the war efforts. They do not include energy for other nations involved. I think it would be better to present figures chronologically. Data on the historic wars is from Vaclav Smil; for current military energy, see the dod_energy.jpg plot.",
    "references":["smil_war","dod_energy","dod_operational"],
    "source_file":"geopolitics.py"
})

#####################################################

# External cost of oil dependence. Based on reference 'oil_security'

oil_table = [
    ["<b>Externality</b>","<b>Cost per imported barrel, relative to domestic oil, in 2013-14, 2010 dollars</b>","<b>Explanation</b>"],
    ["<b>Conservative Estimate</b>","",""],
    ["Change in Expected Transfers for Other Purchasers","$0.92","A supply shock could lead to transfers of wealth from importers to exporters."],
    ["Change in Expected GDP Losses","$1.16","Imports increase the risk of macroeconomic disruption."],
    ["Total","$2.08",""],
    ["<b>Broad Estimate</b>","",""],
    ["Change in Expected Transfers for Other Purchasers","$0.92",""],
    ["Change in Expected GDP Losses","$1.16",""],
    ["Monopsony Premium","$15.99","If major importers of oil restrict consumption to reduce market risk, the result is consumption reduced below competitive levels."],
    ["Expected Price Shock for Purchaser of Marginal Imports","$6.95","Imports increase exposure for purchasers of oil to supply shocks."],
    ["Expected Defense Spending Associated with Oil Price Shocks","$0.29","Supply shocks have been observed to lead to additional defense spending and risk of military intervention."],
    ["Total","$25.31",""]
]

helper.save_image({
    "filename":"import_cost.jpg",
    "status":"Done",
    "table":oil_table,
    "details":"An estimate of the external costs of imported oil, relative to domestic oil. Environmental costs are not included since we discuss them elsewhere, and for environmental costs there isn't much difference between domestic and imported. There are two overall estimates given. The authors feel confident including the 'hange in Expected Transfers for Other Purchasers' and 'Change in Expected GDP Losses' categories, so they are included in the conservative estimate. For the other three things, they are uncertain whether they are externalities in the true sense, so if included they give up the larger, broad estimate. I think the best way to portray this one would be a stacked bar plot with two bars, showing each of the five costs.",
    "references":["oil_security"],
    "source_file":"geopolitics.py"
})

helper.save_image({
    "filename":"100_renewable_material.jpg",
    "status":"Done",
    "details":"Material requirements for a future of 100% wind and solar electricity and electric vehicles, relative to current consumption. The figures are as follows. For cobalt, 420% of current consumption would be required. For lithium, it's 170%. For silver, it's 50%.", # See https://link.springer.com/chapter/10.1007/978-3-030-05843-2_11, Table 11.5
    "references":["giurco"],
    "source_file":"geopolitics.py"
})

helper.save_image({
    "filename":"rare_earths.jpg",
    "status":"Done",
    "details":"World reserves of Rare Earth metals. This is a two-in-one, simplified version of what appears in the USGS fact sheet. Figures are in tons. Figures are 44 million tons in China, 22 million tons in Brazil, 22 million tons in Vietnam, 12 million tons in Russia, 6.9 million in India, 3.3 million in Australia, 1.5 million in Greenland, 1.4 million in the United States, and 6.9 million in other countries. As for production, China produces 132,000 out of 210,000 tons per year as of 2019.",
    "references":["usgs_rare_earth"],
    "source_file":"geopolitics.py"
})

#####################################################

# Mineral concentration

concentration_table = [
    ["<b>Mineral or resource</b>","<b>Largest national share</b>","<b>Country with largest share</b>"],
    ["Oil","18%","United States"],
    ["Natural Gas","23%","United States"],
    ["Copper","29%","Chile"],
    ["Nickel","33%","Indonesia"],
    ["Cobalt","69%","Democratic Republic of the Congo"],
    ["Graphite","63%","China"],
    ["Rare Earths","60%","China"],
    ["Lithium","52%","Australia"],
    ["Platinum","71%","South Africa"]
]

helper.save_image({
    "filename":"mineral_concentration.jpg",
    "status":"Not Done",
    "table":concentration_table,
    "details":"A measure of how concentrated minerals are. I did this by reporting which country has the largest share of world production of the mineral (with oil and natural gas for comparison), as well as which country.",
    "references":["iea_mining"],
    "source_file":"geopolitics.py"
})