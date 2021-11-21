# Calculations and plots related to nuclear energy solution(s).

# Parameters for the low nuclear cost scenario.
# Based on ReEDS. https://openei.org/apps/reeds/#national-tech-chart

import helper

co2_savings = [0,0,0,0,0,0, 0.01, 0.03, 0, 0.01, 0.02, 0.03, 0.02, 0.02, 0.05] # Billions of tons, in 2 year increments, 2022-2050

elec_price_savings = [0.02, -0.02, 0.02, 0.06, 0.61, 0.35, -0.06, 0.26, -0.14, 0.27, 0.17, 0.66, -0.23, -0.14, 0.62] # 2018 $/MWh, starting in 2022 and going in 2 year increments to 2050

# From Annual Energy Outlook 2020: https://www.eia.gov/outlooks/aeo/data/browser/#/?id=8-AEO2020&cases=ref2020&sourcekey=0
electricity_gen = [4018, 4053, 4088, 4121, 4171, 4225, 4282, 4353, 4429, 4505, 4585, 4672, 4766, 4865, 4969] # Billions of kWh, in 2 year increments, 2022-2050

# From International Energy Outlook: https://www.eia.gov/outlooks/aeo/data/browser/#/?id=30-IEO2019&region=0-0&cases=Reference&f=A
world_electricity = [26830.3, 27771.5, 28809.6, 29953.2, 31094.2, 32265.7, 33442.2, 34649.2, 35878.5, 37107.0, 38592.5, 40086.5, 41518.0, 42880.5, 44247.3] # Billions of kWh, 2 year increments, 2022-2050

coal_share = [0,0,0,0,0,0,0,0,0,0, 0.01, 0, 0.01, 0, 0.01] # Share of total electricity that coal is reduced in the nuclear scenario. More precise numbers would be better.

export_share = 0.25 # Wild guess as to the share of nuclear exports that could be captured by US companies in the nuclear scenarios
discount_rate = 0.05 # Discount rate as applied to electricity monetary savings and non-GHG benefits, but not to CO2 reduction.

def nuclear_value():
    a = (1-discount_rate)**30
    
    co2_benefit_by_year = [50*2*co2_savings[i] for i in range(len(co2_savings))] # Assume a flat $50/ton carbon price
    co2_benefit = sum(co2_benefit_by_year)
    co2_benefit *= 1+1/(1-a)*a
    
    elec_benefit_by_year = [elec_price_savings[i]*electricity_gen[i]/1000.*(1-discount_rate)**(2*i+2) for i in range(len(elec_price_savings))]
    elec_benefit = sum(elec_benefit_by_year)
    elec_benefit *= 1+1/(1-a)*a
    
    non_ghg_benefit_by_year = [coal_share[i]*electricity_gen[i]*(0.0136+0.0085+0.0016+0.0006)*(1-discount_rate)**(2*i+2) for i in range(len(coal_share))] # See Coal page for external costs per kWh
    non_ghg_benefit = sum(non_ghg_benefit_by_year)
    non_ghg_benefit *= 1+1/(1-a)*a
    
    co2_export_by_year = [export_share*(co2_benefit_by_year[i])*(world_electricity[i]/electricity_gen[i]-1.) for i in range(len(co2_benefit_by_year))]
    co2_export_total = sum(co2_export_by_year)
    co2_export_total *= 1+1/(1-a)*a
    
    elec_export_by_year = [export_share*(elec_benefit_by_year[i])*(world_electricity[i]/electricity_gen[i]-1.) for i in range(len(co2_benefit_by_year))]
    elec_export_total = sum(elec_export_by_year)
    elec_export_total *= 1+1/(1-a)*a
    
    non_ghg_export_by_year = [export_share*(non_ghg_benefit_by_year[i])*(world_electricity[i]/electricity_gen[i]-1.) for i in range(len(co2_benefit_by_year))]
    non_ghg_export_total = sum(non_ghg_export_by_year)
    non_ghg_export_total *= 1+1/(1-a)*a
    
    export_by_year = [export_share*(co2_benefit_by_year[i]+elec_benefit_by_year[i]+non_ghg_benefit_by_year[i])*world_electricity[i]/electricity_gen[i] for i in range(len(co2_benefit_by_year))]
    export_total = sum(export_by_year)
    export_total *= (1+(1-discount_rate)**30)
    
    return [
        ["<b>Benefit</b>","<b>Net present value, billions USD</b>"],
        ["CO<sub>2</sub> reduction, domestic",co2_benefit],
        ["Electricity cost savings, domestic",elec_benefit],
        ["Non-GHG environmental benefit, domestic",non_ghg_benefit],
        ["CO<sub>2</sub> reduction, export",co2_export_total],
        ["Electricity cost savings, export",elec_export_total],
        ["Non-GHG environmental benefit, export",non_ghg_export_total]
    ]
    
helper.save_image({
    "filename":"nuclear_benefit.jpg",
    "status":"Done",
    "table":nuclear_value(),
    "details":"Estimated benefits of a cost reduction in nuclear power. The AEO is the source for domestic electricity, IEO for international electricity. See also, the Coal page for external impacts of coal, the reduction of which is how the non-GHG benefits of nuclear is estimated. The ReEDS scenario analysis is used to estimated the domestic benefits. Assumptions include a $50/ton carbon price (undiscounted) up to 2050 and a 5% discount rate for everything else. For benefits after 2050, the pre-2050 benefits are applied with a 5% discount rate thereafter. See the Nuclear page for some details and assumptions.",
    "references":["aeo2020","ieo2019","reeds"],
    "source_file":"nuclear_solution.py"
})