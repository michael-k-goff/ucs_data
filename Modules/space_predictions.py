# Plots for space predictions

import helper

asteroid_table = [
    ["<b>Type of Event</b>","<b>Diameter of Objects, Meters</b>","<b>Fatalities</b>","<b>Frequency of Impact (years)</b>"],
    ["High altitude breakup","<50","~0","1"],
    ["Tunguska-like event","50+","5000","250-500"],
    ["Regional Event","140+","50,000","5000"],
    ["Large sub-global event","300+","500,000","25,000"],
    ["Low global event","600+","5M","70,000"],
    ["Nominal global event","1000+","1B","1 million"],
    ["High global event","5000+","2B","6 million"],
    ["Extinction-class event","10,000+","~8B","100 million"]
]

helper.save_image({
    "filename":"asteroid_impact.jpg",
    "status":"Not Done",
    "details":"A review of asteroid impacts and their expected frequencies.",
    "table":asteroid_table,
    "references":["asteroid_table"],
    "source_file":"space_predictions.py"
})

helper.save_image({
    "filename":"asteroid_finds.jpg",
    "status":"Done",
    "details":"Some basic statistics on how many large asteroids have been found so far. I would like to have much more here. The April 2018 Mike Wall article reports 8000 of 25000 140m+ asteroids (32%) found. The July 2018 Mike Wall article reports 95% of the 1km+ asteroids found. See e.g. NASA page for a review of the Congressional mandate (which was for 2020 and not even close to being met).",
    "table":[
        ["<b>Size Class</b>","<b>Percentage of near-Earth asteroids founds.</b>"],
        ["1 km+","95% as of 2015"],
        ["140m+","32% as of 2018"],
        ["140m+","Congressionally mandated goal of 90%"]
    ],
    "references":["asteroid_find1","asteroid_find2","asteroid_find3"],
    "source_file":"space_predictions.py"
})

geomagnetic_storm_table = [
    ["<b>Severity (Negative of Dst in nanoteslas)</b>","<b>Expected frequency per century</b>","<b>Notes</b>"],
    ["100+","460"],
    ["200+","94"],
    ["400+","9.73"],
    ["589","","March 1989 that caused a major blackout in Quebec and other problems"],
    ["800+","0.286"],
    ["850","","Carrington Event of 1859"],
    ["1200","","A July 2012 storm that narrowly missed Earth"],
    ["1600+","0.0000741"]
]

helper.save_image({
    "filename":"geomagnetic_storms.jpg",
    "status":"Not Done",
    "details":"Estimated frequencies of geomagnetic storms. This is an active area of research, so the best known values could change. I have also interspersed some historical storms for comparison. Information about storm frequency is from the OECD report, and the three historic storms from the Reuters article.",
    "table":geomagnetic_storm_table,
    "references":["oecd_geostorm","reuters_geostorm"],
    "source_file":"space_predictions.py"
})

satellite_table = [
    ["<b>Purpose</b>","<b>Number of Satellites as of January 1, 2021</b>"],
    ["Defunct",3170],
    ["Communications",1832],
    ["Earth Observation",906],
    ["Technology development and demonstration",350],
    ["Navigation and positioning",150],
    ["Space science and observation",104],
    ["Earth science",20],
    ["Other Purposes",10]
]

helper.save_image({
    "filename":"satellite_count.jpg",
    "status":"Done",
    "details":"Number of satellites by purpose as of January 1, 2021. I am using data from Geospatial World, which in turn was pulled from Union of Concerned Scientists. It would be better if I used the data set from the latter directly, but that's more work and I am just trying to get something up quick and dirty now.",
    "table":satellite_table,
    "references":["geospatial_satellites","ucs_satellites"],
    "source_file":"space_predictions.py"
})