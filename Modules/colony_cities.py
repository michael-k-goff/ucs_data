# Colony cities calculations

import helper

helper.save_image({
    "filename":"sea_cost.jpg",
    "status":"Done",
    "details":"Compare the cost of building floating cities, as envisioned by the Seasteading Institute, and real estate in some expensive markets around the world.<br><br>Costs are $978 per square foot for the floating city, $1773 in Manhattan, $902 in San Francisco, $2091 in Hong Kong, $1063 in Singapore, $714 in Shanghai, $776 in London, $985 in Paris.",
    "references":["hencken","neighborhoodx","cbre"],
    "source_file":"colony_cities.py"
})

cost_table = [
    ["<b>Settlement</b>","<b>Cost per person, millions of USD</b>","<b>Explanation</b>","<b>Status</b>","<b>Source</b>"],
    ["Manhattan",0.408,"One Bedroom in Manhattan, assumes 2 people.","Observed market conditions in 2018","Frank"],
    ["Songdo",0.153,"A $40 billion dollar development (2010) planned for 300,000 people","Partially constructed","Poon"],
    ["Land Reclamation",0.1,"East Lantau Metropolis land reclamation project, based on 2016 estimate. Only includes the land itself","Proposed","Zhao"],
    ["City at Sea",0.674,"Seasteading Institute: estimated cost of $255 million (2014) for a project to hold 360 people","Concept","Hencken et al."],
    ["Underwater City",1.467,"The Hydropolis project promised (2008) a 220 room facility for $550 million. We assume two people per room.","Cancelled","Ros"],
    ["Antarctica",0.25,"McMurdo Station upgrade has an estimated cost of $300 million and hosts up to 1200 people.","Planned","Gramling"],
    ["Space Station",25000,"The International Space Station has cost $150 billion and has a crew of 6.","Cumulative and planned costs as of 2010","Lafleur"],
    ["Lunar Base",1000,"Proposal for a $10 billion base that would host 10 people.","Proposal","Hall and Miller"],
    ["Mars Colony",50,"Proposal for a 1000 person Mars colony for $50 billion.","Concept","Heidmann and Brisson"]
]

helper.save_image({
    "filename":"city_cost.jpg",
    "status":"Done",
    "table":cost_table,
    "details":"Estimates of cost per person for living in various types of settlements. Figures are CPI-adjusted to 2018 USD. Because the space settlements are so much more expensive than the land settlements, I think it will be best to show those separately and then do a blow-out to show the costs for Earth-based settlements. Be aware that there is a lot of non-comparability here. They compare different things (market conditions for Manhattan, land only for the East Lantau project, upgrades instead of fresh construction for McMurdo), and one cannot place too much stock in cost estimates for concept projects.",
    "references":["cnbc_manhattan","songdo","land_reclamation","hencken","underwater_hotel","mcmurdo","iss_cost","lunar_base","mars_colony"],
    "source_file":"colony_cities.py"
})