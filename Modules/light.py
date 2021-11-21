# Efficiency of lighting, not to be confused with light pollution.

import helper

light_table = [
    ["<b>Light Source</b>","<b>Typical Efficiency, lumens per watt</b>"],
    # The following six can be found in various tables in reference 'u4elight'.
    ["LED Luminaire","80-150"],
    ["LED Lamp","60-130"],
    ["Fluorescent Lamp","80-110"],
    ["Compact Fluorescent Lamp","50-70"],
    ["Halogen Lamp","11-21"],
    ["Incandescent Bulb","8-17"],
    # From Guttag
    ["Laser Diode","240-258"],
    # From the DOE
    ["Organic LED, now","55-85"],
    ["OLED, 2035 Projection","180"]
]

helper.save_image({
    "filename":"light_efficiency.jpg",
    "status":"Done",
    "table":light_table,
    "details":"Efficacy, in lumens per watt, of various types of lighting. Did we do this one already? If so, let me know. Laser diode figures from Guttag, OLED from the DOE, and the rest from U4E. I'm going with the DOE's efficiency for the OLED light itself; the luminaire (full fixture) is given at 154 lm/W in 2035.",
    "references":["u4elight","guttag","oled"],
    "source_file":"light.py"
})