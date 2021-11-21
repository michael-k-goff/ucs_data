# Various economic plots. Designed mainly for the Macroeconomics section of the site.

import helper

elasticity_table = [
    ["<b>Energy Product</b>","<b>Consumption Reduction from 10% Price Increase</b>"],
    ["Oil, short term","0.2-0.7%"], # imf2011 for smaller number, hamilton_elasticity for larger number
    ["Oil, long term","0.7-3.0%"], # imf2011 for smaller number, hamilton_elasticity for larger number
    # Remaining values from rand_elasticity
    ["Residential Electricity","2.4%"],
    ["Commercial Electricity","2.1%"],
    ["Residential Natural Gas","1.3%"]
]

helper.save_image({
    "filename":"elasticity.jpg",
    "status":"Done",
    "table":elasticity_table,
    "details":"Show the impact of an increase in energy prices on consumption. The technical term is price elasticity of demand. I would sneak in that phrase because it is a bit of jargon that is important to people who know economics, but most of the public won't know what it means. Anyway, for both oil values, the smaller numbers are from the IMF and the larger numbers from Hamilton. The rest come from Bernstein and Griffin.<br><br>One broader issue to consider is that this material needs to be well motivated. The way I plan to frame it on the site for now is that energy prices have a modest effect on consumption, so you would really have to jack up prices high if you wanted to cut demand. Probably so high that it would cause serious damage to the economy. And really the broader message in the Economics section is the centrality of energy in the world economy. It's a tough section, but I think it is important.",
    "references":["imf2011","hamilton_elasticity","rand_elasticity"],
    "source_file":"economics.py"
})

helper.save_image({
    "filename":"income_elasticity.jpg",
    "status":"Done",
    "details":"This one is income elasticity of demand. Price elasticity of demand (see elasticity.jpg) is how demand for a product responds to the price of that product. Income elasticity of demand is how demand for a product response to income. Again, put in that bit of jargon somewhere, but don't assume that people know what it means. The key point is that, if incomes increase by 10%, we should expect short term oil usage to go up 6.9% and long-term usage to go up 2.9%. This fact is in the site now, and maybe it's too basic to present as a graphic, but I think we should do that. Later on we might include more estimates of income elasticity of demand from other sources.",
    "references":["imf2011"],
    "source_file":"economics.py"
})