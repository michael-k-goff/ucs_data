# Benchmarking

# General parameters
discount_rate = 0.05
benefit_length = 20 # Number of years the energy efficiency benefit is taken to apply

# From https://www.energy.gov/sites/prod/files/2014/07/f17/sep_costbenefits_paper13.pdf
# Over 1.1 years.
cost = 319000 # Total cost
cost_staff = 214000
cost_external_technical_assistance = 58000
cost_monitoring_metering = 28000
cost_audit = 18000

# Assuming that the cost given is for 1.1 years, and after that maintaining gains is 1/10 the cost annually
cost_year1 = cost * 1/1.1
cost_year2 = 1/11 * cost + 10/11 * (cost/10)
cost_year3plus = cost/10
total_cost = cost_year1 + (1-discount_rate)*cost_year2 + sum([(1-discount_rate)**i*cost_year3plus for i in range(2,benefit_length)])

# Benefit. From https://scholarworks.uark.edu/cgi/viewcontent.cgi?article=1047&context=meeguht
# Reports the low and high annual energy savings value.
energy_savings_low = 87000
benefit_low = sum([(1-discount_rate)**i*energy_savings_low for i in range(benefit_length)])
energy_savings_high = 984000
benefit_high = sum([(1-discount_rate)**i*energy_savings_high for i in range(benefit_length)])

cost_benefit_table = [
    ["<b>Quantity</b>","<b>Value</b>"],
    ["Cost",total_cost],
    ["Low Benefit Estimate",benefit_low],
    ["High Benefit Estimate",benefit_high]
]

import helper

helper.save_image({
    "filename":"benchmarking_cba.jpg",
    "status":"Done",
    "table":cost_benefit_table,
    "details":"Cost and benefit estimates for companies to participate in the Superior Energy Performance program run by the U. S. Department of Energy. Cost figures from Therkelsen et al. Benefit figures derived from Maldonado.",
    "references":["ems","maldonado"],
    "source_file":"benchmarking.py"
})