# Mining figures

import helper

type_table = [
    ["<b>Target mineral</b>","<b>Share of surface mining in the US</b>"],
    ["All minerals","85%"],
    ["Metallic ores","98%"],
    ["Non-metallic ores","97%"],
    ["Coal","61%"]
]

helper.save_image({
    "filename":"mining_techniques.jpg",
    "status":"Done",
    "details":"A basic plot about how much mining in the US is done by surface mining. This will be a good start to the mining section, but I imagine we'll eventually want to replace this.",
    "table":type_table,
    "references":["mining_techniques"],
    "source_file":"mining.py"
})

metals_recycling = [
    ["<b>Recycling rate bucket</b>","<b>Metals</b>"],
    [">50%","Aluminum, Titanium, Chromium, Manganese, Iron, Cobalt, Nickel, Copper, Zinc, Niobium, Rhodium, Palladium, Silver, Tin, Rhenium, Platinum, Gold, Lead"],
    ["25-50%","Magnesium, Molybdenum, Iridium"],
    ["10-25%","Rubidium, Cadmium, Tungsten"],
    ["1-10%","Antimony, Mercury"],
    ["<1%","Lithium, Beryllium, Boron, Scandium, Vanadium, Gallium, Germanium, Arsenic, Selenium, Strontium, Yttrium, Zirconium, Indium, Tellurium, Barium, Hafnium, Tantalum, Osmium, Thallium, Bismuth, Lanthanum, Cerium, Praesodymium, Neodymium, Samarium, Europium, Gadolinium, Terbium, Dysprosium, Holmium, Erbium, Tm, Ytterbium, Lutetium"]
]

helper.save_image({
    "filename":"metals_recycling.jpg",
    "status":"Done",
    "details":"It looks like the last line got cut off. Also, check the spelling (e.g. cpper => copper).",
    "table":metals_recycling,
    "references":["metals_recycling"],
    "source_file":"mining.py"
})

metals_waste = [
    ["<b>Metal</b>","<b>Tailings Generated per Ton Ore</b>","<b>Source</b>"],
    ["Copper","167 tons","University of Arizona"],
    ["Gold","200000 tons","Rashotte"],
    ["Lead and Zinc","17 tons","Calvo et al."],
    ["Lithium","77 tons","Nemaska Lithium"],
    ["Iron Ore","1.4-2 tons","IEA"],
    ["Nickel","50+ tons","IEA"],
    ["Deep Sea Mining (sediment per ton of ore)","4 tons","Sharma"]
]

helper.save_image({
    "filename":"metals_waste.jpg",
    "status":"Done",
    "details":"Added the deep sea mining figure.",
    "table":metals_waste,
    "references":["copper_tailings","gold_tailings","leadzinc_tailings","lithium_tailings","iea_mining","sharma_dsm"],
    "source_file":"mining.py"
})

########################################

# Overall production. Figures from https://pubs.usgs.gov/periodicals/mcs2021/mcs2021.pdf unless otherwise noted. In tons and 2020 figures unless otherwise noted.

production = [
    ["<b>Mineral</b>","<b>Production, Tons</b>","<b>Main Uses</b>","<b>Category, if any</b>"],
    ["Abrasives, fused aluminum oxide",1300000],
    ["Abrasives, silicon carbide",1000000],
    ["Aluminum",65200000,"Widely used","Base Metal"],
    ["Antimony",153000],
    ["Arsenic",32000],
    ["Asbestos",1200000,"Building material in low-income countries, despite toxicity","Mineral"],
    ["Barite",7500000,"Oil and gas drilling","Mineral"],
    ["Alumina",136000000],
    ["Bauxite",371000000,"Aluminum and Gallium production","Mineral"],
    ["Beryllium",240,"","Precious Metals"],
    ["Bismuth",17000,"","Precious Metals"],
    ["Boron",1000*(70+200+400+250+120+110+80+2400),"Precursor to boric acid and borax, used in turn to make glass, ceramics, and other items.","Mineral"], # Doesn't seem to be complete
    ["Bromine",430000],
    ["Cadmium",23000],
    ["Cement",4100000000],
    # Cesium: Don't have good numbers
    ["Chromium",40000000,"Stainless steel and other alloys.","Base Metal"],
    ["Bentonite",16000000],
    ["Kaolin",44000000],
    ["Cobalt",140000],
    ["Copper",20000000,"Electrical wires, roofing and plumbing, industrial machinery, other uses","Base Metal"],
    ["Diamond, Industrial",54*0.2], # Given as 54 million carats. According to Appendix A, a carat is 200 milligrams.
    ["Diatomite",2200000,"Abrasives and many other uses","Mineral"],
    ["Feldspar",23000000,"Glassmaking, ceramics, and other uses","Mineral"],
    ["Fluorspar",7600000,"Source of fluorine and fluoride","Mineral"],
    ["Gallium",300,"","Precious Metals"],
    ["Garnet, Industrial",1100000,"Abrasives, other uses","Mineral"],
    # $74B in gemstones produced (maybe just only diamonds?)
    ["Germanium",130,"","Precious Metals"],
    ["Gold",3200,"","Precious Metals"],
    ["Graphite (natural)",1100000,"Many uses","Mineral"],
    ["Gypsum",150000000,"Building material, other uses","Mineral"],
    # 140 million cubic meters of helium produced
    ["Indium",900,"","Precious Metals"],
    ["Iodine",30000],
    ["Pig Iron",1200000000],
    ["Raw Steel",1800000000],
    ["Iron Ore",2400000000,"Steelmaking","Mineral"], # 1.5 billion production of usable iron.
    ["Iron Oxide Pigments",3500+8000+360000+2500000+9000+50000+10000], # Not complete apparently
    # Kyanite and related minerals: numbers don't look to usable
    ["Lead",4400000,"Lead-acid batteries, other uses","Base Metal"],
    ["Lime",420000000,"Concrete","Mineral"],
    ["Lithium",82000],
    ["Magnesium compounds",26000000,"Aerospace, cars, electronics, other uses","Base Metal"], # Magnesium oxide content
    ["Magnesium metal",1000000],
    ["Manganese",18500000,"Steel production, aluminum alloys","Base Metal"],
    ["Mercury",3700,"","Precious Metals"],
    ["Mica",350000], # Scrap and flake, not sheet
    ["Molybdenum",300000],
    ["Nickel",2500000,"Stainless steel and other alloys","Base Metal"],
    ["Niobium",78000],
    ["Nitrogen (ammonia)",144000000,"Fertilizer","Mineral"],
    ["Peat",29000000,"Energy","Mineral"],
    ["Perlite",3400000,"Plaster, filtration, other uses","Mineral"],
    ["Phosphate Rock",223000000,"Fertilizer","Mineral"],
    ["Palladium",210,"","Precious Metals"],
    ["Platinum",170,"","Precious Metals"],
    # A few other platinum group metals are mentioned, but I don't have production statistics
    ["Potash",43000000,"Fertilizer","Minerals"],
    ["Pumice and Pumicite",21000000,"Construction, horticulture, medicine, cosmetics","Mineral"],
    # Quartz crystals mentioned but don't have good numbers
    ["Rare Earths",240000],
    ["Rhenium",53,"","Precious Metals"],
    # Don't have good Rubidium data
    ["Salt",270000000,"Sodium chloride and other industrial uses. A minority is used for food.","Mineral"],
    ["Sand and Gravel, Construction",50*10**9,"Many uses, especially cement and bricks. River and sea sand, as opposed to desert sand, is used for cement","Mineral"], # Not in the USGS report but it is here: https://www.visualcapitalist.com/all-the-worlds-metals-and-minerals-in-one-visualization/
    ["Sand and Gravel, Indusrial",265000000],
    # Data on Scandium is not available
    ["Selenium",2900],
    ["Silicon",8000000,"Cement, bricks, alloys, electronics","Base Metal"],
    ["Silver",25000,"","Precious Metals"],
    ["Soda Ash",52000000,"Soap, manufacture of glass and paper, other uses.","Minerals"],
    # Crushed stone and dimension stone isn't here
    ["Strontium",210000],
    ["Sulfur",78000000,"Precursor to sulfuric acid and other chemicals.","Mineral"],
    ["Talc and Pyrophyllite",5800000,"Many industries","Mineral"],
    ["Tantalum",1700],
    ["Tellurium",490,"","Precious Metals"],
    # Don't have good figures on thallium
    # Don't have good figures on thorium either
    ["Tin",270000,"Solder, tin plating, tin chemicals, brass and bronze alloys, other uses","Base Metal"],
    ["Titanium and titanium oxide",210000],
    ["Titanium minerals",8200000],
    ["Tungsten",84000],
    ["Vanadium",86000],
    ["Vermiculite",380000],
    ["Wollastonite",1100000,"Ceramics and other industries.","Mineral"],
    ["Yttium",10000], # 8000-12000 tons is stated
    ["Zeolites",1100000,"Widely used in industry","Mineral"],
    ["Zinc",12000000,"Anti-corrision, alloys such as brass and bronze","Base Metal"],
    ["Zirconium",1400] # Zirconium ores and zircon concentrates
]

mineral_table = [production[i][:3] for i in range(len(production)) if i==0 or (len(production[i])>3 and production[i][3] == "Mineral")]

helper.save_image({
    "filename":"mineral_production.jpg",
    "status":"Done",
    "table":mineral_table,
    "details":"Minerals that are most heavily produced. Most figures are from the USGS, and the sand and gravel figure is from Visual Capitalist. These are all minerals (not nonferrous metals and not fuels) the USGS reports with production figures above one million tons per year in 2020. If this list is too long, consider truncating it at a higher production value.",
    "references":["usgs2021","vc_minerals"],
    "source_file":"mining.py"
})

base_metal_table = [production[i][:3] for i in range(len(production)) if i==0 or (len(production[i])>3 and production[i][3] == "Base Metal")]

helper.save_image({
    "filename":"base_metal_production.jpg",
    "status":"Done",
    "table":base_metal_table,
    "details":"Top 10 base metals (nonferrous, or not iron) that are most heavily produced. Most figures are from the USGS, and the sand and gravel figure is from Visual Capitalist. These are all base metals the USGS reports with production figures above one million tons per year in 2020.",
    "references":["usgs2021"],
    "source_file":"mining.py"
})

precious_metal_table = [production[i][:3] for i in range(len(production)) if i==0 or (len(production[i])>3 and production[i][3] == "Precious Metals")]

helper.save_image({
    "filename":"precious_metal_production.jpg",
    "status":"Done",
    "table":precious_metal_table,
    "details":"Precious metal production in 2020.",
    "references":["usgs2021"],
    "source_file":"mining.py"
})

########################################

# Impacts. From reference 'dsm_comparison'

dsm_table = [
    ["<b>Impact</b>","<b>Terrestrial Mining</b>","<b>Deep Sea Mining</b>"],
    ["Climate change, billions of tons CO<sub>2</sub>e",1.5,0.4],
    ["Land use and forest use, km<sup>2</sup>",156000+66000,9800+5200],
    ["Seabed use, km<sup>2</sup>",2000,508000],
    ["Water use, km<sup>3</sup>",45,5],
    ["Primary and secondary energy, PJ",24500,25300],
    ["Solid waste, billions of tons",64,0],
    ["Terresterial toxicity, 1,4-DCB equivalent, millions of tons",33,0.5],
    ["Freshwater toxicity, 1,4-DCB equivalent, millions of tons",21,0.1],
    ["Eutrophication potential, PO<sub>4</sub> equivalent, millions of tons",80, 0.6],
    ["Human toxicity, 1,4-DCB equivalent, millions of tons",37000, 286],
    ["SO<sub>2</sub> and NO<sub>x</sub> emissions, millions of tons",180, 18],
    ["Human lives at risk",1800, 47],
    ["Megafauna wildlife at risk, trillions of organisms",47,3],
    ["Biomass at risk, millions of tons",568, 42]
]

helper.save_image({
    "filename":"dsm_impacts.jpg",
    "status":"Done",
    "table":dsm_table,
    "details":"Selected impacts of terrestrial mining (represented by a nickel laterite mine in Indonesia) and a deep sea nodule collector. You can see this summary chart on page 7 of the report. I didn't include every imapct considered. Both scenarios are assessed at the nickel sulfate, manganese sulfate, colbalt sulfate, and copper cathode required for one billion electric vehicles.",
    "references":["dsm_comparison"],
    "source_file":"mining.py"
})

########################################

# Impacts. Results from a few studies on asteroid mining

asteroid_mining_table = [
    ["<b>Mineral</b>","<b>Economic Viability</b>","<b>Source</b>"],
    ["Platinum","Yes","Hein et al."],
    ["Platinum-group","Yes","Busch"],
    ["Nickel","No","Lu"],
    ["Helium-3","No","Kleinschneider et al."]
]

helper.save_image({
    "filename":"asteroid_mining.jpg",
    "status":"Done",
    "details":"Although it gets a lot of attention in the press, there are few rigorous studies on the economic viability of asteroid mining. I've cited a few of them here, though some of them aren't really studies even. This is all I have so far.",
    "table":asteroid_mining_table,
    "references":["as_plat","as_nickel","as_pgroup","as_he3"],
    "source_file":"mining.py"
})

########################################

# Figures on the growth of minerals necessary for clean energy transition.

growth_table = [
    ["<b>Mineral</b>","<b>Demand in 2040 relative to 2020</b>"],
    ["Lithium",42],
    ["Graphite",25],
    ["Cobalt",21],
    ["Nickel",19],
    ["Rare Earths",7]
]

helper.save_image({
    "filename":"mineral_growth.jpg",
    "status":"Done",
    "table":growth_table,
    "details":"Anticipated growth in demand for several minerals under the IEA's sustainable development scenario, which envisions a high deployent of clean energy. Demand in 2040 is expressed relative to the 2020 demand for each mineral.",
    "references":["iea_mining"],
    "source_file":"mining.py"
})

############################################# More metals recycling

# There is a recycling plot above, but this is different data that can't easily be harmonized with the above source

recycling_table2 = [
    ["<b>Metal</b>","<b>Recycling Rate</b>"],
    ["Gold","85%"],
    ["Platinum and Palladium","60%"],
    ["Nickel","60%"],
    ["Silver","50%"],
    ["Copper","45%"],
    ["Aluminum","41%"],
    ["Chromium","34%"],
    ["Zinc","33%"], # Come back zinc!
    ["Cobalt","32%"]
]

helper.save_image({
    "filename":"metals_recycling2.jpg",
    "status":"Done",
    "details":"There are a few more recycling rate figures here. It's from a different source, and these figures are lower than those in the UNEP report when they disagree. There are any number of possible reasons for this: different methodology, different data sources, the fact that this report is more recent, etc. But I think it's good to have a second plot, both to clarify differing values in the literature and because these are more precise.",
    "table":recycling_table2,
    "references":["iea_mining"],
    "source_file":"mining.py"
})

secondary_table = [
    ["<b>Metal</b>","<b>Share of secondary supply</b>"],
    ["Lead","60%"],
    ["Aluminum","26%"],
    ["Copper","18%"],
    ["Cobalt","8%"]
]

helper.save_image({
    "filename":"secondary_metal.jpg",
    "status":"Done",
    "table":secondary_table,
    "details":"These are the share of metal production that is secondary, which means from recycling metals. Because of overall demand growth, these figures are less than the recycling rates.",
    "references":["iea_mining"],
    "source_file":"mining.py"
})

time_to_market_table = [
    ["<b>Metal</b>","<b>Years from discovery to production</b>"],
    ["Lithium in Australia",4],
    ["Lithium in South America",7],
    ["Nickel Sulfide",13],
    ["Lateritic Nickel",19],
    ["Average, 2010-2019",16.9]
]

helper.save_image({
    "filename":"lead_time.jpg",
    "status":"Done",
    "table":time_to_market_table,
    "details":"Average time from discovery to production of a few minerals. The point here is to illustrate the kind of lead times that may cramp the development of clean energy technology and other things.",
    "references":["iea_mining"],
    "source_file":"mining.py"
})

########################################### Energy use

energy_use_table = [
    ["<b>Metal (in mining)</b>","<b>Share of cost that is energy</b>"],
    ["Copper","19%"],
    ["Nickel","14%"],
    ["Lithium","8.5%"],
    ["Zinc","7.5%"],
    ["Iron Ore","7.5%"],
    ["<b>Metal (in smelting and refining)</b>","<b>Share of cost that is energy</b>"],
    ["Zinc","39%"],
    ["Aluminum","39%"],
    ["Copper","27%"],
    ["Nickel","19%"],
    ["Steel, electric arc furnace","9.5%"],
    ["Steel, blast furance","3%"]
]

helper.save_image({
    "filename":"metals_energy.jpg",
    "status":"Done",
    "details":"The share of total costs for metals (the mining stage and the refining/smelting stage) that is energy. Graphically, keep the two phases separate.",
    "table":energy_use_table,
    "references":["iea_mining"],
    "source_file":"mining.py"
})

############################################ Copper grades

helper.save_image({
    "filename":"copper_grade.jpg",
    "status":"Done",
    "details":"Replicate the red plot on the left hand plot on p. 124 of <a href=\"https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions\">this report</a>. Only do the one plot, average grade of copper ores in Chile from 2005-2019."
})

############################################ Biodiversity impacts

mining_bio_table = [
    ["<b>Mineral</b>","<b>Biodiversity impact (MiBiD)</b>"],
    ["Iron","1.2"],
    ["Bauxite","2"],
    ["Zinc","2.5"],
    ["Lead","5.2"],
    ["Copper","65"]
]

helper.save_image({
    "filename":"mining_bio.jpg",
    "status":"Done",
    "table":mining_bio_table,
    "details":"A measure of the impact of mining various minerals on biodiversity. MiBiD is, as the report describes, ' a non-dimensional index based on data regarding land cover, protected areas and mining operations'",
    "references":["iea_mining"],
    "source_file":"mining.py"
})

########################################## Water impacts

mining_water_table = [
    ["<b>Mineral</b>","<b>Water Use (m<sup>3</sub> per kg ore)</b>","<b>Eutrophication Potential (kgP-eq per kg ore)</b>","<b>Exotoxicity (CTUeco/kg)</b>"],
    ["Bauxite","0.0005","",""],
    ["Iron","0.0007","",""],
    ["Cobalt","0.06","0.00003","0.5"],
    ["Copper","0.03","0.01","10"],
    ["Nickel","0.05","0.015","15"],
    ["Rare Earth Elements","0.8","0.03","700"],
    ["Lithium","0.9","0.0015","4000"]
]

helper.save_image({
    "filename":"mining_water.jpg",
    "status":"Not Done",
    "table":mining_water_table,
    "details":"CTUeco = comparative toxic unit for ecosystems. Display this one with logarithmic scales, as I don't think this will look decent otherwise. It's hard to read the graph, so these figures are pretty rough.",
    "references":["iea_mining"],
    "source_file":"mining.py"
})

########################################### More figures on deep sea mining

dsm_ghg_table = [
    ["<b>Mineral</b>","<b>Terresterial GHG impact, kg CO<sub>2</sub>e for the metal needed for 1 EV battery","<b>Nodule Impact</b>"],
    ["Nickel Sulfate",1103,221],
    ["Cobalt Sulfate",100,71],
    ["Manganese Sulfate",42,33],
    ["Copper Cathode",503,119],
    ["Total",1749,445]
]

helper.save_image({
    "filename":"dsm_ghg_comp.jpg",
    "status":"Done",
    "details":"A lifecycle comparison of greenhouse gas emissions between terrestrial mining and nodules from deep sea mining. Many of the same authors as the source in the other graphic and the results are similar, but this paper may be better because it is is in a peer-reviewed journal.",
    "table":dsm_ghg_table,
    "references":["dsm_paulikas"],
    "source_file":"mining.py"
})