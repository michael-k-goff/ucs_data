# Social endeavors
# -*- coding: utf-8 -*-

import helper

# Start with a list of parameters on costs and benefits for social endeavors.

# Some calculations for congestion pricing in Stockholm. Currency is millions of SEK.
cost = 1900 # Upfront investment cost
operational = 220 # Annual reinvestment and maintenance cost
benefit = 683+220 # Annual net benefit, excluding operational
discount = 0.07
exchange_rate = 1/7.2*1.30091276/1000 # Based on https://www.poundsterlinglive.com/bank-of-england-spot/historical-spot-exchange-rates/usd/USD-to-SEK-2006 and CPI adjust 2006 -> 2020
overall_benefit = benefit*1./discount*exchange_rate
overall_cost = (cost+operational*1./discount)*exchange_rate

endeavors = { 
    "Human Genome Project": { # From reference 'human_genome_project'
        "cost":5.6 * 1.19052366, # 2010 dollars, CPI adjusted to 2020. See Point 2, Page ES-2 (p. 6 of the document)
        "cost_basis":"Government spending over the project lifetime, 1990-2003",
        "benefit":796. * 1.19052366, # See the table on page ES-3.
        "benefit_basis":"Cumulative induced economic activity through 2010",
        "reference":"Tripp and Grueber"
    },
    "Smallpox Eradication":{ # From reference 'smallpox'
        "cost":0.298 * 4.95145873, # Money give just as "1970s". Taking it as 1975 and CPI adjusting to 2020
        "cost_basis":"World expenditures on eradication program",
        "benefit":(0.35+1.07)/0.03 * 4.95145873,
        "benefit_basis":"Avoided vaccination costs and avoided deaths, 3% discount rate",
        "reference":"Barrett"
    },
    "Phaseout of Lead in U. S. Gasoline":{
        "cost":(96+608+558+532)*2.63774029/1000, # 1983 dollars, CPI adjusted to 2020
        "cost_basis":"Compliance cost of refiners, 1983-86",
        "benefit":(2084+7821+7474+7105)*2.63774029/1000,
        "benefit_basis":"Monetized health benefits, improved fuel economy, lower maintenance costs, 1983-86",
        "reference":"Newell and Rogers"
    },
    "National Institutes of Health":{
        "cost":41.7,
        "cost_basis":"FY2020 budget appropriation for the NIH",
        "benefit":41.7*1.47,
        "benefit_basis":"Estimated market value of drugs that result from patents",
        "reference":"Azoulay et al., NIH"
    },
    # For this one, may want to cite the following with a note that the rate of return has been decreasing.
    # http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.352.8782&rep=rep1&type=pdf
    "Interstate Highway System":{
        "cost":329*1.67079663, # Based on 1996 dollars. See cox_highway
        "cost_basis":"Construction cost through 1995",
        "benefit":329*1.67079663 * 0.18 / 0.03, # Based on 18 annual cents saved per $1 invested. Assuming a 3% discount rate. See fhwa.
        "benefit_basis":"Reduced costs to industry. Rate of return estimated for all US highway spending from 1950 to 1989.",
        "reference":"Cox and Love, FHWA"
    },
    "U. S. Acid Rain Program":{
        "cost":3. * 1.52826422, # CPI adjust from 2000 to 2020
        "cost_basis":"Per year, 2010. Industry compliance costs with SO<sub>2</sub> and NO<sub>x</sub> controls.",
        "benefit":122. * 1.52826422,
        "benefit_basis":"Per year, 2010. Mostly monetized health benefits, some scenic and ecosystem benefits.",
        "reference":"Chestnut and Mills"
    },
    "U. K. Vehicle Exhaust Catalyst Mandate":{
        "cost":2.9445*0.7756*1.59635520, # Converting 1998 GPB to USD, then CPI adjust to 2020. See https://www.majorexchangerates.com/gbp/1998-usd.html
        "cost_basis":"Cost of converters, 1993-2005",
        "benefit":(7.378-2.3063+0.02972)*0.7756*1.59635520,
        "benefit_basis":"Monetized health benefits, 1993-2005",
        "reference":"Hutchinson and Pearson"
    },
    "Montreal Protocol":{
        "cost":235*1.62143935, # 1997 USD
        "cost_basis":"World cost of replacing ozone depleting substances, 1987-2060",
        "benefit":(459+1109)*1.62143935,
        "benefit_basis":"Health benefits, reduced damage to fisheries, agriculture, and materials.",
        "reference":"Benefits from Markandya and Dale, costs from Gåverud"
    },
    "Renewable Portfolio Standards":{
        "cost":31*1.08887116, # Based on +- 31 B
        "cost_basis":"Existing RPS in the US. Net increase or decrease in electricity cost. Estimated at $(+34 to -34), so the given ROI is a lower bound based on the study.",
        "benefit":(97+161)*1.08887116,
        "benefit_basis":"Reduced pollution and greenhouse gas emissions",
        "reference":"Mai et al."
    },
    "Wind Energy R&D":{
        "cost":1.719, # 2008 dollars. See p. ES-3 of the report
        "cost_basis":"Department of Energy spending on wind technologies, 1976-2008",
        "benefit":8.716, # End of p. ES-5
        "benefit_basis":"Health and economic benefits attributable to R&D spending",
        "reference":"Pelsoci"
    },
    "Energy Efficiency Regulation":{
        "cost":((33+129+975+192+381+179+69+218+803+151+475+17+209+47+75+393+32+199+239+395+16+567) + (38+182+1122+657+426+153+81+218+1283+253+724+21+264+55+129+425+41+216+329+547+19+691))/2/1000 * 1.47327813,
        "cost_basis":"Annual monetized costs of regulations by the Department of Energy implemented 2006-15. Estimate is taken as sum of midpoints of costs for all rules.",
        "benefit":((120+169+1274+1111+490+760+186+668+1660+1010+719+46+653+177+294+909+91+746+1129+1322+64+1042) + (182+310+1817+2886+865+1556+224+827+3034+1802+1766+67+1017+266+346+1116+134+956+2238+2566+80+1089))/2/1000 * 1.47327813, # Reported as millions of 2001 USD. Average of low and high values. See Table A-2.
        "benefit_basis":"Monetized benefits of regulations",
        "reference":"OMB"
    },
    "Transportation Safety":{
        "cost":(6.0+10.1)/2 * 1.47327813,
        "cost_basis":"Annual monetized cost of 24 transportation safety regulations adopted in the United States from 2006-2015",
        "benefit":(12.9+26.5)/2 * 1.47327813,
        "benefit_basis":"Monetized benefit of regulations",
        "reference":"OMB"
    },
    "Building Technology R&D":{
        "cost":0.330333*1.10382231, # Given as 2015 dollars. Take mid range, 7% discount rate, Table ES-2.
        "cost_basis":"Building Technologies Office investment in R&D, 1976-2015",
        "benefit":13.874*1.10382231,
        "benefit_basis":"Monetized energy and resource savings attributable to investment",
        "reference":"Gallaher et al., 2017"
    },
    "Hybrid and Electric Vehicle R&D":{
        "cost":0.971*1.13811572, # Table ES-3. CPI-adjusted from 2012 to 2020.
        "cost_basis":"Department of Energy R&D spending on hybrid and electric vehicles, 1992-2012",
        "benefit":0.971*3.63*1.13811572,
        "benefit_basis":"Discounted monetized energy and CO<sub>2</sub> emissions savings",
        "reference":"Link et al."
    },
    "Solar Photovoltaic R&D":{
        "cost":3.7099*1.22214800, # 2008 dollars. See Table ES-2
        "cost_basis":"Department of Energy R&D spending on solar photovoltaics, 1975-2008",
        "benefit":3.7099*1.83*1.22214800,
        "benefit_basis":"Discounted monetized energy and pollution savings attributable to investment",
        "reference":"O'Connor et al."
    },
    "Geothermal R&D":{
        "cost":1.660194*1.22214800, # Table ES-6. CPI-adjusted from 2008
        "cost_basis":"Department of Eergy R&D spending on geothermal technologies, 1980-2008",
        "benefit":8.076518*1.22214800,
        "benefit_basis":"Discounted monetized economic, environmental, and energy security benefits attributable to investment",
        "reference":"Gallaher et al., 2010"
    },
    "Combustion Engine R&D":{
        "cost":23.1/53*1.22214800, # Table ES-3. CPI-adjusted from 2008
        "cost_basis":"Department of Energy spending on combustion engine R&D, 1986-2007",
        "benefit":23.1*1.22214800,
        "benefit_basis":"Discounted monetized economic and health benefits",
        "reference":"Link"
    },
    "Congestion Pricing":{
        "cost":overall_cost,
        "cost_basis":"Stockholm system, investment cost and annual maintenance cost, 5% discount rate",
        "benefit":overall_benefit,
        "benefit_basis":"Monetized benefit of reduced travel time, net revenue change to city, environmental, and safety benefit",
        "reference":"Eliasson"
    },
    "NASA Life Sciences R&D":{
        "cost":0.264 * 1.59635520, # CPI adjusted from 1998 to 2020
        "cost_basis":"R&D spending by NASA and induced private sector spending, select projects",
        "benefit":1.5 * 1.59635520,
        "benefit_basis":"Value added from products attributable to R&D spending",
        "reference":"Hertzfeld"
    },
    "National Parks":{
        "cost":2.6*1.39293197, # CPI adjusted from 2004 to 2020
        "cost_basis":"Annual expenditure by U. S. National Park System",
        "benefit":10.1*1.39293197,
        "benefit_basis":"Annual monetized benefit of national parks: recreation, ecosystem services, public valuation of preservation, others",
        "reference":"Hardner and McKenney"
    },
    "Weather Forecasting":{
        "cost":5.1*1.22178334,
        "cost_basis":"Annual budget of the U. S. National Weather Service as of 2009",
        "benefit":31.5**1.22178334,
        "benefit_basis":"Benefit estimated by a willingness-to-pay study",
        "reference":"Lazo et al."
    },
    "Airports":{
        "cost":1.366 * 0.66 * 1.1, # 0.66 to convert NZ dollar to USD
        "cost_basis":"Estimated cost of an airport expansion in Wellington, New Zealand (median option)",
        "benefit":2.22 * 0.66 * 1.1,
        "benefit_basis":"Estimated economic benefit",
        "reference":"Murray et al."
    },
    "Panama Canal":{
        "cost":8.3*1.39293197,
        "cost_basis":"Construction cost, 1903-1914",
        "benefit":0.09541*16*14.91161850,
        "benefit_basis":"Reduced shipping costs, 1921-1937",
        "reference":"Maurer and Yu"
    },
    "Olympics":{
        "cost":11.401 * 1.10382231, # 2015 dollars
        "cost_basis":"Spending on the 2012 London Games",
        "benefit":(3.27+3.4) * 1.10382231,
        "benefit_basis":"Revenue and intangible benefits",
        "reference":"Baade and Matheson"
    },
    "Earthquake Risk Mitigation":{
        "cost":209.66 * 1.13811572, # Assuming 2012 dollars
        "cost_basis":"Retrofitting schools in countries with high earthquake risk", # Table A4
        "benefit":770.112 * 1.13811572,
        "benefit_basis":"Benefit, primarily based on stastical value of life",
        "reference":"Kunreuther and Michel-Kerjan"
    },
    "Suncreen Campaign":{
        "cost":0.01563 * 0.9 * 1.19052366, # 2010 Australian dollars. Was roughly 0.9 USD then.
        "cost_basis":"Mass media public education campaign to wear sunscreen in New South Wales, Australia",
        "benefit":0.06017 * 0.9 * 1.19052366,
        "benefit_basis":"Avoided skin cancer and death",
        "reference":"Doran et al."
    },
    "Smoking Cessation":{
        "cost":0.17694652*1.06231289, # CPI adjusted from 2017
        "cost_basis":"Estimated cost based on analysis of providing smoking cessation under Affordable Care Act plans.",
        "benefit":0.61869511*1.06231289,
        "benefit_basis":"Estimated savings of commercial, Medicare, and Medicaid claims.",
        "reference":"Baker et al."
    },
    "Antibiotics Conservation":{
        "cost":0.0059*0.72*1.10283606, # Billions of Canadian dollars, 2014,
        "cost_basis":"Cost of implementing an antibiotic conservation program in Alberta in 2005. (Actual value is about $4.7 million but got rounded away.)",
        "benefit":0.4497*0.72*1.10283606,
        "benefit_basis":"Cost of antibiotics that were conserved.",
        "reference":"Manun et al."
    },
    "Summer Reading Program":{
        "cost":(0.0706+0.0755)/8,
        "cost_basis":"Cost of administering a modeled summer reading program",
        "benefit":(0.0706+0.0755)/2,
        "benefit_basis":"Saved future education costs",
        "reference":"Reed et al."
    },
    "Universal Preschool":{
        "cost":3.54445*2.359*1.62143935, # 1997 Euros
        "cost_basis":"Expanding universal preschool subsidy eligibility from age 4 to 3 in Spain.",
        "benefit":15.27269*2.359*1.62143935,
        "benefit_basis":"Earnings potential for mothers and future potential for children.",
        "reference":"van Huizen et al."
    },
    "Hydropower":{
        "cost":(50+15+12+5+3+3+0.7+0.4+0.2)*1.39293197, # Not sure the date; guessing 2004 dollars. See table on p. 6, https://www.tandfonline.com/doi/pdf/10.3152/147154604781765888
        "cost_basis":"Three Gorges Dam: estimated construction costs, archeological losses, resettlement costs, and other costs",
        "benefit":(82+31++17+5+3)*1.39293197,
        "benefit_basis":"Economic growth, clean energy generation, flood control, navigation",
        "reference":"Morimoto and Hope"
    },
    "Bottle Deposit":{
        "cost":0.118882 / 4 * 1.22178334, # Figure given in Israeli Shekels. Dividing by 4 to convert to USD, then CPI-adjusting from 2009
        "cost_basis":"Cost of a bottle deposit program in Israel",
        "benefit":0.161694 / 4 * 1.22178334,
        "benefit_basis":"Financial and environmental benefits",
        "reference":"Lavee"
    },
    "Industrial Energy Efficiency":{
        "cost":0.054179060 * 1.62143935, # CPI adjusting from 2001
        "cost_basis":"Total cost of a set of industrial energy efficiency projects in the US",
        "benefit":0.028493331 / 0.07 * (1-0.93**20) * 1.62143935,
        "benefit_basis":"Energy savings and productivity gains, assuming a 7% discount rate and a 20 year lifetime.",
        "reference":"Worrell et al."
    },
    "Building Energy Efficiency":{
        "cost":1.863*1.10283606, # Assuming 2014 dollars
        "cost_basis":"Cost of retrotting buildings in Qatar", # Level 3
        "benefit":1.111 / 0.07 * (1-0.93**20)*1.10283606,
        "benefit_basis":"Energy savings, assuming 7% discount rate and 20 year lifetime.",
        "reference":"Krarti et al."
    },
    "High Speed Rail":{
        "cost":19.59457*1.17140807, # CPI-adjusting from 2011
        "cost_basis":"Construction, operating, and external costs of HSR line from Hong Kong to mainland China",
        "benefit":21.66306*1.17140807,
        "benefit_basis":"Revenue, time savings, pollution reduction, travel reliability, safety improvements",
        "reference":"Tao and Liu"
    },
    "Mercury Reduction":{
        # For exchange rate, see https://www.exchangerates.org.uk/AUD-USD-spot-exchange-rates-history-2016.html#:~:text=Average%20exchange%20rate%20in%202016,USD%20on%2017%20Jan%202016.
        # Benefit and cost: From https://www.environment.gov.au/system/files/consultations/4068cac4-a2ba-4036-a9e0-7bdee4f558fd/files/minamata-mercury-ris-dec-2016.pdf. See Option 4
        "cost":(0.3087-0.207)/0.7, 
        "cost_basis":"Australian industry cost of complying with Minamata Convention (Net Present Value)",
        "benefit":0.3087/0.7,
        "benefit_basis":"Health benefit to Australia, net present value",
        "reference":"Department of the Environment and Energy"
    }
}

print("Number of Endeavors Listed: "+str(len(endeavors))+".")

endeavors_table = [
    ["<b>Endeavor</b>","<b>Cost (billions USD)</b>","<b>Cost Explanation</b>","<b>Benefit (billions USD)</b>","<b>Benefit Explanation</b>","<b>ROI</b>","<b>References</b>"]
]

for key in endeavors:
    endeavors_table = endeavors_table + [[
            key,
            round(endeavors[key]["cost"],2),
            endeavors[key]["cost_basis"],
            round(endeavors[key]["benefit"],2),
            endeavors[key]["benefit_basis"],
            round(endeavors[key]["benefit"]/endeavors[key]["cost"],3),
            endeavors[key]["reference"]
]]

helper.save_image({
    "filename":"social_endeavors.jpg",
    "status":"Done",
    "details":"Cost/benefit analysis of select social endeavors. Figures are CPI-adjusted to 2020. This piece of data is going online July 27, 2020 and may go through a few iterations shortly thereafter. In general this is a plot that I think we will revisit more than most others.",
    "table":endeavors_table,
    "references":["human_genome_project","smallpox","newell","nih","nih_budget","cox_highway","fhwa","acidrain","vec_uk","montreal","montreal2","rps_cb","pelsoci", "omb2017","bto_review","hybrid_electric_review","solar_research","geothermal_research","combustion_rd","eliasson","nasa_spinoff", "national_parks","nws","nz_airport", "panama_canal","olympics", "disaster_risk","sunscreen","smoking_cessation","manun","summer_reading","preschool","three_gorges", "lavee","worrell2001","taoliu","mercury2"],
    "source_file":"endeavors.py"
})

# Calculate total costs and benefits of all these endeavors.
cost_sum = 0
benefit_sum = 0
for key in endeavors:
    cost_sum += endeavors[key]["cost"]
    benefit_sum += endeavors[key]["benefit"]
print(cost_sum) # 1497.8947013267023
print(benefit_sum) # 9041.223069588637

helper.save_image({
    "filename":"Various Social Endeavors",
    "status":"Done",
    "details":"On the Endeavors page, we have now broken up the list of endeavors into sets. The images whose filemane ends with '...1.jpg' show total investment cost, images whose filename ends in a '...2.jpg' portray the ROI (return on investment) of various endeavors, and those that end in '...3.jpg' portray net benefits. After talking with John on March 5, it looks like he really does want all three. The tables are not images but rather generated with CSS.",
    "references":[],
    "source_file":"endeavors.py"
})