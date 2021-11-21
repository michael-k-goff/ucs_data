# Economic system

# Correlation between environmental performance index and economic freedom index.

import helper

# First number is EPI, second is EFI.
countries = [
    ["Albania",49,66],
    ["Algeria",44.8,56.9],
    ["Angola",29.7,48.4],
#    ["Antigua and Barbuda",48.5]
    ["Argentina",52.2,51.2],
    ["Armenia",52.3,69.2],
    ["Australia",74.9,82.6],
    ["Austria",79.6,71.6],
    ["Azerbaijan",46.5,58.8],
    ["Bahamas",43.5,67.3],
    ["Bahrain",51,76.3],
    ["Bangladesh",29,51.1],
    ["Barbados",45.6,68.3],
    ["Belarus",53,48.7],
    ["Belgium",73.3,70.1],
    ["Belize",41.9,61.5],
    ["Benin",30,55.4],
    ["Bhutan",39.3,57.0],
    ["Bolivia",44.3,49.4],
    ["Bosnia and Herzegovina",45.4,56.2],
    ["Botswana",40.4,70.3],
    ["Brazil",51.2, 55.6],
#    ["Brunei Darussalam",54.8,]
    ["Bulgaria",57,62.3],
    ["Burkina Faso",38.3,59.4],
    ["Burundi",27,47.5],
    ["Burma/Myanmar",25.1,36.7],
    ["Cambodia",33.6,56.6],
    ["Cameroon",33.6,52.3],
    ["Canada",71,80.4],
    ["Cape Verde",32.8, 61.8],
    ["Central African Republic",36.9,48.4],
    ["Chad",26.7,47.5],
    ["Chile",55.3,77.2],
    ["China",37.3,51.0],
    ["Colombia",52.9,65.5],
    ["Comoros",32.1,44.9],
    ["Costa Rica",52.5,65.9],
    ["Democratic Republic of Congo",36.4,41.4],
    ["Republic of Congo",30.8,43.2],
    ["Cote d'Ivoire",25.8,54.1],
    ["Croatia",63.1,59.2],
    ["Cuba",48.4,26.7],
    ["Cyprus",64.8,70.9],
    ["Czech Republic",71,69.8],
    ["Denmark",82.5,77.9],
    ["Djibouti",28.1,51.0],
    ["Dominica",44.6,63.2],
    ["Dominican Republic",46.3,60.3],
    ["Ecuador",51,49.3],
    ["Egypt",43.3,59.0],
    ["El Salvador",43.1,69.9],
    ["Equatorial Guinea",38.1,48.6],
    ["Eritrea",30.4,35.3],
    ["Estonia",65.3,74.7],
    ["Eswatini",33.8,57.4],
    ["Ethiopia",34.4,51.2],
    ["Fiji",34.4,60.3],
    ["Finland",78.9,73.8],
    ["France",80,64.2],
    ["Gabon",45.8,55.4],
    ["Gambia",27.9,55.1],
    ["Georgia",41.3,70.4],
    ["Germany",77.2,71.1],
    ["Ghana",27.6,60.2],
    ["Greece",69.1,62.7],
#    ["Grenada",43.1,]
    ["Guatemala",31.8,61.0],
    ["Guinea",26.4,51.8],
    ["Guinea-Bassau",29.1,43.6],
    ["Guyana",35.9,48.4],
    ["Haiti",27.0, 50.8],
    ["Honduras",37.8,58.3],
    ["Hungary",63.7,66.1],
    ["Iceland",72.3,73.7],
    ["India",27.6,53.8],
    ["Indonesia",37.8,55.5],
    ["Iran",48,43.4],
#    ["Iraq",39.5]
    ["Ireland",72.8,81.3],
    ["Israel",65.8,67.7],
    ["Italy",71,62.7],
    ["Jamaica",48.2,65.5],
    ["Japan",75.1,72.9],
    ["Jordan",53.4,66.1],
    ["Kazakhstan",44.7,61],
    ["Kenya",34.7,57.5],
    ["Kiribati",37.7,43.7],
    ["Kuwait",53.6,67.7],
    ["South Korea",66.5,69.9],
    ["Kyrgyzstan",39.8,61.3],
    ["Laos",34.8,51.1],
    ["Latvia",61.6,66.2],
    ["Lebanon",45.4,59.5],
    ["Lesotho",28,48.1],
    ["Liberia",22.6,46.2],
    ["Lithuania",62.9,70.3],
    ["Luxembourg",82.3,75.4],
    ["Madagascar",26.5,63.2],
    ["North Macedonia",55.4,65.7],
    ["Malawi",38.3,54.1],
    ["Malaysia",47.9,64.8],
    ["Maldives",35.6,49],
    ["Mali",29.4,55.6],
    ["Malta",70.7,67.2],
#    ["Marshall Islands",30.8,]
    ["Mauritania",27.7,52],
    ["Mauritius",45.1,76.3],
    ["Mexico",52.6,68.3],
    ["Micronesia",33,50.6],
    ["Moldova",44.4,53.7],
    ["Mongolia",32.2,60],
    ["Montenegro",46.3,63.6],
    ["Morocco",42.3,59.2],
    ["Mozambique",33.9,56],
    ["Namibia",40.2,62.2],
    ["Nepal",32.7,52.7],
    ["The Netherlands",75.3,75],
    ["New Zealand",71.3,82.1],
    ["Nicaragua",39.2,58.3],
    ["Niger",30.8,52.9],
    ["Nigeria",31,56.8],
    ["Norway",77.7,69.4],
    ["Oman",38.5,67.7],
    ["Pakistan",33.1,55.2],
    ["Panama",47.3,64.8],
    ["Papua New Guinea",32.4,53.5],
    ["Paraguay",46.4,61.3],
    ["Peru",44,67.6],
    ["The Philippines",38.4,56.3],
    ["Poland",60.9,63.2],
    ["Portugal",67,64.4],
    ["Qatar",37.1,69],
    ["Romania",64.7,64.2],
    ["Russia",50.5,50.3],
    ["Rwanda",33.8,59.1],
    ["Saint Lucia",43.1,70.5],
    ["Saint Vincent and the Grenadines",48.4,66.9],
    ["Samoa",37.3,60.4],
    ["Sao Tome and Principe",37.6,48.8],
    ["Saudi Arabia",44,64,1],
    ["Senegal",30.7,54.6],
    ["Serbia",55.2,56.9],
    ["Seychelles",58.2,47.9],
    ["Sierra Leone",25.7,47.9],
    ["Singapore",58.1,86.1],
    ["Slovakia",68.3,69.7],
    ["Slovenia",72,64.7],
    ["Solomon Islands",26.7,42.9],
    ["South Africa",43.1,62.8],
    ["Spain",74.3,69.6],
    ["Sri Lanka",39,54.6],
#    ["Sudan",34.8,]
    ["Suriname",45.2,52.5],
    ["Sweden",78.7,72.4],
    ["Switzerland",81.5,81.1],
    ["Taiwan",57.2,70.4],
    ["Tajikistan",38.2,53],
    ["Tanzania",31.1,58.3],
    ["Thailand",45.4,64.1],
    ["Timor-Leste",35.3,45.8],
    ["Togo",29.5,47.1],
    ["Tonga",45.1,53.4],
    ["Trinidad and Tobago",47.5,65.7],
    ["Tunisia",46.7,58.9],
    ["Turkey",42.6,63.8],
    ["Turkmenistan",43.9,42.5],
    ["Uganda",35.6,62.2],
    ["Ukraine",49.5,46.4],
    ["United Arab Emirates",55.6,67.3],
    ["United Kingdom",81.3,76.5],
    ["United States of America",69.3,78],
    ["Uruguay",49.1,69.8],
    ["Uzbekistan",44.3,47.5],
    ["Vanuatu",28.9,56.4],
    ["Venezuela",50.3,37.1],
    ["Vietnam",33.4,49.8],
    ["Zambia",34.7,58],
    ["Zimbabwe",37,21.4]
]

efi_s = sorted([countries[i][2] for i in range(len(countries))])
quintiles = [efi_s[len(efi_s)*i//5] for i in range(5)] # Economic freedom quintiles
quintiles.append(9999)
epi_s = sorted([countries[i][1] for i in range(len(countries))])
top_50 = epi_s[-50]

quintile_scores = [0,0,0,0,0]
for i in range(len(countries)):
    for j in range(5):
        if (countries[i][2] >= quintiles[j] and countries[i][2] < quintiles[j+1] and countries[i][1] >= top_50):
            quintile_scores[j] += 1
            
economic_system_table = [
    ["<b>Quintile</b>","<b>Number of top-50 environmental performers</b>"],
    ["Quintile 1",quintile_scores[0]],
    ["Quintile 2",quintile_scores[1]],
    ["Quintile 3",quintile_scores[2]],
    ["Quintile 4",quintile_scores[3]],
    ["Quintile 5",quintile_scores[4]]
]

helper.save_image({
    "filename":"economic_system.jpg",
    "status":"Done",
    "details":"The purpose of this analysis is to investigate how economic freedom is correlated with environmental performance. The EPI is based on air quality, water and sanitation, climate change, biodiversity and habitat, and a bunch of other environmental metrics; see the link for details. Economic freedom is as defined on the Social Well-Being page; it refers to the ability of private actors to make free economic decisions. The 10 year gap is based on the theory that policy changes now will have environmental impacts in the future, and 10 years is my best guess for the length of time.<br><br>To try to keep the results as simple as possible, I looked at the Top 50 environmental performers, as indicated by the EPI, and arranged them into five equally-sized groups of economic freedom. For example, of the top 50 performers, 28 are countries that rank in the top fifth of countries by economic freedom.<br><br>These results show pretty clearly that economic freedom is associated with environmental performance. However, this establishes only correlation and not causation. Trying to prove causation would be much more difficult.",
    "table":economic_system_table,
    "references":["economic_freedom_2010","epi"],
    "source_file":"economic_system.py"
})

############################## SDA's

# Not sure what most of these terms means, so skipping this for now.
sda_table = [
    ["<b>Factor</b>","<b>Percent growth or shinkage in emissions, 2000-2009</b>"],
    ["Intensity Effect","-11.7%"],
    ["DH_d","-3.9%"],
    ["DH_t","0.7%"],
    ["Ds_d","-1.3%"],
    ["Ds_t","-0.8%"],
    ["Du","15.6%"],
    ["Total","-1.7%"]
]

material_table = [
    ["<b>Factor</b>","<b>Increase/decrease in total material usage, billions of tons</b>"],
    ["Actual material use",33],
    ["Final demand per capita",78],
    ["Population growth",11],
    ["Import structures",10],
    ["Material efficiency",-66],
    ["Production recipe",1],
    ["Composition of final demand",-1]
]

helper.save_image({
    "filename":"material_sda.jpg",
    "status":"Done",
    "table":material_table,
    "details":"These figures are results of a structural decomposition analysis. The main objective of an SDA is to determine the factors that drive increase or decrease in environmental impacts. This one in particular breaks down the total growth in material usage from 1990-2010 (+33 billion tons total). The 78 billion tons for final demand, for example, mean that total material usage would have grown 78 billion tons if final demand grew as in reality and all other factors stayed the same. The -66 for material efficiency means that if material efficiency happened as in real life, and everything else stayed the same, total material usage would have gone down 66 billion tons (yeah, I know that would make it negative. It's a mathematical formalism). \"Production recipe\" refers to the structure, but not the size, of inputs into final goods. \"Import structures\" basically means material moving, via imports, from more to less efficient countries. See the reference for more details.",
    "references":["material_sda"],
    "source_file":"economic_system.py"
})

############################################

# Some figures on progress indicators

alt_gdp_table = [
    ["<b>Metric</b>","<b>What is included?</b>","<b>Source</b>"],
    ["Genuine Progress Indicator","Economic measures include personal income, housework work and parenting, volunteer work, higher education, value of infrastructure, net capital and financial flows. Several social and environmental metrics, measured solely as costs.","UN"],
    ["OECD's Better Life Index","Material well-being (income, jobs, housing), quality of life metrics, sustainability (natural, human, economic, social capital).","UN"],
    ["Human Development Index","Life expectancy, schooling, income","UNDP"],
    ["Bhutan's Gross National Happiness","Nine domains, revolving around sustainable and equitable development, environmental conversation, preservation and promotion of culture, and good governance.","Ura et al."],
    ["Sweden's wellbeing index","GDP per capita, (un)employment, household and government debt, air and water quality, land protection, chemical pollution, greenhouse gases, poverty, health, education, trust, life satisfaction.","Government of Sweden"]
]

helper.save_image({
    "filename":"gdp_alt.jpg",
    "status":"Done",
    "table":alt_gdp_table,
    "details":"These are some measures that are used or proposed of human progress generally.",
    "references":["gpi","hdi","bhutan","sweden_wellbeing"],
    "source_file":"economic_system.py"
})