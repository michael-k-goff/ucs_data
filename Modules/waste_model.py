# Updated waste analysis

import helper

# Figures are in millions of tons
# See https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials#NationalPicture
msw_composition = {
    "Paper and Paperboard":292.4 * 0.2305,
    "Glass":292.4 * 0.0419,
    "Metals":292.4 * 0.0876,
    "Plastic":292.4 * 0.122,
    "Yard Trimmings":292.4 * 0.1211,
    "Food":292.4 * 0.2159,
    "Wood":292.4 * 0.0619,
    "Rubber and Leather":292.4 * 0.0313,
    "Textiles":292.4 * 0.0583,
    "Other":292.4 * 0.0156,
    "Miscellaneous Organic Wastes":292.4 * 0.0139
}

# Breakdown for some specific waste items
# https://rc.library.uta.edu/uta-ir/bitstream/handle/10106/29764/AURPA-THESIS-2021.pdf?sequence=1&isAllowed=y, p. 3
# Share of all plastics that are a given type.
msw_plastic = {
    "PETE":0.14, # Same as PET
    "HDPE":0.256,
    "PVC":0.0003,
    "LDPE":0.3,
    "PP":0.123,
    "PS":0.148,
    "Other":0.031
}

# From https://www.oregon.gov/deq/mm/pages/waste-composition-study.aspx
# Share of all metals that are a given type.
msw_metals = {
    "Aluminum":0.39/5.16,
    "Copper":0.12/5.16, # The "Other Nonferrous Metal" category in the spreadsheet, but I am treating it as copper wires.
    "Steel":0.51/5.16,
    "Mixed Metal":(5.16-0.51-0.12-0.39)/5.16 # Different from the "Mixed Metal" category in the spreadsheet.
    # There is some e-waste in this category as well.
}

# From https://www.oregon.gov/deq/mm/pages/waste-composition-study.aspx
# Share of all paper that is a given type.
msw_paper = {
    "Cardboard":3.5/15.3,
    "Magazines":0.52/15.3,
    "Newspaper":0.55/15.3,
    "Office Paper":0.9/15.3,
    "Textbooks":0.06/15.3,
    "Mixed Paper":(15.3-3.5-0.52-0.55-0.9-0.06)/15.3
}

# From WARM (ref. warm15). Figures are metric of tons CO2/ton of material.
msw_ghg = {
    "HDPE":{
        "Recycling":-0.76,
        "Landfilling":0.02,
        "Incineration":1.29
    },
    "PETE":{
        "Recycling":-1.02,
        "Landfilling":0.02,
        "Incineration":1.24
    },
    "Aluminum":{
        "Recycling":-9.13, # Aluminum cans
        "Landfilling":0.02,
        "Incineration":0.03
    },
    "Copper":{
        "Recycling":-4.49,
        "Landfilling":0.02,
        "Incineration":0.03
    },
    "Steel":{
        "Recycling":-1.83,
        "Landfilling":0.02,
        "Incineration":-1.59 # Why is this negative? That's what WARM says.
    },
    "Mixed Metal":{
        "Recycling":-4.39,
        "Landfilling":0.02,
        "Incineration":-1.02
    },
    "Glass":{
        "Recycling":-0.28,
        "Landfilling":0.02,
        "Incineration":0.03
    },
    "Cardboard":{ # Corrugated Containers
        "Recycling":-3.14,
        "Landfilling":0.18,
        "Incineration":-0.49
    },
    "Magazines":{
        "Recycling":-3.07,
        "Landfilling":-0.43,
        "Incineration":-0.35
    },
    "Newspaper":{
        "Recycling":-2.71,
        "Landfilling":-0.85,
        "Incineration":-0.56
    },
    "Office Paper":{
        "Recycling":-2.86,
        "Landfilling":1.13,
        "Incineration":-0.47
    },
    "Textbooks":{
        "Recycling":-3.10,
        "Landfilling":1.13,
        "Incineration":-0.47
    },
    "Mixed Paper":{
        "Recycling":-4,
        "Landfilling":0.07,
        "Incineration":-0.49
    },
    "Yard Trimmings":{
        "Recycling":-0.34, # Dry digestion (anaerobic digestion)
        "Landfilling":-0.2,
        "Incineration":-0.17
    },
    "Food":{
        "Recycling":-0.16, # Wet digestion
        "Landfilling":0.5,
        "Incineration":-0.13
    },
    "Wood":{ # Dimensional lumber
        "Recycling":-2.66,
        "Landfilling":-0.92,
        "Incineration":-0.58
    },
    "Rubber and Leather":{ # Tires
        "Recycling":0,
        "Landfilling":-0.02,
        "Incineration":0.5
    },
    "Textiles":{ # Carpet
        "Recycling":-2.38,
        "Landfilling":0.02,
        "Incineration":1.01
    }
}

################################################################

# A single MSW dictionary

msw = {
    key: {"Million tons in the US": msw_composition[key]} for key in msw_composition
}
for key in msw_plastic:
    msw[key] = {"Million tons in the US": msw_plastic[key]*msw_composition["Plastic"]}
for key in msw_metals:
    msw[key] = {"Million tons in the US": msw_metals[key]*msw_composition["Metals"]}
for key in msw_paper:
    msw[key] = {"Million tons in the US": msw_paper[key]*msw_composition["Paper and Paperboard"]}
for key in msw_ghg:
    msw[key]["Recycling"] = msw_ghg[key]["Recycling"]
    msw[key]["Landfilling"] = msw_ghg[key]["Landfilling"]
    msw[key]["Incineration"] = msw_ghg[key]["Incineration"]

def display():
    for key in msw:
        print(key)
        print(msw[key])
        print("")
#display()

################################################################

# MSW Composition plot
compo_table = [
    ["<b>Material</b>","<b>Tonnage</b>"]
]

for key in msw:
    if key not in ["Plastic","Paper and Paperboard","Metals"]:
        compo_table.append([key,10**6*msw[key]["Million tons in the US"]])
    
def save_waste_compo_image():
    helper.save_image({
        "filename":"waste_composition.jpg",
        "status":"Done",
        "table":compo_table,
        "details":"These are figures on municipal solid waste composition. I haven't tried to break this down in as much detail as possible, only as much as I can for the purposes of calculating landfill taxes. Top level categories are reported by the EPA. I used the Aurpa study to break down 'Plastics' into various types. The Oregon waste composition analysis is used to break down the shares of metals and paper. I made a few assumptions where data is lacking. In the Oregon study, 'other nonferrous metals', which I presume are other than aluminum, are assumed to be copper.",
        "references":["waste_compo1","waste_compo2","waste_compo3"],
        "source_file":"waste_model.py"
})

save_waste_compo_image()
landfill_ghg, incin_ghg = 0,0
for key in msw:
    if key not in ["Plastic","Paper and Paperboard","Metals"]:
        if "Recycling" in msw[key]:
            landfill_ghg += msw[key]["Million tons in the US"] * (msw[key]["Recycling"]-msw[key]["Landfilling"]) / 292.4
        if "Incineration" in msw[key]:
            incin_ghg += msw[key]["Million tons in the US"] * (msw[key]["Recycling"]-msw[key]["Incineration"]) / 292.4
        
print(landfill_ghg)
print(incin_ghg)