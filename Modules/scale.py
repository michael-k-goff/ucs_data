# Figures for the Scale page.

import helper

size_table = [
    ["<b>Figure</b>","<b>Value</b>"],
    ["Diameter of Earth","12742 km"],
    ["Diameter of Jupiter","142 Mm"],
    ["Earth-Moon Distance","384.4 Mm"],
    ["Diameter of the Sun","1.39 Gm"],
    ["Earth-Sun Distance","150 Gm"],
    ["Diameter of Betelgeuse","1.3 Tm"],
    ["Diameter of VY Canis Majoris, one of the largest known stars","2 Tm"],
    ["Average Sun-Pluto Distance","5.9 Tm"],
    ["Outer radius of Kuiper Belt (approximate)","7.5 Tm"],
    ["Event Horizon radius of the largest known black hole","62.03 Tm"],
    ["Outer radius of the Oort Cloud (approximate)","7.5 Pm"],
    ["Distance to Proxima Centauri, nearest star to the Earth except the Sun","39.9 Pm"],
    ["Average thickness of Milky Way","9.46 Em"],
    ["Distance to Large Magellanic Cloud (a dwarf galaxy)","1.62 Zm"],
    ["Approximate diameter of Milky Way stellar disk","1.8 Zm"],
    ["Distance to Andromeda Galaxy","24 Zm"],
    ["Diameter of Local Group of galaxies","50 Zm"],
    ["Distance to Virgo Cluster","300-600 Zm"],
    ["Diameter of Local Supercluster","2.19 Ym"],
    ["End of Greatness, beyond which size distinct structures are not observed","2.8 Ym"],
    ["Diameter of Pisces–Cetus Supercluster Complex, where we live","9.461 Ym"],
    ["Length of Sloan Great Wall","13 Ym"],
    ["Diameter (comoving distance) of observable universe","870 Ym"],
    ["Size of universe","Unknown, possibly infinite"]
]

helper.save_image({
    "filename":"cosmic_scale.jpg",
    "status":"Not Done",
    "table":size_table,
    "details":"Select figures illustrating sizes, starting at Earth and working up to cosmic scales. All figures come from Wikipedia and no separate source will be added. Metric prefixes are used throughout. Many more sizes could be added, and maybe some will be added later. One candidate would be smaller sizes, going to subatomic scales. I imagine this will look a bit like the timeline plot in terms of how it is presented, though hopefully a lot simpler.",
    "references":[],
    "source_file":"scale.py"
})

energy_table = [
    ["<b>Figure</b>","<b>Energy Consumption (Watts)</b>","<b>Rating on Kardeshev Scale</b>","<b>(Possible) Power Sources</b>","<b>Source</b>"],
    ["Human Metabolic Rate","10^2-10^3","-0.4 to -0.3"],
    ["Blue Whale Metabolic Rate","1.9 X 10^4","-0.17","","Lockyer"],
    ["Biological Energy","10^6","0.0"],
    ["Civilizational Power Consumption, 1800","6.4 X 10^11","0.58","Traditional Biomass"],
    ["Civilizational Power Consumption, 1900","1.4 X 10^12","0.61"],
    ["Civilizational Power Consumption, 1965","4.9 X 10^12","0.67"],
    ["Civilizational Power Consumption, 2000","1.3 X 10^13","0.71"],
    ["Civilizational Power Consumption, 2015","1.7 X 10^13","0.72","Fossil Fuels"],
    ["Heat Flow from Earth's Interior","4.42 X 10^13","0.77","","Pollack et al."],
    ["Planetary Civilization","10^16","1.0","Nuclear Fission, Fusion, Solar-Power Beaming"],
    ["Earth's Solar Insolation","1.7 X 10^17","1.12","","Prša et al."],
    ["Luminosity of the Dimmest Red Dwarfs","1.1 X 10^23","1.71","","Mamajek"],
    ["Stellar Civilization","10^26","2.0","Dyson Sphere, Star Lifting"],
    ["Luminisity of the Sun","3.828 X 10^26","2.06","","Prša et al."],
    ["Luminosity of Betelgeuse, One of the Brightest Stars","5.74 X 10^31","2.58","","Smith et al."],
    ["Galactic Civilization","10^36","3.0","Dyson Spheres, Supermassive Black Holes"],
    ["Luminisity of the Milky Way","2.6 X 10^37","3.14","","Kent et al."],
    ["Luminosity of the Virgo Supercluster","1.1 X 10^39","3.31","","Einesto et al."],
    ["Cosmic Civilization","10^46","4.0","Dark Energy, ?","Kaku"],
    ["Lumonisity of the Observable Universe","10^48","4.2","","Wijers"]
]

helper.save_image({
    "filename":"kardeshev.jpg",
    "status":"Done",
    "table":energy_table,
    "details":"Figures on energy consumption at (mostly) large scales. The center of this is the Kardeshev scale, as extended by Carl Sagan and Robert Gray. I think the best way to portray this graphically would be by the K-scale rating, which would make this a logarithmic plot. All numbers are taken from Gray unless otherwise noted.",
    "references":["kardeshev_gray","kardashev1967","sagan","blue_whale_size","prsa","kent_milkyway","wijers","kaku","geothermal_total","mamajek","betelgeuse_lumin","vs_lumin"],
    "source_file":"scale.py"
})