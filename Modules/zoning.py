# Zoning

import helper

zoning_tax_table = [
    ["<b>City</b>","<b>Zoning tax for a 1/4 acre lot</b>"],
    ["Atlanta",15111],
    ["Boston",46358],
    ["Charlotte",7529],
    ["Chicago",63345],
    ["Cincinnati","---"],
    ["Columbus",2326],
    ["Dallas",2217],
    ["Deltona, FL",3911],
    ["Denver",13059],
    ["Detroit",10089],
    ["Los Angeles",198769],
    ["Miami",37799],
    ["Minneapolis",4379],
    ["Nashville",10325],
    ["New York",152417],
    ["Orlando",11126],
    ["Philadelphia",76672],
    ["Phoenix",21872],
    ["Portland",54781],
    ["Riverside, CA",32771],
    ["San Francisco",409706],
    ["San Jose",111793],
    ["Seattle",174850],
    ["Washington DC",59689]
]

helper.save_image({
    "filename":"zoning_tax.jpg",
    "status":"Done",
    "details":"This paper assesses the zoning tax, or the economic cost on a 1/4 acre lot (typical size for a detached single family home) of zoning regulations. They do it by subtracted the market rate for property and construction costs. In an unregulated market, these two values should be equal by principles of supply and demand, so a difference indicates that the market rate is artificially inflated by regulation. The method is crude but sound. A negative value for Cincinnati is reported, meaning that houses sell for less than construction costs, so I am leaving that city blank. Values are in dollars",
    "table":zoning_tax_table,
    "references":["zoning_tax"],
    "source_file":"zoning.py"
})



























