# Metals

import helper

# A few guesses made on production numbers

metals_table = [
    ["<b>Metal/Mineral</b>","<b>Energy, MJ per kg material</b>","<b>Greenhouse gas emissions, kg CO<sub>2</sub>e/kg material</b>","<b>Production, of tons in 2015</b>"],
    ["Helium",67.5,0.9,""],
    ["Lithium",125,7.1,77000],
    ["Beryllium",1720,122,205/88.9], # Based on the fact that the US produces 88.9% of the world's beryllium
    ["Boron",27.3,1.5,9380000],
    ["Magnesium",18.8,5.4,27700000*(24.305)/(24.305+12.011+3*15.996)],
    ["Aluminum",131,8.2,57500000],
    ["Calcium",5.8,1.0,""],
    ["Scandium",97200,5710,""],
    ["Titanium",115,8.1,7270000*(47.867)/(47.867+3*15.999+55.845)], # Assuming Ilmenite. There are several ores listed
    ["Vanadium",516,33.1,77800],
    ["Chromium",40.2, 2.4,28000000*(2*51.996)/(2*51.996+55.845+4*15.996)], # Converting mass of chromite ore
    ["Manganese",23.7,1.0,51800000],
    ["Iron",23.1, 1.5,2290000000], # Iron ore
    ["Cobalt",128,8.3,126000], # Mine content
    ["Nickel",111, 6.5,2280000], # Mine content
    ["Copper",53.7,2.8,19100000],
    ["Zinc",52.9,3.1,12800000],
    ["Gallium",8030,205,320000], # https://pubs.usgs.gov/periodicals/mcs2020/mcs2020-gallium.pdf
    ["Germanium",2890,170,130000], # https://pubs.usgs.gov/periodicals/mcs2020/mcs2020-germanium.pdf
    ["Arsenic",5,0.3,36500*(74.922)/(74.922+2*15.999)], # Converting mass of asenic-trioxide to pure arsenic
    ["Selenium",65.5,3.6,2200000],
    ["Strontium",48.8,3.2,220000],
    ["Yttrium",295,15.1,12000],
    ["Zirconium",19.9,1.1,1520000],
    ["Niobium",172,12.5,64300000],
    ["Molybdenum",117,5.7,235000],
    ["Ruthenium",41100,2110,""],
    ["Rhodium",683000,35100,""],
    ["Palladium",72700,3880,215],
    ["Silver",3280,196,27600],
    ["Cadmium",53,3,23200],
    ["Indium",1720,102,759],
    ["Tin",310,17.1,289000],
    ["Antimony",141,12.9,141000],
    ["Tellerium",435,21.9,470], # https://pubs.usgs.gov/periodicals/mcs2020/mcs2020-tellurium.pdf
    ["Barium",4.0,0.2,""],
    ["Lanthanum",215,11,""],
    ["Cerium",252,12.9,""],
    ["Praesodymium",376,19.2,""],
    ["Neodymium",344,17.6,""],
    ["Samarium",1160,59.1,""],
    ["Europium",7750,395,""],
    ["Gadolinium",914,46.6,""],
    ["Terbium",5820,297,""],
    ["Dysprosium",1170,57.6,""],
    ["Holmium",4400,226,""],
    ["Erbium",954,48.7,""],
    ["Thulium",12700,649,""],
    ["Ytterbium",2450,125,""],
    ["Lutetium",17600,896,""],
    ["Hafnium",3510,131,""],
    ["Tantalum",4360,260,1210],
    ["Tungsten",133,12.6,89400],
    ["Rhenium",9040,450,49.4],
    ["Osmium",85500,4560,""],
    ["Iridium",169000,8860,""],
    ["Platinum",243000,12500,189],
    ["Gold",208000,12500,3100],
    ["Mercury",179,12.1,2470],
    ["Thallium",5160,376,8], # https://pubs.usgs.gov/periodicals/mcs2020/mcs2020-thallium.pdf
    ["Lead",18.9,1.3,4950000],
    ["Bismuth",697,58.9,16400],
    ["Thorium",1260,74.9,""],
    ["Uranium",1270,90.7,""]
]

# Many of the production figures from https://prd-wret.s3-us-west-2.amazonaws.com/assets/palladium/production/atoms/files/myb1-2015-stati.pdf
# Cite as https://www.usgs.gov/centers/nmic/statistical-summary

helper.save_image({
    "filename":"metals.jpg",
    "status":"Done",
    "table":metals_table,
    "details":"Lifecycle analysis of metals and other elements of the periodic table. I think I got this right, after looking it over a while. To spot errors, look for any major outliers in the energy/GHG ratio for these elements, since most emissions come from energy. Also, iron and aluminum should be, respectively, in first and second place for the most emissions, so if that's not the case, there's probably an error. Please get total energy and emissions for all elements where we have them, which can be found by multiplying the per-ton energy and emissions by total world tonnage. As you can see, we are missing tonnages for many important elements, including the rare-earths, but at least we have most of the major bulk commodities. This will almost surely require several pages. Sort by highest total emissions, with elements with missing tonnages at the end. All energy and emissions figures per ton come from Nuss and Eckelman, and the tonnages are from Krisanda.",
    "references":["metals","metals2"],
    "source_file":"metals.py",
})