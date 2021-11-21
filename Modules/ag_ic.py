# Industrial crops

import helper

rubber_lca_table = [
    ["<b>Source of rubber</b>","<b>Ozone Depletion, kg CJF-11 * 10<sup>-9</sup>/kg rubber</b>","<b>Global Warming, kg CO<sub>2</sub>e/kg rubber</b>","<b>Acidification, kg SO<sub>2</sub>e/kg rubber</b>","<b>Land Use (kg rubber/hectare)</b>","<b>Water (m<sup>3</sup> per kg rubber)</b>"],
#    ["Hevea","8%","100%","100%"],
#    ["Guayule","80%","38%","97%"], # About 6.9 * 10^-7 kg-CFC-11 ozone depletion
#    ["Synthetic Rubber","100%","8%","12%"], # 2.7 kg CO2e/kg rubber impact. 0.01 kg SO2/kg rubber (acidification).
    ["Hevea","69","33.8","0.08","850","12.1"],
    ["Guayule","685","12.8","0.08","",""],
    ["Synthetic Rubber","856","2.7","0.01","",""]
]

helper.save_image({
    "filename":"rubber_lca.jpg",
    "status":"Done",
    "table":rubber_lca_table,
    "details":"Some LCA results for types of rubber. I'm assuming that the natural rubber, as reported by the Chiarelli et al. source, is Hevea. It would be good to have land use and water figures for other forms of rubber but I don't yet.",
    "references":["rubber_lca","rubber_lca2"],
    "source_file":"ag_ic.py"
})

helper.save_image({
    "filename":"horseshoe_crab.jpg",
    "status":"Done",
    "details":"Simple image: bled horseshoe crabs have a 8% chance of dying at the shore, while unbled crabs have a 0.5% chance of dying. OK, I'll admit that this graphic exists mainly so the pharmaceutical section won't be too devoid of graphics.",
    "references":["horseshoe_crab"],
    "source_file":"ag_ic.py"
})

# Note: terrestrial and aquatic acidification are combined
fiber_lca_table = [
    ["<b>Fiber</b>","<b>Acidification, kg SO<sub>4</sub>/kg textile</b>","<b>Land, m<sup>2</sup>/kg textile</b>","<b>Eutrophication, kg PO4/kg textile</b>","<b>Global warming, kg CO<sub>2</sub>e/kg textile</b>","<b>Energy (non-renewable), MJ/kg textile</b>","<b>Mineral extraction, MJ energy expended</b>"],
    ["Cotton",562+163,8290,6.8,20.338,279.777,1116],
    ["Jute",162+41,1603,3.5,5.032,60.935,69],
    ["Kenaf",158+41,1403,3.4,5.11,62.223,80]
]

helper.save_image({
    "filename":"fiber.jpg",
    "status":"Done",
    "details":"Some LCA figures for different kinds of fibers",
    "references":["fiber_lca"],
    "table":fiber_lca_table,
    "source_file":"ag_ic.py"
})

helper.save_image({
    "filename":"natural_synthetic_fiber",
    "status":"Done",
    "details":"According to the reference, Flax has an eco-indicator of 0.34 millipoints/kg and glass is 2.31 mPt/kg. What is a millipoint, you ask? That's how the authors aggregated several life cycle impacts into a single metric.",
    "references":["flax_glass"],
    "source_file":"ag_ic.py"
})

organic_cotton_table = [
    ["<b>Metric</b>","<b>Organic Cotton</b>","<b>Conventional Cotton</b>","<b>Metric</b>"],
    ["Global Warming","978","1808","kg CO<sub>2</sub>e per 1000 kg lint cotton."],
    ["Acidification","5.7","18.7","kg SO<sub>2</sub>e per 1000 kg lint cotton."],
    ["Eutrophication","2.8","3.8","kg PO<sub>4</sub>e per 1000 kg lint cotton."],
    ["Water withdrawals (blue water)","182","2120","m<sup>3</sup> per 1000 kg lint cotton."],
    ["Energy consumption","5800","15000","MJ per 1000 kg lint cotton."]
]

helper.save_image({
    "filename":"organic_cotton.jpg",
    "status":"Done",
    "details":"Review of life cycle impacts of organic and conventional cotton. I'm not sure how much I trust this source, so I would keep on the lookout for another one.",
    "table":organic_cotton_table,
    "references":["textile_exchange"],
    "source_file":"ag_ic.py"
})