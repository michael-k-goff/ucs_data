# Some figures on economics of waste

import helper

mrf_table = [
    ["<b>Scenario</b>","<b>Dollar Cost per Ton</b>","<b>Source</b>"],
    ["New York City",194.09,"Dubanowitz"], # $127, CPI-adjusted from 2000 to 2020.
    ["Tucson, AZ",156.59,"Gershman, Brickner & Bratton, Inc."], # In the table on p. 43. CPI-adjusted from 2008 to 2020.
    ["Washoe County, NV","71.10-77.41","Harris et al."], # Table 16 on p. 53. Going with the MSF+Recycling entry for the clean MRF. CPI-adjusted $60-70-66.08 from 2011.
    ["Ohio",131.78,"O'Keefe et al."],
    ["Single Stream MRFs in 2020",112,"Paben"],
    ["Dual Stream and Source Separated MRFs in 2020",60,"Paben"],
    ["Montgomery County, Pennsylvania","85-95","Montgomery County Recycling Consortium"]
]

helper.save_image({
    "filename":"mrf_cost.jpg",
    "status":"Done",
    "details":"A review of the cost of some MRFs (material recovery facilities). All figures are CPI-adjusted to 2020.",
    "table":mrf_table,
    "references":["mrf2","mrf3","mrf4","mrf1","resource_recycling","monty_recycling"],
    "source_file":"waste_econ.py"
})

#################################################

comm_table = [
    ["<b>Commodity</b>","<b>Price as of 2018, dollars per ton</b>","<b>Share of waste stream (percentage)<b>","<b>Value, dollars per ton of MSW</b>"],
    ["Old Corrugated Cardboard",75,8.37,6.28],
    ["Old Newsprint",65,33.61,21.85],
    ["Mixed Paper",55,14.16,7.79],
    ["Aluminum",1220,1.26,15.42],
    ["Tin",25,1.99,0.5],
    ["HDPE Plastic, Natural",500,1.24,6.21],
    ["HDPE Plastic, Colored",320,0.99,3.16],
    ["PET Plastic",180,4.06,7.30],
    ["Mixed Plastics",273.24,0.92,2.51],
    ["Mixed Glass",-17.85,25.17,-4.49],
    ["Residue",-45.73,6.90,-3.15],
    ["Total","",98.67,63.36]
]

helper.save_image({
    "filename":"mrf_comm_price.jpg",
    "status":"Done",
    "details":"This graphic shows commodity prices from recycling typical MSW, as of 2018. Price fluctuate quite a lot, so we may need more graphics that capture that fact. Percentages don't add up to 100%, I presume because there is a portion (about 1.3%) of the waste stream that is not characterized.",
    "table":comm_table,
    "references":["mrf_economics"],
    "source_file":"waste_econ.py"
})

#################################################

# Landfill externalities

externality_table = [
    ["<b>Scenario</b>","<b>Externality, dollars per ton</b>"],
    ["Cost found in Australia",32],
    ["Landfill emissions and other pollution in South Africa",19], # $16 in 2011
    ["Greenhouse gases, US waste stream",86],
    # The following are in Euros in 2000. Multiply by 1.375437798 to get USD in 2020.
    ["European Union, assuming leachate collection and treatment, energy recovery","8-33"], # 6-24 Euros in 2000
    ["EU, no leachate or energy collection","15-61"], # 11-44 Euros in 2020
    ["Review of studies","1.29-62"] # $0.91-44, CPI adjusted from 2003.
]

helper.save_image({
    "filename":"landfill_externality.jpg",
    "status":"Done",
    "table":externality_table,
    "details":"A collection of estimates of the externalities associated with landfills. The WA result is from Schollum and does not account for benefits of reducing virgin material. The South Africa figures is from Nahman. The greenhouse gas figure is based on the savings estimated in the EPA's WARM model, applied to the waste composition estimated on that page, valued at $50/ton. The EU figures are from the European Commission. I am planning on looking for more figures.",
    "references":["wa","sa_landfill","euro_landfill","landfill_external_2004","warm15"],
    "source_file":"waste_econ.py"
})

###################################################

# Incineration externalities

inc_table = [
    ["<b>Scenario</b>","<b>Externality, dollars per ton</b>"],
    # For the EU, multiply by 1.375437798 to get USD in 2020.
    # I cut the credit for energy production in half because it assumes that it displaces strictly coal, which I think is unrealistic.
    ["European Union, strict environmental regulation, energy used for combine heat and power","-20 to +1"],
    ["EU, strict environmental regulation, recovered energy used for electricity","22-116"],
    ["EU, weak environmental regulation, no energy recovery","34-171"],
    ["Greenouse gases, US waste stream","76"],
    ["Review of Studies","-15 to 173"], # CPI adjusted from 2003, with initial figures -9 to 124.
    ["Industrial Waste in South Korea","95"]
]

helper.save_image({
    "filename":"incinerator_externality.jpg",
    "status":"Done",
    "details":"Some figures on external costs associated with incineration. All costs are converted to US dollars and CPI-adjusted to 2020. For the EU studies, I cut in half the benefit from energy production, because the study assumes that incinerator energy entirely displaces coal, which I don't think is realistic. Externalized cost of manufacturing from virgin or recycling material are not accounted for here except for greenhouse gas costs. GHG costs are estimated from the WARM model applied to the waste stream estimates on that page, valued at $50/ton.",
    "table":inc_table,
    "references":["euro_landfill","landfill_external_2004","sk_incinerator","warm15"],
    "source_file":"waste_econ.py"
})

###################################################

# Estimate for an appropriate landfill tax

landfill_tax_table = [
    ["<b>Basis</b>","<b>Value, dollars per ton</b>"],
    ["<b>Landfills</b>",""],
    ["Air pollution and leachates",19],
    ["Greenhouse gas cost of virgin material, landfilling",86],
    ["Total",105],
    ["<b>Incinerators</b>",""],
    ["Pollution from the incinerator",33],
    ["Greenhouse gas cost of virgin material, incineration",76],
    ["Energy credit if incinerator produces CHP",49],
    ["Energy credit if incinerator produces electricity only",14],
    ["Total, CHP",58],
    ["Total, Electricity only",93],
    ["Total, no energy production",107]
]

helper.save_image({
    "filename":"landfill_tax.jpg",
    "status":"Done",
    "table":landfill_tax_table,
    "details":"This diagram illustrates recommended taxes on landfills and incinerators, dollars per ton of waste. For landfills, I am using the $19/ton figure from the Australia study for direct pollution impacts, which is from the Australia study. It is one of the lower figures but not the lowest reviewed. For incineration, I am taking the average of the results of the 7 studies in the 2005 review for direct environmental costs. I broke the incinerator results into three scenarios for energy recovery, so that the recommended tax varies by the energy recovery scenario. The methodology for energy costs is the same as in the cited EU study. In both cases, an $83/ton greenhouse gas cost of virgin manufacturing is included.<br><br>I am intentionally leaving out estimates of job creation potential. Although this is a cost of landfilling and incineration, I don't think it can properly be called an external cost that would be a justifiable basis for taxation.<br><br>This plot is likely to be updated. John will almost certainly offer opinions when he sees it. I would like some more recent figures on the environmental cost of landfills and incinerators. I would also like some non-GHG costs of virgin manufacturing, as well as some environmental costs of recycling facilities.",
    "references":[],
    "source_file":"waste_econ.py"
})

###################################################

# Supply and demand for compost

compost_table = [
    ["<b>Metric</b>","<b>Value, millions of tons</b>"],
    ["Current Supply (as of 1992)","8.3"],
    ["Potential Supply","51"],
    ["Demand, Agriculture","895"],
    ["Demand, Silviculture","104"],
    ["Demand, All Other Uses","39.4"],
    ["Total Demand","1038.4"]
]

helper.save_image({
    "filename":"compost_demand.jpg",
    "status":"Not Done",
    "table":compost_table,
    "details":"The purpose of this plot is to show show supply and potential demand for compost. It seems that demand is far higher than supply and there is no possibility of demand being saturated. Unfortunately, the study on which this is based is from 1993. I would very much like to have something more recent, but I haven't been able to find it yet.",
    "references":["compost_battelle"],
    "source_file":"waste_econ.py"
})

###################################################

# Energy savings with recyclables for injection molding

helper.save_image({
    "filename":"energy_molding.jpg",
    "status":"Not Done",
    "table":[
        ["<b>Material</b>","<b>Energy required, relative to virgin material</b>"],
        ["Virgin Material",1],
        ["Recycled paper fibers",0.73],
        ["Agricultural Wastes","0.5-0.7"]
    ],
    "details":"Some estimates of the energy savings for injection molding, using various materials as feedstock for a given part.",
    "references":["molding1"],
    "source_file":"waste_econ.py"
})