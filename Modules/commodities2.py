# More plots related to commodities

import helper

green_steel_chart = [
    ["<b>Production method</b>","<b>Variable cost: oil</b>","<b>Variable cost: coal</b>","<b>Variable cost: graphite</b>","<b>Variable cost: biomass fuel</b>","<b>Variable cost: electricity</b>","<b>Capital investment</b>","<b>Total</b>","<b>Emissions</b>"],
    ["Blast Furnace, Sweden",4,96,0,0,11,0,"","1.5-2.8"],
    ["Green Steel, Sweden",0,0,6,5,157,770/(1/0.07),"","0.2"], # Assuming a 7% discount rate
    ["Blast Furnace, Europe",4,96,0,0,11*65./45.,0,"","1.5-2.8"],
    ["Green Steel, Europe",0,0,6,5,157*65./45.,770/(1/0.07),"","0.2"]
]

for i in range(1,len(green_steel_chart)):
    for j in range(1,6):
        green_steel_chart[i][j] *= 1.27 # This is about the exchange rate used in the source
    green_steel_chart[i][7] = sum( [green_steel_chart[i][j] for j in range(1,6)] )

helper.save_image({
    "filename":"green_steel.jpg",
    "status":"Solution",
    "details":"This is a Solution plot, showing the economics of producing steel from hydrogen that is produced from low-carbon electricity (green steel). A 7% discount rate is used when assessing the capital investment of the green steel. There are not separate capital investment figures for blast furnace steel, so really this assesses the economics of retrofitting a blast furnace facility, rather than building something fresh.<br></br>I am using an exchange rate of 1 Euro = 1.27 USD, which seems a bit high, but that's the rate used in the source. See the commodities text for emissions data.<br><br>Also include the carbon abatement costs. They are $29-56/ton CO<sub>2</sub>e for Sweden's grid and $62-119 for the European grid. All monetary figures are in millions of dollars and greenhouse gas reduction figures in millions of tons CO<sub>2</sub>e.",
    "references":["whalen"],
    "table":green_steel_chart,
    "source_file":"commodities2.py"
})