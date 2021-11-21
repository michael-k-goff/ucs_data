# Note: there is another industrial_heat.py in the parent folder. This one actually generates image data.

import helper

# Industrial heat savings potential from electricity over the leading fossil alternative. From bze, Table C-1, p. 82.
electric_heat_savings = [
    ["<b>Industrial Product</b>","<b>Energy Savings Potential</b>"],
    ["Prepared Food","49%"],
    ["Beer","69%"],
    ["Milk Powder","66%"],
    ["Paper","24%"],
    ["Aluminum Casting","50%"],
    ["Brick","50%"],
    ["Glass","30%"],
#    ["Plastic","95%"], # This is based on recycling, which I think is cheating for the purposes of this plot.
    ["Steel","18%"],
    ["Ammonia","4%"]
]

helper.save_image({
    "filename":"electric_heat.jpg",
    "status":"Done",
    "details":"Show on-site energy savings from electric heat in select industries. Values are reported as percentage savings relative to the leading fossil fuel-based option. This report also reports a 95% savings in plastics based on recycling, but that's an entirely different methodology than just replacing the heat source and thus I think it would be inappropriate to include that figure.",
    "table":electric_heat_savings,
    "references":["bze"],
    "source_file":"industrial_heat.py"
})