# Space colonization stuff

import helper

energy_needs_table = [
    ["<b>Location</b>","<b>Electricity Needs per Capita, kWe/capita</b>","<b>Notes</b>","<b>Source</b>"],
    ["Earth","0.4","Electricity only","BP"],
    ["United States","1.5","Electricity only","BP"],
    ["Mars","90","Modeled for a 12 person base","Heidmann"],
    ["Mars","45","Modeled for 150 people","Heidmann"],
    ["Mars","20","Simply reported as \"more advanced\" than the 150 people model","Heidmann"],
    ["Moon","3","Modeled for a 4 person research base","Koster"],
    ["International Space Station","17","Average power of the ISS solar array is 84-120 kW; we are taking the midpoint of 102 kW, over 6 astronauts.","NASA"],
    ["Orbital Habitat","26.4","Model of a Large Orbital Habitat","Soilleux and Gunn"],
    ["Biosphere 2","88","An experiment in Arizona to develop a closed habitat","Soilleux and Gunn"],
    ["Antarctica","6.8","Power requirements in the Winter of McMurdo Station","Soilleux and Gunn"],
    ["Antarctica","30","Power modeled for Halley VI, UK research station","Soilleux and Gunn"],
    ["Orbital Habitat","3","Powered modeled for a Stanford Torus of 10,000 people","Soilleux and Gunn"],
    ["Orbital Habitat","10","Powered modeled for Kalpana One, a hypothetical habitat","Soilleux and Gunn"],
    ["Moon","10-60","This article cites several studies and says they range from 10 kW/person to 60 kW/person","Power Engineering International"]
]

helper.save_image({
    "filename":"col_energy.jpg",
    "status":"Done",
    "table":energy_needs_table,
    "details":"This bar chart is to demonstrated the energy requirements for various kinds of space colonies. Of course, most of them are hypothetical and the given numbers are modeled, not observed operational values. The figures for Earth come from the BP Statistical Review of World Energy and are electricity only. In all cases, values reported are electrical energy rather than the primary energy required to generate the electricity.",
    "references":["bp2021","heidmann","lunar_energy","iss_energy","orbital_energy","lunar_power"],
    "source_file":"space_col.py"
})