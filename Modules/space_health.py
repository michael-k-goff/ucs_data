# Figures related to health in space

import helper

gravity_table = [
    ["<b>Body</b>","<b>Gravity, relative to Earth</b>"],
    ["Earth",1],
    ["Free Space",0],
    ["Moon",0.17],
    ["Mars",0.38],
    ["Venus",0.9],
    ["Ceres",0.03]
]

helper.save_image({
    "filename":"gravity_comp.jpg",
    "status":"Done",
    "details":"Some figures on gravity of various bodies where humans are or might go. No references since this is all fairly standard material.",
    "table":gravity_table,
    "references":[],
    "source_file":"space_health.py"
})

radiation_table = [
    ["<b>Source/Mission</b>","<b>Radiation Exposure in Millisieverts</b>"],
    ["Average annual dose on Earth","3.6"],
    ["Apollo 11 (lowest of successful Apollo moon landings)","1.8"],
    ["Apollo 14 (highest of successful Apollo moon landings)","11.4"],
    ["Lifetime astronaut exposure under NASA regulations","1000-4000, depending on age and gender"],
    ["Annual astronaut exposure under NASA regulations","500"],
    ["30 day astronaut exposure under NASA regulations","250"],
    ["Space Shuttle 41-C: 8 day mission at 460 km","5.59"],
    ["Skylab 4: 87 day mission at 473 km","178"],
    ["International Space Station: 6 months at 353 km","80-160, depending on solar weather"],
    ["Estimated 3 year Mars mission","1200"],
    ["5.5% chance of developing fatal cancer based on linear no-threshold model","1000"]
]

helper.save_image({
    "filename":"space_radiation.jpg",
    "status":"Done",
    "details":"Some figures on radiation exposure for various space missions and how that compares to safety regulations and normal exposure. The ICRP report gives the figure on cancer risk, and all other figures are from the NASA report.",
    "table":radiation_table,
    "references":["nasa_radiation","sievert_def"],
    "source_file":"space_health.py"
})