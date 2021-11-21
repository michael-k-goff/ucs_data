# Industrial summary plots

import helper
import primary_energy_factors

# For emissions, see ag_summary.py also for the emissions intensity of world energy.
emissions_from_energy = 33*0.72/0.76
world_primary = 13864.9 * 0.042 # EJ, from BP
emissions_intensity = emissions_from_energy / world_primary

# See commodities.py and commodity_summary.jpg
major_commodities = {
    "Energy":{ # In PJ
        "Chemicals":66176.893,
        "Iron and Steel":28918.686999999998,
        "Cement":13524.5058732,
        "Paper and Pulp":10613.886999999999,
        "Aluminum":18563.433839999685,
        "Other Industry":90674.96028680028
    },
    "GHG":{ # Millions of tons CO2e
        "Chemicals":1200,
        "Iron and Steel":2000,
        "Cement":2200,
        "Paper and Pulp":200,
        "Aluminum":300,
        "Other Industry":2500
    }
}

############################### Electrification of heat
heat_energy = { # See figures in industrial_heat5.jpg. In PJ energy, worldwide
    "Coal":38300,
    "Natural Gas":25500,
    "Oil":12800
}
heat_intensity = { # Emissions intensity
    "Coal":primary_energy_factors.emissions_factors["Coal"],
    "Natural Gas":primary_energy_factors.emissions_factors["Natural Gas"],
    "Oil":primary_energy_factors.emissions_factors["Oil"],
    "Electricity":50/3.6 # Assuming 50 gCO2e/kWh. Otherwise, with current prevailing carbon intensities, there is no rationale.
}
electricity_factor = 0.8 # Ratio of onsite electric heating to fossil fuel heating for industry overall. This figure is really just a wild guess.
e_heat_energy = sum([heat_energy[key]*(1-primary_energy_factors.primary_factors["Electricity"]) for key in heat_energy])
e_heat_ghg = sum([heat_energy[key]*(heat_intensity[key]-heat_intensity["Electricity"])/1000. for key in heat_energy])

############################### Best practices

best_practices = {
    "Chemicals":[8300, 1200.*8300./66177], # Taking the 8.3 EJ savings, then reducing emissions by the same proportion.
    "Iron and Steel":[28919*(1.-16.3/24.1), 2000*(1.-1.4928117514382784/2.15)],
    "Cement":[0, 2200*0.73/9], # See cement_ghg.jpg. Lacking a figure for energy right now.
    "Aluminum":[18563*(1.-13000./14154.), 300*(1.-13000./14154.)],
    "Paper":[10614*(1-26.555801738344435/34.06245694097675), 200*(1-26.555801738344435/34.06245694097675)]
}
best_practices_energy = sum([best_practices[key][0] for key in best_practices])
best_practices_ghg = sum([best_practices[key][1] for key in best_practices])

############################### Best practices and new technology

new_practices = {
    "Chemicals":[13000, 1200.*13000./66177], # Taking the 13 EJ savings from catalytic processes
    "Iron and Steel":[28919*(1.-16.3/24.1), 2000*(1.-1.4928117514382784/2.15)],
    "Cement":[0, 2200*0.44700000000000006/9], # See cement_ghg.jpg, low estimte for alternative binder.. Lacking a figure for energy right now.
    "Aluminum":[18563*(1.-8492./14154.), 300*(1.-8492./14154.)],
    "Paper":[10614*(1-24.182730093641315/34.06245694097675), 200*(1-24.182730093641315/34.06245694097675)]
}
new_practices_energy = sum([new_practices[key][0] for key in new_practices])
new_practices_ghg = sum([new_practices[key][1] for key in new_practices])

############################### CCS
# Plan: apply CCS to all ammonia, steel, cement, and paper in the world.
# I will treat all chemicals like ammonia. Maybe a bit bold. I will also treat emissions reported in commodity_summary.jpg as capturable emissions.
# Assume 90% capture, using energy figures as in ccs_energy_cost.jpg

# First value is overall emissions in millions of tons, second is capture cost in MJ/kg.
ccs_data = {
    "Chemicals":[1200,1.2768],
    "Paper and Pulp":[200,1.69668],
    "Iron and Steel":[2000,3.7052899999999998],
    "Cement":[2200,3.63503]
}
ccs_energy = sum([ccs_data[key][0]*ccs_data[key][1]*(-0.9) for key in ccs_data])
ccs_ghg = sum([ccs_data[key][0]*0.9 for key in ccs_data])

############################### Recycling. See figures here: https://datatopics.worldbank.org/what-a-waste/trends_in_solid_waste_management.html
# Cite this source: https://openknowledge.worldbank.org/handle/10986/30317
msw_generation = 2.01 # Billion tons per year
msw_composition = { # As shares of total
    "Food and Green":0.44,
    "Glass":0.05,
    "Metal":0.04,
    "Other":0.14,
    "Paper and Cardboard":0.17,
    "Plastic":0.12,
    "Rubber and Leather":0.02,
    "Wood":0.02
}
# Now, based on the msw_stats15 reference (see recycling.py), adding categories to match what we have in WArm.
msw_composition["PET"] = 5100./34500. * msw_composition["Plastic"]
msw_composition["HDPE"] = 6040./34500. * msw_composition["Plastic"]
msw_composition["Tires"] = 3750./8480. * msw_composition["Rubber and Leather"]
msw_composition["Food Waste"] = 39730./(39730.+34720.+3990.) * msw_composition["Food and Green"]
msw_composition["Yard Trimmings"] = 34720./(39730.+34720.+3990.) * msw_composition["Food and Green"]
msw_composition["Steel"] = 18170./(18170.+3610.+2220.) * msw_composition["Metal"]
msw_composition["Aluminum"] = 3610./(18170.+3610.+2220.) * msw_composition["Metal"]
msw_composition["Other Nonferrous"] = 2220./(18170.+3610.+2220.) * msw_composition["Metal"]

recycling_savings = {
    "Energy":{
        "Aluminum":193.97538978382872-34.082829058704505,
        "Steel":37.80247563899231-16.665270493143378,
        "Other Nonferrous":128.49498214713307-41.91916314638948, # Based on copper wire
        "HDPE":27.51075687049938-7.836334087684975,
        "PET":32.233454214010855-15.014416112004408,
        "Paper and Cardboard":33.105272502379435-11.779995338426058,
        "Glass":7.397499378774616-4.900320916165671,
        "Wood":0.17762357265419276-0.5433191634128248,
        "Food Waste":-0.57 / 1.055 / 0.907185, # See recycling.py, with unit conversions
        "Tires":3.87 / 1.055 / 0.907185
    },
    "GHG":{
        "Aluminum":12.114397835061206-2.0282522308018756,
        "Steel":4.012412021803711-1.973136681051825,
        "Other Nonferrous":7.4736685461069134-2.502245958652315,
        "HDPE":1.6755127124015499-0.7165021467506628,
        "PET":2.4361072989522534-1.1464034348010606,
        "Paper and Cardboard":8.388586671957759-4.321059100403996,
        "Glass":0.6613865970006118-0.3306932985003059,
        "Wood":2.22666820990206-0.6172941572005712,
        "Food Waste":0.72 / 0.907185,
        "Tires":0.4 / 0.907185
    }
}
recycling_energy_savings = 0
for key in recycling_savings["Energy"]:
    recycling_energy_savings += recycling_savings["Energy"][key] * msw_generation * msw_composition[key] * 0.81 * 1000 # 19% of MSW is recycled or composted, according to World Bank report
recycling_ghg_savings = 0
for key in recycling_savings["GHG"]:
    recycling_ghg_savings += recycling_savings["GHG"][key] * msw_generation * msw_composition[key] * 0.81 * 1000 # 19% of MSW is recycled or composted, according to World Bank report

############################### Motor and steam systems
motor_system_energy = [1000*8.539498799999995, 1000*18.0278308]
steam_system_energy = [1000*8.8, 1000*8.8]
system_energy = [motor_system_energy[0]+steam_system_energy[0],motor_system_energy[1]+steam_system_energy[1]]
system_ghg = [system_energy[0]*emissions_intensity, system_energy[1]*emissions_intensity]

############################### Material efficiency. I am taking the portion of savings in 2060 for steel, cement, aluminum and applying them to their impacts as reported above.
material_efficiency_savings = {
    "Iron and Steel":[2210,1679.6],
    "Cement":[4510,3833.5],
    "Aluminum":[227.5,188.825]
}
material_efficiency_energy = sum([ (material_efficiency_savings[key][0]-material_efficiency_savings[key][1])/material_efficiency_savings[key][1]*major_commodities["Energy"][key]  for key in material_efficiency_savings])
material_efficiency_ghg = sum([ (material_efficiency_savings[key][0]-material_efficiency_savings[key][1])/material_efficiency_savings[key][1]*major_commodities["GHG"][key]  for key in material_efficiency_savings])

industry_savings_table = [
    ["<b>Method</b>","<b>Potential World Energy Savings, PJ (Primary)</b>","<b>Potential World GHG Savings, millions tons CO<sub>2</sub<e</b>"],
    ["Electrification of Industrial Heat",e_heat_energy,e_heat_ghg],
    ["Best Practices for Major Commodities",best_practices_energy,best_practices_ghg],
    ["New Technologies for Major Commodities",new_practices_energy,new_practices_ghg],
    ["Full Use of Industrial CCS",ccs_energy,ccs_ghg],
    ["100% Recycling of Municipal Solid Waste",recycling_energy_savings,recycling_ghg_savings],
    ["Efficient Steam and Motor Systems",str(system_energy[0])+"-"+str(system_energy[1]),str(system_ghg[0])+"-"+str(system_ghg[1])],
    ["Improve Material Efficiency",material_efficiency_energy,material_efficiency_ghg]
]

helper.save_image({
    "filename":"industry_overview.jpg",
    "status":"Done",
    "table":industry_savings_table,
    "details":"Overall energy and greehouse gas savings potential in world industry. The electric heat scenario assumes that 80% onsite energy is needed with electricity, relative to fossil fuels. That's just a guess based on the data in electric_heat.jpg. Unlike what is portrayed on the Industrial Heat page, here I am assuming that the electricity comes from a low carbon source (50 gCO2e/kWh). Be sure to note this assumption; if we assume the current world average carbon intensity, there really is not case for electric heat. I also assume that electricity replaces 100% of all coal, natural gas, and oil for heating, but not any of the current renewable heat. Also, I used different sources for the carbon intensity of fossil fuel heat that is currently shown on the greenhouse gases in industrial heat plot, and that plot will have to be updated.<br><br>The best practices and new technology scenarios are based on the data presented for the five major commodities. Best practices mean bringing the world up to the currently most efficient systems, while new technology means implementing best practices along with plausible new technologies and deploying them everywhere. The CCS scenario assumes 90% capture of emissions from chemicals, steel, cement, and paper. See the major commodities page for capturable emissions from those industries and the CCS page for the estimated energy cost of doing so. See pages on recycling, industrial systems, and material efficiency for details on those topics. Don't do this until all the boxes in the table are filled in.<br><br>",
    "references":["wb_waste"],
    "source_file":"industry_overview.py"
})

############################################## Overiew of energy usage in industry

# From iea_sankey, year 2017. All in PJ.
industry_energy = {
    "Iron and Steel":{
        "Oil Products":292,
        "Coal":13122,
        "Natural Gas":2320,
        "Biofuels and waste":152,
        "Electricity":4092,
        "Heat":579
    },
    "Chemicals and petrochemical":{
        "Oil":2,
        "Oil Products":2624,
        "Coal":4541,
        "Natural Gas":5721,
        "Biofuels and waste":90,
        "Electricity":4599,
        "Heat":2437
    },
    "Non-ferrous metals":{
        "Oil Products":191,
        "Coal":1064,
        "Natural Gas":695,
        "Electricity":3865,
        "Heat":205
    },
    "Non-metallic minerals":{
        "Oil Products":1661,
        "Coal":9098,
        "Natural Gas":2202,
        "Biofuels and waste":384,
        "Electricity":2110,
        "Heat":125
    },
    "Transport equipment":{
        "Oil Products":88,
        "Coal":97,
        "Natural Gas":523,
        "Electricity":1068,
        "Heat":162
    },
    "Machinery":{
        "Oil Products":230,
        "Coal":330,
        "Natural Gas":1081,
        "Electricity":3462,
        "Heat":367
    },
    "Mining and quarrying":{
        "Oil Products":991,
        "Coal":255,
        "Natural Gas":338,
        "Electricity":1337,
        "Heat":88
    },
    "Food and tobacco":{
        "Oil Products":396,
        "Coal":1164,
        "Natural Gas":1990,
        "Biofuels and waste":1540,
        "Electricity":1842,
        "Heat":488
    },
    "Paper pulp and print":{
        "Oil Products":156,
        "Coal":680,
        "Natural Gas":1030,
        "Biofuels and waste":2744,
        "Electricity":1661,
        "Heat":513
    },
    "Wood and wood products":{
        "Oil Products":92,
        "Coal":53,
        "Natural Gas":124,
        "Biofuels and waste":323,
        "Electricity":414,
        "Heat":99
    },
    "Construction":{
        "Oil Products":1315,
        "Coal":170,
        "Natural Gas":364,
        "Biofuels and waste":22,
        "Electricity":679,
        "Heat":41
    },
    "Textile and leather":{
        "Oil Products":143,
        "Coal":423,
        "Natural Gas":357,
        "Biofuels and waste":132,
        "Electricity":1145,
        "Heat":404
    },
    "Non-specified (industry)":{
        "Oil":242,
        "Oil Products":5009,
        "Coal":3234,
        "Natural Gas":7020,
        "Biofuels and waste":3265,
        "Geothermal":24,
        "Electricity":5945,
        "Heat":255
    },
    "Non-energy use":{
        "Oil":364,
        "Oil Products":24631,
        "Coal":2105,
        "Natural Gas":7786
    }
}

primary_by_industry = {}
for key in industry_energy:
    primary_by_industry[key] = sum([industry_energy[key][k]*primary_energy_factors.primary_factors[k] for k in industry_energy[key]])
    
industry_energy_table = [
    ["<b>Industry</b>","<b>Primary Energy (PJ)</b>"]
]
for key in primary_by_industry:
    industry_energy_table = industry_energy_table + [[key,primary_by_industry[key]]]

helper.save_image({
    "filename":"industry_energy.jpg",
    "status":"Done",
    "details":"This plot is an overall summary of energy in industry for use on the Industry Overview page. Combine the data shown in industrial_heat_context.jpg (including the other major sectors for context) and the table below for an infographic showing how we use energy in industry. Getting greenhouse gas data by industry may be a complicated matter, because I would need to include process emissions as well, so that's not here (for now). The data in this table comes from the IEA sankey diagram.<br><br>Some notes if you think clarification is necessary. The biggest piece of non-metallic minerals is cement, but it includes some other things like bricks. The main pieces of nonferrous (meaning, non-iron) metals are aluminum and copper. Chemicals and petrochemicals includes a lot of things, especially plastic and ammonia, and it would nice to break it further, but that might be hard to do. If you think it's appropriate, highight the five industries we focus on here. Non-energy use is, I think, primarily feedstocks into products, such as oil for plastics.",
    "table":industry_energy_table,
    "references":["iea_sankey"],
    "source_file":"industry_overview.py"
})