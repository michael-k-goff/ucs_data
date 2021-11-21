# Ozone-related plots

import helper

helper.save_image({
    "filename":"ozone_status.jpg",
    "status":"Done",
    "details":"For this, let's replicate the time series plot showing ozone depletion. The image at the top of the references <a href=\"https://ozonewatch.gsfc.nasa.gov/facts/eesc_SH.html\">here</a> shows the evolution, by chemical, of ozone depleting substances from 1950 to 2020. Only do the overall, not by individual chemical, which you will have to estimate visually. The units are the ozone-depleting equivalent of parts per billion of stratospheric chorine.",
    "references":["ozonewatch"],
    "source_file":"ozone.py"
})

odp_table = [
    ["<b>Substance</b>","<b>Emissions in 2016, thousands of tons of CFC-11 equivalent, low estimate</b>","<b>Emissions, high estimate</b>","<b>Major Sources</b>"],
    ["Methyl chloride",2707*0.015,"","Mostly natural sources: plants, biomass burning, the ocean, salt marshes, and fungi. Some from coal combustion."],
    # See figure on p. ES.21 of ozone2018 to estimate that 10* of methyl bromide is artificial
    ["Methyl bromide - natural",85*0.57*0.9,"","From ecosystems."],
    ["Methyl bromide - artificial",85*0.57*0.1,"","Biomass burning, several agricultural sources."],
    ["CFC-11",46,68,"Legacy sources: refrigerants and aerosols; possible unreported production."],
    ["CFC-12",16*0.73,64*0.81,"Legacy sources: refrigerants and aerosols."],
    ["CFC-113",0,7*0.82,"Legacy sources: refrigerants and aerosols."],
    ["CFC-114",0.4*0.5,1.5*0.5,"Legacy sources: refrigerants and aerosols."],
    ["HCFC-22",300*0.024,400*0.034,"Refrigerants and propellants."],
    ["HCFC-141b",58*0.069, 70*0.102,"Refrigerants"],
    ["Carbon tetrachloride",40*0.89,40*0.89,"Legacy sources; unreported use in chemical industry."],
    ["Methyl chloroform",0,5*0.17,"Minimal emissions"],
    ["Halon-1211",0.3*6.9,9.3*7.7,"Legacy sources: fire suppresion"],
    ["Halon-1301",1.4*15.2, 2*19,"Legacy sources: fire suppresion"],
    ["Halon-2402",0.4*15.7, 1.5*15.7,"Legacy sources: fire suppresion"]
]

# Get total emissions across chemicals, excluding the first two which are mostly from natural sources.
sums = [0,0]
for i in range(3,len(odp_table)):
    sums[0] += odp_table[i][1]
    if odp_table[i][2] != "":
        sums[1] += odp_table[i][2]
    else:
        sums[1] += odp_table[i][1]
#print(sums)
# Should get [139.15699999999998, 321.52500000000003]. Meaning 134 thousand to 316 thousand tons CFC-11 equivalent emissions.

helper.save_image({
    "filename":"odp_source.jpg",
    "status":"Done",
    "table":odp_table,
    "details":"Show major ozone-depleting substances, total emissions in terms of CFC-11 equivalent depletion potential as of 2016, and list of major sources of the substances. There are hundreds of chemicals that the WMO has identified as ozone depleting, so only major ones, as listed on the NASA site, are included. Estimates of depletion potential are given as a range in some cases, but if there is only one value, then that is the only value I have. All emissions figures are from the NASA site, information on sources of emissions from the WMO report. \"Legacy sources\" means that the use case has been phased out by the Montreal Protocol, but there are still some old products that leak; for example, there are old fire estinguishers with now-banned halons that still leak them. In the cases of CFC-11 and Carbon tetrachloride (CCl<sub>4</sub>), there appear to be some unreported sources in contravention of the Montreal Protocol.",
    "references":["ozonewatch","ozone2018"],
    "source_file":"ozone.py"
})