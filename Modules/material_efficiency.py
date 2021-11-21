# Material efficiency

import helper

# From mateff, Figure 19. Guesstimating figures by looking at the chart.
efficiency_chart = [
    ["<b>Commodity</b>","<b>2017 Production</b>","<b>2060 Production, business as usual</b>","<b>2060 Production, efficiency scenario</b>"],
    ["Steel",1700, 1700*1.3, 1700*1.3*0.76],
    ["Cement",4100, 4100*1.1, 4100*1.1*0.85],
    ["Aluminum",130, 130*1.75, 130*1.75*0.83]
]
efficiency_chart_im = {
    "filename":"material_efficiency.jpg",
    "status":"Done",
    "table":efficiency_chart,
    "details":"Show current, future under business as usual, and future under a material efficiency scenario for three major commodities. All figures are in millions of tons of the commodity.",
    "references":["mateff"],
    "source_file":"material_efficiency.py"
}
helper.save_image(efficiency_chart_im)

################################### Lightweighting

lightweighting_chart = [
    ["<b>Commodity</b>","<b>Savings Potential (low estimate)</b>","<b>Savings Potential (high estimate)</b>"],
    ["Steel","5%","30%"],
    ["Aluminum","7%","30%"]
]
lightweighting_im = {
    "filename":"lightweighting.jpg",
    "status":"Done",
    "table":lightweighting_chart,
    "details":"Material savings through lightweighting. This is a basic chart that we might try to upgrade with more data from more sources later on. Note that these figures are estimated savings of ALL steel and aluminum produced. Note also that the study does not make any claims that these savings can be achieved economically, and I rather doubt that they can.",
    "references":["lightweight"],
    "source_file":"material_efficiency.py"
}
helper.save_image(lightweighting_im)

#################################### Reuse

reuse_im = {
    "filename":"reuse.jpg",
    "status":"Done",
    "details":"As with the lightweighting chart, it would be good to augment this with more data from more sources, but it's really not that high a priority. Show potential savings of major commodities through component or product reuse. (Reuse is different from recycling in that with reuse, whole products or components are reused as are, whereas with recycling, the material is broken down to the level of the basic commoditiy and made into a different product or component.) Figures are 27% for steel and 33% for aluminum.",
    "references":["reuse"],
    "source_file":"material_efficiency.py"
}
helper.save_image(reuse_im)