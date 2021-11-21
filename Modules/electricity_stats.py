# World electricity figures

import helper

bp_elec = [9879.8,10174.8,10665.1,11134.9,11654.0,11955.0,12216.1,12325.0,12586.4,12910.6,13362.3,13782.2,14115.0,14493.9,14909.0,15548.3,15782.4,16340.5,16918.6,17701.7,18451.7,19155.8,20041.2,20433.3,20269.3,21574.3,22258.7,22807.8,23449.8,23914.6,24286.9,24956.9,25676.6,26614.8]
bp_elec = [[1985+i, bp_elec[i]] for i in range(len(bp_elec))]

im_electricity = {
    "filename":"world_electricity.jpg",
    "status":"Done",
    "details":"This is a replacement for the electricity trend. This time we are only going to show world electricity (in terawatt-hours) by year. All figures from BP",
    "table":bp_elec,
    "references":["bp2019"],
    "source_file":"electricity_stats.py"
}

helper.save_image(im_electricity)

#################### Transmission losses
# This analysis dates back to 2015. I am asking Lee for a plot but am not updating the figures myself at this time. Maybe later.
transmission_losses = [
    ["World",8.1],
    ["United States",6.3],
    ["Germany",3.9],
    ["China",5.8],
    ["India",17.1]
]
im_transmission_losses = {
    "filename":"transmission_losses.jpg",
    "status":"Done",
    "details":"Transmission losses (as percents of total electricity) for the world and select countries.",
    "table":transmission_losses,
    "references":["elec_loss_country"],
    "source_file":"electricity_stats.py"
}
helper.save_image(im_transmission_losses)

##################################### Blackout costs

blackout_table = [
    ["<b>Event</b>","<b>Estimated Loss of Power, GWh</b>","<b>Estimated Cost, Millions of dollars (2020)</b>","<b>Cost per Unserved kWh</b>"],
    ["1977 New York City blackout",101.4,(55.1+290.2)*4.40976068,""], # All from reference blackout1. CPI adusted from 1977
    ["2003 Northeast blackout",920,6000*1.39293197,""], # Loss of power from blackout1, cost from blackout2. CPI adjusted from 2004
    ["2018 California power cuts (low cost estimate)",96,960*1.02486572,""], # CPI-adjusted from 2019. From blackout3
    ["2018 California power cuts (high cost estimate)",96,2500*1.02486572,""], # CPI-adjusted from 2019. From blackout3
    ["2003 Sweden and Denmark blackout",18,(206.22+256)/2*1.19052366,""], # CPI-adjusted from 2010. From blackout4
    ["1999 France blackout",400,1413*1.19052366,""], # From blackout4
    ["2005 Sweden blackout",111,526*1.19052366,""], # From blackout4
    ["2003 Italy blackout",196,1182*1.1068*1.08887116,""] # From blackout5
]

for i in range(1,len(blackout_table)):
    blackout_table[i][3] = "$" + str((blackout_table[i][2] / blackout_table[i][1])) + "/kWh"

helper.save_image({
    "filename":"blackout_cost.jpg",
    "status":"Done",
    "details":"Some cost estimates and estimated loss of power from historic blackouts. Information about 1977 NYC and the power loss from 2003 NE from Adibi and Martins. Cots of the 2003 NE blackout from Electricity Consumers Resource Council. Information about the CA power cuts from Koran. The Sweden, Denmark, and France figures are from Oseni and Pollitt. The Italy figures are from Schmidthaler and Reichl. In all cases, I am citing sources for the total power loss and economic damages, and the cost per unserved kWh is calculated.",
    "table":blackout_table,
    "references":["blackout1","blackout2","blackout3","blackout4","blackout5"],
    "source_file":"electricity_stats.py"
})