import helper

long_duration_table = [
    ["<b>Option</b>","<b>Levelized Cost of Storage, dollars per kWh</b>","<b>Notes</b>"],
    ["Very large pumped hydro","$20-30","Geographically constrained"],
    ["Most pumped hydro","$100+","Geographically constrained"],
    ["Compressed air","$1+","Geographically constrained"],
    ["Gravity-based","$200-250","e.g. Energy Vault"],
    ["Geomechanical, e.g. pumping water underground","$50+","Can't operate for hundreds of hours"],
    ["Flow batteries","$100","e.g. vanadium redox and zinc bromine"],
    ["Flow batteries with novel chemistry","$10-20"],
    ["Metal air batteries","$20"],
    ["Liquid metal batteries","$50-75","e.g. Ambri"],
    ["Hydrogen, synthetic natural gas, ammonia in naturally porous rock formations","$0.50","Low efficiencies apply to H2, SNG, or NH3."],
    ["H2, SNG, NH3 in salt caverns","$0.80"],
    ["H2, SNG, NH3 in lined hard rock caverns","$1-5"],
    ["Compressed hydrogen in steel tanks","$10-15"],
    ["Molten Salt","$30-80"],
    ["Firebrick resistance-heated energy storage","$5-10"],
    ["Reversible heat pump","$15-25"]
]

helper.save_image({
    "filename":"lcos_seasonal.jpg",
    "status":"Done",
    "details":"Completely redoing this table. There is a new paper out, cited below, that has more up-to-date figures and more through figures on long-duration storage.",
    "table":long_duration_table,
    "references":["long_storage"],
    "source_file":"seasonal2.py"
})
