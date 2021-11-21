# Rebound, induced demand, complementarity in transportation

import helper

vmt_lane_rebound = [
    ["<b>Study</b>","<b>Induced Demand from Lane Addition, Low Estimate</b>","<b>High Estimate</b>"],
    ["Hymel, Small, Van Dender",0.186,0.186],
    ["Hanson and Huang",0.6, 0.9],
    ["Noland",0.2, 0.6],
    ["Cervero",0.39, 0.39],
    ["Graham, McCoy, Stephens",0.9, 0.9],
    ["Handy and Boarnet",0.6,1.0],
    ["Kockelman",0.5,1.0],
    ["Schiffer, Steinvorth, Milam",0.5, 1.0]
]

vmt_lane_im = {
    "filename":"vmt_lane.jpg",
    "status":"Done",
    "details":"Show elasticities (e.g. induced demand) of VMT by adding lane-miles, as estimated from several studies. What these numbers mean is that an addition of 1% lane miles should be expected to increase VMT by x%, where x is the elasticity. Studies report either ranges or single values. Whenever a study reports short run and long run values, I include the long run value only.",
    "table":vmt_lane_rebound,
    "references":["vmt_lanes1","vmt_lanes2","vmt_lanes3","vmt_lanes4","vmt_lanes5","vmt_lanes6","vmt_lanes7","vmt_lanes8","vtpi_induced_demand"],
    "source_file":"transportation_demand.py"
}

helper.save_image(vmt_lane_im)

vmt_speed = [
    ["<b>Study</b>","<b>Cost Metric</b>","<b>Induced Demand Estimate</b>"],
    ["SACTRA","Speed",1],
    ["Goodwin","Speed",0.57],
    ["NHI","Generalized Cost",0.5],
    ["Lee, Klein, Camus","Generalized Cost",1]
]
vmt_speed_im = {
    "filename":"vmt_speed.jpg",
    "status":"Done",
    "details":"Another VMT induced demand plot, but this time it is in terms of other parameters. 'Speed' refers to vehicle speed, while 'Generalized Cost' is a composite measure that includes time and financial cost to the driver. As driving gets cheaper in terms of time and money, people do more of it. There are no ranges here because all four studies report only single values.",
    "table":vmt_speed,
    "references":["vmt_speed1","vmt_speed2","vmt_speed3","vmt_speed4","vtpi_induced_demand"],
    "source_file":"transportation_demand.py"
}
helper.save_image(vmt_speed_im)

vmt_av = [
    ["<b>Study</b>","<b>Vehicle Feature</b>","<b>Induced Demand Estimate</b>"],
    ["Wadud, McKenzie, Leiby","Driver Assist","4-13%"],
    ["Wadud, McKenzie, Leiby","Full Autonomy","30-60%"],
    ["Childress et al.","Full Autonomy","19.6%"],
    ["Gucwa","Full Autonomy","4-8%"]
]
vmt_av_im = {
    "filename":"vmt_av.jpg",
    "status":"Done",
    "details":"Induced demand estimated from autonomous vehicles, and in one case from contemporary driver assist technology. Obviously speculative.",
    "table":vmt_av,
    "references":["vmt_av1","vmt_av2","vmt_av3","vmt_av"],
    "source_file":"transportation_demand.py"
}
helper.save_image(vmt_av_im)