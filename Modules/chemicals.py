# Plots related to the chemicals page. Note that some of them are in commodities.py

import helper

death_table = [
    ["<b>Substance</b>","<b>Deaths contributed to</b>","<b>Context</b>"],
    ["Arsenic",52220,"Foodborne"],
    ["Arsenic",43000,"Water Exposure in Bangledesh"],
    ["Radon",87638.73996809360,"Residential"],
    ["Lead",1054471.6276016300,""],
    ["Asbestos",232441.6641824140,"Occupational"],
#    ["Arsenic",9070.946137614210,"Occupational"],
#    ["Benzene",1881.1354272951400,"Occupational"],
#    ["Beryllium",274.13569628810000,"Occupational"],
#    ["Cadmium",658.5655526172360,"Occupational"],
#    ["Chromium",1379.9066523905200,"Occupational"],
    ["Diesel Engine Exhaust",17765.12863385240,"Occupational"],
#    ["Formaldehyde",1061.8031108338500,"Occupational"],
#    ["Nickel",8743.016849700770,"Occupational"],
#    ["Aromatic Hydrocarbons",4841.616666359730,"Occupational"],
    ["Silica",60149.72902220020,"Occupational"],
#    ["Sulfuric Acid",4031.9813626909300,"Occupational"],
#    ["Trichloroethylene",61.01867725522320,"Occupational"],
    ["Other Heavy Metals",9070.946137614210+658.5655526172360+1379.9066523905200+8743.016849700770,"Occupational"], # Includes, in this order, Arsenic, cadmium, chromium, nickel
    ["Other",1881.1354272951400+274.13569628810000+1061.8031108338500+4841.616666359730+4031.9813626909300+61.01867725522320,"Occupational"] # Benzene, beryllium, Formaldehyde, aromatic hydrocarbons, sulfuric acid, Trichloroethylene
]
helper.save_image({
    "filename":"hazardous_exposure.jpg",
    "status":"Done",
    "details":"For various exposures to chemicals and other hazardous materials, show how many deaths they contribute to. As with the risk factors plot, each death may have several contributing factors In the interest of keeping the plot not too big, I combined arsenic, cadmium, chromium, nickel into 'other heavy metals' and benzene, beryllium, formaldehyde, aromatic hydrocarbons, sulfuric acid, trichloroethylene into 'other'. The Residential context for radon means that only residential deaths are counted, and the occupational context means that only occupational deaths are counted. The reference we have now is a good start but woefully incomplete. The foodborne deaths are from Gibbs et al., arsenic from water in Bangledesh deaths from Flanagan et al., and the rest from the GBD statistics.",
    "table":death_table,
    "references":["disease_burden","foodmetals","arsenic"],
    "source_file":"chemicals.py"
})

#######################

# DALYs lost

daly_table = [
    ["<b>Substance</b>","<b>Millions of Disability-adjusted life years lost</b>","<b>Context</b>"],
    # Started with the GBD table
    ["Arsenic",1419566.,"Foodborne"],
    ["Methylmercury",1963869.,"Foodborne"],
    ["Radon",1931739.2202721100,"Residential"],
    ["Lead",24419846.576449000,""],
    ["Asbestos",3932221.430824620,"Occupational"],
    ["Diesel Engine Exhaust",494412.25850975500,"Occupational"],
    ["Silica",1588950.642449680,"Occupational"],
    ["Other Heavy Metals",245333.2205097420+18292.448490045700+38318.63689629580+238300.94870654700,"Occupational"], # Includes, in this order, Arsenic, cadmium, chromium, nickel
    ["Other",84266.96543872890+7636.483254227370+46358.564863158600+134466.88426902300+123496.66023765300+1842.7768671483500,"Occupational"] # Benzene, beryllium, Formaldehyde, aromatic hydrocarbons, sulfuric acid, Trichloroethylene
]

for i in range(1,len(daly_table)):
    daly_table[i][1] /= 10**6

helper.save_image({
    "filename":"daly_exposure.jpg",
    "status":"Done",
    "table":daly_table,
    "details":"Show disability-adjusted life years lost due to pollutants. The Foodborne figures are from Gibbs et al., everything else from the GBD. The other heavy metals and other categories cover the same things as in the hazardous_exposure.jpg plot. They should not be treated as comprehensive, though. A life year is what is sounds like: a year of life lost from illness due to the pollutant. If someone dies, the life years lost are based on some actuarial estimate of how many years they would have had left otherwise. The disability-adjusted term means that, if someone is ill or disabled for a year, that is considered a partial loss. I'm considering some more content on DALYs on the Health section, but I'm not sure it's worth the trouble. The main reason I wanted this is so that we would have something on mercury, which is a significant issue but one for which I am not finding good information on attributable deaths.",
    "references":["disease_burden","foodmetals"],
    "source_file":"chemicals.py"
})

################################

# Monetized damages. Will be pulled from grandjean.

monetized_table = [
    ["<b>Substance</b>","<b>Monetized Damages, billions of USD</b>","<b>Context</b>","Harm assessed"],
    ["Lead",54+60.6,"US+EU","Cognitive"],
    ["Lead",1040,"Lower and middle income countries","Cognitive"],
    ["Methylmercury",15.6,"US+EU","Cognitive"],
    ["Organophosphate pesticides",248.7,"US+EU","Cognitive"],
    ["Polybrominated diphenyl ethers",278.6,"US+EU","Cognitive"],
    ["Endocrine Disruptors",557,"US+EU","Multiple problems"],
    ["Lead","500-700","All countries","Loss of life and cognitive damage"],
    ["Household Air Pollution","2900-4300","Worldwide","Loss of life"],
    ["Ambient Air Pollution","3000-4200","Worldwide","Loss of life"],
    ["Ambient Ozone","300","Worldwide","Loss of life"],
    ["Unsafe Water Sanitation","300-800","Worldwide","Loss of life"],
    ["Unsafe Water Source","500-1300","Worldwide","Loss of life"],
    ["Occupational Carcinogens","100-500","Worldwide","Loss of life"],
    ["Occupational Particulates","200-400","Worldwide","Loss of life"],
    ["Soil Pollution","200-400","Worldwide","Loss of life"],
    ["Methylmercury","1.4-575","Worldwide","Health benefits from the Minimata Convention on Mercury"]
]

helper.save_image({
    "filename":"chemical_econ_damage.jpg",
    "status":"Done",
    "table":monetized_table,
    "details":"This plot again. I've added a few more items and generalized beyond pure chemical pollution by adding figures from the Lancet study. Figures here differ from each other and from figures from other tables because they come from different sources. The first six come from the Grandjean source, everything from the third Lead to Soil Pollution comes from the Lancet source, and the last Methylmercury item comes from the Giang and Selin source.",
    "references":["grandjean","lancet_pollution","mercury"],
    "source_file":"chemicals.py"
})

########################################

# Radiation exposure. From reference 'ncrp'

radiation_table = [
    ["<b>Source</b>","<b>Average American exposure of ionizing radiation, milliSieverts/year</b>","Note"],
    ["<b>Natural Sources</b>","",""],
    ["Radon and Thoron",0.37*6.2,"Not dangerous except in high concentrations, e.g. when trapped in a basement."],
    ["Cosmic Radiation",0.05*6.2,""],
    ["Ingestion",0.05*6.2,"Potassium-40 and trace amounts of uranium and thorium."],
    ["Terrestrial",0.03*6.2,"From radionuclides in soil and building material."],
    ["<b>Medical</b>","",""],
    ["Computed Tomography",0.24*6.2,"A method of scanning in interior of a body, such as MRI."],
    ["Nuclear Medicine",0.12*6.2,"Medicine involving radioactive materials in the body, either for diagnostics or treatment."],
    ["Interventional Fluoroscopy",0.07*6.2,"X-rays used in surgeries."],
    ["Conventional Radiography/Fluoroscopy",0.05*6.2,"X-rays used for diagnostics."],
    ["<b>Other</b>","",""],
    ["Consumer Products",0.02*6.2,"Examples include smoke detectors (Americium), old CRT monitors, not cell phones (they do not emit ionizing radiation)."],
    ["Industrial",0.001*6.2,"Includes public exposure from nuclear power and the nuclear fuel cycle."],
    ["Occupational",0.001*6.2,""]
]

helper.save_image({
    "filename":"radiation_exposure.jpg",
    "status":"Done",
    "table":radiation_table,
    "details":"Exposure of ionizing radiation that the average American receives each year. Figures are from Schauer and Linton, with explanatory notes from the World Nuclear Association. The Sun is not listed here; although it is a source of dangerous ultraviolent and infrared radiation, these are not forms of ionizing radiation.",
    "references":["ncrp","nrc_rad"],
    "source_file":"chemicals.py"
})

