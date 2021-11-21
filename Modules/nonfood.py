# Nonfood calculations

area_dict = {}
with open('Modules/FAO/area_harvested_2020_02_22.csv') as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        blocks = line.split('"')
        if (len(blocks)> 23) and (len(blocks[23])>0):
            area_dict[blocks[15]] = {"Area": float(blocks[23])}
            
fb_to_area = {"Maize and products":"Maize", "Wheat and products":"Wheat", "Soyabeans":"Soybeans", "Rape and Mustard Oil":"Rapeseed",
    "Sorghum and products":"Sorghum", "Palm Oil":"Oil palm fruit"}
        
balance_dict = {}
with open('Modules/FAO/food_balance_2020_02_22.csv') as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        blocks = line.split('"')
        if len(blocks) > 23:
            key = blocks[15]
            if key in fb_to_area:
                key = fb_to_area[key]
            if key not in balance_dict:
                balance_dict[key] = {}
            balance_dict[key][blocks[11]] = blocks[23]

nonfood_sum=0
uncounted_keys = []
nonfood_dict = {}
for key in balance_dict:
    if "Production" in balance_dict[key] and float(balance_dict[key]["Production"])>0:
        if "Losses" not in balance_dict[key]:
            balance_dict[key]["Losses"] = 0
        if "Other uses (non-food)" in balance_dict[key] and balance_dict[key]["Other uses (non-food)"] > 0:
            nonfood_dict[key] = float(balance_dict[key]["Other uses (non-food)"])/(float(balance_dict[key]["Production"])-float(balance_dict[key]["Losses"]))
            if key in area_dict:
                nonfood_sum += nonfood_dict[key] * area_dict[key]["Area"]
                print(key+" "+str( nonfood_dict[key] * area_dict[key]["Area"]))
            else:
                uncounted_keys.append(key)
                pass

# Don't have to run it again if the data files go away
result = {
    "Cloves": 500056.769231
    "Sesame seed"; 226697.098733
    "Rapeseed"; 18456276.6946
    "Sorghum": 1936376.40296
    "Soybeans": 1421472.16541
    "Wheat": 7637799.69269
    "Dates": 8901.19094437
    "Oats": 62600.1875546
    "Sugar beet": 85270.6048899
    "Oil palm fruit": 9417852.22338
    "Maize": 40915538.2238
    "Sunflower seed": 586304.019633
    "Sugar cane": 5093211.4664
    "Yams": 2287597.34159
    "Bananas": 6184.51514574
    "Sweet potatoes": 24646.333584
}
# Total is 88666784.9306
