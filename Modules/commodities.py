#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Commodities

import helper
import pandas as pd
import numpy as np

from primary_energy_factors import primary_factors # Source is 'energycode'
primary_factors["Oil"]=1
primary_factors["Oil Products"]=1.05
primary_factors["Natural Gas"]=1.05
primary_factors["Biofuel"]=1.05
primary_factors["Heat"]=1
primary_factors["Geothermal"]=1

# From IEA Sankey diagram, energy input into Chemicals industry in 2016, 'iea_sankey'
# In PJ. Includes all industrial feedstock.
chemicals_energy = {
    "Oil":2+375,
    "Oil Products":2426+24932,
    "Coal":4995+2317,
    "Natural Gas":5051+7066,
    "Biofuel":91,
    "Electricity":4479,
    "Heat":2393
}
chemical_energy = sum([chemicals_energy[key]*primary_factors[key] for key in chemicals_energy])
chemical_energy_no_electricity = sum([chemicals_energy[key]*primary_factors[key] for key in chemicals_energy if key != "Electricity"])

chemical_energy_savings = [
    ["Best Practices",chemical_energy_no_electricity * 0.00016], # saygin
    ["Catalytic Processes",13.000], # chemicals_roadmap
    # The ((87.4+56.7)/2-(55.+8.)/2) term is recycling energy savings per ton of plastic, based on plastic_recycling (I think).
    # Text that was deleted from the site: Plastics recycling is a major opportunity for energy reduction.  Energy costs of new plastics range from 56.7 GJ (gigajoules) per ton for PVC to 87.4 GJ for polystyrene. Depending on recycling practices, recycled plastics require 8-55 GJ per ton, including collection, sorting, and remanufacturing.
    # The 348 is 348 million tons of plastic worldwide, as given in plasticseurope
    # The 0.8 is based on 20% of plastic already being recycled, as stated on p. 61 of futureofpetrochemicals.
    ["Plastics Recycling",0.8 * ((87.4+56.7)/2-(55.+8.)/2) * 348 * 0.001]
]
im_chemical_energy = {
    "filename":"chemical_energy_savings.jpg",
    "status":"Done",
    "details":"Show worldwide energy savings (in exajoules) for three strategies in the chemicals industry.",
    "table":chemical_energy_savings,
    "references":["iea_sankey","saygin","chemical_roadmap","futureofpetrochemicals","plasticseurope","plastic_recycling"],
    "source_file":"commodities.py"
}
#helper.save_image(im_chemical_energy)

################### Energy to electrify chemcials. It's a lot.

chemical_elec_table = [ # Reference: ccu_chemical
    ["<b>Scenario, 2030</b>","<b>Electricity Required, PWh per year</b>"],
    ["High TRL",32000],
    ["Low TRL",18100],
    ["World Electricity Production",33000]
]

#helper.save_image({
#    "filename":"chemical_electrolysis.jpg",
#    "status":"Done",
#    "table":chemical_elec_table,
#    "details":"In this plot we try to answer the question of how much electricity it would take to replace heat and feedstocks in the chemical industry with electricity. Turns out it's a lot, according to this paper. They analyze 20 major chemicals, which cover about 75% of emissions from the industry, so even these numbers aren't complete. The High TRL (technological readiness scenario) envisions electrolyzing methanol and methane, using them as feedstock for olefins and BTX, and then transforming into other chemicals. The Low TRL scenario envisions using captured CO2 to directly produce olefins, BTX, carbon monoxide, ethylene oxide, and styrene. The Low TRL scenario should be less energy intensive, but it entails industrial processes that are not commercialized, whereas everything in the High TRL scenario is pretty much commercially available, just really expensive. The paper gives the 33000 PWh (petawatt-hour) electricity demand in 2030. Bottom line: it is hard to come up with economical alternatives to fossil fuel feedstocks in the chemical industry.",
#    "references":["ccu_chemical"],
#    "source_file":"commodities.py"
#})

################## Plastic pollution
# Source: https://ourworldindata.org/plastic-pollution
# In both cases, 2010 figures.
 # Total waste generated
df_plastic_waste = pd.read_csv('/Users/michaelgoff/Desktop/Reading Material/plastic-waste-generation-total.csv')
#waste_codes = df_plastic_waste[df_plastic_waste["Plastic waste generation (tonnes, total) (tonnes per year)"] > 7000000]["Code"].as_matrix()
# Mismanaged waste that is within 50 kilometers of the ocean. Includes 2% of total waste generation as litter.
# Title of waste column is "Mismanaged waste (% global total) (% of global total)"
df_mismanaged_plastic_waste = pd.read_csv('/Users/michaelgoff/Desktop/Reading Material/mismanaged-waste-global-total.csv')
# Countries with most dismanaged waste
#mismanaged_codes = df_mismanaged_plastic_waste[df_mismanaged_plastic_waste["Mismanaged waste (% global total) (% of global total)"]> 4]["Code"].as_matrix()
#combined_codes = np.union1d(mismanaged_codes, waste_codes)
plastic_waste = [
     ["<b>Country</b>","<b>Plastic Waste Generation, Tons, 2010</b>","<b>Share of World Mismanaged Waste, 2010</b>"],
     ["Brazil",11852055, 1.4804],
     ["China",59079741, 27.6966],
     ["Germany",14476561, 0.0981],
     ["Indonesia",5045714, 10.1019],
     ["Japan",7993489, 0.4494],
     ["Philippines",2565766, 5.9153],
     ["Sri Lanka",2621606, 4.9968],
     ["United States",37825550, 0.8649],
     ["Vietnam",3268227, 5.7588],
     ["Other Countries",273271934-144728709,100-57.3622],
     ["Marine Sources","--",20.]
]
for i in range(1,len(plastic_waste)-1):
    plastic_waste[i][2] *= 0.8
    
im_plastic = {
    "filename":"plastic_pollution.jpg",
    "status":"Done",
    "details":"Plastic waste and pollution. The following table shows the top five countries in total plastic waste generation and the top five in mismanaged waste that has the potential to get into the ocean. China is the only country in the top five on both categories. The key message here is that good waste management practices, rather than the total volume of plastic generated, is the main factor in pollution. I'm not sure how best to set up the plot, but do it in a way that highlights this observation. Note also the 20% that comes from marine activities, mostly fishing.",
    "table":plastic_waste,
    "references":["owid_plastic","plastic_marine","plastic_mis"],
    "source_file":"commodities.py"
}
#helper.save_image(im_plastic)

######################################## Steel

# Average GHG intensity in steel_production2018. Average of three primary production methods
average_ghg_intensity = (1.5/18.3 + 2.3/23.2 + 2.8/29.9)/3.
steel_energy_intensity = [
    ["<b>Method</b>","<b>Primary Energy, Low (GJ/ton)</b>","<b>Primary Energy, High (GJ/ton)</b>","<b>Greenhouse Gases, Low (tons CO<sub>2</sub>e/ton)</b>","<b>GHG, High (tons CO<sub>2</sub>e/ton)</b>"],
    ["Modern Production",18.3,29.9,1.5,2.8], # steel_production2018, p. 15
    ["Best Practices",14.8,17.8, 14.8*average_ghg_intensity, 17.8*average_ghg_intensity], # best_practices
    ["From Scrap",18.3*0.26, 29.9*0.26, 1.5*0.26, 2.8*0.26], # From steel_energy_recycling, 74% less energy to recycle.
    # The following three are from fisch. See p. 15 for primary energy and p. 21 for GHG. Based on eyeballing the chart, long term value.
    ["Blast Furnace, CCS",1.2*primary_factors["Electricity"]+14.4, 1.2*primary_factors["Electricity"]+14.4, 0.75, 0.75], # fisch, p. 15
    ["Hydrogen Direct Reduction",13.1*primary_factors["Electricity"], 13.1*primary_factors["Electricity"], 0.18, 0.18], # fisch, p. 15
    ["Electrowinnowing",9.3*primary_factors["Electricity"], 9.3*primary_factors["Electricity"], 0.18, 0.18] # fisch, p. 15
]

im_steel = {
    "filename":"steel_energy.jpg",
    "status":"Done",
    "details":"Show energy and greenhouse gases from steel production. The Modern Production and Best Practices estimates are ranges over several steel making techniques, the details of which we don't need to burden the reader with. From Scrap is based on 100% recycling, which of course is not possible on a global scale, but it does illustrate the advantage of maximizing recycling.",
    "table":steel_energy_intensity,
    "references":["steel_production2018","best_practices","steel_energy_recycling"],
    "source_file":"commodities.py"
}
#helper.save_image(im_steel)

steel_energy = {
    "Oil Products":278,
    "Coal":12301,
    "Natural Gas":2174,
    "Biofuel":144,
    "Electricity":4011,
    "Heat":574
}
#steel_primary_energy = sum([steel_energy[key]*primary_factors[key] for key in steel_energy]) # From iea_sankey and energycode

################################# Cement

# Total cement emissions: for now, go with 0.9 tons CO2e / ton cement, based on altcement.
cement_emissions = [
    ["Portland Cement",0.9], # altcement
    ["Process Improvements",0.9-0.17], # From iea_cement, sum of savings from direct and energy emissions (but not from alternative energy or CCS) on p. 19.
    ["Alternative Binder, Low Estimate",0.9-(0.813-0.36)], # altcement, see Figure 7
    ["Alternative Binder, High Estimate",0.9-(0.813-0.663)] # altcement, see Figure 7
]
im_cement = {
    "filename":"cement_ghg.jpg",
    "status":"Done",
    "details":"Show greenhouse gas emissiosn from cement production, with various strategies for reduction. For now I am planning only on GHG and not energy. CCS might be added here later.<br><br>I just noticed this file was marked as done, but I don't see it. Did you send it already and I forgot to upload it? Or maybe I marked it off as done by mistake.",
    "table":cement_emissions,
    "references":["altcement","iea_cement"],
    "source_file":"commodities.py"
}
#helper.save_image(im_cement)

# All from altcement, Fig. 1
cement_emissions_breakdown = [
    ["Calcination",0.9*0.5],
    ["Pyroprocessing",0.9*0.5*0.85],
    ["Quarrying",0.9*0.5*0.07],
    ["Grinding",0.9*0.5*0.05],
    ["Transportation",0.9*0.5*0.03]
]
im_cement_breakdown = {
    "filename":"cement_breakdown.jpg",
    "status":"Done",
    "details":"Show the main sources of greenhouse gas emissions from current cement production. The main point to illustrate is that about half are from the calcination process, and the other half is from energy.",
    "table":cement_emissions_breakdown,
    "references":["altcement"],
    "source_file":"commodities.py"
}
#helper.save_image(im_cement_breakdown)

######################################## Aluminum

# kWh/MJ, onsite.
aluminum_energy = [
    ["World Average, 2017",14154], # iea_aluminum
    ["State of the Art",13000], # kvande
    ["Secondary",3.35/0.0036], # etsap_alum. See table on p. 5, converting GJ/ton to kWh/MJ. I am assuming this is onsite electricity; might be wrong.
    ["New Technology, High End",12000], # Based in iea_aluminum, novel physical designs for anodes
    ["New Technology, Low End",14154*0.6] # Based on iea_aluminum, multipolar cells
    # Note that the above range includes the carbothermic reaction described by kvande.
]
im_aluminum = {
    "filename":"aluminum_energy.jpg",
    "status":"Done",
    "details":"Show energy consumption for various current and possible future methods of aluminum production. Figures are in kWh/ton of aluminum. Unlike some of the other plots, these are all onsite rather than primary energy figures, as they all are mostly electricity. <font color='blue'>In earlier version, the secondary aluminum figure was in error and has been corrected.</font> Secondary production from the ETSAP study, state of the art figure from Kvande and Drabløs, and all others from the IEA.",
    "table":aluminum_energy,
    "references":["iea_aluminum","kvande","etsap_alum"],
    "source_file":"commodities.py"
}
#helper.save_image(im_aluminum)

################### Pulp and paper

paper_energy = [
    ["Virgin Pulp",29.29/0.907185*1.055], # Based on warm15. For the main scenario, say 1 ton of paper landfilled, and for the alternative, 1 ton source reduced. Then go to the Summary Report (energy) tab. Also did unit conversions.
    ["Recycled Paper",8.88/0.907185*1.055], # Based on warm15. Similar to the above, but the baseline is recycling.
    ["Best Technology",29.29/0.907185*1.055 * (1645./2110.)], # Based on paper_bandwidth, p. 6
    ["Best Technology and New Technology",29.29/0.907185*1.055 * (1498./2110.)] # Based on paper_bandwidth, p. 6
]
im_paper_energy = {
    "filename":"paper_energy.jpg",
    "status":"Done",
    "details":"Details from current and potential future paper production in the United States. These are all US specific figures, unlike the other major commodities. They are in GJ/ton of paper.",
    "table":paper_energy,
    "references":["warm15","paper_bandwidth"],
    "source_file":"commodities.py"
}
helper.save_image(im_paper_energy)

# From fao_wood2016, millions of cubic meters of production.
wood_products = [
    ["Wood Panels",416],
    ["Fiber Furnish", 415],
    ["Paper and Paperboard",409],
    ["Wood Fuel, Charcoal, Pellets",1863]
]
im_wood_products = {
    "filename":"wood_products.jpg",
    "status":"Done",
    "details":"Major classes of wood products worldwide. The key message here is that wood usage is still dominated by fuel. Units are millions of cubic meters.",
    "table":wood_products,
    "references":["fao_wood2016"],
    "source_file":"commodities.py"
}
#helper.save_image(im_wood_products)

####################################
# Overall energy and GHG by commodity
cement_energy = (3.5*0.6*primary_factors["Coal"] + 91*0.0036*primary_factors["Electricity"])*4171 # PJ. Table 2 of iea_cement for all relevant figures except PEFs
paper_pulp_energy_sankey = { # PJ, worldwide. From iea_sankey
    "Oil Products":156,
    "Coal":680,
    "Natural Gas":1030,
    "Biofuel":2744,
    "Electricity":1661,
    "Heat":513
}
#paper_pulp_energy = sum([paper_pulp_energy_sankey[key]*primary_factors[key] for key in paper_pulp_energy_sankey])
#aluminum_energy = 140*10**6/23884.58966275 *primary_factors["Electricity"] # From futureofpetrochemicals, assuming all the energy is electricity

industry_energy_sankey = {
    "Oil":245+364,
    "Oil Products":13187+24631,
    "Coal":34232+2105,
    "Natural Gas":23764+7786,
    "Biofuel":8671,
    "Geothermal":24,
    "Electricity":32201,
    "Heat":5764
}
#industrial_energy = sum([industry_energy_sankey[key]*primary_factors[key] for key in industry_energy_sankey])

commodity_summary = [
    ["<b>Commidity</b>","<b>Primary Energy Consumption (PJ/year)</b>"],
    ["Chemicals",chemical_energy], # iea_sankey
    ["Iron and Steel",steel_primary_energy], # iea_sankey
    ["Cement",cement_energy],
    ["Paper and Pulp",paper_pulp_energy],
    ["Aluminum",aluminum_energy],
    ["Other Industry",industrial_energy - chemical_energy - steel_primary_energy - cement_energy - paper_pulp_energy - aluminum_energy],
    ["<b>Commodity</b>","<b>Greenhouse Gases (million tons CO2e/year)</b>"],
    ["Chemicals",1200], # iea_ind
    ["Iron and Steel",2000], # iea_ind
    ["Cement",2200], # iea_ind
    ["Paper and Pulp",200], # iea_ind
    ["Aluminum",300], # iea_ind
    ["Other Industry",2500] # iea_ind of course
]
summary_im = {
    "filename":"commodity_summary.jpg",
    "status":"Done",
    "details":"Summaryize energy and GHG for major commodities. I have ongoing uncertainty as to the correct values for cement, so that could change. The emissions figures are direct emissions, excluding emissions from electricity. That may be something we want to change later.",
    "table":commodity_summary,
    "references":["iea_sankey","iea_cement2","altcement","futureofpetrochemicals","energycode","iea_ind"],
    "source_file":"commodities.py"
}
#helper.save_image(summary_im)

######################################################### Solution for green steel

green_steel_chart = [
    ["<b>Production method</b>","<b>Variable cost: oil</b>","<b>Variable cost: coal</b>","<b>Variable cost: graphite</b>","<b>Variable cost: biomass fuel</b>","<b>Variable cost: electricity</b>","<b>Capital investment</b>"],
    ["Blast Furnace, Sweden",4,96,0,0,11,"---"],
    ["Green Steel, Sweden",0,0,6,5,157,770/(1/0.07)] # Assuming a 7% discount rate
]

helper.sve_image({
    "filename":"green_steel.jpg",
    "status":"Not Done",
    "details":"This is a Solution plot, showing the economics of producing steel from hydrogen that is produced from low-carbon electricity (green steel). A 7% discount rate is used when assessing the capital investment of the green steel. There are not separate capital investment figures for blast furnace steel, so really this assesses the economics of retrofitting a blast furnace facility, rather than building something fresh.",
    "references":["whalen"],
    "source_file":"commodities.py"
})