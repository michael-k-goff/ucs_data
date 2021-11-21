# Environmental policy. Comparison of policy options.

import helper
import load_balancing

# Plan here:
# Based on the NAS report, get figures for Production Tax Credit, fuel excise tax, maybe aviation excise tax
# Also compare the RPS study from UChicago.
# For each one, report the range of costs if applicable and be sure to indicate what kind of cost they are (social, fiscal, etc.)
# More would be nice.

# Based on the ghg_tax references (see notes in energy - policy.txt).
ptc_cost = 280 # Applying the CPI calculator (https://data.bls.gov/cgi-bin/cpicalc.pl) to $250 from January 2013 to January 2020
motor_fuel_high = 25000 / 3.5 * 1.12025 # 8001.785714285715. See notes in energy - policy.txt
motor_fuel_low = 25000 / 9.8 * 1.12025 # 2857.780612244898
aviation_fuel = (390.+22.)/(70./25.) * 1.12025 # 164.8367857142857
rps_low = 115*1.02487 # 117.86005
rps_high = 530*1.02487 # 543.1811

policy_options = [
    ["<b>Policy</b>","<b>Cost of Emissions Reduction</b>","<b>Additional Considerations</b>"],
    ["Production Tax Credit","$280/ton, fiscal cost","Incentivizing energy production may discourage efficiency."],
    ["Highway Motor Fuel Excise Tax","$2900-8000/ton, tax revenue","Emissions reduction not primary goal."],
    ["Aviation Fuel Excise Tax","$165/ton, tax revenue","Emissions reduction not primary goal."],
    ["Renewable Portfolio Standard","$120-540/ton, social cost","Most costs are grid integration; does not account for induced innovation benefits."]
]

helper.save_image({
    "filename":"policy_comparison.jpg",
    "status":"Done",
    "details":"Here we portray the cost, per ton of emissions reduction, of several policies. I expect that over time we will want to add to the list, as I don't know yet very well the full lay of the land for the literature on this topic. It is also very important to emphasize that costs are measured in different ways. The best measure of the true cost of a policy is, I think, the social cost, which is how much is being spent by society as a whole. Fiscal costs and tax burden are monetary flows from and to the government, respectively, but a transfer of money to another party is not the same as a loss. So, in general, a dollar of fiscal cost or tax burden should not be regarded as as much of a loss to society as a dollar of social cost, but I am not aware of any good general strategy to translate one into the other.<br><br>Production Tax Credit, motor fuel excise tax, and aviation fuel excise tax come from the NAS study. RPS standards from Greenstone and Nath. All figures are CPI adjusted to 2020.",
    "table":policy_options,
    "references":["ghg_tax","rps_cost"],
    "source_file":"policy.py"
})

###################################### R&D statistics

# From https://www.iea.org/reports/energy-technology-rd-and-d-budgets-2019
iea_government_rd = { # All government spending from IEA countries in 2018, by general category. In millions of USD, 2018 PPP.
    "Energy Efficiency":4132,
    "Fossil Fuels":1858,
    "Renewable":2983,
    "Nuclear":4228,
    "Hydrogen and Fuel Cells":611,
    "Other power and storage technologies":1148,
    "Cross-cutting":4496,
    "Unallocated":178,
    "Total":19634
}

iea_private_rd = { # Billions of USD. Having to estimate by eyeballing the chart. See p. 160 of the full report. 2018, not sure if it is PPP but will guess it is.
    "Other":4,
    "Oil and Gas":20,
    "Thermal Power and Combustion Equipment":5,
    "Nuclear":1,
    "Electricity Generation and Networks":17,
    "Renewables":5,
    "Automobiles":42
}

# From World Energy Investment 2019, according to text on p. 159, world government energy R&D is about $26B. Is USD, PPP?

# From WEI 2019, current world energy investment by area. Billions of USD
# See https://www.iea.org/reports/world-energy-investment-2019
world_energy_investment = {
    "Battery Storage":4,
    "Networks":293,
    "Renewable Power":304,
    "Nuclear":47,
    "Fossil Fuel Power":127,
    "Oil & Gas: Downstream, Midstream, Refining":249,
    "Oil & Gas: Upstream":477,
    "Energy Efficiency, Industrial":38,
    "Energy Efficiency, Transport":63,
    "Energy Efficiency, Buildings":139,
    "Coal Supply":80,
    "Renewables for Transport and Heat":25
}

world_energy_investment_table = [["<b>Energy Sector</b>","<b>World investment in 2018, billions of US Dollars</b>"]] + [[key,world_energy_investment[key]] for key in world_energy_investment]

helper.save_image({
    "filename":"world_energy_investment.jpg",
    "status":"Done",
    "details":"World energy investment in 2018, billions of US Dollars",
    "table":world_energy_investment_table,
    "references":["wei2019"],
    "source_file":"policy.py"
})

iea_government_rd_table = [["<b>Energy Technology</b>","<b>Government investment by IEA member countries in R&D in 2018, millions of US Dollars</b>"]] + [[key,iea_government_rd[key]] for key in iea_government_rd]

helper.save_image({
    "filename":"public_rd.jpg",
    "status":"Done",
    "details":"Government investment by IEA member countries in R&D in 2018. Figures all come from the IEA's R&D Budget report. Not all countries are members of the IEA, and nonmembers evidently don't report statistics. However, by comparing the total figure here to the R&D figures in the World Energy Investment report, IEA member country governments apparently spend about three quarters of all public energy R&D in the world. Here, government expenditures include direct expenditures as well as tax subsidies.",
    "table":iea_government_rd_table,
    "references":["wei2019","iea_rd2019"],
    "source_file":"policy.py"
})

iea_private_rd_table = [["<b>Energy Technology</b>","<b>Corporate investment by in R&D in 2018, billions of US Dollars</b>"]] + [[key,iea_private_rd[key]] for key in iea_private_rd]

helper.save_image({
    "filename":"corporate_rd.jpg",
    "status":"Done",
    "table":iea_private_rd_table,
    "details":"Corporate R&D into various energy technologies in 2018. I didn't find the numbers stated explicitly and had to read them off a table, so they're not very exact. Not that they probably would be anyway. This comes from a different report from the government investment, so the categories are evidently not the same. This report classifies Automobiles as an energy technology, though I'm not sure what all is constituted in that figure.",
    "references":["wei2019"],
    "source_file":"policy.py"
})

################################################# Figures for investment quantities needed

# Maybe useful for calculations: US energy investment was (2+42+173+134=351) billion in 2018, as per https://www.iea.org/reports/world-energy-investment-2019.
# From BP Statistical Review of Energy, US electricity generation in 2018 was 4460.8 TWh and worldwide was 26614.8
# Capital cost of nuclear in the US: $4100-5000. May use the midpoint for calculations. Capacity factor of 90%.
# 2018 generation stats, in TWh: nuclear in US: 192.2. nuclear worldwide: 611.3. Solar in the US: 97.1. Solar in the world: 584.6.
# ... wind in the US: 277.7. Wind in the world: 1270.0.

us_investment = 351 # Billions of dollars per year, see above
world_investment = sum([world_energy_investment[key] for key in world_energy_investment])

us_generation = 4460.8
us_fossil_generation = 26.4+1578.5+1245.8

world_generation = 26614.8
world_fossil_generation = 802.8+6182.8+10100.5

nuclear_capacity = 0.9
nuclear_capital = (4100+5000)/2.
solar_capacity = 0.3
solar_capital = 1750 # Reference: nrel_atb_solar
wind_capital = 1610 # Reference: wind_capital
wind_capacity = 0.415 # From wind_capital

nuclear_time = (5*84+5*92+5*81+5*120+5*58+5*76+5*66+74+58)/37./12 # nuclear_build2
solar_time = 6. # solar_build

us_nuclear = us_fossil_generation * 10**9 / 8760. / nuclear_capacity * nuclear_capital
world_nuclear = world_fossil_generation * 10**9 / 8760. / nuclear_capacity * nuclear_capital
us_solar = us_fossil_generation * 10**9 / 8760. / solar_capacity * solar_capital + load_balancing.hvdc_cost_average
us_solar_nogrid = us_fossil_generation * 10**9 / 8760. / solar_capacity * solar_capital # For use elsewhere. The cost of only the solar power without the grid.
world_solar = world_fossil_generation * 10**9 / 8760. / solar_capacity * solar_capital + load_balancing.hvdc_cost_average * world_fossil_generation / us_fossil_generation
us_wind = us_fossil_generation * 10**9 / 8760. / wind_capacity * wind_capital # Meant for use in economics_overview.py. Not including grid integration.

investment_table = [
    ["<b>Strategy</b>","<b>Region</b>","<b>Investment Cost, trillions of US Dollars</b>","<b>Years at Current Energy Investment Levels</b>"],
    ["Replace fossil electricity with nuclear","United States",us_nuclear/10**12,nuclear_time+us_nuclear/10**9/us_investment],
    ["Replace fossil electricity with nuclear","World",world_nuclear/10**12, nuclear_time+world_nuclear/10**9/world_investment],
    ["Replace fossil electricity with solar","United States",us_solar/10**12,solar_time+us_solar/10**9/us_investment],
    ["Replace fossil electricity with solar","World",world_solar/10**12,solar_time+world_solar/10**9/world_investment]
]

helper.save_image({
    "filename":"transition_scenarios.jpg",
    "status":"On Hold",
    "table":investment_table,
    "details":"Data sources: capital, including system, cost of solar of $1.75/watt from the NREL study. For nuclear capital costs, I am using the midpoint of the range for the US on the nuclear page and applying it to the world scenario as well. Total energy production figures from BP. Capacity factors of 30% for solar and 90% for nuclear. The US solar scenario includes the cost of an HDVC supergrid. See the Grid Design page for details on the cost estimate of that. For the world solar scenario, lacking good figures on worldwide grid integration, I assumed a per-kW grid integration cost the same as in the US solar scenario. To get the time length for deployment, I divided total investment required by annual energy invested to get total time, and then added just under 7 years for the nuclear scenarios, based on the World Nuclear Association report (average time times from 1981 to 2017), and 6 years for solar to reflect the construction time for those technologies. <font color=\"red\">I have tentatively decided to cut the section where this plot was going to be included. The content is partially superseded by data presented in investment_overview.jpg. I will leave this in the list for now for reference, though.</font>",
    "references":["nrel_atb_solar","bp","wei2019","nuclear_build2","solar_build"],
    "source_file":"policy.py"
})

# 6 years for solar? https://www.seia.org/research-resources/development-timeline-utility-scale-solar-power-plant
# 7.5 for nuclear? http://euanmearns.com/how-long-does-it-take-to-build-a-nuclear-power-plant/

# Some old text that was on the the 'policy' section.
# Substantial investments in time and money are required for any clean energy transition. Following are estimates of the time and money required to replace fossil fuels in electricity with low carbon options at current energy investment rates.
# -transition_scenarios.jpg
# !Estimated investment and time required to transition the United States and the world to all low carbon electricity, using <a href=\"/solution/nuclear\">nuclear</a> or <a href=\"/solution/solar\">solar</a>. The solar scenarios assume the construction of a <a href=\"/solution/grid_design\">high voltage direct current supergrid</a> to ensure reliability. Capital costs for nuclear are the midpoint of the range for the United States as reported in our nuclear analysis, and for solar are estimated at $1.75/watt, including system integration costs [nrel_atb_solar]. Capacity factors of 90% and 30% are assumed respectively for nuclear and solar. Transition times are estimated as the total investment required divided by all energy investment as indicated above. An additional 7 years and 6 years are added respectively to the nuclear [nuclear_build2] and solar [solar_build] scenarios to account for typical plant construction times. Overall plants needs are determined by electricity demand in 2018, as reported by BP [bp].

#####################################################

# Studies on effect of Kyoto on emissions

kyoto_table = [
    ["<b>Source</b>","<b>Emissions Reduction from Kyoto Ratification</b>"],
    ["Iwata and Okada","11%"],
    ["Aichele and Felbermayr","7%"],
    ["Grunewald and Martinez-Zarzoso","8%"]
]
# Note from the aichele reference: emissions reductions offset by imports

helper.save_image({
    "filename":"kyoto.jpg",
    "status":"Done",
    "table":kyoto_table,
    "details":"Show several estimates of how much the Kyoto Protocol reduced emissions in countries that adopted it. It should be noted that determining this figure with any precision is nearly impossible, since that requires having a counterfactural scenario.",
    "references":["iwata","aichele","grunewald"],
    "source_file":"policy.py"
})