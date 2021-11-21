# Some figures related to noise pollution

import helper

noise_table = [
    ["<b>Sound</b>","<b>Volume (approximate, dB)</b>","<b>Source</b>"],
    ["Limit for 8 hour workplace average","85","CDC"],
    ["Limit for instantaneous noise","140","CDC"],
    ["Recommendation for a bedroom at night","30","WHO"],
    ["Recommendation for a classroom","35","WHO"],
    ["Recommendation for nighttime noise, outside of bedrooms","40","WHO"],
    ["Noise from traffic affecting 40% of Europeans","55","WHO"],
    ["Daytime noise affecting 20% of Europeans","65","WHO"],
    ["Nighttime noise affecting 30% of Europeans","55","WHO"],
    ["Guidelines for road traffic noise","53","WHO Guidelines"],
    ["Guidelines for rail","54","WHO Guildlines"],
    ["Guidelines for aircraft","45","WHO Guidelines"],
    ["Guidelines for wind turbines","45","WHO Guidelines"],
    ["Average street level noise in New York City","73.4 (ranges from 55.8-95.0)","McAlexander et al."],
    ["Car horn","90","Iberdrola"],
    ["Bus","100","Iberdrola"],
    ["Aircraft overhead","130","Iberdrola"],
    ["Pneumatic Drill","110","Iberdrola"],
    ["Bars, restuarants, outdoor terraces","100+","Iberdrola"],
    ["Barking Dog","60-80","Iberdrola"],
    ["Rustling Leaves","20-30","National Geographic"],
    ["Thunderclap","120","National Geographic"],
    ["Siren","120-140","National Geographic"],
    ["Power Lawn Mower","90","National Geographic"],
    ["Subway","90-115","National Geographic"],
    ["Rock Concert","110-120","National Geographic"]
]

helper.save_image({
    "filename":"noise_level.jpg",
    "status":"Done",
    "details":"A list of some common noise levels, in decibels. This is meant to give the view a sense of what we mean by noise pollution and some common regulations. Volume is in decibels, which is a logarithmic unit. An increase in volume of 10 decibels means that a sound is 10 times louder.",
    "table":noise_table,
    "references":["cdc_noise","who_noise","who_noise2","nyc_noise","iberdrola","natgeo_noise"],
    "source_file":"noise_pollution.py"
})

#########################################

# Underwater noise

underwater_noise_table = [
    ["<b>Noise Source</b>","<b>Energy Released per year (GJ)</b>"],
    ["Underwater Nuclear Explosions",2600000],
    ["Airgun Arrays",39000],
    ["Military Sonar (53C)",8500],
    ["Super Tankers",3700],
    ["Ship Shock Trials",3300],
    ["Military Sonar (SURTASS/LFA)",170],
    ["Merchant Vessels",140],
    ["Navigation Sonar",36],
    ["Research Sonar",0.91],
    ["Fishing Vessels",0.13]
]

helper.save_image({
    "filename":"underwater_noise.jpg",
    "status":"Done",
    "details":"Nuclear weapons were once tested underwater, but that activity is banned under the Comprehensive Test Ban Treaty. Geopolitical conditions could evolve so that testing resumes, and the figures assumed one device is tested every 20 years. 53C and SURTASS/LFA are two types of sonar.",
    "table":underwater_noise_table,
    "references":["cdc_noise","who_noise","who_noise2","nyc_noise","iberdrola","natgeo_noise"],
    "source_file":"noise_pollution.py"
})

######################################### Source of noise

# norway_noise

noise_annoyance_table = [
    ["<b>Source</b>","<b>Annoyance Index</b>"],
    ["Road Traffic",446862],
    ["Manufacturing",24237],
    ["Other Industry",16087],
    ["Air Traffic",22233],
    ["Railways",25542],
    ["Construction",21678],
    ["Shooting Ranges", 12060],
    ["Motor Racing Tracks",4848]
]

helper.save_image({
    "filename":"annoyance_index.jpg",
    "status":"Done",
    "details":"Results from a study that was done in Norway for 2003. These indices are based on how people people expressed annoyance over a particular noise. The meaning of the numbers is inscrutable; what matters is how they compare, and in particular how much greater road traffic is than all other figures.",
    "table":noise_annoyance_table,
    "references":["norway_noise"],
    "source_file":"noise_pollution.py"
})

######################################### DALY's in Europe lost due to noise pollution

# eu_noise_daly

daly_table = [
    ["<b>Cause</b>","<b>DALY's lost in Europe due to noise pollution</b>"],
    ["Ischaemic heart disease",61000],
    ["Cognitive impairment of children",45000],
    ["Sleep disturbance",903000],
    ["Tinnitus",22000],
    ["Annoyance",587000]
]

helper.save_image({
    "filename":"noise_daly.jpg",
    "status":"Done",
    "details":"A study in Europe of how many disability-adjusted life-years (DALYs) were lost due to noise pollution.",
    "table":daly_table,
    "references":["eu_noise_daly"],
    "source_file":"noise_pollution.py"
})