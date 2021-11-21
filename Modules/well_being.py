# Plots related to well-being

import helper

# Factors related to life satisfaction

life_satisfaction_table = [
    ["<b>Factor</b>","<b>Explanation of life satisfaction</b>"],
    ["Income",0.07],
    ["Education (1 standard deviation)",0.02],
    ["Not unemployed",0.08],
    ["Non-criminality",0.06],
    ["Partnered",0.17],
    ["Physical health",0.06],
    ["Emotional health (lagged)",0.18]
]

helper.save_image({
    "filename":"life_satisfaction.jpg",
    "status":"Done",
    "table":life_satisfaction_table,
    "details":"How different factors affect life satisfaction. See the caption in the Well Being section for details.",
    "references":["happiness_origins"],
    "source_file":"well_being.py"
})

country_satisfaction_table = [
    ["<b>Factor</b>","<b>Explanation of life satisfaction</b>"],
    ["Income",0.49*0.76],
    ["Health",0.2*0.76],
    ["Social support",0.14*0.76],
    ["Freedom",0.11*0.76],
    ["Trust",0.04*0.76],
    ["Generosity",0.02*0.76],
    ["Other factors (e.g. war, climate, culture)",0.24]
]

helper.save_image({
    "filename":"country_satisfaction.jpg",
    "status":"Done",
    "table":country_satisfaction_table,
    "details":"Factors that contribute to differing levels of reported life satisfaction across countries. This is different from the other plot above in that we are comparing national scores rather than individual scores, and so different factors emerge as being important. Also, the metric being reported is different for technical reasons I won't go into.",
    "references":["happy_choice"],
    "source_file":"well_being.py"
})

event_satisfaction_table = [
    ["<b>Event, From</b>","<b>To</b>","<b>Effect on life satisfaction</b>","<b>Confidence</b>"],
    ["Employment","Unemployment","-0.46 (UK) to -0.71 (Germany)","High"],
    ["No commute","1 hour commute","-0.012 (UK) to -0.151 (Germany)","Low"],
    ["Doubling of household income","","0.14 to 0.5","High"],
    ["Single","Partnered/married","0.1 (Germnay) to 0.28 (UK)","High"],
    ["Partnered","Separated","0.4 (UK)","High"],
    ["Healthy (self-rated)","Poor health","0.96 (Germany) to -1.08 (UK)","High"],
    ["Depression","Full mental health","0.71","High"],
    ["Victim of violent crime","","-0.4 (Australia), effect mostly in first year","High"],
    ["Increase of 10 micrograms/m<sup>3</sup> SO<sub>2</sub>","","-0.08 (Germany)","High"],
    ["Increase of 10 micrograms/m<sup>3</sup> PM<sub>10</sub>","","-0.051 (US)","Medium to high"],
    ["Increase of 1 hectare of green space within 1 km of household","","0.0031 (UK) to 0.0066 (Germany)","Medium to high"],
    ["Increase of 1 hectare of vacant land within 1 km of household","","-0.0395 (Germany)","Medium"],
    ["Wind turbine within 4 km of household","","-0.1405 (Germany), disappears in five years","High"],
    ["Blue collar job","White collar job","0.8 (Worldwide)","High correlation but causality unclear"]
]

helper.save_image({
    "filename":"event_satisfaction.jpg",
    "status":"Done",
    "table":event_satisfaction_table,
    "details":"This table shows the effect of certain events on life satisfaction. For comparison, note that the EPA's safe 24-hour standard for PM<sub>10</sub> is 150 micrograms/m<sup>3</sup> (first EPA reference) and for SO<sub>2</sub> is 200 micrograms/m<sup>3</sup> (second EPA reference) (see <a href=\"https://uk-air.defra.gov.uk/assets/documents/reports/cat06/0502160851_Conversion_Factors_Between_ppb_and.pdf\">this sheet</a> (lower temperature) for SO<sub>2</sub> conversion, which I am not including as a separate reference).",
    "references":["happy_choice","epa_pm10","epa_so2"],
    "source_file":"well_being.py"
})

################################

# Select studies on income and well-being

income_wellbeing_table = [
    ["<b>Study</b>","<b>Conclusion</b>"],
    ["Easterlin, 2017","Short term correlation between happiness and GDP but no long term correlation."],
    ["Layard, 2003","National happiness grows with income but saturates at around $23,000 per capita (2020 dollars)"],
    ["Yu and Chen, 2016","Positive emotions associated with relative income position, negative emotions with absolute position."],
    ["Kahneman and Deaton, 2010","Life satsifaction rises with income indefinitely, emotional well-being caps at around $90,000/year (2020 dollars)."],
    ["Stevenson and Wolfers, 2008","GDP and happiness are correlated at all income levels, within countries, between countries, and over time."],
    ["Diener et al., 2013","Rising incomes leads to improved subjective wellbeing, even in wealther countries, and benefits are persistent."],
    ["Veenhoven and Vergunst, 2014","At all income levels, a 1% increase in GDP/cap/year is followed by 0.0034 points rise in happiness"],
    ["Diener et al., 1993","Income produces happiness at all levels in the United States, no evidence the effect is relative."]
]

helper.save_image({
    "filename":"income_happiness,jpg",
    "status":"Done",
    "details":"Summary of several leading studies that have investigated the link between income and well-being. This is meant to investigate the Easterlin Paradox, the notion that as national incomes rise beyond a certain level, individual happiness ceases increasing. I started with the lateset Easterlin study (he has a bunch of older ones, going back to 1974 where he introduced the concept, but all argue the same basic point). The Layard study supports the conclusion and estimates the income threshhold. The next two studies show partial evidence for the Easterlin Paradox, with some metrics of well-being plateauing and others continuing to increase. The last four refute the paradox.",
    "table":income_wellbeing_table,
    "references":["easterlin","wolfers","layard","diener","veenhoven","diener2","yuchen","kahneman"],
    "source_file":"well_being.py"
})