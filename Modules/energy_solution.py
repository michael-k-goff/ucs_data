# General solutions for the energy page

import helper

energy_solutions_table = [
    ["<b>Solution</b>","<b>Estimted Cost</b>","<b>Estimated Benefit</b>","<b>Return on Investment</b>","<b>Notes</b>"],
    ["Full funding to develop advanced nuclear reactor","$11.5 billion","$26.2 billion","2.279","See Nuclear page. The benefits of the advanced reactor are discounted 25 years at 5% annually."],
    ["Fund a national wave energy R&D program","$9.4 billion","$25.5 billion","3.5","See Ocean page. We assume a 5% discount rate and that a research program would take 15 years to reach maturity."],
    ["National carbon pricing in the United States","$1.82 to $10.79 trillion","$10.54 to $18.47 trillion","1.71 to 5.79","Estimate costs, climate benefits, and health benefits of recent carbon pricing proposals in the United States Congress"]
]

helper.save_image({
    "filename":"energy_solutions.jpg",
    "status":"Done",
    "table":energy_solutions_table,
    "details":"The main exhibit in the new energy priorities page; it is still under development. This presents the estimated cost, benefit, and ROI for proposed solutions. Probably no references here since details on the solutions are given elsewhere on the site.",
    "references":[],
    "source_file":"energy_solution.py"
})