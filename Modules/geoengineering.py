# Geoengineering-related plots and calculations

import helper

# See environment - geoengineering.txt.

geo_table = [
    ["<b>Method</b>","<b>Description</b>","<b>Effective emissions reduction potential</b>","<b>Cost per ton CO<sub>2</sub> mitigated</b>","<b>Limitations</b>","<b>Risks and drawbacks</b>"],
    ["Stratospheric Aerosol Injection","Release aerosols in the stratosphere to reflect sunlight and induce cooling.","Unlimited","$0.10 to $0.25 (Smith and Wagner)","Does not address ocean acidification.","Termination could lead to abrupt temperature rise (Parker and Irvine), interstate conflict (Halstead), drought, ozone depletion, loss of sunlight (Robock et al.)."],
    # Table 3.2 of the srm source for temperature reduction from clouds brightening.
    # For cost, I am making the crude assumption that the 5 W/m^2 effectively mitigates all warming, the equivalent of 40B/year tons emissions, and it costs $5B/year.
    ["Marine Cloud Brightening","Add aerosols to clouds to increase their reflectivity (NRC)","Reduce temperatures 0.6-1.1 &#8451;","$0.13 (NRC)","Does not address ocean acidification.","Unknown effects on weather patterns."],
    ["Afforestation","Plant trees, which absorb CO<sub>2</sub>.","116 (Veldman et al.) to 564 (Bastin et al.) tons CO<sub>2</sub>e (3-14 years of emissions at 2020 levels)","$20-50/ton, depending on amount of afforestation (Busch et al.)","Limited land available for forestation, potential land use conflict","Carbon sequestration potential of forests is highly debated (Lewis et al.)."],
    ["Ocean Iron Fertilization","Seed oceans with iron particles, which induce algae growth, absorb CO<sub>2</sub>, and sequester it in the deep ocean","196-790 billion tons CO<sub>2</sub> over 100 years (NOAA), the equivalent of about 5-20 years of world emissions at 2020 rates","$13-133 (Boyd)","---","Efficiency of iron in absorbing carbon is disputed, negative feedbacks are uncertain (NOAA). Ocean acidification would be exacerbated (NOAA). Unknown risk to ecosystems (Strong et al.)"],
    ["Ocean Afforestation","Farm ocean algae, harvest for biomethane, and sequester carbon from combustion.","36 billion tons CO<sub>2</sub> sequestered per year, almost to current emissions (N'Yeurt et al.).","$18 (N'Yeurt et al.)","---","May stress coastal ecosystems (Royal Society)"],
    ["Wetland, peatland and coastal habitat restoration","Active restoration.","0.4-20 billion tons CO<sub>2</sub>/year","$10-100","---","Short term release of methane and N<sub>2</sub>O."],
    ["Soil carbon sequestration","Modify farming practices so as to increase soil carbon content.","1-10 billion tons CO<sub>2</sub>/year","-$10 to +$3","Saturation of soil carbon in 10-20 years.","Carbon storage can be reversed."],
    ["Biochar","Pyrolysis of biomass into charcoal, which as a soil amendment enhances carbon storage and improves soil fertility.","3-5 billion tons CO<sub>2</sub>/year","$0-200","---","Reduced soil albedo may cause warming."],
    ["Biomass building materials","Increase used of plant-based building materials, such as wood--including cross-laminated timber--bamboo, straw, or hemp.","0.5-1 billion tons CO<sub>2</sub>/year","$0","Market size for new buildings.","Fire risk."],
    ["Enhanced terrestrial weathering","Mill silicate rocks to increase the rate of weathering, which sequesters CO<sub>2</sub>.","0.5-4 billion tons CO<sub>2</sub>/year","$50-500","---","Energy intensive."],
    ["Mineral carbonation","Grind and treat minerals and react with CO<sub>2</sub> for stable sequestration. Resulting products may be commercially valuable.","Effectively unlimited","$50-300 (above ground), $20 (below ground)","Below ground sequestration depends on geological availability","Mining for minerals, high energy consumption."],
    ["Ocean alkalinity","Add positive charged calcium or magnesium to the ocean to increase alkalinity and accelerate CO<sub>2</sub> uptake.","40 billion tons CO<sub>2</sub>/year","$70-200","---","Loss of alkalinity could reverse CO<sub>2</sub> uptake. Unknown risk to ecosystems."],
    ["Low carbon concrete","Methods of concrete production that incorporate atmospheric CO<sub>2</sub>","100 million tons CO<sub>2</sub>/year","$50-300","Based on market size for concrete.","Market acceptance of alternatives to Portland cement."]
]

helper.save_image({
    "filename":"geoengineering.jpg",
    "status":"Done",
    "table":geo_table,
    "details":"Summary of major geoengineering approaches. There is overlap with carbon removal, which in turn has overlap with CCS. I am including carbon removal methods that are not addressed on the CCS page. Everything at 'Wetland, peatland and coastal habitat restoration' and below comes from the Royal Society reference.",
    "references":["sai","sai2","halstead","sai_risk","veldman","bastin","busch","lewis","boyd","congress_oif","oif","ocean_afforestation","ras_ghg_removal","srm"],
    "source_file":"geoengineering.py"
})