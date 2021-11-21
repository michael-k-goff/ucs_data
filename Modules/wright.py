# Wright's Law calculations

import helper

wright_table = [
    ["<b>Product</b>","<b>Learning Rate</b>","<b>Reference</b>"],
    ["Airplanes","20%","Wright"],
    ["Shipbuilding","15-20%","Chen et al."],
    ["Semiconductors","20%","Chen et al."],
    ["Solar PV","17-47%","Chen et al."],
    ["Wind Turbine Generators","4-10%","Chen et al."],
    ["Wind Turbine Generators (citing a different analysis)","12%","Chen et al."],
    ["Food Service Industry","2-15%","Chen et al."],
    ["Several Industries","10-25%","Hax and Majluf"],
    ["Hard Disk Drives (per gigabyte), 1980-2002","50%","Reeves et al."],
    ["Laser Diodes","40-45%","Reeves et al."],
    ["Solar Thermal Plants","10-16%","Samadi"],
    ["Biomass Power Plants","2-15%","Samadi"],
    ["Biomass Feedstock","10-45%","Samadi"],
    ["Nuclear Power Plants","-49 to 22%","Samadi"],
    ["Coal Power Plants","6-12%","Samadi"],
    ["Natural Gas Power Plants","-13 to 25%","Samadi"],
    ["Lithium-Ion Batteries","18%","Goldie-Scot"]
]

helper.save_image({
    "filename":"wrights_law.jpg",
    "status":"Done",
    "table":wright_table,
    "details":"Learning rate observed for various technologies. The goal here is to establish Wright's Law as a principle, which is important, and have some decent figures that can be applied to other technologies we might be interested in. The Chen et al. study itself cites several other studies. I got lazy and decided to just use the Chen et al. source for them.",
    "references":["wright1936","wright_smr","experience_curve","reeves","elec_learning","liion_learning"],
    "source_file":"wright.py"
})