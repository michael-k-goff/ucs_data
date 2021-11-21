# HVDC stuff
# Other grid stuff

import helper

# Cost figures from hvdc_cost_km, image on p. 303
cost = [
    ["<b>Type</b>","<b>Length (km)</b>","<b>Annual Cost per MW, Low (Dollars)</b>","<b>Cost, High</b>"],
    ["HVAC",100,10,12],
    ["HVDC",100,17,18],
    ["HVAC",300,31,34],
    ["HVDC",300,34,37],
    ["HVAC",475,42,47],
    ["HVDC",475,42,47],
    ["HVAC",800,70,75],
    ["HVDC",800,65,70]
]

hvdc_cost_im = {
    "filename":"transmission_cost.jpg",
    "status":"Done",
    "details":"Compare the annual cost of transmitting 1 MW of power over various distances using HVDC and HVAC. DC wins out after about 500 km and decisively after 800 km.",
    "table":cost,
    "references":["hvdc_cost_km"],
    "source_file":"hvdc.py"
}
helper.save_image(hvdc_cost_im)

##################### Right of way

hvdc_row_im = {
    "filename":"transmission_row.jpg",
    "status":"Done",
    "details":"Show right of way required for 6 GW transmission. Figures are 100 meters for HVAC and 40 meters for HVDC. Easy peasy.",
    "references":["hvdc_row"],
    "source_file":"hvdc.py"
}
helper.save_image(hvdc_row_im)

###################### Line losses.
# From hvdc_losses
hvdc_loss_rate = 0.965 # Over 1000 km
hvac_loss_rate = 0.933
hvdc_converter_loss = 0.984
hvac_converter_loss = 0.992
def hvdc_loss(km):
    return 1-(hvdc_converter_loss)*hvdc_loss_rate**(km/1000.)
def hvac_loss(km):
    return 1-(hvac_converter_loss)*hvac_loss_rate**(km/1000.)
losses = [["<b>Transmission Type</b>","<b>Distance (km)</b>","<b>Electricity Loss</b>"]]
line_lengths = [100,250,500,1000]
for i in range(len(line_lengths)):
    losses.append(["HVAC",line_lengths[i],"{0:.1f}".format(100*hvac_loss(line_lengths[i]))+"%"])
    losses.append(["HVDC",line_lengths[i],"{0:.1f}".format(100*hvdc_loss(line_lengths[i]))+"%"])
hvdc_loss_im = {
    "filename":"transmission_loss.jpg",
    "status":"Done",
    "details":"Power loss modeled for hypothetical 1200 MW long distance lines. The following models losses for AC and DC lines over various distances, including converter stations.",
    "table":losses,
    "references":["hvdc_losses"],
    "source_file":"hvdc.py"    
}
helper.save_image(hvdc_loss_im)

########################### Smart grid electricity and GHG savings
# From sreedharan
smart_grid_im = {
    "filename":"smartgrid.jpg",
    "status":"Done",
    "details":"Show electricity and GHG savings enabled by a smart grid. Note that I just said 'enabled'; the smart grid still needs to be paired with renewable energy, variable pricing, and other features to achieve savings. Figures are 1-4% for electricity and 2-7% for emissions.",
    "references":["sreedharan"],
    "source_file":"hvdc.py"
}
helper.save_image(smart_grid_im)
    
##################### HVDC cost benefit analyses. Add to this as appropriate

hvdc_table = [
    ["<b>Study</b>","<b>Cost</b>","<b>Benefit</b>"],
    ["MISO 2014","$36.2 billion","$41.4 billion"],
    ["Macdonald et al.","$18B","$47B"] # I'm guessing on the cost since I don't see that in the paper. Just that benefits are almost three times cost.
]

# There is a mistake with now the Macdonald result is reported. Those numbers are annual figures and should be adjusted accordingly.
# I would guess a 7% discount rate. Then the cost is $671.4285714285713 billion.
# The benefit is just given as just under third of that, so maybe guess $220 billion?

helper.save_image({
    "filename":"hvdc_cba.jpg",
    "status":"Done",
    "details":"Costs and benefits of HVDC from several studies.",
    "table":hvdc_table,
    "references":["miso2014","hvdc_cost"],
    "source_file":"hvdc.py"
})

# What is the benefit from the US HVDC grid? We'll calculate by assuming:
# - 50% renewable would be feasible without it, 80% with (and the grid induces that 30%)
# - Electricity would be natural gas otherwise
# - US electricity is about 4 trillion kWh per year
# - GHG impact is about 450 g/kWh for gas,, 50 g/kWh for renewables, so 400 g/kWh saved for each kWh from renewables.
hvdc_ghg_savings = 4*10**12 * 0.3 * 400 * 10**(-6) # Works out to 480 million tons per year

###################### Ancillary service stuff

ancillary_services_table = [
    ["<b>Service</b>","<b>Duration</b>","<b>Description</b>"],
    ["Black Start Services","Less than a second","Restart from a blackout."],
    ["Frequency and voltage regulation","Less than a second to seconds","Ensure the grid's frequency and voltage is in specified ranges."],
    ["Spinning reserves","Seconds or tens of seconds","Retain back-up power in active generators."],
    ["Non-spinnng reserves","Tens of seconds to minutes","Retain back-up power in inactive generators."],
    ["Peak shaving","Hours","Respond to daily peaks or troughs in demand."],
    ["Firm power/avoid curtailment","Hours to tens of hours","Keep daily demand and supply profile flat."],
    ["Seasonal storage","Days to months","Provide power during summer and winter."]
]

helper.save_image({
    "filename":"ancillary_services.jpg",
    "status":"Done",
    "details":"Information about ancillary services.",
    "table":ancillary_services_table,
    "references":["anc_services"],
    "source_file":"hvdc.jpg"
})