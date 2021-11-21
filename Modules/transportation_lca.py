# Transportation LCA figures

import helper

lca_table = [
    ["<b>Mode</b>","<b>In-vehicle energy</b>","<b>Upstream energy for fuel</b>","<b>Vehicle Manufacturing & Maintenance</b>","<b>Infrastructure Construction & Operation</b>"],
    ["35 MPG Sedan (1 passenger)",2.37,0.5,0.69,0.06],
    ["Boeing 737 Legacy (82 passengers)",1.99,0.09,0.013,0.19],
    ["San Francisco BART",0.71,0.17,0.05,0.37],
    ["Urban Diesel Bus (Peak)",0.52,0.07,0.06,0.02],
    ["San Francisco Bay Area Caltrain (before electrification)",0.66,0.12,0.19,0.43]
]

helper.save_image({
    "filename":"transportation_lca.jpg",
    "status":"Done",
    "details":"Show lifecycle energy, including upstream usage, for select transportation modes. Units are MJ/passenger-km. The first column is energy used by the vehicle, except for BART--which uses electricity--the figure is the primary energy behind the electricity. The second column is energy that goes into fuel production. For the non-electric modes, that's refining, distribution of fuel, etc. For electricity, I'm not 100% sure, but I think it would include energy to build the power plant or stuff like that. The third column is energy to build and maintain the vehicle itself, while the fourth column is energy for infrastructure (e.g. roads, track). The key message here is that there is significant energy associated with transportation that is not used directly by the vehicle. For most of our plots, we are ignoring this, because trying to account for these figures would be very difficult, but at least we want the reader to be aware of the issue.<br><br>Throughout the Transportation section, figures on energy for various transportation modes are quoted, usually as ranges, because they incorporate multiple studies. The numbers in this table are pulled just from a single study by Chester and Horvath, so they don't necessarily agree.<br><br>BTW, did you know that Caltrain was only recently electrified? The construction for that project started in either 2017 or 2018, when I was in SF. Until then--and maybe still now for all I know--Caltrain ran on diesel. My friends from overseas would have been only slightly more astonished to learn that it is pulled by horses.",
    "table":lca_table,
    "references":["chester","chester2","chester3"],
    "source_file":"transportation_lca.py"
})